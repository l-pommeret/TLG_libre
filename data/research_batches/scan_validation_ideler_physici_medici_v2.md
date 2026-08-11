# Validation de scan — Ideler, *Physici et medici Graeci minores*, II

## Décision

**READY.** `b33490983_0002` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. Son index imprimé et les pages contrôlées concordent avec les sept notices TLG dont le canon prescrit le tome II d'Ideler, pp. 194–327. La source déclare explicitement le **Creative Commons Public Domain Mark 1.0**, le paquet JP2 traité fait 384 Mo et les images à 360 ppi sont nettement lisibles. Aucun OCR n'a été ouvert ou utilisé.

La métadonnée IA indique l'année 1841, alors que le canon désigne le tome II comme « 1842 » : cette divergence de catalogue est conservée, mais le contenu imprimé tranche la question de concordance, puisque l'index de l'exemplaire place précisément les textes de pp. 194, 282, 303, 305, 307, 317 et 323–327.

## Concordance canonique et pagination

| Notice TLG | Œuvre | Pages selon le canon | Preuve dans l'exemplaire |
|---|---|---:|---|
| 0721.009 | *De diaeta* | 194–198 | Index p. 194; début du texte visible p. 194 |
| 0721.011 | *Περὶ λυκανθρωπίας* | 282 | Index p. 282 |
| 0721.012 | *De urinis secundum Syros* | 303–304 | Index p. 303; début visible p. 303 |
| 0721.013 | *De urinis secundum Persos* | 305–306 | Index p. 305 |
| 0721.014 | *Commentatio de urinis* | 307–316 | Index p. 307 |
| 0721.015 | *De pulsibus* | 317 | Index p. 317 |
| 0721.016 | *De urinis in febribus* | 323–327 | Index p. 323; fin visible p. 327 sous l'en-tête *IN FEBRIBUS* |

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / source | `b33490983_0002` — [Internet Archive](https://archive.org/details/b33490983_0002) |
| Titre / créateur / date IA | *Physici et medici Graeci minores...* ; Julius Ludwig Ideler ; 1841 (voir réserve de catalogue ci-dessus) |
| Fichier image traité | `b33490983_0002_jp2.zip` |
| SHA-1 / taille / nombre d'images | `54c74e3a41c777f8a6f2de1034146bca0a4934e6` ; 384 501 241 octets ; 480 images |
| Original distinct | aucun paquet d'images original distinct publié dans les métadonnées IA |
| Données de numérisation | `b33490983_0002_scandata.xml` ; SHA-1 `a827b5b7f967544d74e5271f51c8e2795badaf04` ; 571 510 octets |
| PPI / qualité | 360 ppi déclarés; grec et pagination nets dans les contrôles |
| Droits | champ IA `rights` : [Creative Commons Public Domain Mark 1.0](http://creativecommons.org/publicdomain/mark/1.0/) |

## Contrôles visuels temporaires

Les vues BookReader suivantes ont été récupérées temporairement à distance, inspectées, puis supprimées :

| Vue | Page imprimée | Constat |
|---|---:|---|
| `n10` | index | La table imprime les entrées *Anonymou peri diaites* p. 194, *Peri lykanthropias* p. 282 et les séries urinaires p. 303–317/323. |
| `n203` | 194 | Titre grec « ΠΕΡΙ ΔΙΑΙΤΗΣ ΑΝΩΝΥΜΟΥ », début lisible de 0721.009. |
| `n312` | 303 | Titre « ΕΚ ΣΥΡΙΚΟΥ ΒΙΒΛΙΟΥ — Περί ούρων », début lisible de 0721.012. |
| `n336` | 327 | En-tête *IN FEBRIBUS*, fin lisible de 0721.016. |

Les fichiers de vue, y compris les repérages intermédiaires, ont été détruits après contrôle; aucune image ni archive n'est conservée localement.

## Action recommandée

Ajouter le volume comme source d'images `REMOTE_ONLY` pour les sept notices ci-dessus : édition et bornes imprimées confirmées, droits explicites PDM, intégrité et qualité technique suffisantes. Conserver la différence 1841/1842 dans le manifeste de provenance, sans la confondre avec une divergence de contenu.
