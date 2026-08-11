# Audit de remplacement HF — *Patrologia Graeca* 37

## Décision

**READY pour compaction du contenant, avec couverture TLG partielle inchangée.**
Le PDF Commons natif peut remplacer le tar de rendus pour préserver le
fac-similé du volume. Cela ne fait pas passer en READY les notices 2022.057 et
2022.058, dont les loci MPG restent non vérifiés.

## Source directe et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 37](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._037.pdf)
* **Original direct :** [PDF](https://upload.wikimedia.org/wikipedia/commons/d/d4/Patrologia_Graeca_Vol._037.pdf)
* **API Commons, 2026-08-11 :** MIME `application/pdf`, taille `100503252`
  octets, SHA-1 `c1a0531688165fbd422aba9ecaa96836a2fd17ba`, dimensions source
  1035 × 1579 px, 974 pages.
* **Droits :** `Public domain`, `Copyrighted: False`, avec PDM 1.0 inscrit
  dans `data/scan_sources.csv`.

## Comparaison HF

| Élément | Valeur |
|---|---:|
| Archive rendue actuelle | `webdataset/volumes--pg37-gregory-nazianzen--8ff45c95b44a.tar` |
| État HF | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Pages/images dans le tar | 974 |
| Taille tar | 638 668 800 octets |
| SHA-256 du manifeste/tar vérifié | `69baaf9c814418fb28bdcad3dd7b16d6f54aea2764225f6bddb5d18aab370a8f` |
| PDF source natif | 100 503 252 octets ; 974 pages |
| Économie estimée | 538 165 548 octets (84,26 %) |

Le PDF et le tar portent tous deux les 974 pages du volume. Le PDF peut donc
remplacer le cache de rendus sans perte documentaire ou bibliographique. Il ne
sera pas identique bit à bit aux JPEG du tar : tout consommateur de WebDataset
devra rendre localement les pages du PDF. Ce rendu se limite aux images ; aucun
texte intégré ou OCR fournisseur ne doit être extrait.

## Couverture validée et qualité grecque

Quatre notices restent **READY** selon
`scan_validation_pg37_gregory_nazianzen.md` :

| Notice | Loci MPG 37 validés |
|---|---:|
| 2022.059, *Carmina dogmatica* | 397–522 |
| 2022.060, *Carmina moralia* | 521–968 |
| 2022.061, *Carmina de se ipso* | 969–1029 ; 1166–1452 |
| 2022.062, *Carmina quae spectant ad alios* | 1451–1577 |

Le rapport de validation fixe ces loci sur l'édition Migne et documente des
preuves visuelles grecques nettes aux feuilles de repère IA n204 (cols 397–398),
n500 (989–990) et n794 (1577–1578). L'IA sert seulement de contrôle de
pagination/qualité ; le PDF Commons PDM reste la source d'ingestion ouverte.

Les notices 2022.057 (*Epigrammata*) et 2022.058 (*Testamentum*) restent
**REVIEW** et ne doivent pas être incluses dans la couverture revendiquée tant
que leurs loci MPG ne sont pas établis. Cette restriction est indépendante du
remplacement du contenant complet.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg37-gregory-nazianzen/pg37-original-image-only.pdf`.
2. Vérification distante achevée : 100 503 252 octets, 974 pages et SHA-256
   `7ad53d25e9fd8b15218267c90d452e42dec881eb23f2802a92db8f74037eb7d1`.
3. Conserver avec lui ce mapping et les statuts READY/REVIEW ci-dessus.
4. Tar supprimé après validation distante ; les JPEG peuvent être régénérés
   localement à partir du PDF, sans OCR, et le tar reste dans l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
