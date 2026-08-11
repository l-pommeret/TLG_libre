# Validation scan — *Patrologia Graeca* 26 (Athanase)

Date de contrôle : 2026-08-11  
Décision : **READY** — volume entier image-only, sous réserve de sélectionner les feuilles par les colonnes imprimées ci-dessous ; aucun OCR fournisseur ne doit être conservé ou utilisé.

## Source et droits

- Fichier exact : [*Patrologia Graeca* vol. 026 (PDF)](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._026.pdf), *Patrologiae Cursus Completus: Series Graeca*, J.-P. Migne, 1860.
- Provenance déclarée : Internet Archive (crédit de la page-fichier Commons) ; fichier servi par Wikimedia Commons.
- Droits explicites Commons : **Public domain / CC Public Domain Mark**, `Copyrighted: False`, attribution non requise. Catégories : `PD-old-70-expired`, `CC-PD-Mark`.
- Original : PDF, 94 774 657 octets (90,38 MiB), SHA-1 `62d373c614cfc82b6019b77f8ea295ccd085f072`, 785 pages ; géométrie déclarée 991 × 1554 px, 476,64 × 746,88 pt. Cela correspond approximativement à 150 ppi ; pas de paquet JP2 distinct ni de PPI natif séparément déclaré par Commons.
- Le fichier est absent de `data/scan_sources.csv` et aucun chemin d’images PG26 n’existe sous `scans/` au moment du contrôle.

## Concordance canonique et sélection image-only

Le volume est bien l’édition **MPG 26** des *Opera* d’Athanase : les en-têtes visibles portent `S. ATHANASII OPP. PARS I. — HISTORICA ET DOGMATICA.`. Les seize notices ci-dessous citent directement MPG 26 dans le Canon. Les notices modernes qui ne font qu’indiquer une duplication partielle vers ces textes ne sont pas ajoutées comme équivalentes éditoriales.

| TLG | œuvre canonique | colonnes MPG 26 à sélectionner |
|---|---|---:|
| 2035.042 | *Orationes tres contra Arianos* | 12–468 |
| 2035.043 | *Epistulae quattuor ad Serapionem* | 529–648b |
| 2035.044 | *In illud: Qui dixerit verbum in filium* | 648c–676 |
| 2035.045 | *Tomus ad Antiochenos* | 796–809 |
| 2035.046 | *Petitiones Arianorum* | 820–824 |
| 2035.047 | *Vita Antonii* | 835–976b |
| 2035.049 | *Epistula ad Afros episcopos* | 1029–1048 |
| 2035.050 | *Epistula ad Adelphium* | 1072–1084 |
| 2035.051 | *Epistula ad Maximum* | 1085–1089 |
| 2035.052 | *Epistula ad Joannem et Antiochum presbyteros* | 1165–1168b |
| 2035.053 | *Epistula ad Palladium* | 1168b–1169 |
| 2035.054 | *Fragmenta varia* | 1224 ; 1233–1249 ; 1252–1260 ; 1293b–1296c ; 1313b–1313c ; 1320–1325 |
| 2035.055 | *Epistula ad monachos* | 1185–1188 |
| 2035.056 | *Sermo de patientia* [Sp.] | 1297–1309 |
| 2035.057 | *Scholia in Acta* | 1316–1317 |
| 2035.058 | *De azymis* [Sp.] | 1328–1332 |

La pagination de fichier n’est pas assez stable pour remplacer les bornes imprimées : l’ingestion doit inspecter l’en-tête de chaque première et dernière image et enregistrer un manifeste colonne→image. Ne pas déduire les feuilles seulement du nombre de pages.

## Contrôle visuel et qualité

Trois rendus temporaires 960 px du PDF, obtenus directement via l’API Commons (aucun PDF, archive, OCR ou image de volume conservé), ont été inspectés :

| page PDF temporaire | colonnes imprimées observées | résultat |
|---:|---:|---|
| 100 | 187–188 | grec et latin nets, en-tête Athanase conforme |
| 350 | 667–668 | grec lisible, impression homogène |
| 650 | 1267–1268 | grec lisible, impression homogène |

Ces trois vues couvrent début, milieu et fin de l’étendue 12–1332 ; elles confirment le volume et une qualité visuelle exploitable, tout en signalant la résolution modeste (~150 ppi). Les trois rendus ont été supprimés après contrôle. Aucun OCR de Commons, d’Internet Archive ou d’un autre tiers n’a été téléchargé ou consulté.

## Recommandation d’ingestion

**READY (priorité haute, 16 notices directes).** Transférer directement l’original PDM ou, si l’espace impose un ciblage, seulement les images contenant les colonnes listées, avec contrôle visuel des six lacunes du `Fragmenta varia`. Conserver l’URL Commons, la déclaration PDM, le SHA-1 du PDF et un manifeste de bornes imprimées. Lancer exclusivement l’OCR du projet après transfert.

## Compaction HF vérifiée

- PDF image-only original transféré sous `scans/volumes/pg26-athanasius/pg26-original-image-only.pdf` : 94 774 657 octets, 785 pages.
- SHA-256 local et distant : `fb5b12164f77ad1e5296784d1e5e13ffb57b495007c8729e231926fac4a6c4a2`.
- Le tar redondant de 598 251 520 octets a été supprimé après vérification distante ; récupération possible via l'historique HF.
