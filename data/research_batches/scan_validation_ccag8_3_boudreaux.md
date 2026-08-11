# Validation de scan — Boudreaux, *CCAG* 8.3 (1912)

**Candidat :** Internet Archive
[`CatalogusCodicumAstrologorumGraec8p3`](https://archive.org/details/CatalogusCodicumAstrologorumGraec8p3).

**Sélection.** Cet identifiant a été recherché explicitement dans
`data/scan_sources.csv` et sous `scans/` : il n’y est pas présent. Il s’agit
de l’édition Boudreaux, *Codices Parisini*, *Catalogus Codicum Astrologorum
Graecorum* 8.3, Bruxelles, Lamertin, 1912, soit l’édition, le volume, le lieu
et l’année des deux notices du canon.

**Décision : READY, avec réserve technique.** Le fichier processed est de
50,6 Mo et porte une licence Public Domain Mark explicite. Les trois pages
contrôlées sont très lisibles à la consultation web (grec, apparat et notes) et
les deux plages canoniques sont présentes. La métadonnée IA annonce cependant
`ppi=72`, anormalement faible par rapport au rendu : conserver cette valeur
dans le manifeste et recontrôler la résolution effective avant une extraction
en masse. Aucun OCR n’a été ouvert ni utilisé.

## Concordance canonique

| Notice TLG | Référence du canon | Contrôle visuel / pagination |
| --- | --- | --- |
| 1144.004 — *Fragmenta* (e cod. Paris.) | P. Boudreaux, *Codices Parisini*, CCAG 8.3, Bruxelles, 1912, pp. 104–119 | `n119` est la p. 104 et `n126` la p. 111 : texte grec et notes éditoriales continus au sein de la plage canonique. |
| 2577.003 — *Περὶ γεννήσεως* [Dub.] | Boudreaux, ibid., p. 188 | `n203` est la p. 188 : en-tête **EXCERPTA EX CODICE 45 (PARIS. GR. 2381)**, puis **Ἀνατολίου περὶ γεννήσεως**, exactement le codex et le titre de la notice. |

## Métadonnées Internet Archive

| Champ | Valeur contrôlée |
| --- | --- |
| Identifiant / titre | `CatalogusCodicumAstrologorumGraec8p3` — *Catalogus codicum astrologorum graecorum. VIII. Codicum parisinorum partem tertiam* |
| Créateur / édition | Pierre Boudreaux ; Bruxelles, Henri Lamertin, 1912 |
| Droits | `licenseurl=http://creativecommons.org/publicdomain/mark/1.0/` |
| Imagecount / PPI | 250 fichiers JP2 processed ; `ppi=72` dans IA (réserve technique) |
| JP2 processed | `Catalogus_codicum_astrologorum_graec_8p3_jp2.zip`, 50,621,608 octets, 250 fichiers, SHA-1 `8f1514a2a5c21cf5c1d55e6ff4308a2f3ea49862` |
| JP2 original | Aucun paquet original distinct exposé dans les métadonnées IA ; ne pas inférer un SHA-1 ou une taille. |
| Scandata | `Catalogus_codicum_astrologorum_graec_8p3_scandata.xml`, 82,701 octets, SHA-1 `249aac7f20f46ae1af9a2064785b0d456e672694` |

## Contrôles visuels temporaires

Trois JPEG BookReader à 1400 px ont été téléchargés provisoirement dans
`/tmp`, inspectés visuellement, puis supprimés avec leur répertoire temporaire.
Ils n’ont jamais été OCRisés ni ajoutés au dépôt.

| Vue | Feuillet IA / page imprimée | Résultat |
| --- | --- | --- |
| [début 1144.004](https://archive.org/download/CatalogusCodicumAstrologorumGraec8p3/page/n119_w1400.jpg) | `n119`, p. 104 | Texte grec, apparat et notes très lisibles ; début de la plage canonique 104–119. |
| [milieu 1144.004](https://archive.org/download/CatalogusCodicumAstrologorumGraec8p3/page/n126_w1400.jpg) | `n126`, p. 111 | Continuité de l’édition Boudreaux et qualité homogène. |
| [2577.003](https://archive.org/download/CatalogusCodicumAstrologorumGraec8p3/page/n203_w1400.jpg) | `n203`, p. 188 | Titre du codex Paris. gr. 2381 et **Ἀνατολίου περὶ γεννήσεως** : correspondance exacte. |

## Suite autorisée

Le volume est admissible comme source distante d’images, avec le SHA-1 du
paquet processed, la licence PDM et la réserve PPI ci-dessus. Aucune archive
complète ni aucun dérivé OCR n’a été téléchargé pendant la validation.
