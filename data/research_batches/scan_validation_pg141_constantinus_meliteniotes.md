# Validation de scan — *Patrologia Graeca* 141, Constantinus Meliteniotes

**Décision : READY — extraction image-only ciblée.** Le fichier Commons
[`Patrologia Graeca Vol. 141.pdf`](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._141.pdf)
est absent de `data/scan_sources.csv` et aucun chemin d'images correspondant
n'existe dans `scans/`. Les contrôles sont faits sur les rendus d'images
individuels de Commons ; le PDF n'a pas été téléchargé.

| Contrôle | Résultat vérifié |
|---|---|
| Notice / édition | TLG `4443.002`, *Orationes de processione spiritus sancti*, canon : MPG 141, cols. 1032–1273. Le volume est la *Patrologiae cursus completus*, vol. 141, J.-P. Migne (1857–1866) ; la page de titre imprimée confirme `Constantini Meliteniotae` et *De ecclesiastica unione Latinorum et Graecorum, et de processione Spiritus Sancti per Filium*. |
| Droits | [CC Public Domain Mark 1.0](https://creativecommons.org/publicdomain/mark/1.0/) explicite sur la page Commons ; aucune attribution imposée. |
| Fichier source | PDF Commons, 754 pages, 89,19 Mo ; raster source annoncé `995 × 1 620` px par page. Il ne s'agit pas d'une archive IA : aucun paquet JP2, SHA-1 d'archive ou PPI n'est publié par Commons. Conserver l'URL, la licence, les dimensions et les URL d'images comme provenance. |
| Qualité | Les quatre rendus distants vérifiés à 960 px de large (source 995 px) sont nets, complets et lisibles en grec/latin. Ils conviennent à une OCR ultérieure effectuée par le projet, sans employer aucun OCR du fournisseur. |

## Mapping visuel vérifié

La règle constatée sur cette séquence est : page PDF Commons `N` porte les
colonnes `2N−45` (gauche) et `2N−44` (droite). Elle est vérifiée aux quatre
bornes ci-dessous, et non inférée du seul nombre total de pages.

| Page PDF Commons | Colonnes visibles | Preuve de concordance |
|---:|---:|---|
| `538` | 1031–1032 | La colonne 1032 est visible en haut à droite ; au milieu de la même image commence le titre grec et latin de Constantinus, *Oratio I*. Cette image est nécessaire malgré la colonne 1031 hors notice. |
| `591` | 1137–1138 | En-tête *De processione S. Spiritus Orat. I* et texte continu : fin de l’*Oratio I*. |
| `592` | 1139–1140 | Titre grec/latin *De processione Spiritus Sancti etiam ex Filio*, *Oratio II* : la coupure bibliographique signalée entre 1137 et 1140 est ainsi matérialisée, sans trou. |
| `659` | 1273–1274 | En-tête *De processione S. Spiritus Orat. II* ; colonne 1273 à gauche et sa continuation grecque/latine. Cette image est nécessaire malgré 1274 hors notice. |

## Bornes d’ingestion et recommandation

Extraire seulement les pages-images Commons **538–659 incluses** (122 images),
en préservant les deux pages de bord qui contiennent respectivement les
colonnes 1032 et 1273. Inclure sans interruption les pages 591–592 : elles
documentent le passage de l’*Oratio I* à l’*Oratio II* (cols. 1137–1140).
Télécharger directement les images de pages rendues ou leurs originaux image
équivalents, et non le PDF ni du texte/OCR fournisseur. Avant toute ingestion,
enregistrer les URL exactes, tailles et empreintes calculées sur les images
effectivement retenues.

Les quatre JPEG de vérification et les pages HTML intermédiaires ont été
supprimés après inspection. Aucun OCR, PDF ni archive d’images n’a été
conservé localement, et aucun commit/push n’a été effectué.
