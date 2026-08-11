# Audit de remplacement HF — *Patrologia Graeca* 28

## Décision

**READY pour remplacer le gros tar rendu par le PDF Commons image-only.**
Cette compaction conserve la couverture déjà validée de 47 notices TLG qui
citent directement MPG 28, avec les attributs *spuria* et les segments
non contigus. Les renvois 2035.x07–x12 et le duplicat 5119.001 restent exclus
du décompte conformément au rapport de validation.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 28](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._028.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/c/c3/Patrologia_Graeca_Vol._028.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  97 254 718 octets, SHA-1 `54b2e051fc2db65bde61cb78389eaba0834d5566`,
  987 × 1581 px. Le rapport de validation documente 842 pages et ~149 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est enregistré dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg28-athanasius-spuria--fcf233658a7a.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 842 |
| Taille tar | 624 732 160 octets |
| SHA-256 tar/manifeste | `dc92b92afd37f0163facba67411e0f624473019924b5ded1a3417c152ff244bc` |
| PDF natif | 97 254 718 octets ; 842 pages |
| Gain estimé | 527 477 442 octets (84,43 %) |

Le PDF et le tar correspondent au même volume de 842 pages. Il peut donc
remplacer le contenant de fac-similé sans perte de pages ni changement
bibliographique. Le format de distribution change : il faudra produire de
nouveau les images depuis le PDF si elles sont requises. Cette production doit
rester image-only; aucun texte intégré ou OCR tiers ne doit être extrait.

## Couverture, bornes et preuve grecque déjà validées

`scan_validation_pg28_athanasius_spuria.md` consigne toutes les bornes
colonne→notice des 47 notices directes (2035.064–.109 avec lacunes,
2035.125–.126 et 2800.003–.008). Les limites imprimées s'étendent de cols
29–80 (2035.064) à 1637–1644 (2035.126). Il faut préserver, en particulier,
les trois segments de 2035.109 (1116–1173a; 1201c–1249b; 1265c–1285b) et
dédupliquer les bornes communes 501, 597, 700, 773, 849 et 1081.

La validation existante apporte trois preuves grecques réparties sur toute
l'étendue : PDF p. 30, cols 47–48 (*DUBIA*), p. 430, cols 843–844 (*SPURIA*)
et p. 830, cols 1643–1644 (*ADDENDA*). Elles sont grec/latin nettes et ont été
supprimées après contrôle. La résolution moyenne (~149 ppi) est jugée
visuellement exploitable; aucun échantillon, PDF ou OCR local ne demeure.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg28-athanasius-spuria/pg28-original-image-only.pdf`.
2. Vérification distante achevée : 97 254 718 octets, 842 pages et SHA-256
   `07e4f263a7aa3e88fee398c0115b37c3c758b328037f53d4b3e8cadf60dbeffb`.
3. Conserver avec le PDF le manifeste source 47-notices et ses exclusions;
   toute extraction ultérieure doit se faire par colonnes imprimées.
4. Tar supprimé après ces vérifications ; les rendus sont régénérables depuis
   le PDF sans OCR, et le tar reste récupérable dans l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
