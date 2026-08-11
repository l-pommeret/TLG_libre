#!/usr/bin/env bash
set -euo pipefail

: "${SCOPE_MANIFEST:?scope_manifest is required}"
: "${GREEK_SAMPLE_EVIDENCE:?greek_sample_evidence is required}"

[[ ${#SCOPE_MANIFEST} -ge 12 ]] || { echo "scope manifest is too short" >&2; exit 2; }
[[ ${#GREEK_SAMPLE_EVIDENCE} -ge 20 ]] || { echo "Greek sample evidence is too short" >&2; exit 2; }
grep -Eqi 'greek|grec|ελλην' <<<"$GREEK_SAMPLE_EVIDENCE" || {
  echo "sample evidence must explicitly confirm Greek content" >&2
  exit 2
}

if [[ "${WHOLE_VOLUME_MODE:-false}" == "true" ]]; then
  [[ "${WHOLE_VOLUME_GREEK_VERIFIED:-false}" == "true" ]] || {
    echo "whole-volume ingestion requires explicit whole-volume Greek verification" >&2
    exit 2
  }
  for marker in first middle last; do
    grep -Eqi "${marker}[=: ]" <<<"$GREEK_SAMPLE_EVIDENCE" || {
      echo "whole-volume evidence must document first, middle, and last samples" >&2
      exit 2
    }
  done
fi

echo "Greek-content preflight accepted for scope: $SCOPE_MANIFEST"
