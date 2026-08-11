# Validation de scan — Jernstedt, *Liber Syntipae* (1912)

**Candidat :** Internet Archive
[`michandreopulili00sind`](https://archive.org/details/michandreopulili00sind).

**Sélection.** L’identifiant a été vérifié absent de `data/scan_sources.csv`
et de tous les chemins sous `scans/`. Les métadonnées IA donnent le titre
*Mich. Andreopuli Liber Syntipae*, Saint-Pétersbourg, 1912 : elles concordent
avec l’édition V. Jernstedt du canon (la forme IA « Ernshtedt » est une
translittération catalogographique du nom).

**Décision : REJECT pour ingestion à ce stade (droits fournisseur non
documentés).** L’édition, les deux recensions et la pagination sont exactes,
et les pages source sont lisibles à 350 ppi. Mais IA n’expose ni `rights`, ni
`licenseurl`, ni `possible-copyright-status`; le statut historique ne suffit
pas à établir une réutilisation explicite. Aucun OCR n’a été consulté ni
retenu.

## Concordance bibliographique et TLG

| Notice TLG | Référence du canon | Contrôle de page |
| --- | --- | --- |
| 3118.001 — *Liber Syntipae* | V. Jernstedt, *Liber Syntipae*, *Mémoires de l’Académie Impériale des Sciences*, XI.1, Saint-Pétersbourg, 1912, pp. 3–130 | Les pages d’ouverture et centrale portent **LIBER SYNTIPAE**, le texte grec et les variantes de la première recension ; la p. 130 porte **MICH. ANDREOPULI** et clôt le texte. |
| 3118.002 — *Liber Syntipae* (recensio altera) | Jernstedt, ibid., pp. 3–129 | Les mêmes vues présentent, sous **RETRACTATIO**, la recension seconde en regard de la première, comme l’indiquent les plages canoniques parallèles. |

## Métadonnées Internet Archive

| Champ | Valeur contrôlée |
| --- | --- |
| Identifiant / fournisseur | `michandreopulili00sind` — Internet Archive, `university_of_illinois_urbana-champaign` / `americana` |
| Titre / créateur | *Mich. Andreopuli Liber Syntipae* — Sindbad, Michael Andreopulus, P. Nikitin, V. Ernshtedt |
| Éditeur / date | Saint-Pétersbourg / 1912 |
| Droits | `rights`, `licenseurl` et `possible-copyright-status` absents : motif du rejet |
| Imagecount / PPI | 238 images / 350 ppi |
| JP2 processed | `michandreopulili00sind_jp2.zip`, 127,745,349 octets, 238 fichiers, SHA-1 `afd8f4a2ad8f59b3f5fd5c667c81c85374625540` |
| JP2 original | `michandreopulili00sind_orig_jp2.tar`, 246,528,000 octets, 238 fichiers, SHA-1 `694d59d859ccbe878bf642a1616d9e2285100ea6` |
| Scandata | `michandreopulili00sind_scandata.xml`, 312,622 octets, SHA-1 `6875e1cb5747b133c582e097a611a52bfb96a4a1` |

## Contrôles visuels temporaires

Trois JPEG BookReader ont été obtenus à 1400 px dans `/tmp`, contrôlés
visuellement, puis supprimés définitivement avec le répertoire temporaire.
Ils n’ont été ni OCRisés ni ajoutés au dépôt.

| Vue | Feuillet IA / page imprimée | Résultat |
| --- | --- | --- |
| [ouverture](https://archive.org/download/michandreopulili00sind/page/n28_w1400.jpg) | `n28`, p. 3 (ouverture de la séquence) | Prologue grec et **RETRACTATIO** parallèle, mise en page caractéristique des deux recensions. |
| [milieu](https://archive.org/download/michandreopulili00sind/page/n90_w1400.jpg) | `n90`, p. 65 | **LIBER SYNTIPAE**, texte grec et appareil/recension parallèle nets. |
| [fin](https://archive.org/download/michandreopulili00sind/page/n155_w1400.jpg) | `n155`, p. 130 | En-tête **MICH. ANDREOPULI**, dernière page imprimée et fin de 3118.001 lisible. |

## Suite autorisée

Ne pas l’inscrire dans `scan_sources.csv` ni récupérer l’archive tant qu’une
licence ou déclaration de droits réutilisable n’a pas été retrouvée. Le
candidat reste techniquement valable : 2 notices, paquet processed de 128 Mo,
238 images à 350 ppi.
