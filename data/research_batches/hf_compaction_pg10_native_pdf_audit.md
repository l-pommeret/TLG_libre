# Audit de remplacement HF — *Patrologia Graeca* 10

## Décision

**READY pour le remplacement du fac-similé ; REVIEW pour toute extension ou
extraction ciblée nouvelle.** Le PDF Commons PDM remplace sans perte les 826
feuilles du tar. Le manifeste actuellement validé ne comprend toutefois que
cinq notices et ses preuves grecques détaillées proviennent du témoin IA de la
même édition, non d'un échantillon PDF Commons documenté par segment. La
compaction est donc sûre; un nouveau dispatch ciblé devra échantillonner le
grec dans le PDF Commons à chaque segment retenu.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 10](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._010.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/8/8e/Patrologia_Graeca_Vol._010.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  97 803 048 octets, SHA-1 `3d3f305f98234423f64e8859b4fb1c5e5a55ed13`,
  991 × 1595 px. Le registre et le rapport de validation établissent 826
  pages; aucun paquet JP2 ni PPI natif distinct n'est publié par Commons.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); la provenance est consignée comme
  `Creative Commons Public Domain Mark 1.0` dans `data/scan_sources.csv`.

Le témoin auxiliaire Internet Archive `patrologiaecursu10mignuoft` est utile
pour sa pagination (830 vues, JP2 300 ppi), mais n'a pas de droit IA explicite.
Il ne doit donc ni remplacer le PDF Commons ni être transféré dans cette
opération.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg10-gregory-thaumaturgus--b921a1d937d2.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 826 |
| Taille tar | 621 762 560 octets |
| SHA-256 tar/manifeste | `ea7aa3c06e281ef966ed35ec6d4e93d80a15a0cb3c8828b71355808577dc9250` |
| PDF natif Commons | 97 803 048 octets ; 826 pages |
| Gain estimé | 523 959 512 octets (84,27 %) |

Le tar et le PDF Commons ont le même nombre de feuilles. Le PDF peut donc
remplacer le tar comme fac-similé sans perte de page, d'édition ni de
provenance. Les JPEG du tar ne sont pas byte-identiques au PDF, mais sont
régénérables depuis lui. Le remplacement reste image-only : aucun OCR
fournisseur, texte dérivé ou fichier OCR ne doit être transféré.

## Mappings directs actuellement validés

Le registre contient exactement cinq lignes
`ARCHIVED_DIRECT_REGISTRY_MAPPING`, toutes fondées sur des colonnes MPG 10
directes. Les numéros de feuilles IA ne sont que des repères de contrôle : ils
ne doivent pas être convertis par décalage en numéros de pages PDF Commons.
Sélectionner les feuilles du PDF uniquement après lecture des colonnes
imprimées.

| TLG | Colonnes MPG 10 | Repères IA non transférables |
|---|---:|---:|
| 2063.006 — *Metaphrasis in Ecclesiasten* | 988–1017 | `n501–n516` |
| 2063.008 — *Ad Tatianum de anima* `[Sp.]` | 1137–1145 | `n576–n580` |
| 2063.009 — *In annuntiationem* `[Sp.]` | 1145–1169 | `n580–n592` |
| 2063.013 — fr. Mt 6.22–23 | 1189 | `n602` |
| 2063.010 — *Sermo in omnes sanctos* `[Sp.]` | 1197–1204 | `n606–n609` |

Le chevauchement col. 1145 est une borne commune entre `.008` et `.009` et
doit être dédupliqué sans rompre les deux liens canoniques. Les marqueurs
`[Sp.]` restent des attributions du Canon. La mention de duplication partielle
avec `2892.043` dans la notice de `2063.008` n'autorise pas à créer un mapping
PG10 pour `2892.043`.

## Preuves grecques et limites de confiance

Les vues temporaires IA, maintenant supprimées, ont montré du grec net avec de
légères rousseurs à `n516` (cols. 1017–1018), `n590` (1165–1166) et `n607`
(1199–1200). Elles couvrent le début, milieu et fin des cinq loci et confirment
la pagination de l'édition Migne. Elles ne constituent cependant pas une
preuve de licence IA ni une preuve visuelle directe du fichier Commons : le
PDF Commons PDM doit être échantillonné, sans conservation locale, dans chacun
des cinq segments avant une extraction ciblée. Cette réserve ne remet pas en
cause l'équivalence 826-feuilles nécessaire au remplacement du tar.

## Exclusions et notices à ne pas inférer

Le manifeste existant doit rester limité aux cinq TLG ci-dessus. En particulier
`2022.x02` n'est qu'un renvoi vers `2063.006`, et ne crée aucune nouvelle
notice. Les autres œuvres de `2063` sans locus MPG 10 direct dans le Canon
restent exclues.

Quatre autres notices canoniques citent bien MPG 10 (`2577.002`, cols. 232–236;
`2115.019`, 632–633; `2115.059`, 868–869; `2859.002`, 1177–1189), mais elles
ne figurent ni dans le registre PG10 ni dans le rapport de validation actuel.
Elles sont donc **REVIEW non mappées**, non pas des couvertures implicites ni
des alternatives du groupe `2063`. Les préfaces, apparats, traductions et tout
autre contenu de volume restent hors manifeste tant que leurs colonnes et leur
preuve grecque Commons ne sont pas contrôlées.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg10-gregory-thaumaturgus/pg10-original-image-only.pdf`.
2. Chemin, 97 803 048 octets, SHA-256 et 826 pages vérifiés à distance avant
   toute suppression.
3. Les cinq mappings directs, leurs attributions et
   le maintien hors manifeste des quatre notices `REVIEW` non mappées.
4. Tar retiré seulement après ces vérifications distantes. Avant un
   manifeste ciblé, contrôler le grec Commons dans chacun des cinq segments;
   aucun OCR ne sera utilisé.

Le téléchargement distant forcé a confirmé le SHA-256
`e9b636cdcc32147f1183adca1035ad4bbac698bcc41c97d140c3853ce467e7fe`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
