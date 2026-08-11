# Validation de scan — Berthelot–Ruelle, *Collection des anciens alchimistes grecs*, tome II, fascicules 3–6

**Décision : READY, mais uniquement pour TLG `2181.002`; REJECT pour
`2181.001` dans cet exemplaire.** Le fichier Commons est absent de
`data/scan_sources.csv` et de `scans/`. C'est le tome II, texte grec de
l'édition Berthelot–Ruelle (Paris, Steinheil, 1888) prescrite par le canon.
Son contenu matériel est toutefois explicitement les fascicules **3–6** : il
contient la plage imprimée 300–315, mais pas les pp. 38–39 du fascicule 1–2.

| Contrôle | Résultat vérifié |
|---|---|
| Source / droits | [Wikimedia Commons — *Collection des anciens alchimistes grecs*, L2, 3–4–5–6, 1888](https://commons.wikimedia.org/wiki/File:Collection_des_anciens_alchimistes_grecs_-_L2,_3-4-5-6,_1888.djvu). **CC Public Domain Mark 1.0** / domaine public explicite. |
| Fichier / intégrité | DJVU de 708 pages, `2 187 × 3 147` px, 18 275 541 octets (17,43 Mo), SHA-1 `509d06381aa17ef7b276674ffccc1a9cb6560df5`. Ce n'est pas un item IA avec paquet JP2 : aucun JP2, PPI ou fichier `scandata` ne doit être inventé. |
| Qualité | Les trois rendus Commons temporaires à 960 px inspectés (source 2 187 px) sont très nets : grec, accents, notes critiques et numérotation restent lisibles. De légères taches de papier ne masquent aucun texte. |
| Édition | La page 300 porte le titre **« Chimie de Moïse »** et l'incipit grec `Εὐποία καὶ εὐτυχία...`, exactement le titre de TLG 2181.002. La borne p. 315 porte l'explicit de ce texte avant l'ouverture de l'article suivant. |

## Concordance et bornes

| Notice TLG | Référence canonique | Contrôle / décision |
|---|---|---|
| `2181.001` — *Μωσέως δίπλωσις* | CAAG II (1888), pp. 38–39 | **REJECT pour ce fichier.** Le fichier est étiqueté L2, fascicules 3–6 et ses séquences textuelles observées commencent bien après p. 38 ; il ne fournit donc pas les pp. 38–39. Rechercher un exemplaire PDM des fascicules 1–2, sans remplacer silencieusement la source. |
| `2181.002` — *Εὐποία καὶ εὐτυχία…* | CAAG II (1888), pp. 300–315 | **READY.** `page=342` affiche p. 300, le titre « Chimie de Moïse » et le début grec ; `page=350` affiche p. 308 au milieu de la continuité ; `page=357` affiche p. 315, l'explicit, puis le titre de l'article suivant. |

## Mapping image-only pour TLG 2181.002

Le décalage vérifié dans la section grecque pertinente est `page Commons =
page imprimée + 42`. Prélever les images Commons **342–357 incluses** (16
images) : la page 357 contient aussi le départ de l'article suivant, mais est
nécessaire à l'explicit de p. 315. Les conserver sous la portée stricte
`TLG2181.002 / CAAG-II-1888 / fasc.3–6`, avec URL de fichier, PDM, SHA-1 du
DJVU source et pagination imprimée. Ne pas utiliser de texte ou OCR fourni par
un tiers.

Les rendus JPEG et HTML de contrôle ont été supprimés après inspection. Aucun
DJVU, PDF, archive d'images ni OCR n'a été conservé localement, et aucun
commit/push n'a été effectué.
