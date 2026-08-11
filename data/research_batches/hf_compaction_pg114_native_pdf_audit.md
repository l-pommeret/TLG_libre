# Audit de remplacement HF — *Patrologia Graeca* 114

## Décision

**READY_PARTIAL pour remplacer le tar rendu par le PDF Commons image-only.**
La compaction conserve strictement les 26 notices aux mappings sûrs, ainsi que
l'exclusion obligatoire de 5295.001. Le PDF source contient la même dégradation
matérielle : son usage ne rend pas les cols 1357–1358 exploitables et ne permet
pas de transformer 5295.001 en notice READY.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 114](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._114.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/d/d3/Patrologia_Graeca_Vol._114.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  90 347 679 octets, SHA-1 `24171c3cedf3fca56a856cb6fa715c41f9584f10`,
  991 × 1550 px. Le rapport de validation documente 768 pages et des rendus
  de ~145 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg114-symeon-metaphrastes--de5e27d45f14.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 768 |
| Taille tar | 602 255 360 octets |
| SHA-256 tar/manifeste | `2a429f5c8db8968bf398ea6cc8b664c9d2586ce17e45416b53b126286b6573e2` |
| PDF natif | 90 347 679 octets ; 768 pages |
| Gain estimé | 511 907 681 octets (85,00 %) |

Les deux conteneurs portent les mêmes 768 pages du volume. Le PDF remplace donc
le tar comme fac-similé sans perte de pagination ni de provenance; il préserve
également, intentionnellement, la zone endommagée. Les JPEG du tar ne sont pas
byte-identiques au PDF, mais peuvent être rendus à nouveau depuis celui-ci. Ce
rendu est exclusivement image-only : aucun OCR fournisseur ne doit être
extrait ou conservé.

## Périmètre inchangé : mappings sûrs et zone masquée

`scan_validation_pg114_symeon_metaphrastes.md` donne les 26 notices sûres :

| Notices TLG | Colonnes MPG 114 |
|---|---:|
| 3115.026, .029, .037, .040 | 1001–1009 ; 968–981 ; 816–893 ; 336–392 |
| 3115.049, .056, .067 | 1293–1312 ; 305–321 ; 397–416 |
| 3115.082, .091 | 896–965 ; 1437–1452 |
| 3115.101–.110 | 417–429 ; 429–456 ; 469–553 ; 553–565 ; 761–773 ; 981–1000 ; 1014–1043 ; 1253–1268 ; 1232–1249 ; 1312–1328 |
| 3115.116–.117 | 133–134 ; 133 |
| 5123.001 ; 5239.001 ; 5291.001 ; 5296.001 ; 5474.001 | 1377–1436 ; 1332–1345 ; 568–581 ; 1368–1376 ; 1213–1224 |

| Exclusion impérative | Colonnes | Effet de la compaction |
|---|---:|---|
| 5295.001, *Vita sancti Parthenii* | 1348–1365 | **Toujours exclue** : p. 700 / cols 1357–1358 sont matériellement masqués; le PDF natif conserve ce défaut. |

Les échantillons grecs p. 20 (cols 27–28), p. 400 (773–774, début du
*Martyrium Anastasi Persae*) et p. 740 (1417–1418) sont nets. Le contrôle p.
700 documente la zone occultée; les quatre vues temporaires ont été supprimées.
Les colonnes imprimées, et non une interpolation de pages, restent la règle de
découpage.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg114-symeon-metaphrastes/pg114-original-image-only.pdf`.
2. Vérification distante achevée : 90 347 679 octets, 768 pages et SHA-256
   `f926b79c3a89a18aed1e4a1018dac8f6c889d800e5fa7e150ffdeebf4cc7aa80`.
3. Conserver avec le PDF le manifeste des 26 notices et un drapeau
   `EXCLUDED_DAMAGED_SOURCE` pour 5295.001 (cols 1348–1365, masquage
   1357–1358).
4. Tar retiré après validation distante ; les rendus restent régénérables
   depuis le PDF sans OCR et récupérables via l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
