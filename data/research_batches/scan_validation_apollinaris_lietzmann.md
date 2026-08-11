# Validation de scan — Lietzmann, *Apollinaris von Laodicea*, I (1904)

**Sélection :** meilleur rendement des audits IA non validés sous 500 Mo :
28 notices TLG, paquet JP2 de 71,543,217 octets à 600 ppi.

**Cibles couvertes :** TLG 2074.001–028 (*Apollinaris Theol.*).

**Décision : READY, avec réserve de licence IA.** L'édition, les plages de
pagination et les trois contrôles visuels concordent avec les 28 notices.
L'item porte `possible-copyright-status=NOT_IN_COPYRIGHT`; les champs
`rights` et `licenseurl` sont toutefois vides. Un seul paquet JP2 processed
est publié : aucun paquet raw/original distinct n'est disponible dans les
métadonnées IA.

## Concordance bibliographique et rendement

| Élément | Contrôle |
|---|---|
| Volume IA | [`apollinarisvonl00apolgoog`](https://archive.org/details/apollinarisvonl00apolgoog), H. Lietzmann, *Apollinaris von Laodicea und seine Schule: Texte und Untersuchungen*, I, Tübingen, J. C. B. Mohr (Paul Siebeck), 1904. |
| Correspondance canon | Les 28 notices `2074.001`–`2074.028` renvoient toutes à Lietzmann 1904, pp. 167–270 (à l'exception des lacunes internes de la sélection). |
| Rendement | 28 notices / 71,543,217 octets = le meilleur candidat exact non validé de `scan_volume_audit_ia_01.csv` sous le seuil préférentiel de 500 Mo. |
| Édition | Titre, éditeur H. Lietzmann, lieu, éditeur commercial et année concordent exactement avec les notices canon. |

### Mapping TLG → pages de l'édition

| Notices | Pages Lietzmann 1904 |
|---|---|
| 2074.001–003 | 167–199 |
| 2074.004–005, 2074.028 | 204–207 |
| 2074.006–011 | 207–236 |
| 2074.012–019 | 237–249 |
| 2074.020–026 | 250–263 |
| 2074.027 | 269–270 |

Cette répartition est dérivée des 28 notices individuelles du
`canon_coverage.csv`; elle couvre notamment la plage intermédiaire p. 220 et
la borne finale p. 270 contrôlées ci-dessous.

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / accès | `apollinarisvonl00apolgoog` — <https://archive.org/metadata/apollinarisvonl00apolgoog> |
| Collection / contributeur | `americana`; Harvard University; numérisation Google |
| Langues | `ger`, `grc` |
| Nombre d'images | 360 |
| Résolution déclarée | 600 ppi |
| JP2 processed | `apollinarisvonl00apolgoog_jp2.zip`, 71,543,217 octets, SHA-1 `542dd33254faeb3a52d73333097ca737f933e206` |
| JP2 raw/original | Aucun fichier raw/original distinct publié dans la réponse de métadonnées IA. |
| Données de scan | `apollinarisvonl00apolgoog_scandata.xml`, SHA-1 `f2e7a16d0cc7af5d067bd284bbf0cf161b152807` |
| Droits | `possible-copyright-status=NOT_IN_COPYRIGHT`; `rights` et `licenseurl` absents. |

## Contrôle visuel temporaire (sans conservation)

Trois JPEG de pages individuelles ont été demandés au lecteur IA, examinés
dans `/tmp`, puis supprimés définitivement. Ni paquet complet, ni image,
ni OCR n'a été conservé dans le dépôt.

| Échantillon | Vue IA | Résultat visuel |
|---|---|---|
| Début — 2074.001 | [`n196` (p. 167)](https://archive.org/download/apollinarisvonl00apolgoog/page/n196_w1400.jpg) | Début de **Ἡ κατὰ μέρος πίστις**, grec et apparat critique nettement lisibles. |
| Milieu — 2074.007 | [`n249` (p. 220)](https://archive.org/download/apollinarisvonl00apolgoog/page/n249_w1400.jpg) | P. 220, fragments 66–70 dans la grande plage 208–232 de la *Demonstratio*, impression nette. |
| Fin — 2074.027 | [`n299` (p. 270)](https://archive.org/download/apollinarisvonl00apolgoog/page/n299_w1400.jpg) | P. 270, fin des *Fragmenta ex operibus incertis*, texte grec et allemand lisibles. |

Le paquet JP2 processed est une source image appropriée à une OCRisation
interne ; les fichiers `djvu.xml` et `text.pdf` n'ont pas été lus ni employés
comme texte.
