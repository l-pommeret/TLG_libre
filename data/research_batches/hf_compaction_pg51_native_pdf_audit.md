# Audit de remplacement HF — *Patrologia Graeca* 51

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** Cette
décision préserve le fac-similé des 388 feuilles, mais ne donne pas au volume
une couverture canonique intégrale : seuls les 25 loci TLG listés ci-dessous
sont directs. Les autres textes et feuilles restent hors manifeste jusqu'à une
vérification indépendante.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 51](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._051.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/3/33/Patrologia_Graeca_Vol._051.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  46 102 582 octets, SHA-1 `c17fd0a8e8618c12eac1701f5e453f90ef86b28e`,
  1012 × 1552 px. La validation établit 388 pages, autour de 145 ppi; aucun
  paquet JP2 ni PPI natif distinct n'est publié par Commons.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); la provenance est enregistrée comme
  `Creative Commons Public Domain Mark 1.0` dans `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg51-chrysostom--e395ee823768.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 388 |
| Taille tar | 305 059 840 octets |
| SHA-256 tar/manifeste | `7319c2e05e508a9f5f7ec294a8f9ea161d1b94804eec129bbcc0bcbf9882441e` |
| PDF natif | 46 102 582 octets ; 388 pages |
| Gain estimé | 258 957 258 octets (84,89 %) |

Le tar et le PDF couvrent les mêmes 388 feuilles. Le PDF peut donc remplacer
le tar comme fac-similé sans perte de page, d'édition ni de provenance. Les
JPEG rendus ne sont pas byte-identiques au PDF, mais sont régénérables depuis
lui. Ce remplacement reste image-only : aucun OCR fournisseur, texte dérivé ou
fichier OCR ne doit être transféré.

## Mappings directs stricts et qualité grecque documentée

`scan_validation_pg51_chrysostom.md` et le registre établissent exactement 25
entrées `READY_REPORT_EXACT_MAPPING`. Les colonnes imprimées — y compris
`17*` — sont la seule clé de découpage valide. Les feuilles aux bornes communes
doivent être stockées une fois, puis reliées aux deux notices correspondantes.

| Notices TLG | Colonnes MPG 51 |
|---|---:|
| 2062.061–.066 | 17*–30 ; 31–40 ; 47–64 ; 65–112 ; 113–156 ; 155–164 |
| 2062.067–.072 | 165–172 ; 171–186 ; 187–208 ; 207–218 ; 217–226 ; 225–242 |
| 2062.073–.078 | 241–252 ; 251–260 ; 261–272 ; 271–302 ; 301–310 ; 311–320 |
| 2062.079–.084 | 321–338 ; 337–348 ; 347–354 ; 353–364 ; 363–372 ; 371–388 |
| 2062.141 `[Sp.]` | 41–48 |

Trois rendus temporaires, depuis supprimés, attestent une typographie et un
grec nets : p. PDF 20 (cols. 25–26), p. 200 (307–308) et p. 350 (557–558).
Les deux premiers se situent respectivement dans `2062.061` et `2062.077`;
le troisième contrôle la qualité de fin de volume mais tombe hors des bornes
directes (l'étendue TLG s'arrête col. 388). Pour une extraction ciblée, il faut
donc encore vérifier visuellement une page grecque dans chaque segment retenu
et les feuilles de ses bornes, au lieu d'inférer les contenus à partir des
numéros de page PDF.

## Exclusions strictes

Aucun mapping alternatif PG51 n'est validé : les 25 lignes du registre sont
toutes directes. Ne pas couvrir par défaut les autres œuvres de Chrysostome ou
les autres passages visibles dans ce volume. Sont notamment exclus :

* toutes les notices `2062` hors `.061–.084` et `.141`, car elles ne disposent
  pas d'un locus MPG 51 direct dans le Canon (elles relèvent d'autres éditions,
  d'autres tomes MPG ou d'une vérification à faire);
* les préfaces, apparats, traductions et interstices entre les bornes imprimées;
* toute page au-delà de la col. 388 comme contenu de l'un des 25 loci, y
  compris l'échantillon qualité p. PDF 350.

Le marqueur `[Sp.]` de `2062.141` est une attribution canonique à conserver;
il ne doit ni être supprimé ni conduire à réattribuer l'œuvre à Chrysostome.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg51-chrysostom/pg51-original-image-only.pdf`.
2. Chemin, 46 102 582 octets, SHA-256 et 388 pages vérifiés à distance avant
   toute suppression.
3. Les 25 mappings, l'astérisque de `17*`, les chevauchements et les
   exclusions sans ajouter de mapping alternatif.
4. Tar retiré seulement après ces vérifications distantes; les rendus
   resteront régénérables depuis le PDF, sans OCR.

Le téléchargement distant forcé a confirmé le SHA-256
`1ccb67f650d98aea281707cc512712a73a63a7d87a87ae78fead390f379859cb`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
