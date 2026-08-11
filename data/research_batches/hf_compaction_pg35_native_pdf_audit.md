# Audit de remplacement HF — *Patrologia Graeca* 35

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** La
compaction conserve les 25 mappings **directs** de `2022.015–.039`, leurs
colonnes MPG et les lacunes voulues du Canon. Aucun nouveau mapping alternatif
ne doit être créé du seul fait que le volume contient d'autres textes de
Grégoire de Nazianze.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 35](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._035.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/7/7a/Patrologia_Graeca_Vol._035.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  77 617 616 octets, SHA-1 `c46de993db3e352f55c27e810884d7d20880d61b`,
  977 × 1600 px. Le rapport de validation établit 660 pages; Commons ne publie
  ni paquet JP2 séparé ni PPI distinct.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); la source est enregistrée sous
  `Creative Commons Public Domain Mark 1.0` dans `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg35-gregory-nazianzen--d0b7f912208a.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 660 |
| Taille tar | 490 844 160 octets |
| SHA-256 tar/manifeste | `d8eb075d6c8a05f28d1d398d1364c908f588a18136987915002ea612d92b09dc` |
| PDF natif | 77 617 616 octets ; 660 pages |
| Gain estimé | 413 226 544 octets (84,19 %) |

Le tar et le PDF couvrent les mêmes 660 feuilles. Le PDF natif peut donc
remplacer le tar comme fac-similé sans perte de page, d'édition ni de
provenance. Les JPEG rendus ne sont pas byte-identiques au PDF, mais restent
régénérables à partir de lui. Le remplacement demeure image-only : aucun OCR
fournisseur, texte dérivé ou fichier OCR ne doit être transféré.

## Mappings directs stricts et preuve grecque déjà validée

`scan_validation_pg35_gregory_nazianzen.md` confirme l'en-tête `S. GREGORII
THEOLOGI` et les 25 notices canoniques suivantes. La sélection future doit se
faire par **colonnes imprimées**, non par interpolation du numéro de page PDF;
une feuille de borne commune ne doit être stockée qu'une fois tout en restant
liée aux deux notices concernées.

| Notices TLG | Colonnes MPG 35 |
|---|---:|
| 2022.015–.020 | 396–401 ; 408–513 ; 517–525 ; 532–664 ; 664–720 ; 721–752 |
| 2022.021–.026 | 789–817 ; 820–825 ; 828–832 ; 832–841 ; 844–849 ; 852–856 |
| 2022.027–.032 | 857–909 ; 912–933 ; 933–964 ; 964–981 ; 985–1044 ; 1044–1064 |
| 2022.033–.039 | 1065–1080 ; 1081–1128 ; 1132–1152 ; 1152–1168 ; 1169–1193 ; 1197–1225 ; 1228–1252 |

Trois rendus temporaires, depuis supprimés, constituent les preuves grecques
du début/milieu/fin de l'étendue utile : p. PDF 250 (cols. 491–492), p. 450
(cols. 891–892, début de l'oratio XIII) et p. 650 (cols. 1251–1252,
*Oratio XXVI — In seipsum*). Tous étaient grecs/latins nets et lisibles. Toute
extraction ciblée doit reconfirmer visuellement la première et la dernière
feuille de chaque segment avec les numéros de colonnes imprimés.

## Alternatives et exclusions à préserver

Il n'existe **aucun mapping alternatif validé** pour ce volume dans
`data/scan_work_coverage.csv` : les 25 entrées sont toutes
`ARCHIVED_DIRECT_REGISTRY_MAPPING`. Ne pas dégrader ces entrées directes en
« alternative » ni étendre la couverture à d'autres œuvres présentes dans le
volume sans citation MPG 35 directe dans le Canon.

Sont expressément hors du manifeste PG35 :

* `2022.001–.014`, dont le Canon prescrit d'autres éditions, y compris
  `2022.005` (oratio 7), malgré une éventuelle présence textuelle dans une
  collection ancienne;
* `2022.040–.055`, qui citent MPG 36, et `2022.059–.062` (MPG 37) ainsi que
  `2022.063–.064` (MPG 38) : ces volumes sont des candidats distincts;
* les renvois `2022.x01–x04`, qui ne sont pas des œuvres autonomes à couvrir.

Les intervalles de colonnes intentionnellement absents (notamment 401–408,
752–789 et les lacunes entre les orationes) restent donc des exclusions, et ne
doivent jamais être comblés par inférence de pagination.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg35-gregory-nazianzen/pg35-original-image-only.pdf`.
2. Chemin, 77 617 616 octets, SHA-256 et 660 pages vérifiés à distance avant
   toute suppression.
3. Les 25 mappings directs, les bornes communes et
   toutes les exclusions listées; aucun statut `ALTERNATIVE` n'est à ajouter.
4. Tar retiré seulement après ces vérifications distantes; les rendus
   resteront régénérables depuis le PDF, sans OCR.

Le téléchargement distant forcé a confirmé le SHA-256
`5c8d9bebe21052aa89c31e095ac3f280891345050ed44c039612ee522f88140d`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
