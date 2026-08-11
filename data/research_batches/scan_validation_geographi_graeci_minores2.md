# Validation de scan — Müller, *Geographi Graeci Minores*, II (1861)

**Candidat :** Internet Archive
[`india.history.resource.71426`](https://archive.org/details/india.history.resource.71426).

**Sélection.** L’identifiant a été contrôlé absent de `data/scan_sources.csv`
et de `scans/`. Ses métadonnées donnent sans ambiguïté le volume II des
*Geographi Graeci Minores*, K. Müller, Didot, 1861 : le tome et l’année sont
ceux des deux références canoniques.

**Décision : REJECT pour ingestion à ce stade (droits fournisseur non
documentés).** Les pages, l’édition et la qualité de scan concordent. Mais
Internet Archive ne fournit ni `rights`, ni `licenseurl`, ni
`possible-copyright-status`; l’ancienneté matérielle ne constitue pas une
licence explicite de réutilisation. Aucun OCR n’a été consulté ni retenu.

## Concordance bibliographique et TLG

| Notice TLG | Référence du canon | Contrôle de page |
| --- | --- | --- |
| 2029.001 — *Anonymi summaria ratio geographiae in sphaera intelligendae* | K. Müller, *Geographi Graeci Minores*, II, Paris, Didot, 1861, pp. 488–493 | La p. 488 ouvre les titres grec et latin **SUMMARIA RATIO GEOGRAPHIÆ IN SPHÆRA INTELLIGENDA**, avec texte grec et traduction latine en regard. |
| 0092.001 — *Geographiae expositio compendiaria* | K. Müller, ibid., pp. 494–509 | La continuité des pp. 494–509 est sous l’en-tête **ANONYMI** ; la p. 509 termine la section juste avant **FRAGMENTA**. |

## Métadonnées Internet Archive

| Champ | Valeur contrôlée |
| --- | --- |
| Identifiant / fournisseur | `india.history.resource.71426` — Internet Archive, collection `IndiaHistory` / `JaiGyan` |
| Titre / créateur | *Geographi Graeci Minores … Vol. II* — Carolus Müller |
| Éditeur / date | Ambroise Firmin Didot, Paris / 1861 |
| Droits | `rights`, `licenseurl` et `possible-copyright-status` absents : motif du rejet |
| Imagecount / PPI | `imagecount` absent dans les métadonnées ; 300 ppi ; paquet JP2 processed à 738 fichiers |
| JP2 processed | `71426_jp2.zip`, 633,692,322 octets, 738 fichiers, SHA-1 `3ffef6f61d31ce178dec7f51cc08b972486c57b6` |
| JP2 original | Aucun paquet raw/original JP2 exposé par cet item |
| Scandata | `71426_scandata.xml`, 260,204 octets, SHA-1 `e6011ce5087064abe4706c946aa398e76826b17a` |

## Contrôles visuels temporaires

Trois JPEG BookReader à 1400 px ont été récupérés dans `/tmp`, examinés
visuellement, puis supprimés définitivement avec le répertoire temporaire.
Ils n’ont été ni OCRisés ni ajoutés au dépôt.

| Vue | Feuillet IA / page imprimée | Résultat |
| --- | --- | --- |
| [ouverture](https://archive.org/download/india.history.resource.71426/page/n555_w1400.jpg) | `n555`, p. 488 | Titres grec/latin de la *Summaria ratio*, texte et notes nettement lisibles. |
| [milieu](https://archive.org/download/india.history.resource.71426/page/n565_w1400.jpg) | `n565`, p. 498 | *Anonymi*, texte grec et traduction latine continus ; qualité suffisante. |
| [fin](https://archive.org/download/india.history.resource.71426/page/n576_w1400.jpg) | `n576`, p. 509 | Dernière page de la seconde plage ; **FRAGMENTA** débute après sa clôture. |

## Suite autorisée

Ne pas inscrire ce volume dans `scan_sources.csv` ni récupérer le JP2 tant
qu’une déclaration de droits réutilisable n’est pas obtenue. Le candidat est
sinon techniquement exploitable : 2 notices, 738 images processed à 300 ppi.
