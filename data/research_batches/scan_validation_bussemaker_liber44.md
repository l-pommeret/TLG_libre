# Validation de scan — Bussemaker, *Liber XLIV Collectaneorum Medicinalium Oribasii* (BIU Santé)

## Décision

**REVIEW — substitut partiel, non édition canonique.** `BIUSante_33046` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. Il s'agit bien de l'édition-disssertation de Bussemaker (1835) consacrée au seul livre XLIV des *Collectiones medicae*, sous licence ouverte Etalab, avec un paquet JP2 de 111 Mo. Le canon TLG 0722.001 prescrit toutefois l'édition Raeder (CMG, 1928–1933) et comprend plusieurs livres : le volume ne peut donc pas être enregistré comme scan exact de l'ensemble de la notice. Les feuillets contrôlés confirment une impression nette, mais n'établissent pas à eux seuls le locus XLIV.14 : aucune attribution de ce locus ne doit être automatisée.

## Concordance

| Notice TLG | Œuvre / locus | Édition canonique | Concordance vérifiée |
|---|---|---|---|
| 0722.001 | Oribasius, *Collectiones medicae* (livres 1–16, 24–25, 43–50) | J. Raeder, CMG 6.1.1–6.2.2, 1928–1933 | Bussemaker 1835 ne contient que le livre XLIV : témoin historique partiel, non concordant comme édition complète. |
| 0976.x02 (renvoi) | Meges, fragment ap. Oribasium | CMG 6.2.1, pp. 142–144 ; renvoie à 0722.001 | Le renvoi canonique est confirmé ; le locus XLIV.14 reste à vérifier directement dans Bussemaker avant toute relation de couverture. |

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / source | `BIUSante_33046` — [Internet Archive](https://archive.org/details/BIUSante_33046) |
| Titre / date / créateur | *Dissertatio philologico-medica inauguralis exhibens librum XLIV collectaneorum medicinalium Oribasii* ; 1835 ; Oribase ; U. C. Bussemaker |
| Fichier image traité | `BIUSante_33046_jp2.zip` |
| SHA-1 / taille / images | `30dbfd45c1f08649a8b627010df28c589959158b` ; 110 964 784 octets ; 214 images (métadonnée de volume : 215) |
| Original distinct | aucun paquet image original distinct dans les métadonnées consultées |
| Scandata | `BIUSante_33046_scandata.xml`; SHA-1 `6c51084d4cf92c1ff347696e6efca0db2e5323b6` ; 64 298 octets |
| PPI / qualité | PPI absent des métadonnées ; texte grec et latin net, contraste et marges exploitables dans les trois contrôles |
| Droits | champ `rights` : [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence) |

## Contrôles visuels temporaires

`n10` (p. VII, introduction biographique), `n100` (p. 83, texte médical continu) et `n200` (p. 95, grec et latin) ont été obtenus individuellement par le visualiseur distant et inspectés. Ils montrent une numérisation propre, mais aucun de ces trois échantillons ne porte le marqueur « XLIV.14 ». Les trois JPEG temporaires et leur répertoire ont été supprimés après contrôle ; aucun OCR, PDF ni archive image n'a été conservé localement.

## Action

Conserver comme candidat `REMOTE_ONLY` **REVIEW**, limité au livre XLIV. Avant ingestion ciblée, repérer visuellement le locus XLIV.14 et vérifier sa correspondance avec le fragment de Meges ; ne pas le rattacher globalement à 0722.001.
