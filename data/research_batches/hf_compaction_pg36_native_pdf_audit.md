# Audit de remplacement HF — *Patrologia Graeca* 36

## Décision

**READY pour remplacer le tar par le PDF Commons PDM; REVIEW pour étendre le
manifeste.** Le PDF natif ouvert est l'édition Migne exacte et préserve les 722
feuilles du tar. Le registre actuel ne valide toutefois que neuf loci `2022`;
il ne faut pas étendre mécaniquement leur couverture aux autres textes du tome
avant contrôle individuel des colonnes et du grec dans le fichier Commons.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 36](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._036.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/7/71/Patrologia_Graeca_Vol._036.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  90 293 047 octets, SHA-1 `fa56a9d58ad999479af7a51fd1917262d574116e`,
  1008 × 1583 px. La validation établit 722 pages (environ 86,11 Mo); aucun
  paquet JP2 ni PPI natif distinct n'est publié par Commons.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); la provenance est enregistrée comme
  `Creative Commons Public Domain Mark 1.0` dans `data/scan_sources.csv`.

Le duplicat Internet Archive `patrologiaecursu36mignuoft` (JP2 300 ppi,
licence non déclarée) a servi à la concordance et aux contrôles visuels. Il
reste une source de comparaison, pas une source autorisée à transférer ni un
substitut au PDF Commons PDM.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg36-gregory-nazianzen--f2db448424dd.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 722 |
| Taille tar | 559 779 840 octets |
| SHA-256 tar/manifeste | `66fd33d88617e8a61e33c8d3c71423277c1c3f4bcc873e83e4b78d3b28464338` |
| PDF natif Commons | 90 293 047 octets ; 722 pages |
| Gain estimé | 469 486 793 octets (83,87 %) |

Le tar et le PDF Commons ont le même nombre de feuilles. Le PDF peut donc
remplacer le tar comme fac-similé sans perte de page, d'édition ni de
provenance. Les JPEG rendus ne sont pas byte-identiques au PDF, mais sont
régénérables depuis lui. Le remplacement reste image-only : aucun OCR
fournisseur, texte dérivé ou fichier OCR ne doit être transféré.

## Mappings directs déjà enregistrés

`scan_validation_pg36_gregory_nazianzen.md` et le registre fixent exactement
neuf `ARCHIVED_DIRECT_REGISTRY_MAPPING`. Les numéros de feuilles IA sont de
simples repères de pagination; aucun décalage ne doit les convertir en numéros
de pages du PDF Commons. Pour ce dernier, sélectionner les pages par les
colonnes imprimées et dédupliquer les bornes partagées.

| TLG | Colonnes MPG 36 | Repères IA non transférables |
|---|---:|---:|
| 2022.047 | 336–360 | `n173–n185` |
| 2022.048 | 360–425 | `n185–n218` |
| 2022.049 | 428–452 | `n219–n231` |
| 2022.050 | 457–492 | `n234–n251` |
| 2022.051 | 608–621 | `n309–n316` |
| 2022.052 | 624–664 | `n317–n337` |
| 2022.053 `[Sp.]` | 665–669 | `n338–n340` |
| 2022.054 `[Sp.]` | 675–678 | `n343–n344` |
| 2022.055 `[Sp.]` | 700–733 | `n355–n372` |

La frontière 360 (`2022.047/.048`) est à conserver une fois tout en la liant
aux deux notices. Les marqueurs `[Sp.]` sont des attributions canoniques à
préserver, jamais des motifs de réattribution.

## Preuves grecques et limite de source

Trois vues IA temporaires, depuis supprimées, ont été vérifiées : `n175`
(cols. 339–340), `n320` (629–630, *Oratio XLV*) et `n372` (733–734). Elles
montrent un grec net avec seulement de légères rousseurs et couvrent début,
milieu et fin des neuf loci. Elles confirment l'édition et les colonnes, mais
ne constituent ni une preuve de droit IA ni une inspection visuelle directe du
PDF Commons. Ainsi, avant toute extraction ciblée nouvelle, il faut inspecter
sans conservation locale une page grecque Commons dans chaque segment et ses
deux bornes imprimées. Cette réserve n'affecte pas l'équivalence 722-feuilles
requise pour remplacer le tar.

## Exclusions, alternatives et lacunes à préserver

Le registre ne contient aucune alternative PG36 : les neuf entrées ci-dessus
sont directes. Ne pas ajouter les autres textes du volume à titre d'alternative
ou de couverture implicite. En particulier, les sept loci canoniques MPG 36
`2022.040–.046` (cols. 173–333), ainsi que `4520.001` (757–902) et
`2962.013` (895), ne figurent pas dans le manifeste PG36 actuel. Ils sont
**REVIEW non mappés** : ils doivent être audités séparément plutôt que rejetés
ou inclus par inférence.

Restent hors du manifeste les préfaces, apparats, traductions et intervalles
entre les bornes directes. Les lacunes autour de 425–428, 452–457,
492–608, 621–624, 669–675 et 678–700 ne sont donc pas des segments cibles
tant qu'une notice canonique, une concordance et un contrôle grec Commons ne
les justifient pas.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg36-gregory-nazianzen/pg36-original-image-only.pdf`.
2. Chemin, 90 293 047 octets, SHA-256 et 722 pages vérifiés à distance avant
   toute suppression.
3. Les neuf mappings, leurs `[Sp.]`, les bornes partagées et le statut
   `REVIEW non mappé` des neuf autres loci; ne pas ajouter d'alternative.
4. Tar retiré seulement après ces vérifications distantes. Tout dispatch
   ciblé requiert d'abord un échantillon grec du PDF Commons par segment,
   sans OCR.

Le téléchargement distant forcé a confirmé le SHA-256
`b6186bc9089493f6eaae8b5165835ae70f2cd7b137a2809b5762c43c49b8689f`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
