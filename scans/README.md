# Scan storage

The binary page images formerly tracked in this Git repository are stored in
the public Hugging Face dataset
[`Zual/TLG_libre_scans`](https://huggingface.co/datasets/Zual/TLG_libre_scans).

The dataset contains one deterministic WebDataset TAR archive per scan-source
root. The authoritative completion record is
[`migration/complete.json`](https://huggingface.co/datasets/Zual/TLG_libre_scans/blob/main/migration/complete.json):

- 149 archives;
- 63,853 page images;
- 40,774,717,440 remote bytes.

This Git tree retains the lightweight `README.md`, `SHA1SUMS`, `MAPPING.csv`,
and source metadata files needed to audit provenance and reconstruct the exact
archive names. New page-image ingestion must visually confirm Greek within
every selected segment and must not use provider OCR.
