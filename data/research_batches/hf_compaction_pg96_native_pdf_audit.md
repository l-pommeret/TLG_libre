# Audit de remplacement HF — *Patrologia Graeca* 96

## Décision

**READY — remplacement du tar rendu par le PDF natif image-only, après
vérification distante.** Le PDF Commons est la source de fac-similé sous-jacente
aux rendus du tar ; aucun OCR n'est requis ni autorisé pour ce remplacement.

## Source native vérifiée

* **Notice Commons :** [*Patrologia Graeca* 96](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._096.pdf)
* **Original direct :** [PDF image-only](https://upload.wikimedia.org/wikipedia/commons/3/3f/Patrologia_Graeca_Vol._096.pdf)
* **API Commons, 2026-08-11 :** MIME `application/pdf`, taille `111178601`
  octets, SHA-1 `13cd5118c477a458006f0272697dd241c8abeb85`, dimensions source
  979 × 1581 px, 908 pages.
* **Droits explicitement vérifiés :** `Public domain`, `Copyrighted: False`.
  Le registre conserve aussi le PDM 1.0.

## Équivalence avec l'archive HF

| Élément | Valeur |
|---|---:|
| Archive rendue actuelle | `webdataset/volumes--pg96-john-damascene--ef030e48931e.tar` |
| État HF | `MIGRATED_PUBLIC`, `REMOTE_PATH_AND_SIZE_MATCH` |
| Pages/images dans le tar | 908 |
| Taille tar | 667 535 360 octets |
| SHA-256 du manifeste/tar vérifié | `b20eca5c1dc64f574768a32daaef66d25d539bc572d898644f0602cdac3463b8` |
| PDF source natif | 111 178 601 octets ; 908 pages |
| Économie estimée | 556 356 759 octets (83,34 %) |

Le nombre de pages est identique (908) : contrairement à PG 62, aucune fenêtre
de pages n'est à reconstituer. Le PDF source conserve le volume complet et le
tar n'apporte qu'un cache de rendus JPEG. La substitution est donc sans perte
documentaire ou bibliographique, bien qu'elle ne soit pas une identité binaire
avec les JPEG du WebDataset.

## Couverture TLG et grec documentés

Le rapport `scan_validation_pg96_john_damascene.md` atteste 16 notices directes
et leurs loci imprimés :

* 2017.075 : 476–477 ;
* 2934.019, .054–.057 : 441–544 ; 545–576 ; 576–588 ; 601–644 ; 648–661 ;
* 2934.059–.062, .064, .072 : 761–781 ; 781–813 ; 816–817 ; 818–856 ;
  1252–1320 ; 1408–1413 ;
* 2714.001, 2935.001–.002, 3173.001 : 680–697 ; 1348–1361 ; 1460–1500 ;
  1501–1508.

Les contrôles déjà documentés sur p.20 (cols 23–24), p.400 (719–720) et p.760
(1339–1340) montrent un grec dense, net et lisible. Les chevauchements de
colonnes sont conservés par le volume entier ; les identifiants canoniques avec
suffixe `x` et 5060.003 restent explicitement exclus, comme dans le rapport de
validation. Aucun OCR fournisseur n'a été extrait ou stocké.

## Remplacement exécuté et vérifié

1. PDF original déposé sous
   `scans/volumes/pg96-john-damascene/pg96-original-image-only.pdf`.
2. Vérification HF achevée : 111 178 601 octets, 908 pages et SHA-256
   `4d13ddae7f94e90f8aac6fed58ab5295acfdc46e04a26fbd6a49efa105bc5285`.
3. Conserver, avec le PDF, le tableau des loci MPG 96 du rapport de validation.
4. Tar de rendus supprimé après ces vérifications ; tout besoin de JPEG ou de
   WebDataset peut être satisfait en rendant localement le PDF source, sans OCR.

L'audit préparatoire n'avait téléchargé aucun asset. L'exécution ultérieure a
transféré uniquement le PDF image-only natif ; aucun OCR n'a été produit ou
conservé. La suppression du tar reste réversible via l'historique HF.
