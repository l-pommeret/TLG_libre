# W.521 — manifeste d’ingestion strictement ciblé

## Décision : READY — vingt segments grecs contrôlés et archivés

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

Un second lot couvre les quinze notices supplémentaires dont les checkpoints item-level ont établi la concordance W.521. La notice `5059.013`, initialement laissée de côté, a ensuite été résolue directement dans la description TEI officielle : BHG 1281e, folios 36r–37v.

| Notice | Foliation exacte | IDs transférés | Pré-vol grec |
|---|---|---|---|
| 5059.010 | 12r–22r | 27–47 | image 27 |
| 5059.011 | 23r–24v | 49–52 | image 49 |
| 5059.012 | 28r–35v | 59–74 | image 59 |
| 5059.013 | 36r–37v | 75–78 | image 75 |
| 5059.014 | 48v–50r | 100–103 | image 100 |
| 5059.015 | 56v–60v | 116–124 | image 116 |
| 5059.016 | 61r–70r | 125–143 | image 125 |
| 5059.017 | 70v–74v et 83r–85v | 144–152 et 169–174 | images 144 et 169 |
| 5059.018 | 75r–82v | 153–168 | image 153 |
| 5059.019 | 86r–87v | 175–178 | image 175 |
| 5059.020 | 88r–92r | 179–187 | image 179 |
| 5059.021 | 96r–104v | 195–212 | image 195 |
| 5059.022 | 105r–113r | 213–229 | image 213 |
| 5059.023 | 113v–129r | 230–261 | image 230 |
| 5059.024 | 129v–150v | 262–304 | image 262 |
| 5059.025 | 151r–155r | 305–313 | image 305 |

## Transfert réalisé

Le miroir OPenn a servi les cinq JPEG de pré-vol (`53`, `104`, `188`, `314`, `403`) en 1319–1408 × 1800 pixels. Chaque image a été inspectée visuellement et contient bien du grec manuscrit. Les fichiers temporaires ont ensuite été supprimés.

Les 38 JPEG `sap` ciblés (1800 px sur le grand côté) ont été transférés dans `Zual/TLG_libre_scans` sous `webdataset/walters-w521-targeted-sap-jpeg.tar`. L'archive distante fait 28 323 840 octets et porte le SHA-256 `2dcb385dd1c8e2372f796cb8620911d635deaade837428c300c4334776ae8082`. Son `manifest.json` conserve pour chaque image l'URL source, la taille et le SHA-256. Aucun OCR fournisseur ni folio voisin n'est inclus. Les TIFF 300/600 ppp restent des améliorations possibles lorsque leur endpoint sera de nouveau servi ; cette archive JPEG constitue déjà un scan lisible et auditable pour préparer l'OCR.

Le second lot contient 236 JPEG supplémentaires dans `webdataset/walters-w521-targeted-more-sap-jpeg.tar`, soit 175 144 960 octets et le SHA-256 distant vérifié `b084eee77bcd7d8bfe7f343149383e8b02e3f2aa71f1e782acd971ac7c962f3e`. Ses 16 points de pré-vol sont tous grecs ; les deux séquences de `5059.017` ont été contrôlées séparément. L'archive contient 236 images et un manifeste, sans OCR fournisseur.

Le complément `5059.013` est archivé séparément sous `webdataset/walters-w521-micah-sap-jpeg.tar` : 4 images, 2 846 720 octets, SHA-256 distant `4b102fd4546c4a3fe8617f0f73fdf6728e846d70ad577c9833de354b96f866af`. L'image initiale 75 montre explicitement le texte grec et la miniature du prophète Michée.

Trois dernières concordances canoniques sont directement données par la même description TEI officielle : `5059.026`, BHG 649a, fols. 158v–199v (images 320–402) ; `5059.027`, BHG 1848b, fols. 203v–207r (images 410–417) ; `5059.028`, BHG 634a, fols. 228r–234r (images 459–471). Les images initiales 320, 410 et 459 ont chacune été contrôlées comme grecques. Les 104 JPEG sont archivés sous `webdataset/walters-w521-tail-canon-sap-jpeg.tar`, 80 076 800 octets, SHA-256 distant `a3af839b1350a02145a6f399545afdd6feb418d50ea6c90836828aac7009d1c1`. Les œuvres intercalaires non associées à ces trois notices ont été exclues.
