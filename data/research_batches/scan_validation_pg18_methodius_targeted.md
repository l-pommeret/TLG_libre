# Validation ciblée — *Patrologia Graeca* 18, Methodius (TLG 2959.012–.013)

## Décision

**READY_TARGETED, image-only, source Commons PDM.** Deux segments DjVu sont
résolus avec leurs pages exactes et un échantillon grec visuel dans chacun. Le
fichier est un DjVu, non un PDF : le manifeste doit employer son original PDM
ou des rendus de pages issus de cet original, jamais un OCR de fournisseur.

## Source, droits et intégrité

* **Notice Commons :** [*Patrologia Graeca* vol. 18](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._18.djvu)
* **DjVu original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/8/8e/Patrologia_Graeca_Vol._18.djvu)
* **API Commons contrôlée le 2026-08-12 :** MIME `image/vnd.djvu`,
  71 692 271 octets, SHA-1 `c61649e67a8c66772dee9ab1489398e6c9f7e5b4`,
  3982 × 6482 px.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False`; le registre consigne `Creative Commons Public Domain
  Mark 1.0` pour le même volume.
* **Doublon évité :** la seule ingestion PG18 déjà inscrite est
  `2962.005`, pages 262–265 (cols. 512–517); elle ne recouvre aucun des deux
  segments Methodius et ne doit pas être modifiée.

## Résolution DjVu page → colonnes imprimées

Dans cette zone, le rendu Commons une-based `pageN` porte les colonnes
`2N−9` (gauche) et `2N−8` (droite). Cette relation est vérifiée visuellement
aux quatre bornes : p178 = 347–348, p195 = 381–382, p196 = 383–384 et
p203 = 397–398.

| TLG | Locus canonique exact | Pages DjVu à transférer | Nombre | Bornes à conserver dans le manifeste |
|---|---:|---:|---:|---|
| 2959.012 — *Sermo de Simeone et Anna* `[Sp.]` | 348–381 | **178–195**, inclusives | 18 | p178 contient aussi 347; p195 contient aussi 382 |
| 2959.013 — *Sermo in ramos palmarum* `[Sp.]` | 384–397 | **196–203**, inclusives | 8 | p196 contient aussi 383; p203 contient aussi 398 et le début du contenu suivant |

Le total ciblé est **26 pages DjVu distinctes** : `178–195,196–203`. Les
pages restent physiquement entières, mais les colonnes hors locus dans les
quatre feuilles de borne ne doivent pas être rattachées aux notices TLG.

## Correction de la borne communiquée pour 2959.012

La demande mentionnait « cols. 347–360 » pour `2959.012`. Ce n'est pas le
locus canonique : `data/canon_works.csv` donne **MPG 18: 348–381**, et p178
montre précisément 347–348 avec le titre grec du sermon. Limiter l'acquisition
à 347–360 (p178–184) tronquerait le texte. Le manifeste READY retient donc les
colonnes canoniques complètes 348–381 et les pages 178–195; 347 est seulement
la moitié non cible de la première feuille de borne.

## Contrôle visuel grec sans OCR

Huit JPEG Commons temporaires (rendement `pageN-1280px`, tous supprimés après
contrôle) ont servi uniquement à la validation :

| Segment / contrôle | Pages inspectées | Résultat visuel |
|---|---|---|
| 2959.012, début et borne | 178 (347–348), 195 (381–382) | Titre grec/latin *De Simeone et Anna*, grec nettement lisible; fin confirmée |
| 2959.012, échantillon grec | 180 (351–352) | Grec courant net et complet |
| 2959.013, début et borne | 196 (383–384), 203 (397–398) | Titre grec/latin *Logos eis ta Baia*; col. 397 et passage au contenu suivant confirmés |
| 2959.013, échantillon grec | 198 (387–388) | Grec courant net et complet |

Les rendus 1280 px sont suffisamment nets pour établir pagination, titre et
présence grecque; ils ne doivent pas être confondus avec le master 3982 × 6482
du DjVu. Aucun OCR, PDF, archive ou image d'échantillon n'est conservé
localement.

## Endpoints et préparation de transfert ciblé

Les endpoints JPEG testés et stables suivent exactement ce patron pour chaque
numéro de page explicite ci-dessus :

`https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Patrologia_Graeca_Vol._18.djvu/page{N}-1280px-Patrologia_Graeca_Vol._18.djvu.jpg`

Ainsi, les deux jeux sont `N=178…195` et `N=196…203`; les URLs de contrôle
testées incluent [p178](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Patrologia_Graeca_Vol._18.djvu/page178-1280px-Patrologia_Graeca_Vol._18.djvu.jpg), [p195](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Patrologia_Graeca_Vol._18.djvu/page195-1280px-Patrologia_Graeca_Vol._18.djvu.jpg), [p196](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Patrologia_Graeca_Vol._18.djvu/page196-1280px-Patrologia_Graeca_Vol._18.djvu.jpg) et [p203](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Patrologia_Graeca_Vol._18.djvu/page203-1280px-Patrologia_Graeca_Vol._18.djvu.jpg).

Pour préserver la meilleure définition plutôt que les rendus 1280 px, le
workflow distant doit récupérer l'original DjVu Commons, extraire seulement
les pages 178–203 dans un espace éphémère, pousser les 26 pages ou un paquet
image-only ciblé, puis supprimer les temporaires. Ne pas télécharger le DjVu
sur le poste local, et ne pas inclure les pages 262–265 déjà archivées pour
`2962.005`.

## Exclusions strictes

* Maintenir `[Sp.]` pour les deux notices; ne pas les réattribuer à Methodius.
* Ne pas inclure les portions hors locus des p178, p195, p196 et p203, ni le
  texte suivant visible au bas de p203.
* Ne pas élargir à d'autres œuvres MPG 18 (dont `2962.005`, déjà archivée) sans
  mapping et échantillonnage séparés.
* Ne pas utiliser la traduction allemande First1KGreek comme substitut du grec,
  ni aucun OCR fournisseur.

## Action exécutée et vérifiée

1. Deux jeux image-only ciblés créés : `2959.012` → pages 178–195 /
   cols. 348–381; `2959.013` → pages 196–203 / cols. 384–397.
2. Extraction pleine définition réalisée dans un espace éphémère depuis le
   DjVu Commons PDM, avec provenance URL/SHA-1/droits ci-dessus.
3. Après transfert, le compte de 18 + 8 images et les bornes ont été vérifiés;
   l'absence de pages/colonnes hors cible avant toute suppression distante.

Les 26 JPEG ont été transférés sous `scans/tlg2959/pg18-methodius/`. Un contrôle
distant forcé a confirmé les fichiers extrêmes : p178 SHA-256
`cab78269bbf99f6bbcf3a707ff085218c3fc3b2a0d1c4509c849e4a6cc0ce338` et
p203 `083c574a949cea4cd1eb5b5267dd66d5759a4f5cae482622b3aa2ecfd787f847`.
Aucun OCR n'a été utilisé; tous les assets locaux éphémères sont supprimés.
