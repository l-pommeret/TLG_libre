# TLG libre

## Vision

Construire progressivement un corpus grec libre en examinant, œuvre par œuvre, la liste publique du *Canon of Greek Authors and Works* du Thesaurus Linguae Graecae (TLG).

Pour chaque œuvre, l'objectif est de déterminer :

1. si un texte numérique ouvert existe déjà ;
2. quelle édition ce texte reproduit et quelle est sa qualité ;
3. à défaut de texte exploitable, si les pages d'une édition sont numérisées ;
4. si ces images peuvent être téléchargées, OCRisées, corrigées et redistribuées ;
5. ce qu'il reste à faire pour obtenir un texte structuré, citable et vérifiable.

Le projet ne cherche pas seulement à accumuler des fichiers. Il doit conserver la relation entre l'œuvre, l'édition savante, l'exemplaire numérisé, les images, la transcription et les références canoniques.

## Principe de travail

L'unité de suivi est l'**œuvre dans une édition donnée**. Une même œuvre peut avoir plusieurs éditions et plusieurs numérisations d'une même édition. Il faut éviter de confondre :

- l'œuvre antique ou byzantine ;
- son attribution à un auteur ;
- une édition imprimée particulière ;
- un exemplaire physique de cette édition ;
- sa numérisation ;
- une transcription numérique dérivée de cette numérisation.

Le numéro d'auteur et le numéro d'œuvre du TLG servent d'identifiants de rapprochement, mais les données et textes produits doivent rester indépendants du service propriétaire du TLG.

## Sources de départ

### Inventaire bibliographique

- Canon public du TLG : auteurs, œuvres, datations, genres, éditions et systèmes de citation.
- Canon imprimé du TLG et notices bibliographiques librement consultables.
- Catalogues WorldCat, SUDOC, BnF, Library of Congress et catalogues nationaux.
- Catalogues CTS d'Open Greek and Latin et de Perseus.

### Textes numériques ouverts à rechercher

- Perseus Digital Library ;
- Open Greek and Latin / First1KGreek ;
- Patristic Text Archive ;
- Corpus Corporum ;
- Lace, Classical Language Toolkit et autres corpus documentés ;
- dépôts GitHub, GitLab, Zenodo, Nakala et Hugging Face ;
- projets spécialisés : papyrologie, inscriptions, médecine, patristique, scholies, textes byzantins.

Un texte trouvé n'est pas automatiquement validé : il faut identifier son édition source, sa licence, sa complétude, son encodage et son niveau de correction.

### Images et livres numérisés

- Internet Archive ;
- Google Books ;
- Gallica et son API IIIF ;
- HathiTrust ;
- Bayerische Staatsbibliothek / MDZ ;
- bibliothèques de Heidelberg, Göttingen, Berlin et Vienne ;
- Europeana et bibliothèques nationales ou universitaires disposant d'IIIF.

Lorsqu'il existe plusieurs scans, privilégier l'exemplaire complet, net, en couleur ou niveaux de gris, avec des images originales accessibles page par page. Conserver tous les candidats utiles plutôt que remplacer silencieusement une numérisation par une autre.

## Statuts proposés

Chaque œuvre reçoit un statut principal :

| Statut | Signification |
|---|---|
| `TEXT_OPEN_VERIFIED` | Texte ouvert, complet, édition et licence vérifiées |
| `TEXT_OPEN_UNVERIFIED` | Texte ouvert trouvé, mais provenance ou qualité à vérifier |
| `TEXT_PARTIAL` | Transcription ouverte incomplète |
| `SCAN_READY` | Édition numérisée complète et légalement exploitable, prête pour OCR |
| `SCAN_RESTRICTED` | Scan localisé mais téléchargement ou réutilisation restreints |
| `SCAN_INCOMPLETE` | Scan incomplet ou pages manquantes |
| `EDITION_IDENTIFIED` | Édition cible connue, aucune numérisation trouvée pour l'instant |
| `BIBLIOGRAPHY_NEEDED` | Édition cible encore à déterminer |
| `OCR_IN_PROGRESS` | OCR en cours |
| `OCR_RAW` | OCR brut disponible, non corrigé |
| `OCR_REVIEW` | OCR en correction ou contrôle qualité |
| `TEI_READY` | Texte structuré et contrôlé, prêt à publier |
| `BLOCKED_RIGHTS` | Traitement ou diffusion bloqués par les droits |

Des champs secondaires préciseront la complétude, la qualité des scans, le type d'OCR nécessaire et la présence d'un apparat critique.

## Registre minimal

Le registre principal pourra commencer en CSV, puis être converti en base SQLite lorsque les relations deviendront plus nombreuses. Champs minimaux :

```text
tlg_author_id
tlg_work_id
author_name
work_title
work_attribution
date_range
genre
edition_editor
edition_title
edition_series
edition_place
edition_publisher
edition_year
edition_volume
canonical_citation_scheme
open_text_url
open_text_format
open_text_license
open_text_source_edition
scan_url
scan_provider
scan_identifier
scan_manifest_iiif
scan_rights
scan_completeness
scan_quality
ocr_status
ocr_engine
ocr_quality
tei_status
review_status
notes
last_checked
checked_by
```

Les URL seules ne suffisent pas : enregistrer les identifiants pérennes (ARK, Handle, DOI, Internet Archive ID, Google Books ID, HathiTrust ID, IIIF Manifest URI).

## Procédure œuvre par œuvre

1. Créer ou importer la notice du Canon TLG.
2. Normaliser les noms de l'auteur, de l'œuvre et de l'édition.
3. Chercher une transcription ouverte dans les grands corpus.
4. Comparer son incipit, son explicit, quelques passages et sa structure avec l'édition déclarée.
5. Vérifier la licence et la possibilité de redistribution.
6. Si aucun texte satisfaisant n'existe, chercher l'édition imprimée exacte dans les bibliothèques numériques.
7. Vérifier le volume entier : couverture, préface, texte grec, apparat, index et pages manquantes.
8. Enregistrer la meilleure numérisation et les numérisations alternatives.
9. Évaluer la difficulté OCR : colonnes, grec et latin mêlés, apparat, scholies marginales, caractères rares, qualité d'impression.
10. Attribuer un statut et une prochaine action vérifiable.
11. Pour un OCR produit, conserver le lien page-image ↔ transcription et effectuer un contrôle sur échantillon.
12. Publier en texte brut pour l'accès simple et en TEI XML pour la structure savante, avec provenance complète.

## Recherche des volumes

Les recherches doivent combiner les éléments bibliographiques, par exemple :

```text
nom de l'éditeur + titre latin + année + volume
auteur latinisé + titre de l'œuvre + nom de la collection
éditeur + lieu d'édition + année
```

Une absence de résultat ne signifie pas que le livre n'est pas numérisé : les métadonnées peuvent être fautives, le nom grec absent, le titre abrégé ou le volume catalogué sous le nom de la série.

## Contrôle juridique

Ce dépôt est privé et réservé à l'usage personnel de son propriétaire. Dans ce
cadre, les images dont les conditions autorisent l'usage privé ou non commercial
(par exemple CC BY-NC) peuvent être acquises. La restriction exacte, la source et
la date de contrôle restent obligatoirement enregistrées dans les métadonnées.
Cette règle interne n'autorise ni le contournement d'un contrôle d'accès, ni un
téléchargement expressément interdit, ni la redistribution publique ultérieure
des fichiers concernés.

Pour chaque objet, distinguer :

- le texte ancien, généralement dans le domaine public ;
- l'édition scientifique et ses éventuels éléments originaux ;
- la date de décès de l'éditeur lorsque cela est pertinent ;
- les images produites par la bibliothèque ;
- les conditions contractuelles de téléchargement et de réutilisation du fournisseur ;
- la licence de la transcription ou du fichier TEI existant.

Le statut juridique doit être documenté par territoire et ne doit jamais être déduit uniquement de l'ancienneté de l'œuvre grecque.

## Qualité et traçabilité

Chaque texte devrait permettre de répondre à ces questions :

- De quelle édition provient-il ?
- Quel exemplaire a été numérisé ?
- Quelles pages sources correspondent à chaque portion du texte ?
- Quel logiciel et quelle version ont produit l'OCR ?
- Quelles corrections ont été apportées, par qui et quand ?
- Quel est le taux d'erreur estimé sur un échantillon reproductible ?
- Quels éléments ont été exclus : apparat, scholies, notes, traduction latine ou index ?

Les fichiers bruts ne doivent pas être écrasés. Conserver séparément images sources, OCR brut, OCR corrigé et TEI validé.

## Priorités possibles

1. Importer la liste publique du Canon et créer le registre initial.
2. Faire un rapprochement automatique avec Perseus, First1KGreek, Open Greek and Latin et PTA.
3. Vérifier manuellement les correspondances incertaines.
4. Identifier les œuvres sans aucun texte ouvert.
5. Pour celles-ci, localiser systématiquement les éditions numérisées.
6. Constituer une première file OCR à forte valeur : scans libres, complets et typographiquement simples.
7. Réserver les éditions à scholies marginales ou apparat complexe pour une chaîne spécialisée.

Pour obtenir rapidement un résultat utile, on peut commencer par un lot pilote de 50 à 100 œuvres représentant plusieurs périodes et difficultés typographiques. Ce pilote permettra de stabiliser le registre et les critères avant le traitement de milliers d'entrées.

## Livrables envisagés

- un registre public, versionné et interrogeable ;
- une page de synthèse indiquant la couverture réelle par période, genre et auteur ;
- une liste des textes ouverts vérifiés ;
- une liste des éditions numérisées en attente d'OCR ;
- une liste des éditions encore introuvables ;
- des manifestes de téléchargement reproductibles ;
- les OCR bruts et corrigés avec métriques de qualité ;
- des fichiers TEI XML et une API CTS/DTS ;
- une documentation des décisions bibliographiques et juridiques.

## Critère de réussite

Le progrès ne sera pas mesuré seulement en nombre de mots. Pour chaque entrée du TLG, le projet doit pouvoir produire une réponse explicite et vérifiable :

> texte ouvert disponible ; texte à vérifier ; scan prêt pour OCR ; scan restreint ; édition localisée mais non numérisée ; ou recherche encore à effectuer.

À terme, cette matrice permettra de mesurer précisément ce qui existe déjà librement et ce qu'il reste réellement à numériser, OCRiser, corriger et structurer pour approcher la couverture du TLG.
