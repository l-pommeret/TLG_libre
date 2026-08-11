# Audit de remplacement HF — *Patrologia Graeca* 77

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** La
compaction ne modifie pas le périmètre documentaire : elle conserve la
couverture exactement validée de quinze notices TLG directes. La notice
4090.179 demeure exclue, car le canon ne lui donne pas de locus MPG 77.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 77](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._077.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/e/e5/Patrologia_Graeca_Vol._077.pdf)
* **Métadonnées API Commons contrôlées le 2026-08-11 :** MIME
  `application/pdf`, 101 113 771 octets, SHA-1
  `7c6921f9050bbd490e97612bb335fc078a3385a5`, 822 pages, 1027 × 1579 px.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 également consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg77-cyril-alexandria--c98e766576c9.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 822 |
| Taille tar | 625 694 720 octets |
| SHA-256 tar/manifeste | `6648ec28b6382200e8a3445581a1eba94a88e5dbea94f6065a2dbbc6ae4e25b7` |
| PDF natif | 101 113 771 octets ; 822 pages |
| Gain estimé | 524 580 949 octets (83,84 %) |

Le nombre de pages est identique (822). Le PDF est donc un remplacement du
contenant de fac-similé sans perte bibliographique ni de pages. Il n'est pas
bit à bit identique aux JPEG du tar : les clients WebDataset devront rendre les
pages du PDF au besoin. Cette opération doit rester image-only et ne doit pas
extraire ni conserver d'OCR fournisseur.

## Couverture et preuve grecque déjà validées

Le rapport source
`scan_validation_pg77_cyril_alexandria.md` établit les correspondances exactes
suivantes dans l'édition Migne :

| Notices TLG | Colonnes MPG 77 |
|---|---:|
| 2760.001 | 1516 |
| 4090.032, .114–.124 | 401–981 ; 285–288 ; 365–372 ; 1009–1016 ; 1029–1040 ; 1040–1049 ; 1072–1089 ; 1096–1100 ; 1100–1105 ; 1117 ; 1120–1173 ; 1176–1289 |
| 2778.002, .004 | 1389–1412 ; 1313–1348 |

Les échantillons temporaires déjà inspectés couvrent le début, le milieu et la
fin du volume : p. 20 (cols 19–20), p. 400 (cols 715–716) et p. 700
(cols 1281–1282). Le grec y est lisible et net; les trois vues ont été
supprimées. Les bornes communes doivent rester dédupliquées durant toute
extraction ciblée.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg77-cyril-alexandria/pg77-original-image-only.pdf`.
2. Vérification distante achevée : 822 pages, 101 113 771 octets et SHA-256
   `f93b65fcf355feb9db89d3dfb469b49badb8bfeddb9adeaf68145ea289f3611c`.
3. Associer le PDF au mapping de quinze notices et conserver l'exclusion de
   4090.179.
4. Tar supprimé après ces vérifications ; il reste régénérable depuis le PDF
   sans OCR et récupérable via l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
