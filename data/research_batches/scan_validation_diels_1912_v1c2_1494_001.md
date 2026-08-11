# Contrôle qualité — Diels 1912, vol. I c.2, candidat pour TLG 1494.001

**Décision : REJECT pour TLG 1494.001.** Le volume est légalement réutilisable et techniquement bon, mais la tranche auparavant proposée ne couvre pas Mélissos ; elle couvre Empédocle. Il ne faut donc pas l’ingérer ni l’associer à `1494.001`.

## Identification, droits et objet numérique

- Internet Archive : [`diefragmentederv12diel`](https://archive.org/details/diefragmentederv12diel), *Die Fragmente der Vorsokratiker*, Hermann Diels, Weidmann, Berlin, 1912, `v.1 c.2`.
- Le [fichier Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Die_Fragmente_der_Vorsokratiker_(IA_diefragmentederv12diel).pdf) est marqué **PD-1923 / domaine public**. La métadonnée IA n’énonce pas de licence, mais confirme l’édition, le volume et le dépositaire (Duke University Libraries).
- Contrôle de collision : l’identifiant est absent de `data/scan_sources.csv` et de `scans/`.
- IA déclare 460 images, 350 ppi dans `scandata.xml`.
- Dérivés image complets disponibles mais non téléchargés : JP2 traité, 204 348 905 octets, SHA-1 `890eba6a6cad40371554d9e8cd3e975c4b8f8462` ; JP2 original, 411 719 680 octets, SHA-1 `dbc54ad955cc071263ae0799c9318b5c9a049f0b`.
- Structure de pagination : `diefragmentederv12diel_scandata.xml`, 601 210 octets, SHA-1 `6266c5415b06db2ff2b3e8db9a66df3fcdfbfe4b`.

## Contrôle de la tranche demandée

| Feuille IA | Page imprimée | Observation visuelle | Résultat pour 1494.001 |
|---|---:|---|---|
| `n278` | 258 | En-tête « 21. Empedokles », texte grec et traduction allemande, entrée 99. | Non concordant |
| `n282` | 262 | Même en-tête Empédocle, entrées 109–110. | Non concordant |
| `n287` | 267 | « B. Fragmente. 115. Katharmoi », toujours Empédocle. | Non concordant |

Les trois vues, prises au début, milieu et fin de la tranche `n278`–`n287`, sont nettes, correctement cadrées et d’une qualité suffisante. Elles prouvent cependant que l’équivalence antérieure « Mélissos pp. 258–267 = feuilles 278–287 » est erronée : ces pages imprimées sont celles d’Empédocle dans l’édition 1912. La concordance bibliographique avec le canon de `1494.001` (*Melissus, Testimonia*, Diels–Kranz 1951, pp. 258–267) n’est donc pas établie et est positivement contredite par le scan.

## Suite sûre

Ne télécharger aucune des feuilles `n278`–`n287` pour `1494.001`, et ne pas effectuer d’OCR. Chercher séparément le locus Mélissos dans une édition historiquement concordante, en contrôlant d’abord le titre de chapitre et la pagination sur images. Les trois échantillons temporaires et le `scandata.xml` local ont été supprimés après l’inspection.
