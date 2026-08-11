# Validation scan — *Patrologia Graeca* 79

## Décision : READY (ingestion images-only)

* **Source exacte** : Wikimedia Commons, [*Patrologia Graeca* vol. 79 (Migne)](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._079.pdf).
* **Droits** : Public domain / PDM explicitement indiqué par Commons.
* **Fichier distant** : PDF de **95 488 756 octets**, SHA-1 Commons `ad65e9b5681239130a761f4a14744a27758917f7`; 785 pages (dimensions de rendu Commons : 995 × 1537 px). L'identifiant, le SHA et le nom de fichier ne sont présents ni dans `data/scan_sources.csv` ni dans `scans/` au contrôle du 2026-08-11.
* **Qualité** : trois rendus temporaires Commons contrôlés, puis détruits : pages fichier 20 (cols. 37–38, texte net), 400 (cols. 771–772, grec et latin nets) et 700 (cols. 1331–1332, texte net). Le volume est exploitable; aucune archive, image durable ni OCR n'a été créé.

## Concordance canonique vérifiée

Les bornes MPG sont celles de `canon_coverage.csv`; les deux notices marquées doublon/non-œuvre restent volontairement hors ingestion.

| Notice TLG | Œuvre | Bornes imprimées | Verdict |
|---|---|---:|---|
| 4118.004 | Nilus Ancyranus, *Epistulae* | 82–582 | direct |
| 4110.020 | Evagrius Ponticus, *Tractatus ad Eulogium* (sous Nilus) | 1093–1140 | direct |
| 4110.021 | *De vitiis quae opposita sunt virtutibus* (sous Nilus) | 1140–1144 | direct |
| 4110.023 | *De octo spiritibus malitiae* (sous Nilus) | 1145–1164 | direct |
| 4110.024 | *De oratione* (sous Nilus) | 1165–1200 | direct |
| 4110.025 | *Institutio sive Paraenesis ad monachos*, rec. brevior | 1235–1240 | direct |
| 4110.016 | *Capita paraenetica* | 1249–1252 | direct |
| 4110.022 | *De malignis cogitationibus* | 1200–1233 | exclu : doublon de 4110.034 dans le canon |
| 2743.001 | Hyperechius, *Adhortatio ad monachos* | 1473–1489 | exclu : `is_work=no` dans le canon |

**Rendement** : 7 notices canon `work=yes` directement couvertes. Préparer exclusivement l'ingestion ciblée du manifeste ci-dessous depuis l'URL Commons; ne pas utiliser un texte OCR tiers.

## Manifeste image-only ciblé (pages fichier)

Ne pas transférer le volume complet : les pages sont déduites de la pagination imprimée effectivement contrôlée (fichier p. 45 = cols. 77–78, p. 300 = 571–572, p. 568 = 1083–1084, p. 590 = 1127–1128, p. 650 = 1247–1248), puis des feuillets consécutifs. Les bornes sont inclusives.

| Notice(s) | Locus MPG | Pages fichier à transférer |
|---|---:|---:|
| 4118.004 | 82–582 | 47–305 |
| 4110.020 | 1093–1140 | 573–596 |
| 4110.021 | 1140–1144 | 596–598 |
| 4110.023 | 1145–1164 | 599–608 |
| 4110.024 | 1165–1200 | 609–626 |
| 4110.025 | 1235–1240 | 644–646 |
| 4110.016 | 1249–1252 | 651–652 |

Les chevauchements de feuillet (4110.020/.021) sont intentionnels; dédupliquer lors du transfert. Les segments non listés, notamment préfaces, autres auteurs et pages de garde, sont hors cible.
