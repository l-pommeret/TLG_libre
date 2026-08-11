# Validation scan — Patrologia Graeca 18 : Petrus Alexandrinus

## Décision

**READY — ingestion image-only ciblée** pour **TLG 2962.005**, *De paschate ad Tricentium (fragmenta)*.  Le volume est absent de `data/scan_sources.csv` et de `scans/` au contrôle préalable.  Ne pas l'employer pour les notices dont le canon requiert une édition moderne (notamment 2962.001, .004, .006).

## Concordance bibliographique et pagination

| Notice TLG | Édition canonique | Édition du candidat | Locus vérifié | Décision |
|---|---|---|---|---|
| 2962.005 | *MPG* 18, cols. 512–517 | J.-P. Migne (éd.), *Patrologiae cursus completus. Series Graeca*, t. 18, Paris, 1857–1866 | images DJVU Commons 262–265 : cols. 511–518 ; portion requise 512–517 | READY |

La correspondance est directe : le canon cite explicitement *MPG* 18, 512–517. Les vues montrent à la col. 512 le début du fragment pascal sous Pierre d'Alexandrie, les cols. 513–516 continues et la col. 517 à l'image 265. La formule de pagination est confirmée sur les vues : image 262 = cols. 511–512 ; 263 = 513–514 ; 264 = 515–516 ; 265 = 517–518. L'ingestion ciblée doit donc prendre **262–265**, afin de ne pas couper les colonnes liminaires/finales.

## Source et métadonnées techniques

| Champ | Valeur vérifiée |
|---|---|
| Dépôt / identifiant | Wikimedia Commons, [`File:Patrologia Graeca Vol. 18.djvu`](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._18.djvu) |
| Droits | Public domain / PDM explicite ; `Copyrighted=False` dans l'API Commons |
| Original | DJVU (`image/vnd.djvu`), 70 692 271 octets (≈ 68,4 Mo) |
| Dimensions | 3 982 × 6 482 px |
| SHA-1 original | `c61649e67a8c66772dee9ab1489398e6c9f7e5b4` |
| Nombre d'images | 702 pages DJVU, annoncé par Commons |
| PPI | non déclaré par Commons ; non inféré |
| Rendement | 1 notice TLG exacte / 4 images ciblées |

## Contrôle visuel sans OCR

Trois contrôles représentatifs, par vignettes JPEG web temporaires de 1 280 × 2 084 px, ont été regardés manuellement : image 262 (début, cols. 511–512), image 264 (milieu, cols. 515–516) et image 265 (fin, cols. 517–518). Le grec et le latin sont nets, le contraste est bon et les colonnes/pagination sont lisibles ; aucune coupure de page ni défaut matériel bloquant n'a été constaté. L'image 263 a aussi été contrôlée pour la continuité des cols. 513–514.

Aucun PDF, DJVU, archive JP2, OCR ni image d'ingestion n'a été téléchargé. Les vignettes et fichiers de métadonnées temporaires ont été supprimés après contrôle.

## Action proposée

Télécharger seulement les images sources correspondant aux pages DJVU **262–265**, avec manifeste de provenance Commons, pour l'extraction humaine ultérieure de TLG 2962.005. Ne pas lancer d'OCR tiers.
