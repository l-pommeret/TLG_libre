# Validation scan — *Patrologia Graeca* 46, Grégoire de Nysse (Migne)

## Décision

**READY — 19 notices dont la référence canonique est exactement MPG 46.** Le volume `patrologiaecursu46mignuoft` est absent de `data/scan_sources.csv` et de `scans/`. Il est l’édition Migne, t. 46, de 1857, et son dérivé Commons lié au même identifiant IA porte une **Public Domain Mark 1.0** explicite. Les autres notices de Grégoire de Nysse signalées dans les journaux mais référant à une édition GNO/SC moderne restent volontairement exclues : MPG 46 n’est pour elles qu’une alternative historique.

## Concordance et mapping image-only

La correspondance contrôlée est : feuille IA `n` → colonnes imprimées `2n−15` et `2n−14`. Les bornes ci-dessous incluent donc, le cas échéant, l’image portant la colonne de départ ou de fin. Les recouvrements `n375` et `n563` sont voulus : une même colonne sert à deux notices.

| Notice TLG | Colonnes canoniques MPG 46 | Images IA à ingérer |
|---|---:|---:|
| 2017.056 — *Dialogus de anima et resurrectione* | 12–160 | `n13`–`n87` |
| 2017.057 — *De infantibus praemature abreptis* | 161–192 | `n88`–`n103` |
| 2017.058 — *Testimonia adversus Judaeos* [Sp.] | 193–233 | `n104`–`n124` |
| 2017.059 — *Adversus eos qui castigationes aegre ferunt* | 308–316 | `n161`–`n165` |
| 2017.060 — *De iis qui baptismum differunt* | 416–432 | `n215`–`n223` |
| 2017.061 — *Decem syllogismi contra Manichaeos* [Sp.] | 541 | `n278` |
| 2017.062 — *De deitate filii et spiritus sancti* | 553–576 | `n284`–`n295` |
| 2017.063 — *De spiritu sancto sive In pentecosten* | 696–701 | `n355`–`n358` |
| 2017.064 — *Encomium in sanctum Stephanum protomartyrem* II | 721–736 | `n368`–`n375` |
| 2017.065 — *De sancto Theodoro* | 736–748 | `n375`–`n381` |
| 2017.066 — *Encomium in xl martyres* I | 749–772 | `n382`–`n393` |
| 2017.067 — *Encomium in xl martyres* II | 773–788 | `n394`–`n401` |
| 2017.068 — *In sanctum Ephraim* | 820–849 | `n417`–`n432` |
| 2017.069 — *De vita Gregorii Thaumaturgi* | 893–957 | `n454`–`n486` |
| 2017.070 — *Epistula XXVI ad Evagrium* [Sp.] | 1101–1108 | `n558`–`n561` |
| 2017.071 — *Sermo in illud: Hic est filius meus dilectus* | 1109–1112 | `n562`–`n563` |
| 2017.072 — *Sermo in Mariam et Joseph* | 1112 | `n563` |
| 2017.073 — *De occursu domini* [Sp.] | 1152–1181 | `n583`–`n598` |
| 2017.080 — *Epistula ad Philippum monachum* | 1112 | `n563` |

## Provenance, droits et technique

| Champ | Valeur vérifiée |
|---|---|
| Dépôt image / item | Internet Archive [`patrologiaecursu46mignuoft`](https://archive.org/details/patrologiaecursu46mignuoft) |
| Source de droits explicite, même scan | Wikimedia Commons [`Patrologia Graeca Vol. 046 (bw)`](https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._046_(bw).pdf), dont les métadonnées indiquent l’identifiant IA exact, PDM 1.0 et l’absence de restrictions connues |
| Édition | J.-P. Migne, *Patrologiae cursus completus, Series Graeca*, t. 46, Petit-Montrouge, 1857 |
| Archive image | `patrologiaecursu46mignuoft_jp2.zip`, « Single Page Processed JP2 ZIP » |
| Taille / SHA-1 | 310 036 719 octets; `b17db7773b2e8c1cad9cbeb1a26256f0da44ca94` |
| Images / PPI | 658 images; 300 ppi déclarés par IA |
| Original JP2 | Aucun paquet « original JP2 » distinct listé dans les métadonnées IA; employer uniquement les images-source du flux IA, jamais un OCR/PDF. |
| Scandata | `patrologiaecursu46mignuoft_scandata.xml`, SHA-1 `c87d57a16be7c9ab8e6e8a2db43f607247c617fb` |
| Rendement exact | 19 notices; 248 feuilles distinctes après dédoublonnage des intervalles ci-dessus; archive entière sous 500 Mo |

## Contrôle visuel sans OCR

Trois JPEG individuels et temporaires ont été examinés puis supprimés :

- `n13`, colonnes 11–12 : titre et début du *Dialogus de anima et resurrectione*;
- `n356`, colonnes 697–698 : grec de *De spiritu sancto*, net et complet;
- `n598`, colonnes 1181–1182 : borne finale de *De occursu domini*, pagination et impression nettes.

Les trois échantillons sont bien contrastés; les rousseurs mineures ne gênent pas la lecture du grec. Aucun OCR, PDF, archive JP2 ou image d’ingestion n’a été téléchargé ni conservé.

## Action proposée

Ingestion **image-only READY**, en utilisant les intervalles de la table et en dédoublonnant les images partagées. Enregistrer l’identifiant IA, le lien Commons PDM, le SHA-1 du paquet et cette règle de pagination dans le manifeste. Exclure explicitement du lot les œuvres pour lesquelles les journaux indiquent une édition GNO/SC : leur présence dans PG 46 ne constitue pas une concordance d’édition canonique.
