# Audit de remplacement HF — *Patrologia Graeca* 38

## Décision

**READY pour remplacer le tar par le PDF Commons PDM; REVIEW pour toute
extension de manifeste ou extraction ciblée nouvelle.** Le PDF ouvert est
l'édition Migne exacte et préserve les 748 feuilles du tar. Les deux seuls loci
actuellement enregistrés restent `2022.063–.064`; aucune autre couverture ne
doit être déduite du contenu du tome.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 38](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._038.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/9/9e/Patrologia_Graeca_Vol._038.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  91 939 388 octets, SHA-1 `d73dc72c143d7d1592762d4a208ead0b4efa26b9`,
  981 × 1547 px. Le registre et la validation établissent 748 pages; aucun
  paquet JP2 ni PPI natif distinct n'est publié par Commons.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); la provenance est inscrite comme
  `Creative Commons Public Domain Mark 1.0` dans `data/scan_sources.csv`.

Le duplicat Internet Archive `patrologiaecursu38mignuoft` (664 vues à 300 ppi,
licence non déclarée) sert seulement à la concordance technique et aux
échantillons visuels. Il ne doit pas remplacer le PDF Commons PDM ni être
transféré dans le cadre de cette compaction.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg38-gregory-nazianzen--54cea3c8f6b2.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 748 |
| Taille tar | 536 985 600 octets |
| SHA-256 tar/manifeste | `9c2996aa20835797600b1d5c170394cb20a9ed4e313bf5aa286ed081c725a624` |
| PDF natif Commons | 91 939 388 octets ; 748 pages |
| Gain estimé | 445 046 212 octets (82,88 %) |

Le tar et le PDF Commons ont le même nombre de feuilles. Le PDF peut donc
remplacer le tar comme fac-similé sans perte de page, d'édition ni de
provenance. Les JPEG rendus ne sont pas byte-identiques au PDF, mais sont
régénérables depuis lui. Le remplacement reste image-only : aucun OCR
fournisseur, texte dérivé ou fichier OCR ne doit être transféré.

## Mappings directs, recouvrement et preuve grecque

Le registre contient exactement deux `ARCHIVED_DIRECT_REGISTRY_MAPPING` :

| TLG | Colonnes MPG 38 | Repères IA non transférables |
|---|---:|---:|
| 2022.063 — *Epitaphia* | 11–82 | `n11–n46` |
| 2022.064 — *Epigrammata* | 81–130 | `n46–n70` |

Les colonnes 81–82 (et leur feuille commune) appartiennent aux deux notices;
elles doivent être dédupliquées physiquement tout en étant reliées aux deux
mappings. Les repères IA ne sont pas convertibles automatiquement en pages du
PDF Commons : une sélection doit suivre les colonnes imprimées du fichier PDM.

Les rendus IA temporaires, depuis supprimés, `n13` (cols. 15–16) et `n47`
(83–84) montrent un grec lisible dans chacun des deux loci; `n72` est un
contrôle de qualité en aval, hors de leurs bornes. Les vues attestent la
pagination et la qualité de l'édition mais pas directement le PDF Commons ni
le droit IA. Avant toute extraction ciblée, inspecter sans conservation locale
au moins une page grecque du PDF Commons dans chacun des deux segments et les
feuilles de bornes. Cela ne remet pas en cause l'équivalence 748-feuilles pour
la compaction.

## Exclusions et absence d'alternatives

Il n'existe aucun mapping alternatif PG38 dans le registre : les deux entrées
sont directes. La note canonique « Dup. partim `2022.057` » ne doit pas créer
un mapping PG38 pour `2022.057`; de même, la remarque « Epitaph. 129 spurium »
ne doit pas supprimer ou étendre les bornes canoniques `11–82`.

`2705.027` (MPG 38: 685–841) est une notice canonique présente dans le tome,
mais elle est absente du manifeste PG38 actuel. Elle est **REVIEW non mappée**,
et non une couverture implicite, une alternative des épigrammes, ni une raison
d'étendre cet audit. Toutes les autres feuilles, préfaces, apparats,
traductions et intervalles hors 11–130 restent hors manifeste jusqu'à contrôle
individuel.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg38-gregory-nazianzen/pg38-original-image-only.pdf`.
2. Chemin, 91 939 388 octets, SHA-256 et 748 pages vérifiés à distance avant
   toute suppression.
3. Les deux mappings, leur recouvrement 81–82 et l'exclusion du reste;
   maintenir `2705.027` en `REVIEW non mappée` sans ajouter d'alternative.
4. Tar retiré seulement après ces vérifications distantes; un dispatch
   ciblé devra auparavant échantillonner le grec Commons dans les deux segments,
   sans OCR.

Le téléchargement distant forcé a confirmé le SHA-256
`92303c0230eb0c7855240d51d4a47f6f1870f3aa0983e6c6d93554c76e070750`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
