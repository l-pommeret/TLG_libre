# Audit de remplacement HF — *Patrologia Graeca* 52

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only.** Cette
décision concerne l'équivalence du fac-similé de 476 feuilles et ne confère pas
une couverture canonique au volume entier. Seules les 26 notices et les bornes
MPG imprimées ci-dessous restent exploitables; toutes les autres feuilles sont
hors manifeste TLG jusqu'à vérification séparée.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 52](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._052.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/e/ed/Patrologia_Graeca_Vol._052.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  56 820 963 octets, SHA-1 `2249909539ef454b47810e7ba9149c96fb257ffb`,
  1025 × 1547 px. La validation établit 476 pages, à environ 145 ppi; aucun
  paquet JP2 ni PPI natif distinct n'est publié par Commons.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); `Creative Commons Public Domain Mark 1.0`
  est la provenance enregistrée dans `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg52-chrysostom--054ba5a70336.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 476 |
| Taille tar | 364 677 120 octets |
| SHA-256 tar/manifeste | `7ace6d813a33762c72cf6836264f1ad9f51310647e40d1a473618cbe42bebcf9` |
| PDF natif | 56 820 963 octets ; 476 pages |
| Gain estimé | 307 856 157 octets (84,42 %) |

Le tar et le PDF couvrent les mêmes 476 feuilles. Le PDF peut donc le
remplacer comme fac-similé sans perte de page, d'édition ni de provenance. Les
JPEG du tar ne sont pas byte-identiques au PDF, mais sont régénérables depuis
celui-ci. Le remplacement reste image-only : aucun OCR fournisseur, texte
dérivé ou fichier OCR ne doit être transféré.

## Mappings stricts et qualité grecque documentée

`scan_validation_pg52_chrysostom.md` établit les 26 mappings suivants. Les
astérisques sont des caractères de la pagination MPG imprimée, pas des
notations supprimables; ils doivent être reproduits tels quels. Toute
sélection future doit suivre les **colonnes imprimées**, non une estimation par
numéro de page PDF, et dédupliquer une feuille aux bornes communes tout en la
reliant aux deux notices.

| Notices TLG | Colonnes MPG 52 |
|---|---:|
| 2800.012 | 809–812 |
| 2062.089–.093 | 391–396 ; 413–420 ; 427*–432 ; 435*–438 ; 443–448 |
| 2062.094–.108 | 529–536 ; 535–536 ; 541*–542* ; 623–748 ; 761–766 ; 765–772 ; 791–794 ; 449–460 ; 755–760 ; 793–796 ; 797–800 ; 799–802 ; 801–802 ; 803–808 ; 807–809 |
| 2062.110–.111, .142 | 835–840 ; 841–844 ; 395–414 |
| 4139.002, .010 | 827–835 ; 813–816 |

La validation a inspecté puis supprimé les rendus temporaires p. PDF 20
(cols. 403–404), p. 250 (609–610) et p. 400 (791–792, début de la section
*Spuria*). La typographie et le grec des passages mixtes étaient nets et
lisibles. Ces trois vues prouvent la qualité de début/milieu/fin du volume;
seule p. 400 tombe dans un locus direct (`2062.100`, 791–794). Les deux autres
échantillons sont des zones voisines ou interstitielles et ne constituent pas
une preuve de contenu pour une notice : avant toute extraction ciblée, il faut
contrôler visuellement une feuille grecque dans chaque segment retenu et ses
bornes imprimées.

## Exclusions strictes

Le registre recense exactement les 26 mappings ci-dessus, tous sous
`READY_REPORT_EXACT_MAPPING`; aucun mapping alternatif n'est validé pour PG52.
Ne pas créer d'alternative ni étendre le manifeste au gré du contenu du
volume. Restent expressément exclus :

* `2062.109`, sautée dans la série `.094–.108` et non annoncée par le Canon
  pour un locus MPG 52;
* `2062.344`, `2062.376` et `4139.089`, qui n'ont pas de locus MPG 52 dans
  leur notice canonique;
* toutes les feuilles ou textes non listés, y compris les préfaces, apparats,
  traductions et passages entre les bornes directes.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg52-chrysostom/pg52-original-image-only.pdf`.
2. Chemin, 56 820 963 octets, SHA-256 et 476 pages vérifiés à distance avant
   toute suppression.
3. Les 26 mappings, leurs étoiles, les chevauchements et
   les exclusions; ne pas ajouter d'alternative.
4. Tar retiré seulement après ces vérifications distantes. Les rendus
   resteront régénérables depuis le PDF, sans OCR.

Le téléchargement distant forcé a confirmé le SHA-256
`280e49dc265b516f14e25592fdd7bb6bedfff0be1f373e5efceb6976a849e2bf`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
