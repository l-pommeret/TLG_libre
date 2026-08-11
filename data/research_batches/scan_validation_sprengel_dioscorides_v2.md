# Validation de scan — Sprengel, *Pedanii Dioscoridis Anazarbei*, II (BIU Santé)

## Décision

**READY — extraction ciblée.** `BIUSante_dioscsprengelx02` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. Le volume est exactement le tome II de K. Sprengel (Leipzig, Knobloch, 1830) cité par le canon pour TLG 1118.001, pp. 1–41. Il porte une licence ouverte Etalab explicite. Les trois vues montrent le titre grec-latin, une page médiane et la fin de la plage, toutes lisibles. Le paquet complet fait 586 Mo, au-dessus de la préférence de 500 Mo : prévoir uniquement les images de la section, pas le paquet ni les dérivés OCR.

## Concordance

| Notice TLG | Œuvre | Pages canoniques | Preuve visuelle |
|---|---|---:|---|
| 1118.001 | Pseudo-Dioscorides, *De venenis eorumque praecautione et medicatione* (= *Alexipharmaca*) | 1–41 | `n2` ouvre le traité avec le titre grec « ΠΕΡΙ ΔΗΛΗΤΗΡΙΩΝ ΦΑΡΜΑΚΩΝ… » et le titre latin *Liber de venenis eorumque praecautione et medicatione* ; `n21` = p. 20 ; `n42` = p. 41 et clôt la section. |

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / source | `BIUSante_dioscsprengelx02` — [Internet Archive](https://archive.org/details/BIUSante_dioscsprengelx02) |
| Titre / date / éditeur | *Pedanii Dioscoridis Anazarbei De materia medica quinque, tomus secondus* ; 1830 ; Leipzig, Car. Cnoblochii |
| Éditeur scientifique | Kurt Sprengel ; concordance exacte avec la référence canonique « *Medicorum Graecorum opera quae exstant* 26.2 » |
| Fichier image traité | `BIUSante_dioscsprengelx02_jp2.zip` |
| SHA-1 / taille | `0fb0446bd8f6c16e04f1c02626cc06fa4e2450ae` ; 586 460 070 octets |
| Images / original distinct | métadonnée de volume : 718 images ; aucun paquet JP2 original distinct dans les métadonnées consultées |
| Scandata | `BIUSante_dioscsprengelx02_scandata.xml`; SHA-1 `344b8439ca24459f917895bdd74475482c6b22d1` ; 255 370 octets |
| PPI / qualité | le champ général PPI est absent ; le scandata donne 351 ppi à la feuille 0, et les trois échantillons (grec, latin et notes) sont nets et pleinement lisibles |
| Droits | champ `rights` : [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence) |
| Accès image | vues IA `https://archive.org/download/BIUSante_dioscsprengelx02/page/n{leaf}_w1400.jpg` ; la plage commence au `n2`, les pp. 20 et 41 sont `n21` et `n42` |

## Contrôles visuels temporaires

`n2` (titre et incipit), `n21` (p. 20, texte grec et traduction latine) et `n42` (p. 41, terminaison) ont été obtenus individuellement et inspectés. Les trois JPEG, le `scandata.xml` de repérage et le répertoire temporaire ont ensuite été supprimés. Aucun OCR, PDF ni archive image n'a été téléchargé ou conservé.

## Action

Ajouter une source `REMOTE_ONLY` **READY** pour 1118.001. Puisque le JP2 du volume pèse 586 Mo, privilégier une ingestion image-only ciblée de `n2` à `n42` (à confirmer lors du repérage final des feuilles non numérotées), avec les métadonnées et l'empreinte ci-dessus. Exclure tout OCR tiers.
