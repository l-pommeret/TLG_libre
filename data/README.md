# Registre du canon

`canon_works.csv` est un premier inventaire automatiquement extrait du guide
bibliographique imprimé de Maria C. Pantelia (2022). La notice bibliographique
complète est toujours conservée : les champs `work_title`, `source_medium`,
`tlg_word_count` et `genres` sont des dérivations destinées au tri et peuvent
nécessiter une correction.

Les lignes `extraction_status=needs_review` doivent être corrigées avant tout
rapprochement automatique. Ce registre décrit le canon ; il ne prétend ni que
le texte TLG est ouvert, ni qu'une édition est libre de droits.

`record_type=cross_reference` correspond aux identifiants imprimés `xNN` : ce
sont des renvois vers un texte rangé ailleurs dans le canon, pas des textes à
récupérer une seconde fois. `pipeline_status=NOT_CHECKED` signifie qu'aucune
recherche en ligne n'a encore été validée. Les OCR trouvés sur le Web ne devront
jamais faire passer une ligne à un statut de texte vérifié sans comparaison à
l'édition ; si seul le livre est bon, on conserve le scan et on produit notre
propre OCR.

## Rapprochement avec les corpus

`corpus_matches.csv` contient une ligne par édition numérique trouvée. Seuls
les identifiants TLG explicitement déclarés dans les URN CTS ou les métadonnées
des projets sont acceptés comme correspondances exactes. Le statut
`METADATA_MATCH_UNVERIFIED_TEXT` exige encore le contrôle du fichier, de
l'édition source, de la complétude et de la licence.

`canon_coverage.csv` est la vue œuvre par œuvre du registre, enrichie avec le
nombre de correspondances, les corpus et les URN. `TEXT_OPEN_UNVERIFIED` ne
signifie donc jamais qu'un texte est déjà validé pour redistribution.

Reconstruction du rapprochement :

```sh
python3 scripts/match_corpora.py
```

## Contrôle des fichiers TEI

`text_verification.csv` enregistre le chemin local, la somme SHA-256, la taille,
le nombre de caractères grecs, la licence trouvée dans le TEI et le résultat
des contrôles automatiques. `AUTOMATED_TEI_CHECK_PASSED` garantit seulement
que le fichier attendu existe, est un XML/TEI analysable, contient du grec et
déclare l'URN attendu. La fidélité philologique à l'édition et la complétude
doivent encore être vérifiées sur échantillon avant `TEXT_OPEN_VERIFIED`.

```sh
python3 scripts/fetch_matched_texts.py
python3 scripts/verify_tei.py
```

Les checkouts sous `sources/upstream/` sont des copies de travail clairsemées
liées aux révisions amont. Ils ne doivent pas être modifiés : toute correction
ou transformation devra être écrite dans un emplacement dérivé distinct.

Reconstruction :

```sh
python3 scripts/extract_canon.py \
  thesaurus-linguae-graecae-a-bibliographic-guide-to-the-canon-of-greek-authors-and-works-9780520388208_compress.pdf \
  data/canon_works.csv
```
