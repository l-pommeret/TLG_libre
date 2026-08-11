# Validation de scan — Diels, *Fragmente der Vorsokratiker* (1906)

**Candidat sélectionné :** `diefragmentederv01dieluoft`, absent de
`data/scan_sources.csv` et de `scans/` lors du contrôle, avec 19 notices
associées dans `scan_volume_audit_ia_01.csv` et un paquet JP2 de 209,108,717
octets.

**Décision : REJECT (édition et pagination non exactes).** Le candidat est
une édition Diels de 1906. Les 19 notices canoniques auditées renvoient à
Diels–Kranz, *Die Fragmente der Vorsokratiker*, vol. 1, 6e éd., Weidmann,
1951. Les trois contrôles de page démontrent que les pages du scan 1906 ne
portent pas les entrées attendues à ces paginations. Ne pas l'ajouter à
`scan_sources.csv` ni récupérer ses images pour ces notices.

## Notices prétendument couvertes et test d'exactitude

L'audit IA associait : `2218.001`, `2225.001`, `2226.001`, `2227.001`,
`2228.001`, `2229.001`, `2231.001`, `2232.001–002`, `2234.001`,
`2235.001`, `2237.001`, `2239.001`, `2240.001`, `2241.001`, `2242.001`,
`2244.001`, `2245.001` et `2246.001`.

| Contrôle | Attendu par le canon (Diels–Kranz 1951) | Observé dans le scan Diels 1906 | Résultat |
|---|---|---|---|
| p. 110–112 | TLG 2218.001, testimonia de Calliphon et Démocédès | La page 111 montre `A. Lehre` et des doxographies générales, pas l'entrée attendue. | Échec de pagination/contenu. |
| p. 381–384 | TLG 2232.001–002, testimonia et fragments de Damon | La p. 382 est sous l'en-tête **55. Demokritos**. | Échec de concordance d'auteur. |
| p. 446–480 | TLG 2239.001, Pythagoristes | Le scan s'achève à p. 466; la p. 447 est toujours dans **Demokritos**, non dans les Pythagoristes. | Plage absente/incompatible. |

La bibliographie IA (*Die Fragmente der Vorsokratiker, griechisch und
deutsch*, Diels, 1906) n'est donc pas l'édition de référence et ne peut pas
être traitée comme un substitut exact sans un nouveau mapping, œuvre par
œuvre, vers cette édition antérieure.

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / accès | `diefragmentederv01dieluoft` — <https://archive.org/metadata/diefragmentederv01dieluoft> |
| Titre / date | *Die Fragmente der Vorsokratiker, griechisch und deutsch*; 1906 |
| Créateur | Hermann Diels (1848–1922) |
| Nombre d'images | 490 |
| Résolution déclarée | 400 ppi |
| JP2 processed | `diefragmentederv01dieluoft_jp2.zip`, 209,108,717 octets, SHA-1 `c04304a9874a3b87c61d4c92a90dbe87d53cead0` |
| JP2 original | `diefragmentederv01dieluoft_orig_jp2.tar`, 356,362,240 octets, SHA-1 `e771a70257173e6e87b5f6eeab197829105f2cd8` |
| Données de scan | `diefragmentederv01dieluoft_scandata.xml` (présent dans les métadonnées IA) |
| Droits | `possible-copyright-status=NOT_IN_COPYRIGHT`; `rights` et `licenseurl` absents. |

## Contrôle visuel temporaire (sans conservation)

Trois JPEG de pages individuelles ont été demandés au lecteur IA, examinés
dans `/tmp`, puis supprimés définitivement. Aucun paquet, image ni OCR n'a
été conservé.

| Échantillon | Vue IA | Observation |
|---|---|---|
| Test Calliphon/Démocédès | [`n126` (p. 111)](https://archive.org/download/diefragmentederv01dieluoft/page/n126_w1400.jpg) | Page lisible, mais contenu incompatible avec TLG 2218.001 au lieu attendu. |
| Test Damon | [`n397` (p. 382)](https://archive.org/download/diefragmentederv01dieluoft/page/n397_w1400.jpg) | Page lisible sous **Demokritos**, non Damon. |
| Test Pythagoristes | [`n462` (p. 447)](https://archive.org/download/diefragmentederv01dieluoft/page/n462_w1400.jpg) | Page lisible dans les fragments/imitation de Démocrite; pas de corpus pythagoricien. |

La qualité image est suffisante, mais ne compense pas l'absence de
concordance bibliographique et paginale. Les dérivés `djvu.xml` et autres OCR
n'ont pas été consultés ni utilisés.
