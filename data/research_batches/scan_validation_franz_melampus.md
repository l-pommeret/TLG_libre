# Validation de scan — Franz, *Scriptores physiognomoniae veteres* (BIU Santé / Medica)

## Décision

**READY.** `BIUSante_150173` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. C'est l'édition de J. G. F. Franz (Altenburg, 1780) prescrite exactement par le canon pour TLG 1365.001, aux pp. 501–508. Les trois pages contrôlées portent le titre de Mélampous, les bornes 501, 504 et 508, et le grec avec traduction/notes latines. La licence Etalab est explicite. Le paquet image fait 361 Mo : l'ingestion image-only du volume entier est recommandée, plutôt qu'une découpe ciblée.

## Concordance

| Notice TLG | Œuvre | Pages canoniques | Preuve visuelle |
|---|---|---:|---|
| 1365.001 | Mélampous, *Περὶ ἐλαιῶν τοῦ σώματος πρὸς Πτολεμαῖον βασιλέα* | 501–508 | `n537` = p. 501, page de titre grec « ΜΕΛΑΜΠΟΔΟΣ … ΠΕΡΙ ΕΛΑΙΩΝ ΤΟΥ ΣΩΜΑΤΟΣ … ΠΡΟΣ ΠΤΟΛΕΜΑΙΟΝ ΒΑΣΙΛΕΑ » ; `n540` = p. 504 ; `n544` = p. 508, fin du texte. |

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / source | `BIUSante_150173` — [Internet Archive](https://archive.org/details/BIUSante_150173) ; [notice Medica](http://www.biusante.parisdescartes.fr/histmed/medica/cote?150173) |
| Titre / date / éditeur | *Scriptores physiognomoniae veteres …* ; 1780 ; Altenburgi, Gottlob Emanuel Richter |
| Éditeur scientifique | Johannes Georgius Fridericus Franzius ; texte grec-latin avec les éléments éditoriaux de Peruscus, Sylburgius et Trillerus |
| Fichier image traité | `BIUSante_150173_jp2.zip` |
| SHA-1 / taille | `cd2dd7115b99e18ab0b2f0a948fffa31eb964b47` ; 360 770 111 octets |
| Images / original distinct | métadonnée de volume : 565 images ; aucun paquet JP2 original distinct dans les métadonnées consultées |
| Scandata | `BIUSante_150173_scandata.xml`; SHA-1 `e125c20987bc6cf673bd9b87ba0e0beaadbae232` ; 198 722 octets |
| PPI / qualité | le champ général PPI est absent, mais le scandata donne 360 ppi aux feuillets ; les trois échantillons sont nets, avec grec, latin et notes lisibles |
| Droits | champ `rights` : [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence) |
| Accès image | vues individuelles Internet Archive `https://archive.org/download/BIUSante_150173/page/n{leaf}_w1400.jpg` ; les pages imprimées 501/504/508 correspondent respectivement aux feuilles 537/540/544 |

## Contrôles visuels temporaires

`n537` (p. 501, titre et incipit), `n540` (p. 504, texte grec/latin) et `n544` (p. 508, terminaison) ont été obtenus individuellement par le visualiseur distant puis inspectés. La pagination imprimée et le contenu correspondent exactement aux pp. 501–508 du canon. Les trois JPEG, le `scandata.xml` de repérage et le répertoire temporaire ont ensuite été supprimés. Aucun OCR, PDF ni archive image n'a été téléchargé ou conservé.

## Action

Ajouter comme source `REMOTE_ONLY` **READY** pour TLG 1365.001. Vu la taille de 361 Mo, les droits explicites et l'exactitude de l'édition, planifier l'ingestion image-only du volume complet (et non seulement pp. 501–508), sans aucun dérivé OCR.
