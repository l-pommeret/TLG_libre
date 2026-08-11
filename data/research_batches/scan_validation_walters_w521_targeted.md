# W.521 — manifeste d’ingestion strictement ciblé

## Décision : READY — cinq segments grecs contrôlés et archivés

Objet : [Walters W.521, *Imperial Menologion*](https://purl.thewalters.org/art/W.521/browse), manuscrit grec de janvier (second quart du XIe s.). La page objet actuelle affiche **CC0**. Le miroir institutionnel OPenn de la collection Walters déclare lui aussi explicitement que les substituts numériques complets sont téléchargeables sous **CC0**. Cette double déclaration actuelle lève l'ambiguïté créée par une ancienne mention CC BY-NC-SA 3.0 dans des métadonnées historiques.

L’endpoint documentaire public est `https://www.thedigitalwalters.org/Data/WaltersManuscripts/html/W521/`; les fichiers sont annoncés sous `https://www.thedigitalwalters.org/Data/WaltersManuscripts/W521/data/W.521/` (sous-répertoires `tif/`, `sap/`, `thumb/`). Le patron de master est `tif/W521_000NNN_600.tif`, avec un master `780` quand indiqué dans l’index ; les variantes `300.tif` ne sont pas à sélectionner pour OCR. Les masters texte sont documentés à 600 ppi (certains folios à 780 ppi). Aucun fichier, OCR, ni archive n’a été conservé localement.

| Notice | Texte/témoin strict | Foliation à envoyer | IDs d’images dans l’ordre | Master de départ confirmé | État du contrôle grec |
|---|---|---|---|---|---|
| 5059.002 | *Theopemptus et Theonas*, BHG 2444 | 25r–27v | 53–58 | `W521_000053_780.tif` | Grec manuscrit contrôlé sur l'image 53 |
| 5059.003 | *Zoticus*, BHG 2479 | 50v–56r | 104–115 | `W521_000104_780.tif` | Grec manuscrit contrôlé sur l'image 104 |
| 5059.004 | Martyrs du Sinaï et Raithou, BHG 1307d | 92v–95v | 188–194 | `W521_000188_780.tif` | Grec manuscrit contrôlé sur l'image 188 |
| 5059.005 | Theodotus de Cyrénie, BHG 2437 | 155v–158r | 314–319 | `W521_000314_780.tif` | Grec manuscrit contrôlé sur l'image 314 |
| 5059.006 | Neophytus, BHG 1326b | 200r–203r | 403–409 | `W521_000403_780.tif` | Grec manuscrit contrôlé sur l'image 403 |

Les concordances folio/BHG viennent de la table des matières officielle de W.521 : 25r–27v BHG 2444 ; 50v–56r BHG 2479 ; 92v–95v BHG 1307d ; 155v–158r BHG 2437 ; 200r–203r BHG 1326b. Elles ne désignent pas les éditions modernes citées au canon, mais le témoin manuscrit explicitement demandé par ces notices.

## Transfert réalisé

Le miroir OPenn a servi les cinq JPEG de pré-vol (`53`, `104`, `188`, `314`, `403`) en 1319–1408 × 1800 pixels. Chaque image a été inspectée visuellement et contient bien du grec manuscrit. Les fichiers temporaires ont ensuite été supprimés.

Les 38 JPEG `sap` ciblés (1800 px sur le grand côté) ont été transférés dans `Zual/TLG_libre_scans` sous `webdataset/walters-w521-targeted-sap-jpeg.tar`. L'archive distante fait 28 323 840 octets et porte le SHA-256 `2dcb385dd1c8e2372f796cb8620911d635deaade837428c300c4334776ae8082`. Son `manifest.json` conserve pour chaque image l'URL source, la taille et le SHA-256. Aucun OCR fournisseur ni folio voisin n'est inclus. Les TIFF 300/600 ppp restent des améliorations possibles lorsque leur endpoint sera de nouveau servi ; cette archive JPEG constitue déjà un scan lisible et auditable pour préparer l'OCR.
