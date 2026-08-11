# Manifeste de compaction HF — *Patrologia Graeca* 120

## Décision

**READY — compaction ciblée, images seulement.** L'archive HF actuelle est une
copie intégrale redondante pour la couverture TLG réellement documentée. Elle ne
doit toutefois être supprimée qu'après transfert et vérification distante du
dérivé ci-dessous (compte d'images, manifeste et taille/hash).

* **Entrée HF actuelle :** `Zual/TLG_libre_scans`,
  `webdataset/volumes--pg120-byzantine--33fddbcf2272.tar` ; 724 images,
  526 295 040 octets ; contrôle distant
  `REMOTE_PATH_AND_SIZE_MATCH`, état `MIGRATED_PUBLIC` dans
  `data/hf_scan_migrations.csv`.
* **Source et droits :** [Commons, *Patrologia Graeca* 120](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._120.pdf),
  Migne, *Patrologia Graeca* 120 ; `Public domain` signalé par Commons.
* **Fichier source :** PDF image-only, 724 pages, 84 702 330 octets, SHA1
  `1415ef370676e57a2cf3e45c3bdca6445b54eb53`. Aucun OCR fournisseur n'est
  impliqué.

## Sélection à conserver

Les numéros « page fichier » sont les pages 1-indexées du PDF/jeu d'images.
Les limites imprimées sont contrôlées sur les pages de bord : les colonnes qui
débordent le locus sont tolérées seulement sur les pages de début et de fin.

| Pages fichier à garder | Colonnes MPG couvertes | Notices TLG directes | Preuve visuelle grecque par segment |
|---|---:|---|---|
| 97–100 (4) | 165–172 | 4496.001 | p.97, cols 165–166 : grec net, début du segment (col. 165) |
| 107–162 (56) | 185–260 | 3395.001–002 | p.107, cols 185–186 : titre et texte grec nets ; p.162 finit cols 259–260 |
| 186 (1) | 307–308 | 3247.002 | p.186, cols 307–308 : texte grec net sur toute la page |
| 480–567 (88) | 852–1009 | 3099.004, 3099.009 | p.480, cols 851–852 : grec lisible, entrée effective à col. 852 ; p.567 commence col. 1009 |
| 692–706 (15) | 1260–1288 | 3057.003 | p.692, cols 1259–1260 : titre et texte grec nets, entrée effective à col. 1260 ; p.706 finit cols 1287–1288 |

Les segments sont volontairement fusionnés lorsque les loci sont contigus.
Les deux notices 3099 partagent le même segment. Le total est de **164 images**
pour sept notices couvertes.

## Pages à écarter du dérivé ciblé

`1–96`, `101–106`, `163–185`, `187–479`, `568–691`, `707–724` : **560 images**.
Ces pages ne sont pas nécessaires aux loci canoniques ci-dessus ; elles incluent
notamment préfaces, textes/parties latines et œuvres hors périmètre.

## Instruction de transfert

Créer un nouveau jeu d'images nommé, par exemple,
`webdataset/volumes--pg120-byzantine--targeted--<hash>.tar`, contenant
exclusivement les cinq segments ci-dessus et un manifeste embarqué. Attendu :
164 images, soit environ 119 216 004 octets à contenu/encodage comparable
(~77,35 % de volume économisé, estimation indicative). Vérifier le nouveau
fichier distant avant toute purge de l'archive de 724 images.

## Résultat

Le PDF image-only original complet s’est avéré plus compact que ce dérivé estimé : 84 702 330 octets pour les 724 pages. Il a été vérifié à distance sous `scans/volumes/pg120-byzantine/pg120-original-image-only.pdf`, SHA-256 `7c9d7e5828af3e5a5414e595390eaf80ff0bc8e6ba7810b1e910794981c1bdee`. L’archive JPEG de 526 295 040 octets a ensuite été supprimée. La couverture ciblée reste documentée par la table ci-dessus, tandis que les autres pages grecques du volume demeurent disponibles pour de futurs rattachements.

## Priorité suivante proposée

Après PG 120, traiter **PG 56 — Chrysostome/Sévérien** : l'archive HF entière
`webdataset/volumes--pg56-chrysostom-severianus--bba468331a16.tar` fait 780
images / 671 344 640 octets et ne sert que 23 notices mappées dans
`scan_validation_pg56_chrysostom_severianus.md`. Elle a un fort potentiel de
compaction, mais reste **REVIEW avant transfert** : il faut d'abord convertir
ses colonnes MPG en pages fichier exactes et contrôler au moins une page grecque
dans chaque segment fusionné, comme pour PG 120.

## Nettoyage

Les aperçus Commons utilisés pour les cinq contrôles ont été temporaires ; ils
ont été supprimés après inspection. Aucun asset local ni archive n'est conservé
par cet audit.
