# Audit de remplacement HF — *Patrologia Graeca* 44

## Décision

**READY pour remplacer le tar par le PDF Commons PDM; REVIEW avant toute
extraction ciblée nouvelle.** Le PDF natif ouvert est l'édition Migne exacte et
préserve les 718 feuilles du tar. Les cinq notices canoniques actuelles sont
maintenues; le rapport ne transforme pas l'intégralité du tome en couverture
TLG et impose un échantillon grec Commons par segment avant dispatch.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 44](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._044.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/2/2e/Patrologia_Graeca_Vol._044.pdf)
* **API Commons contrôlée le 2026-08-12 :** MIME `application/pdf`,
  66 785 445 octets, SHA-1 `f769d1e2708131df23af4c6ab7d9c29f13fd8e62`,
  929 × 1545 px. Le registre et la validation établissent 718 pages; Commons
  ne publie ni paquet JP2 séparé ni PPI natif distinct.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); la provenance est consignée comme
  `Creative Commons Public Domain Mark 1.0` dans `data/scan_sources.csv`.

Le comparateur Internet Archive `patrologiaecursu44mignuoft` (722 vues, JP2
300 ppi, licence non déclarée) atteste pagination et qualité de la même
édition, mais il n'est pas une source transférable et ne remplace pas le PDF
Commons PDM.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg44-gregory-nyssa--40d4f3862ecb.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 718 |
| Taille tar | 412 487 680 octets |
| SHA-256 tar/manifeste | `513239768785bd69f9688d7ba349a39f8d6f0b271fa48547989da26f446d3e27` |
| PDF natif Commons | 66 785 445 octets ; 718 pages |
| Gain estimé | 345 702 235 octets (83,81 %) |

Le tar et le PDF Commons ont le même nombre de feuilles. Le PDF peut donc
remplacer le tar comme fac-similé sans perte de page, d'édition ni de
provenance. Les JPEG rendus ne sont pas byte-identiques au PDF, mais sont
régénérables depuis lui. Le remplacement reste image-only : aucun OCR
fournisseur, texte dérivé ou fichier OCR ne doit être transféré.

## Mappings directs et frontières strictes

Le registre contient exactement cinq `ARCHIVED_DIRECT_REGISTRY_MAPPING` :

| TLG | Colonnes MPG 44 | Repères IA non transférables |
|---|---:|---:|
| 2017.078 — *Apologia in hexaemeron* | 61–124 | `n36–n67` |
| 2017.079 — *De opificio hominis* | 124–256 | `n67–n133` |
| 2017.053 — *Orationes viii de beatitudinibus* | 1193–1301 | `n602–n656` |
| 2017.054 — *In illud: Tunc et ipse filius* | 1304–1325 | `n657–n668` |
| 2017.055 — *Ad imaginem dei et ad similitudinem* `[Sp.]` | 1328–1345 | `n669–n678` |

La colonne 124 est une borne commune à `.078` et `.079` : dédupliquer la
feuille qui la porte tout en gardant les deux liens. Les repères IA ne doivent
jamais être transposés en numéros de page PDF Commons par une simple formule;
seules les colonnes imprimées du PDF PDM peuvent fixer les feuilles cibles.

## Preuves grecques et limite de source

Les vues IA temporaires, depuis supprimées, ont montré du grec lisible avec un
papier légèrement jauni : `n36` (cols. 61–62, début de `2017.078`), `n620`
(1229–1230, au sein de `2017.053`) et `n678` (1345–1346, borne finale de
`2017.055`). Elles valident la qualité et la concordance de l'édition aux
trois grandes zones du manifeste, mais ne constituent ni une licence IA ni une
preuve visuelle directe du PDF Commons. Les segments `.079` et `.054` n'ont
pas d'échantillon grec individuel documenté : avant toute extraction ciblée,
inspecter sans conservation locale une page grecque Commons dans chacun des
cinq segments et les feuilles de leurs bornes. Cette réserve ne remet pas en
cause l'équivalence 718-feuilles requise pour la compaction.

## Exclusions et absence d'alternatives

Le Canon ne renvoie que ces cinq notices à MPG 44, et le registre ne contient
aucun mapping alternatif PG44. La mention canonique de duplication de
`2017.055` avec `2896.003` ne crée pas de mapping PG44 pour `2896.003`.
Conserver le marqueur `[Sp.]` sans réattribuer l'œuvre à Grégoire de Nysse.

Toutes les préfaces, apparats, traductions et plages hors 61–256,
1193–1301, 1304–1325 et 1328–1345 restent hors manifeste. Les lacunes
256–1193, 1301–1304 et 1325–1328 ne doivent pas être comblées par inférence
de pagination ou par la présence textuelle dans le volume.

## Action exécutée et vérifiée

1. PDF natif déposé sous
   `scans/volumes/pg44-gregory-nyssa/pg44-original-image-only.pdf`.
2. Chemin, 66 785 445 octets, SHA-256 et 718 pages vérifiés à distance avant
   toute suppression.
3. Les cinq mappings, la frontière commune 124, le `[Sp.]` et les
   exclusions; ne pas ajouter d'alternative ni de couverture implicite.
4. Tar retiré seulement après ces vérifications distantes. Toute sélection
   ciblée doit d'abord échantillonner le grec Commons dans chaque segment, sans
   OCR.

Le téléchargement distant forcé a confirmé le SHA-256
`98eb82ef45c2fcddb2342028cb1baf42585a1ac56651c86c274752a7321e1ba5`.
L'ancien tar reste récupérable dans l'historique HF. Aucun OCR fournisseur n'a
été transféré.
