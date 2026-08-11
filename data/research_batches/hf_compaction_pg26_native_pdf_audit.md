# Audit de remplacement HF — *Patrologia Graeca* 26

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** Le
remplacement conserve exactement la couverture de seize notices qui citent
directement MPG 26; il ne transforme pas des doublons modernes partiels en
équivalences d'édition.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 26](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._026.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/b/b1/Patrologia_Graeca_Vol._026.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  94 774 657 octets, SHA-1 `62d373c614cfc82b6019b77f8ea295ccd085f072`,
  991 × 1554 px. Le rapport de validation documente 785 pages et une qualité
  approchée de 150 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 et provenance Internet Archive
  via Commons sont consignés dans le rapport source.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg26-athanasius--f1bbb16acebe.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 785 |
| Taille tar | 598 251 520 octets |
| SHA-256 tar/manifeste | `08bcb220cd9e65fb006b354dde0672c07f58af6e055cb86faaf7b6788a8f4a3b` |
| PDF natif | 94 774 657 octets ; 785 pages |
| Gain estimé | 503 476 863 octets (84,16 %) |

Le PDF natif et le tar portent le même volume de 785 pages. Le premier peut
donc remplacer le second comme fac-similé, sans perte de pagination ou de
provenance. Les JPEG du tar ne sont pas identiques octet pour octet au PDF;
les pages pourront être rendues de nouveau depuis lui. Cette étape reste
image-only et interdit l'extraction ou la conservation d'OCR tiers.

## Couverture et preuve grecque déjà validées

`scan_validation_pg26_athanasius.md` consigne les seize mappings directs :

| Notices TLG | Colonnes MPG 26 |
|---|---:|
| 2035.042–.047 | 12–468 ; 529–648b ; 648c–676 ; 796–809 ; 820–824 ; 835–976b |
| 2035.049–.053 | 1029–1048 ; 1072–1084 ; 1085–1089 ; 1165–1168b ; 1168b–1169 |
| 2035.054 | 1224 ; 1233–1249 ; 1252–1260 ; 1293b–1296c ; 1313b–1313c ; 1320–1325 |
| 2035.055–.058 | 1185–1188 ; 1297–1309 ; 1316–1317 ; 1328–1332 |

Les échantillons p. 100 (cols 187–188), p. 350 (667–668) et p. 650
(1267–1268) confirment un grec lisible et une impression homogène à travers
l'étendue concernée; ils ont été supprimés. Les pages doivent être sélectionnées
par colonnes imprimées, jamais inférées par interpolation de pagination. Cela
est indispensable pour les six segments discontinus de 2035.054 et pour les
bornes de chaque notice.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg26-athanasius/pg26-original-image-only.pdf`.
2. Vérification distante achevée : 94 774 657 octets, 785 pages et SHA-256
   `fb5b12164f77ad1e5296784d1e5e13ffb57b495007c8729e231926fac4a6c4a2`.
3. Conserver avec le PDF les seize mappings et produire, si besoin d'un
   ciblage, un manifeste colonne→image vérifié aux premières et dernières
   feuilles de chaque segment.
4. Tar retiré après validation distante ; les rendus restent régénérables
   depuis le PDF sans OCR et récupérables via l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
