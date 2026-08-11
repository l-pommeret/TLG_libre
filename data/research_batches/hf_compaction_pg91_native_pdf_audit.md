# Audit de remplacement HF — *Patrologia Graeca* 91

## Décision

**READY pour compacter le contenant, avec deux statuts de couverture
inchangés : 29 notices directes READY et cinq alternatives historiques
REVIEW.** Le PDF Commons conserve le même fac-similé MPG 91; il ne doit jamais
faire passer les cinq témoins historiques au statut d'éditions canoniques.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 91](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._091.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/f/f1/Patrologia_Graeca_Vol._091.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  98 227 411 octets, SHA-1 `5567a23ac412be4449c5fe573d16cdd67ef0e7be`,
  997 × 1581 px. Le rapport de validation documente 818 pages et ~151 ppi.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg91-maximus-thalassius--148279c352ec.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 818 |
| Taille tar | 579 440 640 octets |
| SHA-256 tar/manifeste | `a6fbc544948f126e67ebd95c9e0a61a5c502f67aa74cb57fdc9a27b1c03378b7` |
| PDF natif | 98 227 411 octets ; 818 pages |
| Gain estimé | 481 213 229 octets (83,05 %) |

Le tar et le PDF portent les mêmes 818 pages. Le PDF est donc un remplacement
de fac-similé sans perte de pagination ou de provenance. Les JPEG du tar ne
sont pas identiques octet pour octet au PDF; ils peuvent être rendus depuis ce
dernier au besoin. Toute restitution reste image-only et exclut l'extraction ou
la conservation d'OCR fournisseur.

## Mappings et statuts à préserver

Les 29 notices **READY**, consignées intégralement dans
`scan_validation_pg91_maximus_thalassius.md`, sont :

| Groupe | Notices TLG et limites MPG 91 |
|---|---|
| Fragments/Maxime | 2102.035 : 725, 813, 821, 944, 948, 965, 968; 2892.013–.023 : 9–140 (avec scholia explicitement séparés); 2892.026–.029 : 149–213; 2892.031–.035 : 217–264; 2892.037–.038 : 265–269; 2892.040 : 276–280; 2892.042 : 288–353; 2892.044 : 364–649 |
| Thalassius/autres | 2906.001 : 1428–1470; 3165.001 : 1472–1480; 3413.001 : 216–217 |

Les cinq sections suivantes restent **REVIEW** : elles sont dans le PDF comme
témoin MPG, mais le canon privilégie une édition moderne distincte.

| TLG | Édition canonique | Locus MPG 91 |
|---|---|---:|
| 2892.025 | Levrie, CCG 89 (2017) | 145–149 |
| 2892.030 | van Deun, REB 58 (2000) | 213–216 |
| 2892.039 | van Deun, JECSt 60 (2008) | 269–273 |
| 2892.049 | Cantarella (1931), *Mystagogia* | 657–717 |
| 2892.051 | Constas (2014), *Ambigua ad Joannem* | 1061–1417 |

Ces cinq plages peuvent être conservées seulement sous le label
`REVIEW_HISTORICAL_ALTERNATIVE`; aucune substitution silencieuse d'édition n'est
autorisée. Le renvoi 2808.x02 reste aussi exclu car ce n'est pas une œuvre
autonome.

## Preuve grecque existante

Les contrôles temporaires déjà menés confirment : p. 10 (index du volume),
p. 15 (cols 17–18, grec/latin net), p. 400 (cols 751–752, fragments) et p. 760
(cols 1443–1444, Thalassius). Ces vues ont été supprimées. Toute extraction
doit rester guidée par les colonnes imprimées, notamment pour 2102.035 (sept
fragments non contigus) et les limites qui partagent une colonne.

## Action exécutée et vérifiée

1. Le PDF a été déposé sous
   `scans/volumes/pg91-maximus-thalassius/pg91-original-image-only.pdf`.
2. Un téléchargement distant forcé a confirmé 98 227 411 octets et le SHA-256
   `bbc2e41f37c926e5719cf54e0930d9fa6bfa51cecee59b9e367ee500104fdfa7`.
3. Le manifeste conserve 29 notices READY et cinq drapeaux
   `REVIEW_HISTORICAL_ALTERNATIVE`.
4. L'ancien tar a été retiré seulement après cette validation; il reste dans
   l'historique HF et demeure régénérable depuis le PDF, sans OCR fournisseur.

L'audit préparatoire n'avait conservé aucun asset. L'exécution a transféré
uniquement le PDF image-only, sans OCR.
