# Manifeste de compaction HF — *Patrologia Graeca* 56

## Décision

**READY — compaction ciblée, images seulement.** L'archive HF intégrale peut
être remplacée par un dérivé de ses seuls loci canoniques, après vérification
distante du dérivé. Les numéros de pages fichier ont été relevés sur les
colonnes imprimées, et non extrapolés : le PDF a des décalages et des doublons
ponctuels autour des pp. 300 et 500.

* **Archive HF actuelle :** `Zual/TLG_libre_scans`,
  `webdataset/volumes--pg56-chrysostom-severianus--bba468331a16.tar` ; 780
  images, 671 344 640 octets ; état `MIGRATED_PUBLIC`, contrôle
  `REMOTE_PATH_AND_SIZE_MATCH` dans `data/hf_scan_migrations.csv`.
* **Source/droits :** [Commons, *Patrologia Graeca* 56](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._056.pdf),
  Migne, *Patrologia Graeca* 56, `Public domain` selon Commons.
* **Fichier source :** PDF image-only, 110 584 461 octets, SHA1
  `536b5027c00b51dec199786e0753f791b4ce724b`, 780 pages. Aucun OCR n'a été
  extrait ni utilisé.

## Plages ciblées et contrôles visuels

Chaque ligne est une plage continue de pages fichier. Les pages de bord ont été
inspectées ; lorsque l'une contient une traduction latine ou un avis éditorial,
elle reste nécessaire car elle porte aussi la colonne MPG de début/fin. Une
preuve grecque lisible est fournie dans **chaque** segment.

| Pages fichier à garder | Loci MPG directs inclus | Notices concernées (groupes du rapport de validation) | Contrôles de bornes et preuve grecque |
|---|---|---|---|
| 140–288 (149) | 141–152 ; 153–162 ; 163–192 ; 193–246 ; 247–256 ; 257–262 ; 263–270 ; 271–280 ; 279–290 | 2062.148–151 ; 2062.175, .180, .209–211, .213–214 | p.140 commence cols 141–142 ; p.288 finit cols 289–290. Grec net contrôlé p.150 (151–152) et p.278 (279–280). |
| 302–381 (80) | 313–386 ; 385–394 | 2062.175, .180, .209–211, .213–214 | p.302 commence cols 313–314 ; p.381 finit cols 393–394. Grec net p.312 (323–324) et p.381. |
| 383–396 (14) | 397–410 | 4139.007 | p.382 porte encore 395–396 et est exclue ; p.383 commence 397–398 ; p.396 finit 409–410. Grec net p.383. |
| 416–502 (87) | 429–500 ; 499–516 | 4139.011, .009 | p.416 commence 429–430 ; p.502 finit 515–516. Grec net p.418 et p.450. |
| 505–524 (20) | 519–522 ; 525–538 | 4139.034 ; 2062.216–217 | p.503 porte 517–518 ; p.505 commence 519–520 ; p.524 finit 537–538. Grec net p.515. |
| 527–540 (14) | 541–554 | 2062.219–221 | p.525 porte 539–540 ; p.527 commence 541–542 ; p.540 finit 553–554. Grec net p.527. |
| 550–586 (37) | 563–582 ; 583–586 ; 587–590 ; 589–594 ; 593–600 | 4139.038, .067 ; 2062.219–221 | p.550 commence la séquence 563–564 ; p.586 finit 599–600. Grec net p.586. |

Les sept segments conservent **401 images** couvrant les 23 notices directes
documentées par `scan_validation_pg56_chrysostom_severianus.md`. Les bornes MPG
qui se chevauchent sont dédupliquées ci-dessus.

## Pages à supprimer du dérivé

Après vérification du nouveau jeu distant, les pages suivantes sont hors des
loci TLG ci-dessus : `1–139`, `289–301`, `382`, `397–415`, `503–504`,
`525–526`, `541–549`, `587–780` : **379 images**.

Les feuilles conservées restent des fac-similés de l'édition Migne : certaines
comprennent nécessairement latin, titres, notices ou apparat dans la même image
que le grec ciblé. Elles ne doivent pas être remplacées par du texte OCR ni
découpées artificiellement.

## Action de compaction

Créer un dérivé, par exemple
`webdataset/volumes--pg56-chrysostom-severianus--targeted--<hash>.tar`, avec
les sept plages et un manifeste embarqué. Attendu : 401 images, soit environ
346 861 397 octets à contenu/encodage comparables ; économie indicative
d'environ 324 483 242 octets (48,59 %). Vérifier le compte d'images, manifeste,
taille et hash sur HF avant de supprimer l'archive complète de 780 images.

## Nettoyage

Les vignettes Commons consultées pour les contrôles sont temporaires et seront
supprimées après rédaction du présent manifeste. Aucun asset local, archive ou
OCR n'est conservé par cet audit.
