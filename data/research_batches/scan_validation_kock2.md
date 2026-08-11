# Validation de scan — Kock, *Comicorum Atticorum Fragmenta*, II

**Candidat :** Internet Archive
[`comicorumatticor02kockuoft`](https://archive.org/details/comicorumatticor02kockuoft).

**Sélection.** L’identifiant a été recherché dans `data/scan_sources.csv` et
dans les chemins de `scans/` avant l’audit : il est absent des deux. Il ne faut
pas le confondre avec le volume III de Kock déjà présent localement
(`kock-caf3-1888`).

**Décision : REJECT pour ingestion à ce stade (droits fournisseur non
documentés).** C’est bien le volume et les deux plages canoniques exactes ; le
fichier image et la qualité sont vérifiés. En revanche Internet Archive ne
publie ici ni champ `rights`, ni `licenseurl`, ni `possible-copyright-status`.
L’ancienneté de l’édition ne remplace pas une information de réutilisation
explicite dans cette pipeline. Aucun OCR n’a été consulté ou retenu.

## Concordance bibliographique et TLG

| Notice TLG | Référence du canon | Preuve de concordance |
| --- | --- | --- |
| 0405.001 — Anaxandrides, *Fragmenta* | T. Kock, *Comicorum Atticorum fragmenta*, II, Leipzig, Teubner, 1884, pp. 135–153, 155–164 | L’item se décrit comme *Comicorum atticorum fragmenta*, vol. 2, B. G. Teubneri, date IA `1880-88` (compatible avec 1884). La p. 135 ouvre l’entrée **ΑΝΑΞΑΝΔΡΙΔΗΣ** ; la p. 145 reste dans ses fragments. |
| 0406.001 — Anaxilas, *Fragmenta* | T. Kock, *Comicorum Atticorum fragmenta*, II, Leipzig, Teubner, 1884, pp. 264–275 | La p. 264 porte l’en-tête et l’entrée **ΑΝΑΞΙΛΑΣ** ; la p. 275 poursuit les fragments d’Anaxilas. |

Le bas de page des vues porte « *Comici graeci, ed. Th. Kock. II.* » : il
confirme le tome, l’éditeur et l’absence de substitution par le volume III.

## Métadonnées Internet Archive

| Champ | Valeur contrôlée |
| --- | --- |
| Identifiant / fournisseur | `comicorumatticor02kockuoft` — Internet Archive, collection `robarts` / `toronto` / `university_of_toronto` |
| Titre / créateur / éditeur | *Comicorum atticorum fragmenta* — Theodor Kock — Lipsiae, B. G. Teubneri |
| Date / volume | `1880-88` / `2` |
| Droits | `rights`, `licenseurl` et `possible-copyright-status` absents : motif du rejet, malgré le statut historique de l’édition |
| Imagecount / PPI | 600 images / 400 ppi |
| JP2 processed | `comicorumatticor02kockuoft_jp2.zip`, 257,012,934 octets, 600 fichiers, SHA-1 `b954eba45a0dff5cd553d3884bde6a771c8e9ee0` |
| JP2 raw | `comicorumatticor02kockuoft_raw_jp2.zip`, 393,818,954 octets, 600 fichiers, SHA-1 `8026a8938d8da004c4a632336fd7942526912174` |
| Scandata | `scandata.zip`, 49,963,305 octets, SHA-1 `5885fa07b14514210661b132086497c0b9e824da` |

## Contrôles visuels temporaires

Les vues directes BookReader suivantes ont été récupérées à 1400 px dans un
répertoire `/tmp`, inspectées visuellement, puis supprimées définitivement
avec le répertoire temporaire. Elles n’ont été ni OCRisées ni versées au dépôt.

| Vue | Feuillet IA / page imprimée | Résultat |
| --- | --- | --- |
| [début Anaxandrides](https://archive.org/download/comicorumatticor02kockuoft/page/n140_w1400.jpg) | `n140`, p. 135 | Début exact de **ΑΝΑΞΑΝΔΡΙΔΗΣ** ; grec et apparat nets. |
| [milieu Anaxandrides](https://archive.org/download/comicorumatticor02kockuoft/page/n150_w1400.jpg) | `n150`, p. 145 | Fragments d’Anaxandrides lisibles ; confirme la séquence à l’intérieur de la plage canonique. |
| [début Anaxilas](https://archive.org/download/comicorumatticor02kockuoft/page/n269_w1400.jpg) | `n269`, p. 264 | Entrée **ΑΝΑΞΙΛΑΣ**, texte grec et appareil lisibles. |
| [fin Anaxilas](https://archive.org/download/comicorumatticor02kockuoft/page/n280_w1400.jpg) | `n280`, p. 275 | Fragments 38–44 d’Anaxilas, fin de la plage canonique, lisibles. |

Les trois premières vues satisfont l’échantillonnage début–milieu–début de la
seconde notice ; la quatrième a été ajoutée pour fermer la seconde plage.

## Suite autorisée

Ne pas inscrire ce volume dans `scan_sources.csv` ni télécharger son archive
tant qu’une licence ou une déclaration de droits fournisseur réutilisable n’a
pas été obtenue. Si elle l’est, le volume est techniquement prêt : 2 notices,
257 Mo de JP2 processed à 400 ppi.
