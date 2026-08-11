# Audit de remplacement HF — *Patrologia Graeca* 62

## Décision

**READY — le PDF natif image-only peut remplacer le tar de rendus, sous
vérification distante préalable.** Il ne s'agit pas d'une ré-encodage OCR : le
PDF Commons est le fac-similé source. Le tar actuel est une dérivation de ses
pages rendues. Le remplacement réduit fortement le stockage tout en préservant
la source bibliographique et toutes les pages utilisées.

## Provenance et identité vérifiées

* **Page source :** [Wikimedia Commons — *Patrologia Graeca* 62](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._062.pdf)
* **Original direct :** [PDF image-only](https://upload.wikimedia.org/wikipedia/commons/f/f6/Patrologia_Graeca_Vol._062.pdf)
* **Métadonnées Commons interrogées le 2026-08-11 :** MIME
  `application/pdf`, taille `107694134` octets, SHA-1
  `c8f546fcca368c19a6508117538cbe0b9fba84cd`, rendu 1025 × 1577 px
  (~155 ppi), 814 pages.
* **Droits :** `Public domain` ; `Copyrighted: False` dans les métadonnées
  Commons. `data/scan_sources.csv` consigne aussi `Creative Commons Public
  Domain Mark 1.0`.

## Comparaison avec l'archive HF courante

| Élément | Valeur |
|---|---:|
| Archive rendue actuelle | `webdataset/volumes--pg62-chrysostom--8e56bce80f79.tar` |
| État HF | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images rendues | 791 |
| Taille tar | 658 698 240 octets |
| SHA-256 du manifeste/tar vérifié | `035e2fb94cf7931201399429bc37cfdb0c7a2607a4d8a6d65884bf0b771af41a` |
| PDF source natif | 107 694 134 octets |
| Gain estimé | 551 004 106 octets (83,65 %) |

Le tar de 791 images correspond exactement au manifeste déjà validé : pages
PDF **14–804 incluses** (`804 - 14 + 1 = 791`). Le PDF natif possède 814 pages :
les pp. 1–13 (préface) et 805–814 (hors bornes canoniques) restent présentes
dans le conteneur source, mais ne constituent ni une perte ni une extension de
la couverture TLG si le manifeste de sélection est conservé.

## Couverture canonique préservée

Le rapport `scan_validation_pg62_chrysostom.md` valide 30 notices directes :

* 2062.159–.167 : cols MPG 9–720 ;
* 2720.026 : 721–724 ;
* 2062.318–.336 : courts loci chevauchants 723–780, dont les labels `[Sp.]`
  doivent demeurer associés aux notices ;
* 2755.033 : 727–730.

Les contrôles visuels déjà documentés confirment le grec aux bornes utiles :
p.14 ouvre les cols 9 sqq., p.784 porte 761–762, p.802 777–778 et p.804
clôt 779–780. La conservation de la page source PDF, avec le manifeste
`14–804`, préserve donc toutes les images des loci et les chevauchements courts.

## Procédure exécutée et vérifiée

1. Original déposé sous
   `scans/volumes/pg62-chrysostom/pg62-original-image-only.pdf`.
2. Vérification distante achevée : taille `107694134`, 814 pages et SHA-256
   `96981936718bf2a9f4f5a83a9fb788df2a6a239bbfcf841b05c6501215dc2e6a`.
3. Conserver avec lui un manifeste déclarant que l'ensemble d'ingestion TLG est
   `PDF pages 14–804`, et que les pp. 1–13 et 805–814 sont hors cible.
4. Le tar de 791 rendus a été supprimé après ces contrôles. La suppression reste
   réversible via l'historique HF ; recréer les rendus à partir du PDF ne requiert
   aucun OCR fournisseur.

## Limite de l'équivalence

Le remplacement n'est pas une identité binaire avec les JPEG du tar : il
conserve la **source image-only native**, pas son cache de rendus. Il est donc
sans perte documentaire et bibliographique, mais les consommateurs qui exigent
un WebDataset devront rendre localement les pages 14–804 à partir du PDF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit ni conservé d'OCR.
