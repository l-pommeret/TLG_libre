# Audit de remplacement HF — *Patrologia Graeca* 95

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** La
compaction conserve le périmètre exact déjà validé de 19 notices TLG directes
dans l'édition Migne. Les renvois sans locus MPG 95 canonique restent exclus.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 95](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._095.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/c/c1/Patrologia_Graeca_Vol._095.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  88 078 720 octets, SHA-1 `bd2888d9fee25c83e25553706edc4f05e0876143`,
  1070 × 1702 px. Le rapport de validation documente 834 pages et des rendus
  de ~145 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg95-john-damascene--a76430756999.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 834 |
| Taille tar | 610 304 000 octets |
| SHA-256 tar/manifeste | `dabd4b0798d88f2a1fed08a3a6b7cbc6c0b84b5ba32f602c698a989d1dc9d680` |
| PDF natif | 88 078 720 octets ; 834 pages |
| Gain estimé | 522 225 280 octets (85,57 %) |

Le PDF source et le tar portent le même volume de 834 pages. Le premier peut
donc remplacer le second comme contenant de fac-similé sans perte de pages ni
de provenance bibliographique. Ce n'est pas une identité binaire avec les
JPEG : les pages seront rendues à partir du PDF au besoin. Cette restitution
doit rester image-only, sans extraction ou conservation d'OCR fournisseur.

## Couverture et preuve grecque déjà validées

`scan_validation_pg95_john_damascene.md` fixe les 19 correspondances directes :

| Notices TLG | Colonnes MPG 95 |
|---|---:|
| 2934.021, .035–.048 | 64–77 ; 9–17 ; 80–84 ; 85–97 ; 225–228 ; 228 ; 228–229 ; 229 ; 229–232 ; 232–233 ; 233 ; 233–236 ; 236–237 ; 244–245 ; 248–277 |
| 2934.050–.053 | 345–385 ; 388–396 ; 405–412 ; 441–1033 |
| 3173.002 | 309–344 |

Les contrôles éphémères de p. 20 (cols 31–32), p. 350 (663–664) et p. 600
(1173–1174) ont confirmé un grec lisible et net, notamment dans le texte dense
et les annotations; ils ont tous été supprimés. Les bornes de colonnes communes
doivent être dédupliquées. Les clés 2102.x03/.x05/.x06, 1443.x01 et
2934.015/.x02 demeurent exclues : aucun locus MPG 95 n'est fourni par le canon.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg95-john-damascene/pg95-original-image-only.pdf`.
2. Vérification distante achevée : 88 078 720 octets, 834 pages et SHA-256
   `7011ed3df79c46b3dfd44f2ed9cd4fa3caf7532860821fc7df20a335e2d0ed30`.
3. Attacher au PDF le mapping des 19 notices et ses exclusions ci-dessus.
4. Tar retiré après validation distante ; il reste régénérable depuis le PDF
   sans OCR et récupérable via l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
