# Validation de scan — Kühn, *Galeni opera omnia*, VII (BIU Santé)

## Décision

**READY — volume complet.** `BIUSante_45674x07` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. C'est le volume VII de Kühn (1824 dans les références canoniques), avec licence ouverte Etalab explicite et paquet JP2 de 483 Mo, donc sous la préférence de 500 Mo. Onze notices dont le canon prescrit cette édition et ces bornes sont couvertes. Les vues de début, milieu et fin confirment les titres grecs et latins, la pagination et une qualité d'image lisible. Les notices 0057.046–047, 052 et 054 ne sont pas incluses : le canon y prescrit des éditions modernes différentes.

## Concordance

| Notices TLG | Œuvres / pages canoniques dans Kühn VII | Contrôle |
|---|---|---|
| 0057.042–045 | *De causis morborum* 1–41 ; *De symptomatum differentiis* 42–84 ; *De symptomatum causis* 85–272 ; *De differentiis febrium* 273–405 | Concordance de volume, éditeur et pagination avec le canon. `n5` ouvre p. 1 avec « ΓΑΛΗΝΟΥ ΠΕΡΙ ΤΩΝ ΕΝ ΤΟΙΣ ΝΟΣΗΜΑΣΙΝ ΑΙΤΙΩΝ / Galeni de morborum causis liber ». |
| 0057.048–051 | *De typis* 463–474 ; *Adversus eos qui de typis* 475–512 ; *De plenitudine* 513–583 ; *De tremore…* 584–642 | Pagination canonique continue dans le même volume. `n517` = p. 513 et porte « ΓΑΛΗΝΟΥ ΠΕΡΙ ΠΛΗΘΟΥΣ / Galeni de plenitudine liber ». |
| 0057.053, 0057.055–056 | *De marcore* 666–704 ; *De inaequali intemperie* 733–752 ; *De difficultate respirationis* 753–960 | Concordance de volume et de bornes canonique. `n757` = p. 753 et porte le titre grec-latin de *De difficultate respirationis*. |

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / source | `BIUSante_45674x07` — [Internet Archive](https://archive.org/details/BIUSante_45674x07) |
| Titre / date / éditeur | *Galeni opera omnia*, vol. 7 ; métadonnée IA : 1821/1833 ; Leipzig, Car. Cnoblochii. Le canon date ce volume VII de 1824. |
| Éditeur scientifique | Karl Gottlob Kühn ; concordance exacte pour les onze notices listées ci-dessus |
| Fichier image traité | `BIUSante_45674x07_jp2.zip` |
| SHA-1 / taille | `eb01994cde6b01c0af2b1c0ea8e8a2386c69aa31` ; 482 995 225 octets |
| Images / original distinct | métadonnée de volume : 965 images ; aucun paquet JP2 original distinct dans les métadonnées consultées |
| Scandata | `BIUSante_45674x07_scandata.xml`; SHA-1 `6af5ce2a44ca498036badf6ab22990a6b993ce2f` ; 343 297 octets |
| PPI / qualité | champ général PPI absent ; scandata : 299 ppi aux feuilles contrôlées ; grec, latin et apparat clairement lisibles avec contraste suffisant |
| Droits | champ `rights` : [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence) |
| Accès image | vues IA `https://archive.org/download/BIUSante_45674x07/page/n{leaf}_w1400.jpg` ; p. 1 = `n5` (repérage par séquence), p. 513 = `n517`, p. 753 = `n757` |

## Contrôles visuels temporaires

`n5` (p. 1, *De morborum causis*), `n517` (p. 513, *De plenitudine*) et `n757` (p. 753, *De difficultate respirationis*) ont été obtenus individuellement et inspectés. Les trois JPEG, le `scandata.xml` de repérage et le répertoire temporaire ont ensuite été supprimés. Aucun OCR, PDF ni archive image n'a été téléchargé ou conservé.

## Action

Ajouter comme source `REMOTE_ONLY` **READY** pour 0057.042–045, 0057.048–051, 0057.053 et 0057.055–056. Le paquet étant sous 500 Mo et l'édition/droits étant exacts, préparer l'ingestion image-only du volume complet, en excluant strictement les dérivés OCR et en gardant les quatre notices dont le canon prescrit une autre édition hors de ce rattachement.
