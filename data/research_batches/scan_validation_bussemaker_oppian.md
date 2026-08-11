# Validation scan — Bussemaker, *Scholia et paraphrases in Nicandrum et Oppianum* (1849)

## Décision

**READY — copie Gallica exacte et ingestion ciblée.** L’item Internet Archive `scholiaintheocri00buss` avait confirmé l’édition U. C. Bussemaker, Paris, A. F. Didot, 1849, demandée par le canon pour **TLG 4171.001**, mais sans licence explicite. Une seconde copie exacte est maintenant reliée au catalogue BnF `cb372724539` et à Gallica `bpt6k28230s`; le catalogue qualifie le document numérique de « libre de droits ». Les conditions Gallica et l’attribution BnF doivent rester dans la provenance, sans inférer une licence commerciale générale.

## Concordance bibliographique et pagination

| Notice TLG | Référence canonique | Candidat et locus | Décision |
|---|---|---|---|
| 4171.001 — *In Oppiani halieutica exegesis* (cod. Paris. gr. 2735) | U. C. Bussemaker (éd.), *Scholia et paraphrases in Nicandrum et Oppianum*, dans F. Dübner (éd.), *Scholia in Theocritum*, Paris: Didot, **1849**, pp. 364–369 | Gallica `bpt6k28230s`, IIIF `f383`–`f388`, pp. imprimées **364–369**, sous l’en-tête `EXEGESIS OPPIANI` / `OPΠIANOY ΑΛΙΕΥΤΙΚΩΝ ΕΞΗΓΗΣΙΣ` | READY ciblé |

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

## Copie ouverte retenue

| Champ | Valeur vérifiée |
|---|---|
| Catalogue BnF | [`cb372724539`](https://catalogue.bnf.fr/ark:/12148/cb372724539), même titre, éditeurs, lieu et date; document numérique `NUMM-28230`, indiqué « libre de droits » |
| Gallica / IIIF | [`bpt6k28230s`](https://gallica.bnf.fr/ark:/12148/bpt6k28230s); manifeste IIIF : `https://gallica.bnf.fr/iiif/ark:/12148/bpt6k28230s/manifest.json` |
| Sélection | `f383`–`f388` = pages imprimées 364–369 |
| Dimensions | 2 592 × 3 508 pixels pour les images pleine résolution; service IIIF level 2 |
| Conditions | lien de licence du manifeste vers les conditions Gallica; attribution BnF et restriction de provenance conservées, aucune licence commerciale générale inférée |

## Contrôle visuel sans OCR

Trois JPEG temporaires, demandés individuellement au visualiseur IA puis supprimés, avaient été inspectés :

- `n385`, p. 364 : début de l’*Exegesis Oppiani* et grec net;
- `n388`, p. 367 : page interne, texte grec dense mais lisible;
- `n390`, p. 369 : borne finale, grec net et pagination confirmée.

Le papier est légèrement jauni mais sans coupure ni flou gênant. Aucun OCR, PDF, archive JP2 ou image d’ingestion n'a été téléchargé ni conservé.

Les six pages Gallica `f383`–`f388` ont ensuite été rendues depuis les services IIIF de cette copie précise et contrôlées ensemble. Chacune contient du grec lisible; `f383` porte le titre et le début, `f388` porte la page finale 369. Elles reproduisent la même mise en page et les mêmes bornes que la copie IA. Les rendus de contrôle ont été supprimés après inspection.

## Action proposée

Ingérer uniquement les six images pleine résolution Gallica `f383`–`f388` vers `scans/tlg4171/tlg001/bussemaker-oppian-1849`, avec provenance BnF/Gallica et sans OCR tiers. La copie IA reste un comparateur technique et bibliographique, non la source redistribuée.
