# Validation de scan — Bussemaker, *Liber XLIV Collectaneorum Medicinalium Oribasii* (BIU Santé)

## Décision

**PARTIAL READY — fragment grec de Mégès seulement.** `BIUSante_33046` est absent de `data/scan_sources.csv` au contrôle du 11 août 2026. Il s'agit bien de l'édition-dissertation de Bussemaker (1835) consacrée au seul livre XLIV des *Collectiones medicae*, sous licence ouverte Etalab. Le canon TLG 0722.001 prescrit toutefois l'édition Raeder (CMG, 1928–1933) et comprend plusieurs livres : ce volume ne couvre donc jamais l'ensemble de la notice. En revanche, le chapitre imprimé `XV. (XIV.) E MEGETIS LIBRIS DE FISTULIS` a été repéré directement et rend le renvoi `0976.x02` prêt pour une ingestion image ciblée.

## Concordance

| Notice TLG | Œuvre / locus | Édition canonique | Concordance vérifiée |
|---|---|---|---|
| 0722.001 | Oribasius, *Collectiones medicae* (livres 1–16, 24–25, 43–50) | J. Raeder, CMG 6.1.1–6.2.2, 1928–1933 | Bussemaker 1835 ne contient que le livre XLIV : témoin historique partiel, non concordant comme édition complète. |
| 0976.x02 (renvoi) | Meges, fragment ap. Oribasium | CMG 6.2.1, pp. 142–144 ; renvoie à 0722.001 | Concordance directe : Bussemaker, chapitre `XV. (XIV.) E MEGETIS LIBRIS DE FISTULIS`, pages imprimées 72–80, feuilles grecques IA `n89,n91,n93,n95,n97`. Couverture fragmentaire seulement. |

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

Le contrôle ciblé a établi matériellement l'alternance grec/latin. `n89` porte le titre grec du chapitre de Mégès et son début (p. 72) ; `n91`, `n93` et `n95` en donnent la suite (pp. 74, 76, 78) ; `n97` contient sa fin en haut de la p. 80, puis le titre grec du chapitre suivant d'Archigène. Les feuilles paires `n90,n92,n94,n96,n98` sont la traduction latine en regard et sont exclues de l'ingestion. Les cinq feuilles grecques ont chacune été inspectées : caractères grecs nets, page entière lisible, aucune page allemande ou page de garde dans la sélection. Aucun OCR n'a été utilisé.

## Action

Ingérer uniquement `n89,n91,n93,n95,n97` dans `scans/volumes/oribasius-bussemaker-liber44-meges-1835`, directement vers Hugging Face. Enregistrer la ressource comme couverture du renvoi `0976.x02` et fragment de l'hôte, jamais comme scan complet de `0722.001`.
