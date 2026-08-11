# Validation de scan — Cramer, *Anecdota Graeca Oxoniensia*, III

**READY — ingestion ciblée image-only.** Le candidat `anecdotagraecaec0003cram` est absent de `data/scan_sources.csv` et de `scans/`. Il correspond au volume III de J. A. Cramer, *Anecdota graeca e codd. manuscriptis bibliothecarum Oxoniensium* (Oxford University Press, volume millésimé 1835 par IA/Commons ; référence canonique de l'édition : 1836), qui imprime exactement TLG 0730.001, Meletius, *De natura hominis*, pp. 5–157.

| Contrôle | Résultat vérifié |
|---|---|
| Original Commons / droits | [Fichier original Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Anecdota_graeca_e_codd._manuscriptis_bibliothecarum_oxoniensium_(IA_anecdotagraecaec0003cram).pdf) : PDF de 19 092 691 octets, SHA-1 `16ed0fab56cf016a8b9215c095605f05c03d3eaf`, 837 × 1 516 px, 434 pages. Commons le marque explicitement [CC PDM 1.0](https://creativecommons.org/publicdomain/mark/1.0/) / libre de restrictions connues. |
| Source images à ingérer | [Internet Archive — anecdotagraecaec0003cram](https://archive.org/details/anecdotagraecaec0003cram), même accession que Commons : `anecdotagraecaec0003cram_jp2.zip`, JP2 traité, 187 375 407 octets, SHA-1 `5d635b0dfb6b0d06f6a1c69e34c984b1daab8933`, 436 images. Pas de paquet JP2 « original » distinct publié. |
| Scandata / qualité | `anecdotagraecaec0003cram_scandata.xml`, 446 564 octets, SHA-1 `5667f82f0ff9056b6f15b6818fb408f06a650b0b`. PPI non publié ; les images sources IA sont nettement supérieures au PDF Commons de consultation et présentent un grec lisible, marges et apparat compris. |
| Pagination / vues | `n14` = p. 5, titre *Anthrōpou kataskeuēs* et incipit de Meletius ; `n90` = p. 81, même texte ; `n166` = p. 157, explicit. La feuille suivante `n167` ouvre une autre section (*Epistolai*), confirmant la limite. |
| Ingestion préparée | **Seulement les images `n14` à `n166` incluses** (153 feuilles, pp. 5–157) depuis le JP2 IA ; conserver les images, pas le PDF Commons et aucun OCR. |

Les cinq JPEG de vérification, le scandata et le répertoire temporaire ont été supprimés après contrôle. Aucun OCR, PDF ou archive image n'a été téléchargé ni conservé. Recommandation : `REMOTE_ONLY` **READY** pour 0730.001, ingestion ciblée des 153 images source.
