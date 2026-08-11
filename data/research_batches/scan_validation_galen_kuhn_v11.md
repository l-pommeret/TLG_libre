# Validation de scan — Kühn, *Galeni opera omnia*, XI (BIU Santé)

**Décision : READY — source d’images, avec ingestion ciblée recommandée.** `BIUSante_45674x11` a été vérifié absent de `data/scan_sources.csv` et de `scans/`. Il reproduit le tome XI de Kühn, édition explicitement prescrite par cinq notices canoniques ; une sixième notice y commence et se poursuit au tome XII.

| Contrôle | Résultat vérifié |
|---|---|
| Source / édition | [Internet Archive — BIUSante_45674x11](https://archive.org/details/BIUSante_45674x11), *Galeni opera omnia*, XI, Leipzig, Car. Cnoblochii. La date IA `1821/1833` est générique de la série ; le titre de tome, les titres d’œuvres et les paginations imprimées concordent avec le canon. |
| Droits | [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence), explicitement déclarée dans la métadonnée IA. |
| JP2 traité | `BIUSante_45674x11_jp2.zip`, 516 459 519 octets, SHA-1 `8861915a2d8e92118c82d86d5e29d111a215cd79`. Aucun paquet JP2 original distinct n’est fourni. |
| Scandata / images | `BIUSante_45674x11_scandata.xml`, 319 370 octets, SHA-1 `9fc813ba3e0438978dd6ec9ecbc0b3167df59a10`; 898 images déclarées, 299 ppi par feuille. |
| Qualité | Les échantillons grecs/latins sont nets et complètement cadrés, malgré un léger bruit de fond. La couverture scannée est inversée, sans incidence sur les feuilles textuelles. |

## Concordance canonique et bornes IA

La pagination `scandata` établit le décalage stable `feuille IA = page imprimée + 2` sur les segments textuels.

| Notice TLG | Œuvre | Pages Kühn XI | Feuilles IA | Couverture |
|---|---|---:|---:|---|
| 0057.067 | *Ad Glauconem de medendi methodo* II | 1–146 | `n3`–`n148` | Complète |
| 0057.068 | *De venae sectione adversus Erasistratum* | 147–186 | `n149`–`n188` | Complète |
| 0057.069 | *De venae sectione adversus Erasistrateos Romae degentes* | 187–249 | `n189`–`n251` | Complète |
| 0057.070 | *De curandi ratione per venae sectionem* | 250–316 | `n252`–`n318` | Complète |
| 0057.071 | *De hirudinibus, revulsione, cucurbitula, incisione et scarificatione* | 317–322 | `n319`–`n324` | Complète |
| 0057.075 | *De simplicium medicamentorum temperamentis ac facultatibus* XI | 379–892 | `n381`–`n894` | Segment XI seulement ; la suite canonique est au tome XII, donc ne pas déclarer la notice complète avant validation de ce second tome. |

## Contrôle visuel temporaire

| Feuille / page | Observation |
|---|---|
| `n3`, p. 1 | Titre grec et latin **Ad Glauconem de medendi methodo liber I**, début exact de 0057.067. |
| `n319`, p. 317 | Titre grec et latin **De hirudinibus, revulsione, cucurbitula, incisione et scarificatione**, ouverture exacte de 0057.071. |
| `n894`, p. 892 | Page 892 de *De simplicium medicamentorum…*, grec, latin et apparat nettement lisibles : borne finale du segment XI de 0057.075. |

Les cinq JPEG de contrôle et le fichier `scandata.xml` ont été supprimés après inspection. Aucun OCR, PDF ou paquet d’images n’a été téléchargé ni conservé.

## Recommandation d’ingestion

Le paquet total dépasse légèrement le seuil préférentiel de 500 Mo. Privilégier l’ingestion image-only directement vers le dépôt distant des plages `n3`–`n324` et `n381`–`n894`, ou du volume entier si cette simplification opérationnelle est préférable. Enregistrer `0057.067`–`0057.071` comme **READY** ; rattacher le segment XI de `0057.075` comme couverture partielle, en attente du tome XII. Exclure strictement tous les dérivés OCR.
