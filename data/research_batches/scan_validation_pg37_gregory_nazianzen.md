# Validation scan — *Patrologia Graeca* 37, Grégoire de Nazianze (Migne)

## Décision

**READY partiel — quatre notices à bornes canoniques explicites; deux autres restent REVIEW.** `patrologiaecursu37mignuoft` est absent de `data/scan_sources.csv` et de `scans/`. Une copie PDM est disponible sur Commons sous [*Patrologia Graeca* vol. 037](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._037.pdf). Le volume couvre exactement les références MPG 37 de 2022.059–062. Les journaux signalent aussi 2022.057 (*Epigrammata*) et 2022.058 (*Testamentum*), mais sans bornes MPG vérifiées : elles ne doivent pas être ingérées avant localisation distincte.

## Mapping image-only vérifié

Sur l’exemplaire IA contrôlé, `n` correspond aux colonnes `2n−11` et `2n−10`.

| Notice TLG | Colonnes MPG 37 | Feuilles IA repères |
|---|---:|---:|
| 2022.059 — *Carmina dogmatica* | 397–522 | `n204`–`n266` |
| 2022.060 — *Carmina moralia* | 521–968 | `n266`–`n489` |
| 2022.061 — *Carmina de se ipso* | 969–1029; 1166–1452 | `n490`–`n520`; `n588`–`n731` |
| 2022.062 — *Carmina quae spectant ad alios* | 1451–1577 | `n731`–`n794` |
| 2022.057 — *Epigrammata* | locus MPG non vérifié | REVIEW |
| 2022.058 — *Testamentum* | locus MPG non vérifié | REVIEW |

## Provenance, droits et qualité

| Champ | Valeur vérifiée |
|---|---|
| Source ouverte à employer | Commons, *Patrologia Graeca Vol. 037*, licence Public Domain explicite |
| Duplicat technique contrôlé | IA [`patrologiaecursu37mignuoft`](https://archive.org/details/patrologiaecursu37mignuoft), t. 37, 1857; l’API IA n’expose pas de licence |
| Archive JP2 IA | `patrologiaecursu37mignuoft_jp2.zip`, 341 820 885 octets, SHA-1 `3c2ac3e2030cc43e445fd9571ec8cc2bf5469f22`, 818 vues, 300 ppi |
| Scandata IA | `patrologiaecursu37mignuoft_scandata.xml`, SHA-1 `8bffc588be126d58a06f7d6379158fc775574975` |
| Original JP2 | aucun paquet original distinct listé par IA |
| Rendement READY | 4 notices; 524 feuilles repères distinctes (deux grands blocs `n204`–`n520` et `n588`–`n794`) |

## Contrôle visuel sans OCR

Les trois vues temporaires `n204` (cols. 397–398, début des *Poemata dogmatica*), `n500` (989–990, *Poemata de se ipso*) et `n794` (1577–1578, fin de *Poemata quae spectant ad alios*) sont nettes, complètes et bien contrastées; les rousseurs mineures n’entravent pas le grec. Tous les temporaires ont été supprimés. Aucun OCR, PDF, archive JP2 ou image d’ingestion n’a été conservé.

## Action proposée

Ingestion **image-only READY depuis Commons PDM** pour 2022.059–062, par les colonnes imprimées de la table (vérifier les numéros de pages propres au fichier Commons). Le duplicat IA ne sert qu’à fixer la pagination et la qualité, pas comme preuve autonome de licence. Laisser 2022.057–058 en REVIEW jusqu’à établissement de leurs loci.

## Compaction HF vérifiée

- PDF image-only Commons transféré sous `scans/volumes/pg37-gregory-nazianzen/pg37-original-image-only.pdf` : 100 503 252 octets, 974 pages.
- SHA-256 local et distant : `7ad53d25e9fd8b15218267c90d452e42dec881eb23f2802a92db8f74037eb7d1`.
- Le tar redondant de 638 668 800 octets a été supprimé après vérification distante ; récupération possible via l'historique HF.
