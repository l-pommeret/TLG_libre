# Validation de scan — Kühn, *Galeni opera omnia*, VIII (BIU Santé)

## Décision

**READY — volume complet.** `BIUSante_45674x08` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. Il est le volume VIII de Kühn, sous licence ouverte Etalab, avec un JP2 de 382 Mo. Les quatre notices TLG dont le canon prescrit Kühn VIII, pp. 1–961, sont toutes couvertes. Les vues contrôlées établissent les titres de début, milieu et fin de volume et une qualité régulière à 299 ppi.

## Concordance

| Notices TLG | Œuvres / pages canoniques dans Kühn VIII | Preuve visuelle |
|---|---|---|
| 0057.057 | *De locis affectis*, 1–452 | `n3` ouvre p. 1 avec « ΓΑΛΗΝΟΥ ΠΕΡΙ ΤΩΝ ΠΕΠΟΝΘΟΤΩΝ ΤΟΠΩΝ / Galeni de locis affectis liber I ». |
| 0057.058 | *De pulsibus libellus ad tirones*, 453–492 | `n455` = p. 453 et porte le titre grec-latin du traité. |
| 0057.059 | *De differentia pulsuum*, 493–765 | Concordance de volume et de pagination, en séquence entre les deux titres contrôlés. |
| 0057.060 | *De dignoscendis pulsibus*, 766–961 | `n768` = p. 766 et porte « ΓΑΛΗΝΟΥ ΠΕΡΙ ΔΙΑΓΝΩΣΕΩΣ ΣΦΥΓΜΩΝ / Galeni de dignoscendis pulsibus liber I ». |

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / source | `BIUSante_45674x08` — [Internet Archive](https://archive.org/details/BIUSante_45674x08) |
| Titre / date / éditeur | *Galeni opera omnia*, vol. 8 ; IA : 1821/1833 ; Leipzig, Car. Cnoblochii |
| Éditeur scientifique | Karl Gottlob Kühn ; correspondance exacte avec les quatre notices listées |
| Fichier image traité | `BIUSante_45674x08_jp2.zip` |
| SHA-1 / taille | `b0c1070d4308db4a35cb1519a8d5d25471e2ea33` ; 381 755 194 octets |
| Images / original distinct | métadonnée de volume : 967 images ; aucun paquet JP2 original distinct publié |
| Scandata | `BIUSante_45674x08_scandata.xml`; SHA-1 `a916062aa4fad0f1573baeae03e84b60eb4ed5ed` ; 343 913 octets |
| PPI / qualité | PPI général absent ; scandata : 299 ppi aux feuilles contrôlées ; grec et latin nets, contraste suffisant |
| Droits | champ `rights` : [Licence ouverte / Open Licence Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence) |
| Accès image | vues IA `https://archive.org/download/BIUSante_45674x08/page/n{leaf}_w1400.jpg` ; p. 1 = `n3`, p. 453 = `n455`, p. 766 = `n768` |

## Contrôles visuels temporaires

`n3`, `n455` et `n768` ont été obtenus individuellement et inspectés. Une vue de repérage supplémentaire `n5` (p. 3) a confirmé la continuité au début du volume. Tous les JPEG, le `scandata.xml` et le répertoire temporaire ont ensuite été supprimés. Aucun OCR, PDF ni archive image n'a été téléchargé ou conservé.

## Action

Ajouter comme source `REMOTE_ONLY` **READY** pour 0057.057–060. Les droits explicites, la concordance complète et le paquet sous 500 Mo justifient l'ingestion image-only du volume complet ; exclure tout OCR tiers.
