# Validation scan — Bussemaker, *Scholia et paraphrases in Nicandrum et Oppianum* (1849)

## Décision

**REVIEW — concordance et qualité confirmées, mais droits de réutilisation non explicités par le dépôt.** L’item Internet Archive `scholiaintheocri00buss` est absent de `data/scan_sources.csv` et de `scans/`. Il contient bien l’édition U. C. Bussemaker, Paris, A. F. Didot, 1849, demandée par le canon pour **TLG 4171.001**. Il ne peut toutefois pas être marqué READY selon le protocole actuel : l’API IA ne fournit ni champ `rights` ni `licenseurl`, et aucune copie Commons PDM exactement identique n’a été trouvée au contrôle ciblé.

## Concordance bibliographique et pagination

| Notice TLG | Référence canonique | Candidat et locus | Décision |
|---|---|---|---|
| 4171.001 — *In Oppiani halieutica exegesis* (cod. Paris. gr. 2735) | U. C. Bussemaker (éd.), *Scholia et paraphrases in Nicandrum et Oppianum*, dans F. Dübner (éd.), *Scholia in Theocritum*, Paris: Didot, **1849**, pp. 364–369 | Même volume et édition : IA `n385`–`n390`, pp. imprimées **364–369**, sous l’en-tête `EXEGESIS OPPIANI` / `OPΠIANOY ΑΛΙΕΥΤΙΚΩΝ ΕΞΗΓΗΣΙΣ` | REVIEW droits |

La borne d’ouverture `n385` porte la p. imprimée 364 et le titre grec de l’*Exegesis Oppiani*; la vue médiane `n388` porte 367; la borne finale `n390` porte 369. Ces six images (`n385` à `n390`, incluses) sont donc le mapping image-only exact de la plage canonique.

## Provenance, droits et technique

| Champ | Valeur vérifiée |
|---|---|
| Dépôt / item | Internet Archive [`scholiaintheocri00buss`](https://archive.org/details/scholiaintheocri00buss) |
| Titre, éditeur, date IA | *Scholia in Theocritum; … Scholia et paraphrases in Nicandrum et Oppianum*; Parisiis, A. F. Didot; 1849 |
| Droits / licence | Aucun champ `rights` ni `licenseurl` dans les métadonnées IA. L’édition de 1849 est du domaine public par ancienneté, mais la réutilisation du scan doit être confirmée par une source qui l’énonce explicitement. |
| Archive image source | `scholiaintheocri00buss_jp2.zip`, « Single Page Processed JP2 ZIP » |
| Taille / SHA-1 | 303 007 793 octets; `c7330a197c49677694874515efd4330539707b5f` |
| Original JP2 | Aucun paquet « original JP2 » distinct n’est listé dans les métadonnées de l’item; ne pas substituer un dérivé OCR/PDF. |
| Nombre de vues / PPI | 702 images; 500 ppi déclarés par IA |
| Scandata | `scholiaintheocri00buss_scandata.xml`, SHA-1 `901b77f085f90ec21e3c164380ed908a6771853d`; les images source ont une géométrie de l’ordre de 4 368 px de haut avant rognage. |
| Rendement | 1 notice TLG, 6 images ciblées (`n385`–`n390`), paquet entier inférieur à 500 Mo |

## Contrôle visuel sans OCR

Trois JPEG temporaires, demandés individuellement au visualiseur IA puis supprimés, ont été inspectés :

- `n385`, p. 364 : début de l’*Exegesis Oppiani* et grec net;
- `n388`, p. 367 : page interne, texte grec dense mais lisible;
- `n390`, p. 369 : borne finale, grec net et pagination confirmée.

Le papier est légèrement jauni mais sans coupure ni flou gênant. Aucun OCR, PDF, archive JP2 ou image d’ingestion n’a été téléchargé ni conservé.

## Action proposée

Ne pas ingérer tant qu’un hôte donnant une permission explicite (PDM/CC ou politique institutionnelle claire) n’a pas été relié à ce **même** scan ou à un scan équivalent de l’édition 1849. Dès confirmation, l’ingestion image-only est bornée à `n385`–`n390`; conserver l’identifiant IA, le SHA-1 de l’archive et cette table de pagination dans le manifeste.
