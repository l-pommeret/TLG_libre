# Validation ciblée — FU Berlin, Heisenberg 1908, TLG 3190.006

## Décision

**READY_TARGETED_IMAGE_ONLY.** L'édition est la publication exacte demandée :
August Heisenberg, *Die Apostelkirche in Konstantinopel* (Leipzig, 1908),
pp. 10–96, qui contient la *Descriptio ecclesiae ss. Apostolorum* de Nicolaus
Mesarites (TLG 3190.006). La ressource FU Berlin est explicitement sous **CC0**.

Le seul transfert recommandé est le segment de **87 images JPEG originales**
des pages PDF **24–110 incluses** (pages imprimées **10–96**). Ne pas envoyer le
PDF intégral de 461,6 MB et ne pas produire ni récupérer d'OCR.

## Provenance et intégrité

| Champ | Valeur vérifiée |
|---|---|
| Dépôt / notice | Freie Universität Berlin, Refubium, [handle fub188/28047](https://refubium.fu-berlin.de/handle/fub188/28047) |
| Fichier natif | [heisapos_BV004893928_2.pdf](https://refubium.fu-berlin.de/bitstream/handle/fub188/28047/heisapos_BV004893928_2.pdf?sequence=1&isAllowed=y) |
| Édition | Heisenberg, 1908, vol. II, *Die Apostelkirche in Konstantinopel* |
| Droits | CC0 — indiqué dans le champ `DC.rights` de la notice et par le lien CC0 de Refubium |
| Taille / pages | 484 127 407 octets (461,6 MB décimaux) ; 321 pages PDF |
| MD5 source | `f32f2ea85ffa12eb7508a460e8699871` (identique à la somme publiée par Refubium) |
| SHA-256 source | `71ff324e0412656340ce1b800905aefb55c6939f32823624257ae0db90e0c480` |
| Contenu PDF | une image JPEG couleur par page cible ; aucun texte/OCR n'a été exploité |

## Pagination et manifeste strict

La correspondance a été contrôlée directement sur les numéros imprimés :

| TLG | Édition / pages imprimées | Pages du PDF FU | Images à conserver | Pages immédiatement hors cible |
|---|---|---:|---:|---|
| 3190.006 | Heisenberg 1908, 10–96 | **24–110** | **87** JPEG originaux | 1–23 (préliminaires) ; 111–321 (à exclure) |

La règle est constante dans ce segment : `page PDF = page imprimée + 14`.
La p. PDF 111 est la p. imprimée 97 et commence le chapitre suivant : elle ne
doit donc pas être conservée. Les feuilles 24–110 portent l'édition bilingue
(grec imprimé dans la moitié supérieure et traduction/notes allemandes dans la
moitié inférieure) ; conserver les feuilles telles quelles, sans recadrage qui
risquerait de perdre les apparats grecs.

## Qualité et contrôle visuel grec

L'inspection visuelle a porté sur trois pages éloignées du **fichier FU** :

| Rôle | PDF / imprimé | Constat |
|---|---:|---|
| Borne initiale | PDF 24 / p. 10 | En-tête « Lage und Umgebung der Kirche » ; texte grec net, apparat et traduction ; début du locus. |
| Milieu | PDF 68 / p. 54 | Texte grec continu, lignes et diacritiques lisibles ; image nette. |
| Borne finale | PDF 110 / p. 96 | Texte grec continu jusqu'à la fin de la page ; dernière page du locus. |

Les 87 images natives sont des JPEG à 300 × 300 ppi, 8 bits couleur ICC ;
dimensions observées : 2 509–2 746 × 3 372–3 543 px. L'extraction JPEG sans
réencodage des seules pages 24–110 représente 107 854 971 octets (102,9 MiB),
soit environ 78 % de moins que le PDF complet.

## Transfert exécuté et vérifié

Le 12 août 2026, les pages PDF 24–110 ont été assemblées dans un PDF
image-only ciblé de 87 pages puis transférées vers
`scans/tlg3190/tlg006/fu-berlin-heisenberg-1908-pp10-96.pdf` sur HF.
Le blob distant mesure 132 327 062 octets et son SHA-256 LFS est
`cb37a961d305c63b1b8072620273a4d43493c085e519ebe06b8f7f2bb899c61c`,
identique au dérivé local. Aucun OCR n'a été ajouté.

## Reproduction

Sur le runner distant, télécharger temporairement le PDF depuis l'URL FU,
vérifier son MD5, puis exécuter uniquement :

```sh
pdfimages -f 24 -l 110 -j -p heisapos_BV004893928_2.pdf mesarites_3190_006
```

Conserver les 87 JPEG sortis, avec ce manifeste et la provenance CC0 ; purger
le PDF temporaire et toute page hors 24–110. Cette commande extrait les images
JPEG incorporées sans OCR ni rendu/réencodage.

## Nettoyage

Les trois échantillons visuels et les 87 JPEG de contrôle ont été supprimés
après vérification. Le PDF intégral et le dérivé ciblé temporaires seront
purgés après validation du registre. Aucun OCR n'a été produit ou utilisé.
