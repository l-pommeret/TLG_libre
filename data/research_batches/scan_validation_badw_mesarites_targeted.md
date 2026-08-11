# Validation ciblée — BAdW CC BY, Nicolaus Mesarites (TLG 3190.002–.005)

## Décision

**READY_TARGETED_IMAGE_ONLY, avec réserve de résolution pour l’OCR maison.**
Les deux PDF officiels BAdW sont explicitement sous CC BY 4.0, l'édition
Heisenberg correspond exactement aux quatre notices canoniques et les
frontières de pages imprimées ont été contrôlées visuellement. Les scans
embarqués sont nets et lisibles, mais leur PPI PDF déclaré est ~70 : archiver
les images exactes sans OCR fournisseur et évaluer séparément le résultat de
l'OCR du projet.

## Sources officielles, licence et intégrité

| PDF BAdW | Notice / licence | Taille et intégrité vérifiées | Pages PDF |
|---|---|---:|---:|
| [003832594.pdf](https://publikationen.badw.de/de/003832594/003832594.pdf) | [fiche BAdW 003832594](https://publikationen.badw.de/de/003832594), CC BY 4.0 | 75 674 941 octets; SHA-256 `a7b54472c3921ecc8a635fc671be2fe733fb44c2dcd5314970581191c9ac39e8` | 96 |
| [003832593.pdf](https://publikationen.badw.de/de/003832593/003832593.pdf) | [fiche BAdW 003832593](https://publikationen.badw.de/de/003832593), CC BY 4.0 | 35 938 826 octets; SHA-256 `e9f786badfb1763ace6e73cb6ace1a420fcf2e7dafedc2606bd74962c4345c08` | 56 |

Les fiches officielles affichent le lien de licence
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.de). Les
PDF sont des pages-image : `003832594` embarque principalement des images
grises 1564 × 2424 px et `003832593` 1524 × 2404 px, chacune déclarée à
environ 70 ppi dans le conteneur PDF. Aucun texte ou OCR fourni par BAdW ne
fait partie du transfert proposé.

## Pagination PDF = pagination imprimée

Les pages PDF et numéros imprimés coïncident dans les plages cibles : p. PDF
6 porte le numéro imprimé 6, p. 54 le 54, p. 15 le 15, p. 25 le 25, p. 34 le
34, p. 35 le 35 et p. 46 le 46. Il ne faut appliquer **aucun décalage** dans le
manifeste de transfert.

| TLG | Édition canonique | PDF | Pages PDF = imprimées à conserver | Images physiques |
|---|---|---|---:|---:|
| 3190.002 — *Renuntiatio rerum politicarum et ecclesiasticarum* | Heisenberg, QSG 1923/3, 6–54 | `003832594.pdf` | **6–54** | 49 |
| 3190.003 — *Disputatio* | Heisenberg, QSG 1923/2, 15–25 | `003832593.pdf` | **15–25** | 11 |
| 3190.004 — *Rogationes ad imperatorem Theodorum Lascarem* | Heisenberg, QSG 1923/2, 25–34 | `003832593.pdf` | **25–35** (p35 partagée, voir ci-dessous) | 11 |
| 3190.005 — *Descriptio itineris Nicaeam* | Heisenberg, QSG 1923/2, 35–46 | `003832593.pdf` | **35–46** | 12 |

Total physique : **49 images** pour `003832594`; **32 images uniques**
`15–46` pour `003832593`; **81 images uniques** au total. Les p. 25 et 35 du
second PDF sont stockées une seule fois mais reliées à leurs deux notices.

## Frontières et corrections de pagination

* **p. 25** contient la fin de `3190.003`, puis le titre et le début grec des
  *Rogationes* `3190.004` : elle est obligatoirement partagée.
* La citation canonique de `3190.004` s'arrête à « 25–34 », mais **p. 35**
  porte encore la fin grecque des *Rogationes* au-dessus du titre « III.
  Reisebericht … » qui introduit `3190.005`. La p. 35 doit donc être gardée et
  marquée partagée : supprimer cette moitié de page tronquerait `3190.004`.
* **p. 46** termine `3190.005` puis commence immédiatement une autre section
  (« Die römische Messe … ») : garder l'image parce que le texte cible s'y
  termine, mais ne relier ni la section suivante ni sa portion de page à
  `3190.005`.
* **p. 6** de `003832594` contient les dernières lignes d'introduction
  allemande puis le début grec de `3190.002`; **p. 54** termine le grec puis
  lance le commentaire allemand. Ces portions non textuelles restent exclues
  du mapping sémantique, sans supprimer les feuilles de borne.

## Échantillons grecs visuels, temporaires et supprimés

| Notice | Pages contrôlées | Résultat |
|---|---|---|
| 3190.002 | p6 (début), p10 (grec courant), p54 (fin) | Grec net, mise en page critique lisible; p54 borne confirmée |
| 3190.003 | p15 (titre « Disputation … », grec) et p25 (fin) | Grec net; transition vers `3190.004` observée |
| 3190.004 | p25 (titre/début), p34 (grec courant), p35 (fin partagée) | Grec net; p35 corrige la borne image de la citation 25–34 |
| 3190.005 | p35 (titre/début partagé), p46 (fin) | Grec net; début de la section suivante isolé sur p46 |

Les PDF et JPEG de contrôle ont été employés uniquement dans `/tmp`, puis
supprimés. Aucun OCR, texte extrait, archive ou image ne reste localement.

## Transfert exécuté et vérifié

1. Les deux PDF BAdW image-only officiels ont été transférés une seule fois,
   sans OCR ni réencodage textuel, afin d'éviter la duplication des pages.
2. Les mappings séparés sont : `3190.002` → `003832594:6–54`; et, depuis
   `003832593`, `3190.003` → `15–25`, `3190.004` → `25–35`, `3190.005` →
   `35–46`.
3. Conserver p. 25 et p. 35 une seule fois avec deux liens TLG; conserver
   l'attribution BAdW/Heisenberg et CC BY 4.0 dans chaque manifeste.
4. Après transfert, les deux fichiers, leurs tailles, SHA-256, les pages partagées
   et l'exclusion des portions allemandes/sections suivantes. Évaluer la
   résolution (~70 ppi déclarés) avant tout OCR maison; ne jamais importer un
   OCR de fournisseur.

Les contrôles distants forcés ont confirmé `003832594.pdf` (75 674 941 octets,
SHA-256 `a7b54472c3921ecc8a635fc671be2fe733fb44c2dcd5314970581191c9ac39e8`)
et `003832593.pdf` (35 938 826 octets, SHA-256
`e9f786badfb1763ace6e73cb6ace1a420fcf2e7dafedc2606bd74962c4345c08`).
Aucun OCR n'a été transféré et aucun asset temporaire ne reste localement.
