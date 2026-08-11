# Audit de remplacement HF — *Patrologia Graeca* 65

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** La
compaction conserve les 18 notices à concordance directe, leurs bornes MPG
imprimées, leurs attributions (dont les deux `[Sp.]`) et l'exclusion explicite
de `4110.x07`. Elle ne transforme pas les 690 pages du volume en couverture
canonique : seules les plages ci-dessous sont des loci TLG exploitables.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 65](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._065.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/2/2b/Patrologia_Graeca_Vol._065.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  81 392 703 octets, SHA-1 `1b631a378480d3bd0b6ecdd7192817917c681590`.
  Le rapport de validation documente 690 pages, 1010 × 1550 px et environ
  153 ppi (aucun PPI séparé n'est publié par Commons).
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); la provenance est déjà consignée comme
  `Creative Commons Public Domain Mark 1.0` dans `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg65-proclus-apophthegmata--0668c3e0bc2d.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 690 |
| Taille tar | 503 121 920 octets |
| SHA-256 tar/manifeste | `c3e31d2d80fa354f122da18dad116a2c4ead2f0914f6289a3a47dfe6688ba9e3` |
| PDF natif | 81 392 703 octets ; 690 pages |
| Gain estimé | 421 729 217 octets (83,82 %) |

Le tar et le PDF couvrent les mêmes 690 feuilles. Le PDF peut donc le
remplacer comme fac-similé sans perte de page, d'édition ni de provenance.
Les JPEG rendus ne sont pas byte-identiques au PDF, mais sont régénérables à
partir de celui-ci. Ce remplacement reste strictement image-only : aucun OCR
fournisseur, texte dérivé ou fichier OCR ne doit être transféré.

## Mappings stricts, exclusions et preuve grecque déjà validée

`scan_validation_pg65_proclus_apophthegmata.md` établit les 18 notices directes
ci-dessous. Toute sélection future doit suivre les **colonnes imprimées**,
plutôt qu'une estimation par numéro de page PDF ; les bornes communes sont à
conserver une seule fois tout en restant reliées aux deux notices.

| Notices TLG | Colonnes MPG 65 |
|---|---:|
| 4139.017 | 16–25 |
| 2742.001 | 72–440 |
| 2021.028 `[Sp.]` | 161–168 |
| 2755.006–.010 | 757–764 ; 764–772 ; 772–777 ; 777–781 ; 781–788 |
| 2755.011–.015 | 788–789 ; 789–796 ; 796–800 ; 800–805 ; 805–808 |
| 2755.016–.019 | 809–817 ; 817–821 ; 821–828 ; 833–837 |
| 2755.039 `[Sp.]` | 849–852 |

`4110.x07` (MPG 65, cols. 173–176) est uniquement un renvoi à
`2742.001`, sans œuvre autonome : **il reste exclu**. Les éventuels textes du
volume sans borne MPG canonique directe restent exclus eux aussi. Les marqueurs
`[Sp.]` de `2021.028` et `2755.039` sont des attributions du Canon et doivent
être maintenus, sans les réattribuer à l'auteur affiché.

La validation déjà effectuée a contrôlé et supprimé trois rendus temporaires :
page PDF 13 (cols. 17–18, *Oratio in Dei apparitionem*, `4139.017`), page 200
(cols. 355–356, grec/latin net au sein de `2742.001`) et page 430 (cols.
803–804, grec/latin net dans la série Proclus `2755.006–.039`). Ces preuves
échantillonnent le début, milieu et fin de l'étendue utile 16–852 ; lors d'une
extraction ciblée, contrôler à nouveau visuellement les feuilles de début et
de fin de chaque segment contre les colonnes imprimées.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg65-proclus-apophthegmata/pg65-original-image-only.pdf`.
2. Chemin, 81 392 703 octets, SHA-256 et 690 pages vérifiés à distance avant
   toute suppression.
3. Les 18 mappings, les deux marqueurs `[Sp.]` et
   l'exclusion `4110.x07`; dédupliquer les feuilles aux bornes communes.
4. Tar retiré seulement après ces vérifications distantes; les rendus
   resteront régénérables depuis le PDF, sans OCR.

Le téléchargement distant forcé a confirmé le SHA-256
`ab7c89101fd3ea12066ae462a8f90f852be3a36275599b81b70e251a64bee589`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
