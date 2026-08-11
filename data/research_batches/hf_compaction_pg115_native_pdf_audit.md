# Audit de remplacement HF — *Patrologia Graeca* 115

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** La
compaction préserve les 44 notices à concordance directe, leurs attributions et
leurs bornes MPG imprimées; elle ne change aucun statut canonique.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 115](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._115.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/1/16/Patrologia_Graeca_Vol._115.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  73 776 180 octets, SHA-1 `509e3cfdf8f0f87b0f230119bfa9be63c1147811`,
  1220 × 1718 px. Le rapport de validation documente 710 pages et ~145 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg115-symeon-metaphrastes--abc55701924d.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 710 |
| Taille tar | 546 355 200 octets |
| SHA-256 tar/manifeste | `d31b9963e2081f041885e28330216affaf128333a43bb22f8f8ec988b44e0197` |
| PDF natif | 73 776 180 octets ; 710 pages |
| Gain estimé | 472 579 020 octets (86,50 %) |

Le tar et le PDF correspondent aux mêmes 710 pages. Le PDF peut donc remplacer
le tar comme fac-similé, sans perte de pages, d'édition ou de provenance. Les
JPEG du tar ne sont pas byte-identiques au PDF, mais peuvent être rendus à
nouveau depuis lui. Cette restitution reste image-only et exclut tout OCR
fournisseur.

## Mappings stricts et preuve grecque déjà validée

`scan_validation_pg115_symeon_metaphrastes.md` établit les 44 notices directes
suivantes, toutes à sélectionner par **colonnes imprimées** :

| Notices TLG | Colonnes MPG 115 |
|---|---:|
| 2012.002 | 524–529 |
| 3115.009–.010 | 1141–1160 ; 1160–1264 |
| 3115.018, .024, .027–.028 | 44–77 ; 1289–1293 ; 1293–1308 ; 172–184 |
| 3115.030–.036 | 477–488 ; 881–900 ; 105–125 ; 241–257 ; 1249–1289 ; 900–917 ; 997–1005 |
| 3115.038, .043–.048 | 448–477 ; 617–633 ; 633–640 ; 640–652 ; 653–665 ; 665–689 ; 692–697 |
| 3115.050–.052 | 704–712 ; 497–513 ; 733–749 |
| 3115.055, .058–.060, .062, .064–.065 | 821–845 ; 920–944 ; 944–996 ; 848–881 ; 1005–1032 ; 1053–1065 ; 1068–1080 |
| 3115.068–.070, .072, .083–.084, .093–.094, .113 | 32–44 ; 1129–1140 ; 200–217 ; 1309–1317 ; 188–197 ; 813–820 ; 128–141 ; 372–404 ; 277–308 |
| 5285.001 ; 5460.001 ; 5462.001 ; 5467.001 | 404–425 ; 217–240 ; 596–609 ; 348–353 |

Les frontières communes, notamment 1160, 1289, 1293 et 633, doivent être
stockées une seule fois tout en restant reliées aux deux notices concernées.
Les vues p. 20 (cols 35–36), p. 350 (699–700, début du *Martyrium S.
Severiani*) et p. 680 (1287–1288) ont confirmé un grec/latin net et lisible;
elles ont été supprimées après contrôle.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg115-symeon-metaphrastes/pg115-original-image-only.pdf`.
2. Chemin, taille, SHA-256 et 710 pages vérifiés à distance avant la
   suppression du tar.
3. Manifeste des 44 notices et déduplication des
   colonnes communes.
4. Tar retiré après validation distante; les rendus restent
   régénérables depuis le PDF, sans OCR.

Le PDF image-only a été transféré. Un téléchargement distant forcé a confirmé
73 776 180 octets et le SHA-256
`ae77a932ac777bd603603f77fc78a3f3893bad388e1210b0cb12d543ba817847`.
L'ancien tar a ensuite été retiré; il reste récupérable dans l'historique HF.
Aucun OCR fournisseur n'a été transféré.
