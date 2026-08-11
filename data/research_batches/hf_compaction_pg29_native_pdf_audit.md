# Audit de remplacement HF — *Patrologia Graeca* 29

## Décision

**READY pour remplacer le tar rendu par le PDF Commons image-only**, tout en
conservant la couverture TLG limitée à deux notices exactes. La compaction du
contenant complet ne doit pas être interprétée comme une couverture du volume
hors des segments canoniques ci-dessous.

## Source native et droits vérifiés

* **Notice Commons :** [*Patrologia Graeca* 29](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._029.pdf)
* **PDF original direct :** [fichier natif](https://upload.wikimedia.org/wikipedia/commons/a/af/Patrologia_Graeca_Vol._029.pdf)
* **API Commons contrôlée le 2026-08-11 :** MIME `application/pdf`,
  95 465 952 octets, SHA-1 `82c014913fa601a57ec0def2cbdd03894e459013`,
  987 × 1552 px. Les registres projet documentent 809 pages.
* **Droits :** `Public domain`, `UsageTerms: Public domain`,
  `Copyrighted: False` (API Commons); PDM 1.0 est consigné dans
  `data/scan_sources.csv`.

## Comparaison avec l'objet HF actuel

| Élément | Valeur |
|---|---:|
| Objet HF rendu | `webdataset/volumes--pg29-basilius--7c72ccf55788.tar` |
| État migration | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Images/pages tar | 809 |
| Taille tar | 607 426 560 octets |
| SHA-256 tar/manifeste | `86635e06d86b76b203caed3197f8548d6da65f68b7953f42bf11f6510d9268f8` |
| PDF natif | 95 465 952 octets ; 809 pages |
| Gain estimé | 511 960 608 octets (84,28 %) |

Les deux conteneurs portent les 809 pages du même volume. Le PDF natif peut
donc remplacer le tar sans perte bibliographique ou de fac-similé. Les images
JPEG du tar ne sont toutefois pas identiques octet pour octet au PDF : elles
seront rendues de nouveau si nécessaires. Tout rendu reste image-only; aucun
OCR fournisseur ne doit être extrait ni conservé.

## Couverture et preuve grecque déjà validées

`scan_validation_pg29_basilius.md` fixe le seul périmètre TLG prêt :

| Notice TLG | Colonnes MPG 29 | Repères PDF contrôlés |
|---|---:|---|
| 2040.018, *Homiliae super Psalmos* | 209–494 | débute p. 149 (cols 209–210) |
| 2040.019, *Adversus Eunomium* (lib. 5) | 497–669 ; 672–768 | débute p. 293 (497–498); borne 767–768 à p. 380 |

Les preuves visuelles grecques existantes sont p. 150 (cols 211–212, début),
p. 260 (431–432, milieu) et p. 385 (777–778, juste après la borne finale),
avec un contraste et une netteté jugés suffisants pour OCR interne. Les vues
temporaires ont été supprimées. Toute extraction ultérieure doit sélectionner
les pages par colonnes imprimées, surtout aux bornes 494, 497, 669, 672 et 768.

## Action exécutée et vérifiée

1. PDF déposé sous
   `scans/volumes/pg29-basilius/pg29-original-image-only.pdf`.
2. Vérification distante achevée : 95 465 952 octets, 809 pages et SHA-256
   `53d21bafdbf3a6f308badaa384d06e12940541f8809276721631cddb1e645be4`.
3. Attacher au PDF les deux segments prêts ci-dessus; ne pas déduire une
   couverture TLG globale du seul fait que le volume complet est conservé.
4. Tar retiré après validation distante ; les rendus restent régénérables
   depuis le PDF sans OCR et récupérables via l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
