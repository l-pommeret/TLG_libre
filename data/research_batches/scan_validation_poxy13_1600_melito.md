# Validation de scan — *The Oxyrhynchus Papyri* XIII, P.Oxy. 1600

**Décision : READY — témoin partiel seulement, extraction image-only ciblée.**
Le fichier Commons de l'édition imprimée de 1919 est absent de
`data/scan_sources.csv` et de `scans/`. Il couvre précisément P.Oxy. XIII
1600, l'un des trois témoins explicitement réunis par le canon pour TLG
`1495.001` (*De pascha*), mais **ne couvre ni P.Beatty 8 ni P.Bodmer 13** et
ne peut donc pas être présenté comme une acquisition du texte complet.

| Contrôle | Résultat vérifié |
|---|---|
| Source / édition | [Wikimedia Commons — *The Oxyrhynchus Papyri*, part XIII](https://commons.wikimedia.org/wiki/File:The_Oxyrhynchus_papyri,_part_13._Bernard_Pyne_Grenfell,_Arthur_Surridge_Hunt._1919_(IA_oxyrhynchusppt1300grenuoft).pdf), Grenfell & Hunt, Londres, Egypt Exploration Society, 1919. Le volume imprimé identifie `1600. Treatise on the Passion` aux pp. 19–21. |
| Concordance canonique | Le canon TLG 1495.001 définit *De pascha* par le composite `P. Beatty 8 + P. Bodmer 13 + P. Oxy. 13.1600` et cite Perler 1966, pp. 60–126. Le candidat est donc l'édition princeps imprimée du seul composant P.Oxy. 1600, non l'édition Perler et non une reproduction photographique des trois manuscrits. |
| Droits | Commons déclare le scan **PD-old / PD-scan** et **CC Public Domain Mark 1.0** : statut explicitement libre pour les images du livre de 1919. |
| Fichier / technique | PDF Commons, 268 pages, 12,42 Mo ; raster source annoncé `1 062 × 1 491` px par page. Commons ne publie ni paquet JP2, ni SHA-1, ni PPI. Les rendus distants inspectés à 960 px sont suffisamment nets pour les caractères grecs imprimés. |
| Limite d'attribution | L'introduction de 1919 décrit 1600 comme un traité de la Passion et propose encore prudemment Hippolyte comme possibilité. L'usage pour TLG 1495.001 repose donc sur le raccord explicite du canon au témoin `P.Oxy. 13.1600`, pas sur une réécriture de l'attribution historique incertaine de l'édition princeps. |

## Mapping visuel vérifié

| Page PDF Commons | Page imprimée | Contenu observé |
|---:|---:|---|
| `31` | 19 | Fin de 1599 puis titre `1600. Treatise on the Passion` et description du papyrus. La page est nécessaire pour le titre et le début de l'introduction. |
| `32` | 20 | Texte grec édité de P.Oxy. 1600, recto et verso, avec fragment 2 recto. |
| `33` | 21 | Suite/notes de 1600 et clôture de l'article ; le bas de page ouvre déjà 1601, à ne pas confondre avec le témoin cible. |

## Recommandation

Acquérir seulement les images de pages Commons **31–33 incluses** (3 images)
et les étiqueter `TLG1495.001 / P.Oxy XIII 1600 / PARTIAL_WITNESS`. Les pages
31 et 33 contiennent respectivement un reliquat de 1599 et le début de 1601,
mais sont indispensables aux bornes de l'article 1600 ; aucune découpe ou
extension ne doit être inférée. Conserver l'URL Commons, le statut PDM, les
dimensions et les empreintes calculées lors de l'acquisition effective.

Cette source sert uniquement de route licite vers le **témoin partiel
imprimé** ; elle n'autorise ni une reconstruction complète de *De pascha*, ni
l'usage d'OCR fournisseur. Les rendus JPEG et HTML temporaires employés pour
le contrôle ont été supprimés ; aucun PDF, OCR ou archive d'images n'a été
conservé localement, et aucun commit/push n'a été effectué.
