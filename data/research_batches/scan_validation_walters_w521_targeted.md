# W.521 — manifeste d’ingestion strictement ciblé

## Décision : REVIEW — ne pas déclencher tant que l’échantillon grec n’est pas lisible

Objet : [Walters W.521, *Imperial Menologion*](https://purl.thewalters.org/art/W.521/browse), manuscrit grec de janvier (second quart du XIe s.). La page objet actuelle affiche **CC0**. En revanche, la documentation et le dépôt historique *Digital Walters* qui expose les masters nommés ci-dessous portent explicitement **CC BY-NC-SA 3.0**. Pour une provenance non ambiguë, toute ingestion depuis ce dépôt doit donc enregistrer la restriction la plus spécifique : `CC BY-NC-SA 3.0; usage privé autorisé par le détenteur du dépôt; pas de redistribution sous une étiquette CC0 sans vérification de la couche actuelle`.

L’endpoint documentaire public est `https://www.thedigitalwalters.org/Data/WaltersManuscripts/html/W521/`; les fichiers sont annoncés sous `https://www.thedigitalwalters.org/Data/WaltersManuscripts/W521/data/W.521/` (sous-répertoires `tif/`, `sap/`, `thumb/`). Le patron de master est `tif/W521_000NNN_600.tif`, avec un master `780` quand indiqué dans l’index ; les variantes `300.tif` ne sont pas à sélectionner pour OCR. Les masters texte sont documentés à 600 ppi (certains folios à 780 ppi). Aucun fichier, OCR, ni archive n’a été conservé localement.

| Notice | Texte/témoin strict | Foliation à envoyer | IDs d’images dans l’ordre | Master de départ confirmé | État du contrôle grec |
|---|---|---|---|---|---|
| 5059.002 | *Theopemptus et Theonas*, BHG 2444 | 25r–27v | 53–58 | `W521_000053_780.tif` | À faire : endpoint `sap/W521_000053_sap.jpg` a répondu 522 ici |
| 5059.003 | *Zoticus*, BHG 2479 | 50v–56r | 104–115 | `W521_000104_780.tif` | À faire : endpoint de vue temporaire indisponible ici |
| 5059.004 | Martyrs du Sinaï et Raithou, BHG 1307d | 92v–95v | 188–194 | `W521_000188_780.tif` | À faire : endpoint de vue temporaire indisponible ici |
| 5059.005 | Theodotus de Cyrénie, BHG 2437 | 155v–158r | 314–319 | `W521_000314_780.tif` | À faire : endpoint de vue temporaire indisponible ici |
| 5059.006 | Neophytus, BHG 1326b | 200r–203r | 403–409 | `W521_000403_780.tif` | À faire : endpoint de vue temporaire indisponible ici |

Les concordances folio/BHG viennent de la table des matières officielle de W.521 : 25r–27v BHG 2444 ; 50v–56r BHG 2479 ; 92v–95v BHG 1307d ; 155v–158r BHG 2437 ; 200r–203r BHG 1326b. Elles ne désignent pas les éditions modernes citées au canon, mais le témoin manuscrit explicitement demandé par ces notices.

## Pré-vol obligatoire avant transfert distant

Pour **chaque** ligne du tableau, ouvrir un unique JPEG `sap` ou `thumb` du premier folio listé, constater visuellement la présence de grec manuscrit, le supprimer immédiatement, et noter l’URL effectivement servie. Cette étape n’a pas pu être achevée dans cet environnement : les quatre requêtes de vue (`W521_000104`, `188`, `314`, `403`) et le test de `053` ont échoué par timeout/HTTP 522 chez Digital Walters. Ce n’est pas une preuve de contenu négative : c’est un échec d’accès temporaire, donc ce manifeste reste **REVIEW**, non READY.

Après succès de ces cinq contrôles, transférer uniquement les IDs indiqués, en préférant les masters 600/780 et en journalisant pour chaque fichier l’URL, la résolution réellement retournée, taille et empreinte. Ne pas inclure les folios voisins, miniatures hors texte, OCR fournisseur ou tarball intégral.
