# Validation de scan — Cramer, *Anecdota Graeca Oxoniensia*, IV

**Décision : READY — ingestion ciblée d’images uniquement (34 images).**

## Identifiant, droits et exclusion des doublons

- Candidat : Internet Archive [`anecdotagraecae02unkngoog`](https://archive.org/details/anecdotagraecae02unkngoog).
- Le fichier [Wikimedia Commons correspondant](https://commons.wikimedia.org/wiki/File:Anecdota_Graeca_e_codd._manuscriptis_Bibliothecarum_Oxoniensium_(IA_anecdotagraecae02unkngoog).pdf) décrit le tome IV, Cramer, Oxford, 1836, et le marque explicitement **Public Domain Mark**. La date `1835` de la métadonnée IA est donc une incohérence de catalogue, non une substitution d’édition : le contenu et la pagination concordent avec le tome IV canonique.
- Contrôle préalable : l’identifiant n’est présent ni dans `data/scan_sources.csv` ni dans `scans/`.

## Concordance canonique vérifiée

| Notice TLG | Œuvre | Édition/page canonique | Feuille IA | Contrôle |
|---|---|---|---|---|
| 1617.002 | Marcus Antonius Polemon, *Fragmentum physiognomonicum* | Cramer, IV, p. 255 | `n283` | La page imprimée 255 porte les *Excerpta varia* et le fragment de Polemon. |
| 4286.004 | *Lexicon syntacticum* | Cramer, IV, pp. 275–307 | `n303`–`n335` | `n303` ouvre la p. 275 (« Archē syn Theō ton Syntaxeon… ») ; `n335` est la p. 307, dernière page canonique. |

Le décalage constaté est `feuille = page imprimée + 28`, vérifié sur les trois points ci-dessus ; les étiquettes de pagination de `scandata.xml` ne sont pas utilisées comme unique preuve.

## Objet numérique et qualité

| Élément | Valeur vérifiée |
|---|---|
| Nombre d’images IA | 483 |
| Archive JP2 complète | Non fournie par IA pour cet item |
| Fichier de structure IA | `anecdotagraecae02unkngoog_scandata.xml`, 158 389 octets, SHA-1 `5cd5e0c0b7fa38040b7036083a9724a084cb6512` |
| PPI déclaré | Absent des métadonnées disponibles |
| Accès image | Images originales de page via les points d’accès BookReader IA ; aucun PDF ni archive complète requis |
| Vues temporaires | `n283` (Polemon/p. 255), `n303` (début du lexique/p. 275), `n335` (fin/p. 307), plus contrôles de continuité ; impression grecque nette, marges et numéros de page lisibles. Les fichiers temporaires ont été supprimés. |

## Ingestion recommandée

Télécharger directement vers le dépôt distant seulement `n283` et `n303` à `n335` inclus, soit **34 images**. Ne pas télécharger le PDF Commons, les fichiers texte/ocr IA ni une archive de volume. Conserver avec chaque image l’identifiant IA, le PDM Commons, la feuille et la page imprimée.
