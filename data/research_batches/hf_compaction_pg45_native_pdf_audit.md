# Audit de remplacement HF — *Patrologia Graeca* 45

## Décision

**READY pour remplacer le tar par le PDF Commons PDM.** Le PDF natif est
l'édition Migne exacte, PDM explicite, et comporte les mêmes 696 feuilles que
le tar. Le manifeste TLG est volontairement limité à la seule notice canonique
directe `2017.076`; les autres pages du tome ne deviennent pas des cibles par
le seul fait d'être conservées dans le fac-similé.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 45](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._045.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/e/e8/Patrologia_Graeca_Vol._045.pdf)
* **API Commons contrôlée le 2026-08-12 :** MIME `application/pdf`,
  85 176 089 octets, SHA-1 `9a5da041d7f2e3b83edd239f15c0834ec02577a8`,
  1025 × 1556 px. Le registre établit 696 pages; Commons ne publie ni paquet
  JP2 séparé ni PPI natif distinct.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); la provenance est consignée comme
  `Creative Commons Public Domain Mark 1.0` dans `data/scan_sources.csv`.

Le comparateur Internet Archive `patrologiaecursu45mignuoft` (698 vues, JP2
300 ppi, licence non déclarée) est seulement une preuve de pagination et de
qualité de la même édition. Il ne remplace pas le PDF Commons et ne doit pas
être transféré dans cette compaction.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg45-gregory-nyssa--ca7e12e5c285.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 696 |
| Taille tar | 529 561 600 octets |
| SHA-256 tar/manifeste | `7e817238a8a97c18acae9d337d9b718ef5efabcbb13ab22fb172f4de6c6e2387` |
| PDF natif Commons | 85 176 089 octets ; 696 pages |
| Gain estimé | 444 385 511 octets (83,92 %) |

Le tar et le PDF Commons ont le même nombre de feuilles. Le PDF peut donc
remplacer le tar comme fac-similé sans perte de page, d'édition ni de
provenance. Les JPEG rendus ne sont pas byte-identiques au PDF, mais sont
régénérables depuis lui. Le remplacement reste image-only : aucun OCR
fournisseur, texte dérivé ou fichier OCR ne doit être transféré.

## Mapping strict et preuve grecque

Le registre contient exactement une ligne `ARCHIVED_DIRECT_REGISTRY_MAPPING` :

| TLG | Édition et colonnes MPG 45 | Repères IA non transférables |
|---|---:|---:|
| 2017.076 — *Epistula canonica ad Letoium* | 221–236 | `n120–n127` |

Les vues IA temporaires, depuis supprimées, couvrent toute la notice : `n120`
(cols. 221–222, titre et début), `n124` (229–230, grec net au milieu) et
`n127` (235–236, fin). Le papier est légèrement jauni, mais l'image et la mise
en page sont nettes. Ces contrôles confirment l'édition et ses colonnes; ils
ne sont pas une licence IA ni une équivalence de numérotation avec les 696
pages du PDF Commons. Avant un dispatch ciblé, vérifier sans conservation
locale ces mêmes colonnes et au moins une page grecque dans le PDF Commons.

## Exclusions et absence d'alternatives

La recherche dans le Canon ne retourne aucune autre notice avec un locus
`MPG 45`; il n'existe pas non plus de mapping alternatif PG45 dans le registre.
Le manifeste doit donc rester limité à `2017.076`, cols. 221–236 (huit feuilles
repères dans l'édition IA). Toutes les préfaces, apparats, traductions et
feuilles hors de cette plage sont hors cible TLG et ne doivent pas être
sélectionnés ou qualifiés de couverture implicite.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg45-gregory-nyssa/pg45-original-image-only.pdf`.
2. Chemin, 85 176 089 octets, SHA-256 et 696 pages vérifiés à distance avant
   toute suppression.
3. Le mapping `2017.076` et l'exclusion de toutes les
   autres feuilles; ne pas créer de statut alternatif.
4. Tar retiré seulement après ces vérifications distantes; tout rendu reste
   régénérable depuis le PDF, sans OCR.

Le téléchargement distant forcé a confirmé le SHA-256
`d320e836f92be020a56521a15c2d0ad37e4bdc1516820e3c651d5e2340f98a9d`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
