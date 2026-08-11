# Audit de remplacement HF — *Patrologia Graeca* 93

## Décision

**READY — le PDF natif image-only peut remplacer le tar de rendus après
vérification distante.** Le PDF Commons est le fac-similé source ; le tar ne
fait que matérialiser ses pages en JPEG. Aucun OCR ne participe à cette
substitution.

## Source directe vérifiée

* **Notice Commons :** [*Patrologia Graeca* 93](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._093.pdf)
* **Original direct :** [PDF image-only](https://upload.wikimedia.org/wikipedia/commons/c/cf/Patrologia_Graeca_Vol._093.pdf)
* **API Commons, 2026-08-11 :** MIME `application/pdf`, taille `111047486`
  octets, SHA-1 `dc28ba9b714e69eb69ce00f8d76bd81a9ad8636a`, dimensions source
  1016 × 1556 px, 915 pages.
* **Droits :** `Public domain`, `Copyrighted: False` ; PDM 1.0 également
  consigné dans `data/scan_sources.csv`.

## Comparaison HF

| Élément | Valeur |
|---|---:|
| Archive rendue actuelle | `webdataset/volumes--pg93-hesychius--3688f548c326.tar` |
| État HF | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Pages/images dans le tar | 915 |
| Taille tar | 663 101 440 octets |
| SHA-256 du manifeste/tar vérifié | `3aa7cbf3a8b6cbe47f73abd5dc3ecaf1fd6d87e19ec30b9e169ea67299a51ef3` |
| PDF source natif | 111 047 486 octets ; 915 pages |
| Économie estimée | 552 053 954 octets (83,25 %) |

Les deux objets contiennent le volume complet de 915 pages. Le PDF natif peut
donc remplacer le tar sans fenêtre de pagination à reconstituer : la couverture
documentaire et les images de source restent intactes. Le résultat ne sera pas
identique bit à bit aux JPEG du WebDataset, mais aucune information de l'édition
source n'est perdue.

## Couverture grecque documentée

`scan_validation_pg93_hesychius.md` valide 12 notices directes :

* 2797.009–.011, .013–.014, .024 : cols MPG 1180–1340 ; 1340–1369 ;
  1345–1369 ; 1388–1389 ; 1389–1392 ; 1392–1448 ;
* 2865.002–.006, .009 : 477–628 ; 628–725 ; 725–761 ; 761–773 ; 773–780 ;
  780.

Le même rapport documente trois contrôles visuels grecs lisibles : p.20
(cols 39–40), p.400 (799–800) et p.750 (1427–1428). Les bornes partagées sont
dédupliquées par les colonnes imprimées. 2274.004 et 2865.001, sans locus
MPG 93 canonique, demeurent exclus. Aucun OCR fournisseur n'a été extrait ou
conservé.

## Action exécutée et vérifiée

1. PDF original déposé sous
   `scans/volumes/pg93-hesychius/pg93-original-image-only.pdf`.
2. Vérification distante achevée : 111 047 486 octets, 915 pages et SHA-256
   `34920386a8cff8ef5e89500afdc05863ccec96e8bb837e7d4afc40be79b36828`.
3. Conserver avec lui le mapping MPG 93 et les exclusions ci-dessus.
4. Tar supprimé après cette vérification ; les rendus peuvent être recréés
   localement depuis le PDF sans OCR, et le tar reste dans l'historique HF.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif et n'a produit aucun OCR.
