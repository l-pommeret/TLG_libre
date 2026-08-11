# Audit de remplacement HF — *Patrologia Graeca* 100

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** Le
remplacement garde strictement la couverture déjà validée de dix notices TLG
directes, sans étendre les attributions ou les entrées qui ne disposent pas de
locus MPG 100 dans le canon.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 100](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._100.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/5/5b/Patrologia_Graeca_Vol._100.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  103 339 509 octets, SHA-1 `4a88b715a031792ad7e53f772dd670685fc8fa81`,
  983 × 1554 px. Le rapport de validation documente 830 pages et des rendus
  de ~145 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg100-nicephorus--12e24afb16a4.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 830 |
| Taille tar | 607 784 960 octets |
| SHA-256 tar/manifeste | `e53068add4122635728b0e984924bac1aa9cc1cd5d2cf1b85a34e24ce1d4cbcf` |
| PDF natif | 103 339 509 octets ; 830 pages |
| Gain estimé | 504 445 451 octets (83,00 %) |

Les deux conteneurs portent les mêmes 830 pages du volume. Le PDF peut donc
remplacer le tar comme fac-similé source, sans perte documentaire ou
bibliographique. Les JPEG actuels ne sont pas byte-identiques au PDF : les
pages doivent être rendues depuis le PDF lorsque nécessaire. Le rendu reste
image-only; aucun OCR fournisseur ne doit être extrait ni conservé.

## Couverture et preuve grecque déjà validées

`scan_validation_pg100_nicephorus.md` fixe les dix correspondances directes :

| Notices TLG | Colonnes MPG 100 |
|---|---:|
| 3344.004–.006, .011, .017 | 533–832 ; 205–533 ; 833–849 ; 169–200 ; 852–864 |
| 3405.001 ; 4516.001 ; 3280.003 | 1244–1261 ; 1216–1232 ; 1188–1200 |
| 3292.002–.003 | 1336–1528 ; 1528–1530 |

Les preuves grecques visuelles existantes couvrent p. 20 (cols 31–32), p. 400
(743–744) et p. 750 (1395–1396), avec un grec net et lisible; toutes les vues
temporaires ont été supprimées. Les bornes partagées 533 et 1528 doivent être
dédupliquées. 3344.003 et 3344.015 restent exclues, faute de locus MPG 100
dans le canon.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg100-nicephorus/pg100-original-image-only.pdf`.
2. Vérification distante achevée : 103 339 509 octets, 830 pages et SHA-256
   `d9c11c1a760292bc4e660795a01afb5b0b9086e4af8377e4e2717004dc167620`.
3. Associer au PDF le mapping à dix notices et la déduplication des bornes.
4. Tar retiré après validation distante ; les rendus restent régénérables
   depuis le PDF sans OCR et récupérables via l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
