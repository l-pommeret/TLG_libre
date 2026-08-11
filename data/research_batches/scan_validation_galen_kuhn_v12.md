# Validation de scan — Kühn, *Galeni opera omnia*, XII (BIU Santé)

**Décision : READY — extraction image-only ciblée.** `BIUSante_45674x12` est absent de `data/scan_sources.csv` et de `scans/`; ses droits Etalab sont explicites. Il fournit la seconde et dernière partie de TLG 0057.075, avec le tome XI validé séparément, et le premier segment de 0057.076.

| Contrôle | Résultat vérifié |
|---|---|
| Source / édition | [Internet Archive — BIUSante_45674x12](https://archive.org/details/BIUSante_45674x12), *Galeni opera omnia*, XII, Leipzig, Car. Cnoblochii. Date IA générique `1821/1833`; titre de tome, titres grecs/latins et pagination concordent avec le canon. |
| Droits | [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence), déclarée explicitement par IA. |
| JP2 traité | `BIUSante_45674x12_jp2.zip`, 547 539 543 octets, SHA-1 `76afec4d9e958dda02f104f2713887fe8de309b9`; pas de paquet JP2 original distinct. |
| Scandata / qualité | `BIUSante_45674x12_scandata.xml`, 359 978 octets, SHA-1 `3466a5800b02816c97a883d520cf6d7c37baede0`; 1 012 images, 299 ppi par feuille. Typographie grecque, latin et apparat nets et complets aux trois points contrôlés. |

## Concordance canonique

La pagination vérifiée donne `feuille IA = page imprimée + 2`.

| Notice TLG | Œuvre | Pages Kühn XII | Feuilles IA | Statut |
|---|---|---:|---:|---|
| 0057.075 | *De simplicium medicamentorum temperamentis ac facultatibus* XI | 1–377 | `n3`–`n379` | Ce segment, joint à Kühn XI pp. 379–892 (`n381`–`n894`), achève la notice entière. |
| 0057.076 | *De compositione medicamentorum secundum locos* X | 378–1007 | `n380`–`n1009` | Segment XII exact seulement : la suite pp. 1–361 est au tome XIII et doit être validée séparément. |

## Vues temporaires contrôlées

| Feuille / page | Preuve |
|---|---|
| `n3`, p. 1 | Ouverture du livre VII de *De simplicium medicamentorum…* : correspond à la continuation exacte de 0057.075 depuis le tome XI. |
| `n379`, p. 377 | Dernière page du segment XII de 0057.075, grec/latin parfaitement lisible. |
| `n1009`, p. 1007 | Dernière page du tome XII de *De compositione … secundum locos* : borne finale exacte du segment XII de 0057.076. |

Les trois JPEG de contrôle et le `scandata.xml` ont été supprimés avec leur répertoire temporaire. Aucun OCR, PDF ou archive image n’a été téléchargé ou conservé.

## Recommandation

Le paquet complet dépasse légèrement la préférence de 500 Mo. Ingestion directe vers le dépôt distant, images seulement : `n3`–`n379` pour achever **0057.075 READY** avec le tome XI, puis `n380`–`n1009` comme couverture partielle de 0057.076 en attente du tome XIII. Conserver les métadonnées IA/droits/feuille/page et exclure tout OCR tiers.
