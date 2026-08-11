# Validation de scan — Nau, « Le texte grec des récits utiles à l'âme d'Anastase » (*Oriens Christianus* 3.1)

## Décision

**READY — extraction ciblée.** `OriensChristianus3` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. Il contient exactement l'article de F. Nau cité par le canon pour TLG 2896.012, dans *Oriens Christianus* 3.1 (1903), pp. 61–88. La licence Public Domain Mark 1.0 est explicite, le scan est à 600 ppi et les trois contrôles montrent un grec très net. Le paquet JP2 du volume complet fait toutefois 774 Mo : ne récupérer que les images des pp. 61–88 (feuilles 72–99), jamais l'OCR dérivé.

## Concordance

| Notice TLG | Œuvre | Pages canoniques | Preuve visuelle |
|---|---|---:|---|
| 2896.012 | Anastasius Sinaïta [Dub.], *Narrationes* (BHG 1448q) | 61–88 | `n72` = p. 61, en-tête « Le texte grec des récits utiles à l'âme d'Anastase (le Sinaïte) » et texte grec; `n85` = p. 74, article Nau en continu; `n99` = p. 88, dernière page de la plage. |

## Métadonnées Internet Archive

| Champ | Valeur vérifiée |
|---|---|
| Identifiant / source | `OriensChristianus3` — [Internet Archive](https://archive.org/details/OriensChristianus3) |
| Volume / date | *Oriens Christianus* 3 ; 1903 |
| Article / édition | F. Nau, « Le texte grec des récits utiles à l'âme d'Anastase (le Sinaïte) », 3.1, pp. 61–88 — concordance exacte avec le canon |
| Fichier image traité | `Oriens_Christianus_jp2.zip` |
| SHA-1 / taille | `f498f437e66e8e3edf4a2bc43581c5348c909521` ; 773 851 216 octets |
| Images / original distinct | `leafCount=634` dans le scandata ; aucun paquet JP2 original distinct dans les métadonnées consultées |
| Scandata | `Oriens_Christianus_scandata.xml`; SHA-1 `9160c6fb2a364c3636fa4e1396f309f06ce29b48` ; 210 655 octets |
| PPI / qualité | 600 ppi dans les métadonnées et le scandata ; grec, appareil et pagination lisibles et homogènes dans les trois contrôles |
| Droits | `licenseurl` : [Creative Commons Public Domain Mark 1.0](http://creativecommons.org/publicdomain/mark/1.0/) |
| Accès image | vues IA `https://archive.org/download/OriensChristianus3/page/n{leaf}_w1400.jpg` ; pp. 61–88 = feuilles 72–99 selon le scandata |

## Contrôles visuels temporaires

`n72` (p. 61, début de l'article et texte grec), `n85` (p. 74, texte grec continu) et `n99` (p. 88, terminaison de l'article) ont été obtenus individuellement et inspectés. Les trois JPEG, le `scandata.xml` de repérage et le répertoire temporaire ont ensuite été supprimés. Aucun OCR, PDF ni archive image ne subsiste localement.

## Action

Ajouter une source `REMOTE_ONLY` **READY** pour 2896.012. La priorité de taille (<500 Mo) n'est pas satisfaite par le volume complet (774 Mo) : préparer une ingestion image-only **ciblée** des feuilles 72–99 / pp. 61–88, avec les métadonnées et l'empreinte ci-dessus, sans ouvrir ni employer les dérivés OCR.
