# Validation de scan — Preuschen, *Antilegomena* (2e éd., 1905)

**Candidat :** Internet Archive
[`antilegomenadier00preu`](https://archive.org/details/antilegomenadier00preu).

**Sélection.** L’identifiant est absent de `data/scan_sources.csv` et de
`scans/`. Les métadonnées IA concordent avec E. Preuschen, *Antilegomena*,
seconde édition, Giessen, Töpelmann, 1905, l’édition exactement citée par le
canon pour les *Matthiae traditiones*.

**Décision : REJECT pour ingestion à ce stade (droits fournisseur non
documentés).** La concordance de l’édition, des pp. 13–15 et de la qualité est
complète. IA ne publie cependant ni `rights`, ni `licenseurl`, ni
`possible-copyright-status`; l’âge de l’édition ne vaut pas licence explicite.
Aucun OCR n’a été consulté ni retenu.

## Concordance bibliographique et TLG

| Notice TLG | Référence du canon | Contrôle de page |
| --- | --- | --- |
| 1560.001 — *Matthiae traditiones* | E. Preuschen, *Antilegomena*, 2e éd., Giessen, Töpelmann, 1905, pp. 13–15 | Les pp. 13–14 portent l’en-tête **AUS DEN ÜBERLIEFERUNGEN DES MATTHIAS** ; la p. 15 achève la section avant l’*Evangelium des Philippus* et les *Reste des Petrusevangeliums*. |

## Métadonnées Internet Archive

| Champ | Valeur contrôlée |
| --- | --- |
| Identifiant / fournisseur | `antilegomenadier00preu` — Internet Archive, `robarts` / `toronto` / `university_of_toronto` |
| Titre / créateur | *Antilegomena: Die Reste der ausserkanonischen Evangelien und urchristlichen Überlieferungen* — Erwin Preuschen |
| Éditeur / date | Giessen, Töpelmann / 1905 |
| Droits | `rights`, `licenseurl` et `possible-copyright-status` absents : motif du rejet |
| Imagecount / PPI | 234 dans les métadonnées / 400 ppi |
| JP2 processed | `antilegomenadier00preu_jp2.zip`, 74,407,647 octets, **236 fichiers**, SHA-1 `af72d0ae6b8ac34120e712fb97e5c8e223f6b140` |
| JP2 original | `antilegomenadier00preu_orig_jp2.tar`, 127,447,040 octets, **236 fichiers**, SHA-1 `1b401b7a1bd34387ddcbb6d76ab4668f4c8cc974` |
| Scandata | `antilegomenadier00preu_scandata.xml`, 124,587 octets, SHA-1 `ba96fec2b9efec72b9e3c5d0af5e73e031fe20fa` |

L’écart entre `imagecount=234` et les 236 fichiers de chaque paquet est une
différence de métadonnées fournisseur, non une absence des pages contrôlées.

## Contrôles visuels temporaires

Les trois pages cibles ont été obtenues comme JPEG BookReader à 1400 px dans
`/tmp`, examinées visuellement, puis supprimées définitivement avec le
répertoire temporaire. Elles n’ont été ni OCRisées ni ajoutées au dépôt.

| Vue | Feuillet IA / page imprimée | Résultat |
| --- | --- | --- |
| [p. 13](https://archive.org/download/antilegomenadier00preu/page/n24_w1400.jpg) | `n24`, p. 13 | En-tête de la section Matthiae, grec et références lisibles. |
| [p. 14](https://archive.org/download/antilegomenadier00preu/page/n25_w1400.jpg) | `n25`, p. 14 | Texte continu des *Überlieferungen des Matthias*, net. |
| [p. 15](https://archive.org/download/antilegomenadier00preu/page/n26_w1400.jpg) | `n26`, p. 15 | Fin de la section, avant les sections suivantes, lisible. |

## Suite autorisée

Ne pas inscrire ce volume dans `scan_sources.csv` ni récupérer l’archive tant
qu’une déclaration de droits réutilisable ne complète pas la notice. Le
candidat est techniquement satisfaisant : 1 notice, 74 Mo processed, 400 ppi.
