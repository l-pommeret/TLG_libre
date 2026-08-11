#!/usr/bin/env python3
"""Extract the author/work inventory from Pantelia's 2022 printed TLG guide.

The PDF has two visual columns and no tagged reading order.  This script keeps
the raw notice as the authoritative extracted value and adds conservative,
derived fields suitable for discovery.  Rows marked ``needs_review`` should
not be used for automatic matching before manual correction.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from html.parser import HTMLParser
import re
import subprocess
import tempfile
from pathlib import Path


PDF_FIRST_CANON_PAGE = 51
PDF_LAST_CANON_PAGE = 858
COLUMN_X = 252.0

AUTHOR_RE = re.compile(r"^\s*(\d{4})\s+([\[A-ZΑ-Ω][^,;:]*)$")
WORK_RE = re.compile(r"^\s{0,3}(\*?)\s*([0-9x]\d{2})\s+(.+)$")
DATE_RE = re.compile(r"^\s*(?:(?:ca\.|post|ante)\s+)?(?:A\.D\.|B\.C\.|Varia|Incertum)", re.I)
CODE_RE = re.compile(r"\b(Cod|Pap|Inscr|NQ|Q):\s*(?:([0-9,]+)\s*:\s*)?(.+?)(?:\.|$)")


class BBoxParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.pages: list[list[tuple[float, float, str]]] = []
        self.page: list[tuple[float, float, str]] | None = None
        self.line: tuple[float, float] | None = None
        self.words: list[str] = []
        self.in_word = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        at = dict(attrs)
        if tag == "page":
            self.page = []
        elif tag == "line":
            self.line = (float(at["xmin"]), float(at["ymin"]))
            self.words = []
        elif tag == "word":
            self.in_word = True

    def handle_data(self, data: str) -> None:
        if self.in_word:
            self.words.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "word":
            self.in_word = False
        elif tag == "line" and self.page is not None and self.line is not None:
            self.page.append((*self.line, " ".join(self.words)))
            self.line = None
        elif tag == "page" and self.page is not None:
            self.pages.append(self.page)
            self.page = None


def pdf_columns(pdf: Path) -> list[tuple[list[str], list[str]]]:
    """Return each page as left/right lines using PDF coordinates."""
    with tempfile.TemporaryDirectory() as tmp:
        xml_path = Path(tmp) / "canon-bbox.html"
        subprocess.run(
            ["pdftotext", "-f", str(PDF_FIRST_CANON_PAGE), "-l",
             str(PDF_LAST_CANON_PAGE), "-bbox-layout", str(pdf), str(xml_path)],
            check=True,
        )
        parser = BBoxParser()
        parser.feed(xml_path.read_text(encoding="utf-8"))
    result = []
    for page in parser.pages:
        sides: list[list[tuple[float, str]]] = [[], []]
        for x, y, text in page:
            text = text.strip()
            if text:
                sides[0 if x < COLUMN_X else 1].append((y, text))
        result.append(tuple([[text for _, text in sorted(side)] for side in sides]))
    return result  # type: ignore[return-value]


def clean_join(lines: list[str]) -> str:
    text = " ".join(part.strip() for part in lines if part.strip())
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "", text)
    return re.sub(r"\s+", " ", text).strip()


def title_from_notice(notice: str) -> str:
    # The first "ed." normally starts the edition statement.  Retaining the
    # complete notice prevents this deliberately cautious heuristic losing data.
    title = re.split(r",?\s+ed\.\s", notice, maxsplit=1)[0]
    return title.rstrip(" ,.;")


def extract(pdf: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    author_id = author_heading = author_date = ""
    current: dict[str, object] | None = None

    def finish() -> None:
        nonlocal current
        if not current:
            return
        notice = clean_join(current.pop("lines"))  # type: ignore[arg-type]
        code = CODE_RE.search(notice)
        current["work_title"] = title_from_notice(notice)
        current["bibliographic_notice"] = notice
        current["source_medium"] = code.group(1) if code else ""
        current["tlg_word_count"] = (code.group(2) or "").replace(",", "") if code else ""
        current["genres"] = code.group(3) if code else ""
        flags = []
        if not author_id:
            flags.append("missing_author")
        if not notice or len(str(current["work_title"])) < 2:
            flags.append("missing_title")
        if not code:
            flags.append("no_code_line")
        current["extraction_status"] = "needs_review" if flags else "parsed"
        current["extraction_notes"] = ";".join(flags)
        rows.append(current)  # type: ignore[arg-type]
        current = None

    printed_page = 0
    for page in pdf_columns(pdf):
        printed_page += 1
        for col in page:
            for raw in col:
                text = raw.strip()
                if not text or re.fullmatch(r"\d+", text):
                    continue
                am = AUTHOR_RE.match(raw)
                if am and not WORK_RE.match(raw):
                    finish()
                    author_id, author_heading = am.groups()
                    author_date = ""
                    continue
                if author_id and not current and DATE_RE.match(text):
                    author_date = text
                    continue
                wm = WORK_RE.match(raw)
                if wm:
                    finish()
                    old, work_id, first = wm.groups()
                    current = {
                        "tlg_author_id": author_id,
                        "tlg_work_id": work_id,
                        "author_heading": author_heading,
                        "author_date": author_date,
                        "legacy_entry": "yes" if old else "no",
                        "canon_printed_page": str(printed_page),
                        "lines": [first],
                    }
                elif current:
                    current["lines"].append(text)  # type: ignore[union-attr]
    finish()
    key_counts = Counter((str(row["tlg_author_id"]), str(row["tlg_work_id"])) for row in rows)
    for row in rows:
        key = (str(row["tlg_author_id"]), str(row["tlg_work_id"]))
        if key_counts[key] > 1:
            row["extraction_status"] = "needs_review"
            prior = str(row["extraction_notes"])
            row["extraction_notes"] = ";".join(filter(None, [prior, "duplicate_key"]))
        row["record_type"] = "cross_reference" if str(row["tlg_work_id"]).startswith("x") else "work"
        row["pipeline_status"] = "NOT_CHECKED"
        row["open_text_url"] = ""
        row["open_text_license"] = ""
        row["scan_url"] = ""
        row["next_action"] = "verify_extraction" if row["extraction_status"] == "needs_review" else "search_open_text"
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    rows = extract(args.pdf)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "tlg_author_id", "tlg_work_id", "author_heading", "author_date",
        "work_title", "record_type", "legacy_entry", "source_medium", "tlg_word_count",
        "genres", "bibliographic_notice", "canon_printed_page",
        "extraction_status", "extraction_notes",
        "pipeline_status", "open_text_url", "open_text_license", "scan_url",
        "next_action",
    ]
    with args.output.open("w", encoding="utf-8", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} work rows to {args.output}")


if __name__ == "__main__":
    main()
