# Audit de remplacement HF — *Patrologia Graeca* 64

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** La
compaction maintient exactement le périmètre validé de 26 notices TLG directes
dans MPG 64; elle ne doit pas faire entrer 2914.016, qui n'a pas de locus
MPG 64 sur sa ligne canonique.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 64](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._064.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/e/e7/Patrologia_Graeca_Vol._064.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  94 500 422 octets, SHA-1 `05d804d24899106722fb803e73f8ef5aa75dc0d5`,
  1187 × 1631 px. Le rapport de validation documente 776 pages et des rendus
  de ~145 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg64-chrysostom--84b040964da9.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 776 |
| Taille tar | 577 341 440 octets |
| SHA-256 tar/manifeste | `f25d35ca58cfa9e946e42a1fa9d1412687599c6f395514220c6b7216018008c3` |
| PDF natif | 94 500 422 octets ; 776 pages |
| Gain estimé | 482 841 018 octets (83,63 %) |

Le PDF et le tar correspondent aux mêmes 776 pages. Le PDF peut remplacer le
tar comme fac-similé source sans perte de pages ou de provenance
bibliographique. Les JPEG actuels ne sont pas byte-identiques au PDF; les
pages individuelles seront rendues à la demande depuis celui-ci. L'opération
reste image-only et exclut l'extraction ou la conservation d'OCR fournisseur.

## Couverture et preuve grecque déjà validées

`scan_validation_pg64_chrysostom.md` fixe les 26 notices directes :

| Notices TLG | Colonnes MPG 64 |
|---|---:|
| 2720.028 | 45–48 |
| 2062.182–.187 | 424–433 ; 504–506 ; 505–656 ; 660–740 ; 740–1037 ; 1040–1061 |
| 2062.352–.362 | 11–16 ; 15–16 ; 17–18 ; 17–18 ; 17–20 ; 19–22 ; 21–26 ; 25–34 ; 37–44 ; 43–46 ; 47–52 |
| 2062.363–.366 | 433–444 ; 453–461 ; 461–465 ; 473–480 |
| 2062.368–.371 | 1061 ; 1061–1064 ; 1064 ; 1064–1068 |

Les preuves visuelles existantes couvrent p. 20 (cols 25–26), p. 350
(631–632) et p. 600 (1107–1108); le grec imprimé est net et lisible dans les
trois zones et les échantillons ont été supprimés. Les colonnes limites
partagées doivent être dédupliquées lors de toute extraction ultérieure.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg64-chrysostom/pg64-original-image-only.pdf`.
2. Vérification distante achevée : 94 500 422 octets, 776 pages et SHA-256
   `c07270bcbb7f2a1c7a0d25a221c6f9800d6b08d147295529798c554aa6fafee8`.
3. Associer au PDF le mapping à 26 notices, l'exclusion de 2914.016 et la
   déduplication des colonnes communes.
4. Tar retiré après validation distante ; les rendus restent régénérables
   depuis le PDF sans OCR et récupérables via l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
