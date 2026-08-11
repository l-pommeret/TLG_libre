# Validation scan — *Patrologia Graeca* 31, Basile de Césarée

**READY — 50 notices directes à pagination MPG 31 exacte.** Source d’ingestion : [Wikimedia Commons, *Patrologia Graeca* vol. 031](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._031.pdf), explicitement Public Domain et absente de `data/scan_sources.csv`/`scans/`. L’unique doublon 4124.003 (MPG 31, 1476–1488) reste rattaché à 2040.060 et n’est pas une acquisition indépendante.

## Mapping canonique complet

Les numéros sont les notices TLG 2040, les colonnes celles imprimées dans MPG 31.

| Notices | Colonnes MPG 31 |
|---|---|
| .020 | 164–184 |
| .021 | 185–197 |
| .022 | 217–237 |
| .023 | 237–261 |
| .024 | 304–328 |
| .025 | 329–353 |
| .026 | 353–372 |
| .027 | 372–385 |
| .028 | 385–424 |
| .029 | 424–444 |
| .030 | 444–464 |
| .031 | 464–472 |
| .032 | 472–481 |
| .033 | 484–489 |
| .034 | 489–508 |
| .035 | 508–525 |
| .036 | 525–540 |
| .037 | 540–564 |
| .038 | 589–600 |
| .039 | 600–617 |
| .040 | 620–625 |
| .041 | 625–648 |
| .042 | 648–652 |
| .043 | 653–676 |
| .044 | 869–881 |
| .045 | 676–692 |
| .046 | 881–888 |
| .047 | 889–901 |
| .048 | 901–1052 |
| .049 | 1080 |
| .050 | 1052–1305 |
| .051 | 692–869 |
| .052 | 1513–1628 |
| .057 | 1429–1437 |
| .058 | 1437–1457 |
| .059 | 1457–1476 |
| .060 | 1476–1488 |
| .061 | 1488–1496 |
| .062 | 1497–1508 |
| .063 | 1508–1509 |
| .064 | 1677–1684 |
| .065 | 1305–1308 |
| .066 | 1313–1316 |
| .067 | 1308–1313 |
| .068 | 1713–1722 |
| .069 | 1705–1714 |
| .070 | 1685–1688 |
| .071 | 1629–1656 |
| .073 | 1685 |
| .074 | 1320–1428 |

## Contrôles source et qualité

- Fichier Commons : 110 555 071 octets ; SHA-1 `ff8153f0c296846184acddc9c69b6060b824a23b`; images PDF déclarées 991 × 1550 px ; droits « Public domain » explicites.
- La correspondance PDF n’est pas uniforme après les sections liminaires : sélectionner obligatoirement par colonnes imprimées, non par une formule de numéro de page. Repères contrôlés : p. 100 = cols. 195–196; p. 300 = 593–594; p. 500 = 901–902; p. 850 = 1675–1676.
- Trois échantillons représentatifs (p. 100, p. 500, p. 850) inspectés visuellement : grec lisible, contraste et définition suffisants pour OCR interne. Ils ont été supprimés immédiatement après contrôle.

**Action :** ingestion image-only PDM des colonnes listées, avec repérage visuel des bornes. Aucun OCR fournisseur, PDF complet, archive ni image locale n’a été conservé.
