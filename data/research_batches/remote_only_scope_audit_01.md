# Audit de périmètre — REMOTE_ONLY transférés comme volumes

Audit effectué sans modifier `data/scan_sources.csv` ni les contenus distants. Ne sont signalés que les items dont le rapport de validation borne effectivement une plage grecque; les volumes dont le rapport valide le tome entier comme pertinent ne sont pas mélangés à cette liste.

| Identifiant / chemin distant | Preuve du rapport | Feuilles à garder | Feuilles hors cible à supprimer | État |
|---|---|---|---|---|
| `BIUSante_44233x01` / `scans/volumes/puschmann-alexander-1878/vol1` | `scan_validation_puschmann_alexander_v1.md` : pp. 441–617 = `n453–n629` | `n453–n629` (177) | `n1–n452`, `n630–n632` (455) | **déjà appliqué** : la ligne registre annonce 177 images et 455 vues retirées |
| `BIUSante_44233x02` / `scans/volumes/puschmann-alexander-1878/vol2` | `scan_validation_puschmann_alexander_v2.md` : pp. 3–585 = `n9–n591` | `n9–n591` (583) | `n1–n8`, `n592–n628` (45) | **déjà appliqué** : 583 images et 45 vues retirées dans le registre |
| `BIUSante_150173` / `scans/volumes/franz-scriptores-physiognomoniae-1780` | `scan_validation_franz_melampus.md` ne valide que TLG 1365.001, pp. 501–508 = `n537–n544` | `n537–n544` (8) | `n1–n536`, `n545–n565` (557) | **ACTION REQUIRED** : la ligne registre déclare encore 565 images et recommande alors à tort le volume complet |
| `anecdotagraecaec0003cram` / deux chemins Cramer III | `scan_validation_cramer_anecdota_oxon_3.md` | `n10–n166` pour 0730.001–002; `n237–n245` pour 0087.045 | toutes les autres feuilles du volume, si elles existent sur le chemin concerné | **déjà ciblé** : les deux lignes registre déclarent 157 et 9 images, pas le volume complet |
| `OriensChristianus3`, `BIUSante_dioscsprengelx02`, `adw8682.0003.001.umich.edu`, `oxyrhynchusppt1300grenuoft`, `Collection_des_anciens_alchimistes_grecs_L2_3-6_1888` | notes de registre explicitement ciblées | respectivement `n72–n99`, `n2–n42`, `n392`, PDF 31–33, DjVu 342–357 | hors plages respectives | **déjà ciblés**; aucune suppression additionnelle à déduire |

## Conclusion opérationnelle

La seule purge certaine encore nécessaire est **Franz 1780 / `BIUSante_150173`** : conserver exactement huit feuilles `n537–n544`, supprimer 557 feuilles hors cible. Les deux Puschmann constituent le contrôle de cohérence : leur réduction est déjà reflétée par les comptes distants. Les volumes Galien, FHG, CAG, Patrologia Graeca et autres volumes multi-notices ne sont volontairement pas inscrits ici, car leurs rapports ne se limitent pas à une unique plage grecque et exigent un manifeste séparé avant toute purge.
