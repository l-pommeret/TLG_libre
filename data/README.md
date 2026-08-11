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
python3 scripts/build_open_text_aliases.py
python3 scripts/apply_text_verification.py
python3 scripts/apply_external_text_verification.py
```

`external_open_text_verification.csv` conserve les preuves vérifiées
manuellement pour les textes grecs ouverts qui ne sont pas distribués dans
les corpus TEI locaux. Le script refuse les clés absentes, les renvois, les
doublons de preuve, les licences manquantes et tout type de correspondance qui
n'est pas explicitement exact ou une édition alternative.

Au 11 août 2026, la vue Canon contient 13 765 notices d'œuvres, hors 1 536
renvois : 1 759 (12,78 %) ont un texte grec ouvert vérifié sous le même
identifiant TLG et 135 (0,98 %) supplémentaires ont une édition alternative
ouverte vérifiée. La couverture textuelle directement exploitable est donc de
1 894 notices (13,76 %). Les
deux catégories restent séparées afin de ne pas présenter une édition
alternative comme l'édition bibliographique exacte du Canon.

`open_text_aliases.csv` conserve la preuve reliant une notice du Canon à une
édition alternative dont le TEI, le grec, l'URN, la licence et la somme SHA-256
ont été vérifiés localement.
`open_text_anthology_rejections.csv` conserve les loci AG refusés et les
attributions réellement observées, afin qu'une divergence ne soit jamais
silencieusement convertie en correspondance positive.
`open_text_candidate_rejections.csv` conserve les autres faux rapprochements
vérifiés au niveau du contenu TEI, pour empêcher leur réintroduction lors des
reconstructions futures.

`open_text_fragments.csv` conserve séparément les témoignages et fragments
partiels transmis par des textes hôtes vérifiés. Ils ne font jamais passer une
œuvre au statut de texte complet. Le relevé courant contient 19 œuvres sans
texte complet disposant néanmoins d'au moins un témoin partiel vérifié.

`scan_work_coverage.csv` relie les scans déjà archivés sur Hugging Face aux
notices exactes du Canon. `coverage_summary.md` croise ensuite texte et scan :

```sh
python3 scripts/build_scan_work_coverage.py
python3 scripts/build_coverage_summary.py
```

Les checkouts sous `sources/upstream/` sont des copies de travail clairsemées
liées aux révisions amont. Ils ne doivent pas être modifiés : toute correction
ou transformation devra être écrite dans un emplacement dérivé distinct.

## Scans en attente de notre OCR

`scan_sources.csv` recense les éditions dont les images ont été sécurisées.
`storage_status=REMOTE_ONLY` signifie que les images sont présentes dans le
dépôt GitHub mais volontairement exclues du checkout local. Les notices,
sommes de contrôle, métadonnées et fichiers `scandata.xml` restent locaux.
`ocr_source_used=no` confirme qu'aucun OCR proposé par le fournisseur n'a été
ingéré.

Reconstruction :

```sh
python3 scripts/extract_canon.py \
  thesaurus-linguae-graecae-a-bibliographic-guide-to-the-canon-of-greek-authors-and-works-9780520388208_compress.pdf \
  data/canon_works.csv
```
