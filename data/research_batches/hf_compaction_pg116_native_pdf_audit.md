# Audit de remplacement HF — *Patrologia Graeca* 116

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** La
compaction conserve les 27 notices à concordance directe et maintient séparées
les deux réimpressions dont le canon privilégie une édition moderne (`REVIEW`).

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 116](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._116.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/7/73/Patrologia_Graeca_Vol._116.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  94 479 951 octets, SHA-1 `e30c838807ddeb12c5ed2e8cccb9ac845e9e75df`,
  1020 × 1595 px. Le rapport de validation documente 747 pages et ~145 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg116-symeon-metaphrastes--b9a5de7449f9.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 747 |
| Taille tar | 577 064 960 octets |
| SHA-256 tar/manifeste | `ac3cd8f1562b5918ccd3a8161c5a52727d6790aac306eea9d1614d6970ac9f35` |
| PDF natif | 94 479 951 octets ; 747 pages |
| Gain estimé | 482 585 009 octets (83,63 %) |

Le PDF et le tar correspondent aux mêmes 747 pages. Le PDF peut donc remplacer
le tar comme fac-similé, sans perte de pagination ou de provenance. Les rendus
JPEG ne sont pas byte-identiques au PDF mais restent régénérables à partir de
celui-ci. Toute restitution est image-only : aucun OCR fournisseur ne doit être
extrait ni conservé.

## Mappings et statuts à préserver

`scan_validation_pg116_symeon_metaphrastes_ii.md` établit les 27 notices
**READY** suivantes, à sélectionner seulement par colonnes imprimées :

| Notices TLG | Colonnes MPG 116 |
|---|---:|
| 2705.019 | 189–269 |
| 3115.020–.022 | 9–36 ; 276–301 ; 301–316 |
| 3115.025, .057, .063, .066 | 956–969 ; 684–705 ; 908–920 ; 896–908 |
| 3115.071, .075–.077 | 1185–1201 ; 36–92 ; 93–108 ; 884–896 |
| 3115.085–.090 | 317–356 ; 357–368 ; 368–416 ; 417–468 ; 468–505 ; 508–560 |
| 3115.092, .095–.100 | 573–609 ; 565–573 ; 609–652 ; 653–684 ; 1037–1081 ; 705–745 ; 753–793 |
| 5057.007 ; 5258.001 | 1173–1184 ; 817–829 |

| Notice REVIEW, à préserver telle quelle | Locus MPG 116 | Motif |
|---|---:|---|
| 3115.011 | 128–161 | réimpression; le canon cite Gebhardt–Dobschütz 1911 |
| 3115.019 | 832–860 | réimpression; le canon cite Delehaye 1905 |

Les bornes communes doivent être dédupliquées au découpage. Les deux plages
REVIEW peuvent être conservées uniquement comme témoins historiques et ne
doivent jamais remplacer silencieusement leurs éditions canoniques.

## Preuve grecque existante

Les échantillons temporaires p. 20 (cols 35–36, *Vita Joannicii*), p. 350
(685–686, *Vita S. Joannis Evang.*) et p. 700 (1345–1346, *Acta S. Demetrii*)
présentent un grec et une mise en page bilingue nets et lisibles. Ils ont été
supprimés après contrôle; aucune image, archive ou OCR local ne reste.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg116-symeon-metaphrastes/pg116-original-image-only.pdf`.
2. Chemin, taille, SHA-256 et 747 pages vérifiés à distance avant la
   suppression du tar.
3. Les 27 mappings READY et les deux drapeaux
   `REVIEW_HISTORICAL_REPRINT` ci-dessus.
4. Tar retiré après validation distante; les rendus restent
   régénérables depuis le PDF, sans OCR.

Le PDF image-only a été transféré. Un téléchargement distant forcé a confirmé
94 479 951 octets et le SHA-256
`a882cfe49c0bd9e23d698ba6073511746f5984303f3ed5787b760b731c62f595`.
L'ancien tar a ensuite été retiré; il demeure récupérable dans l'historique HF.
Aucun OCR fournisseur n'a été transféré.
