# Validation de scan — Kühn, *Galeni opera omnia*, IV (BIU Santé)

## Décision

**READY — volume complet.** `BIUSante_45674x04` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. Il correspond au volume IV de Kühn (1822 dans les références canoniques), sous licence ouverte Etalab explicite. Son paquet JP2 fait 318 Mo et couvre cinq notices dont le canon donne exactement Kühn IV et les mêmes bornes. Les contrôles de début, milieu et fin confirment les titres grecs-latins et une image lisible à 299 ppi.

## Concordance

| Notices TLG | Œuvres / pages canoniques dans Kühn IV | Contrôle |
|---|---|---|
| 0057.018 | *De motu musculorum* I–II, 367–464 | `n369` = p. 367, titre « ΓΑΛΗΝΟΥ ΠΕΡΙ ΜΥΩΝ ΚΙΝΗΣΕΩΣ / Galeni de motu musculorum liber I ». |
| 0057.114 | *De causis respirationis*, 465–469 | Concordance de volume et pagination canonique ; suit directement la plage 367–464 dans le même exemplaire. |
| 0057.021–022 | *De semine* I–II, 512–651 ; *De foetuum formatione*, 652–702 | `n514` = p. 512, titre « ΓΑΛΗΝΟΥ ΠΕΡΙ ΣΠΕΡΜΑΤΟΣ / Galeni de semine liber I » ; la séquence de pagination confirme la plage suivante. |
| 0057.084 | *De substantia facultatum naturalium fragmentum*, 757–766 | `n759` = p. 757, titre grec « ΠΕΡΙ ΟΥΣΙΑΣ ΤΩΝ ΦΥΣΙΚΩΝ ΔΥΝΑΜΕΩΝ » et titre latin du fragment. |

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / source | `BIUSante_45674x04` — [Internet Archive](https://archive.org/details/BIUSante_45674x04) |
| Titre / date / éditeur | *Galeni opera omnia*, vol. 4 ; métadonnée IA : 1821/1833 ; Leipzig, Car. Cnoblochii. Les références canoniques datent le volume IV de 1822. |
| Éditeur scientifique | Karl Gottlob Kühn ; concordance exacte pour les cinq notices ci-dessus |
| Fichier image traité | `BIUSante_45674x04_jp2.zip` |
| SHA-1 / taille | `58b76212fc7bcf187e56d4c8b5ca90b41f807e0f` ; 317 663 957 octets |
| Images / original distinct | métadonnée de volume : 827 images ; aucun paquet JP2 original distinct dans les métadonnées consultées |
| Scandata | `BIUSante_45674x04_scandata.xml`; SHA-1 `e37cc7cd9d381d8c63324573a626cd49dadb05ca` ; 294 162 octets |
| PPI / qualité | champ général PPI absent ; scandata : 299 ppi aux feuilles contrôlées ; grec et latin nettement lisibles, avec légère transparence sans perte critique |
| Droits | champ `rights` : [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence) |
| Accès image | vues IA `https://archive.org/download/BIUSante_45674x04/page/n{leaf}_w1400.jpg` ; p. 367 = `n369`, p. 512 = `n514`, p. 757 = `n759` |

## Contrôles visuels temporaires

`n369` (*De motu musculorum*, p. 367), `n514` (*De semine*, p. 512) et `n759` (*De substantia facultatum naturalium*, p. 757) ont été obtenus individuellement et inspectés. Les trois JPEG, le `scandata.xml` de repérage et le répertoire temporaire ont ensuite été supprimés. Aucun OCR, PDF ni archive image n'a été téléchargé ou conservé.

## Action

Ajouter comme source `REMOTE_ONLY` **READY** pour 0057.018, 0057.021–022, 0057.084 et 0057.114. Les droits explicites, l'édition exacte, les bornes vérifiées et le paquet inférieur à 500 Mo justifient une ingestion image-only du volume complet ; exclure tout OCR tiers.
