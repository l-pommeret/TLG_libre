# Validation de scan — Kühn, *Galeni opera omnia*, XIII (BIU Santé)

**Décision : READY — extraction image-only ciblée.** `BIUSante_45674x13` est absent de `data/scan_sources.csv` et de `scans/`. Le tome achève TLG 0057.076, dont le segment précédent a été validé au tome XII, et contient entièrement TLG 0057.077.

| Contrôle | Résultat vérifié |
|---|---|
| Source / édition | [Internet Archive — BIUSante_45674x13](https://archive.org/details/BIUSante_45674x13), *Galeni opera omnia*, XIII, Leipzig, Car. Cnoblochii. Date IA générique `1821/1833`; titres, numéros de tomes et bornes imprimées concordent avec le canon. |
| Droits | [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence), explicitement déclarée par IA. |
| JP2 traité | `BIUSante_45674x13_jp2.zip`, 625 518 223 octets, SHA-1 `a817116427e84617c5676637d5896b1ba952cacf`; aucun paquet JP2 original distinct. |
| Scandata / qualité | `BIUSante_45674x13_scandata.xml`, 377 909 octets, SHA-1 `d01a1d236f9b013c7d1266de1046dfacddba97f7`; 1 062 images, 299 ppi par feuille. Les quatre pages contrôlées sont nettes et lisibles en grec, latin et apparat. |

## Concordance et bornes

Le décalage vérifié est `feuille IA = page imprimée + 2`.

| Notice TLG | Œuvre | Pages Kühn XIII | Feuilles IA | Couverture |
|---|---|---:|---:|---|
| 0057.076 | *De compositione medicamentorum secundum locos* X | 1–361 | `n3`–`n363` | Ce segment achève la notice, après XII pp. 378–1007 (`n380`–`n1009`). |
| 0057.077 | *De compositione medicamentorum per genera* VII | 362–1058 | `n364`–`n1060` | Complète. |

## Contrôle visuel temporaire

| Feuille / page | Preuve |
|---|---|
| `n3`, p. 1 | Titre grec/latin du livre VII *De compositione medicamentorum secundum locos* : début du segment XIII de 0057.076. |
| `n363`, p. 361 | Dernière page du segment XIII de 0057.076, texte grec et traduction conservés. |
| `n364`, p. 362 | Titre grec/latin du livre I *De compositione medicamentorum per genera* : début exact de 0057.077. |
| `n1060`, p. 1058 | Dernière page de 0057.077, explicit et grec/latin lisibles. |

Les quatre JPEG de contrôle et le `scandata.xml` ont été supprimés après inspection. Aucun OCR, PDF ou archive d’images n’a été téléchargé ou conservé.

## Recommandation

Le paquet complet (625,5 Mo) dépasse le seuil préférentiel. Transférer directement vers le dépôt distant les seules images `n3`–`n1060` : la plage contient précisément la fin de **0057.076 READY** et l’intégralité de **0057.077 READY**, sans préliminaires inutiles. Préserver les métadonnées de provenance et exclure tout OCR tiers.
