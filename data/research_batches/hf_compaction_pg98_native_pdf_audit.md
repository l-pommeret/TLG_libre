# Audit de remplacement HF — *Patrologia Graeca* 98

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** La
compaction préserve la couverture déjà validée de neuf notices TLG directes,
sans changer les attributions éditoriales ni englober les notices qui n'ont pas
de locus MPG 98 dans le canon.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 98](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._098.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/b/bc/Patrologia_Graeca_Vol._098.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  103 744 495 octets, SHA-1 `c62fc965421e011132098457399a17358ec654df`,
  983 × 1547 px. Le rapport de validation documente 832 pages et des rendus
  de ~145 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg98-germanus-tarasius--2a98bb8983bb.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 832 |
| Taille tar | 609 546 240 octets |
| SHA-256 tar/manifeste | `4e8abe4f7e25f9975d4dfd0edddc6fe3557b0049159c7343791f9f5b7d8ecf23` |
| PDF natif | 103 744 495 octets ; 832 pages |
| Gain estimé | 505 801 745 octets (82,98 %) |

Les deux conteneurs représentent le même volume de 832 pages. Le PDF peut
ainsi remplacer le tar sans perte de fac-similé, de pages ou de provenance. Il
n'est pas binaire-identique aux JPEG actuels : tout client nécessitant des
pages unitaires les rendra depuis le PDF. Cette étape reste image-only et
exclut l'extraction ou la conservation de tout OCR fournisseur.

## Couverture et preuve grecque déjà validées

`scan_validation_pg98_germanus_tarasius.md` fixe les neuf correspondances
directes suivantes :

| Notices TLG | Colonnes MPG 98 |
|---|---:|
| 2933.003–.005 | 40–88 ; 147–221 ; 221–381 |
| 2938.001 | 221–289 |
| 3416.001 ; 9052.007–.009 | 1265–1269 ; 1333–1360 ; 1360–1364 ; 1364–1368 |
| 3119.001 | 1481–1500 |

Les vues temporaires déjà vérifiées sont p. 20 (cols 31–32), p. 400
(711–712) et p. 750 (1337–1338); le grec y est net et lisible. Elles ont été
supprimées. Toute extraction doit dédupliquer les frontières 221 et 1360/1364
et respecter les limites imprimées ci-dessus.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg98-germanus-tarasius/pg98-original-image-only.pdf`.
2. Vérification distante achevée : 103 744 495 octets, 832 pages et SHA-256
   `4d8c8c698fb095a7dbf60ad25dc3a7863a281490074bc9140b3bbfd3a8d91b3c`.
3. Conserver avec le PDF le mapping à neuf notices et la règle de
   déduplication des bornes.
4. Tar retiré après validation distante ; les rendus restent régénérables
   depuis le PDF sans OCR et récupérables via l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
