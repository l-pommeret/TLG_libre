# Validation de scan — Kühn, *Galeni opera omnia*, IX (BIU Santé)

## Décision

**READY — volume complet.** `BIUSante_45674x09` est absent de `data/scan_sources.csv` et de `scans/` au contrôle du 11 août 2026. Licencié Etalab, son JP2 de 455 Mo reste sous la préférence de 500 Mo. Il couvre exactement les quatre notices canoniques de Kühn IX : pp. 1–204, 205–430, 431–533 et 769–941. Les trois pages contrôlées portent les titres distribués du volume et sont nettement lisibles.

## Concordance et métadonnées

| Notices TLG | Œuvres / preuves |
|---|---|
| 0057.061 | *De causis pulsuum*, 1–204 ; `n7` ouvre la p. 1 avec le titre grec-latin. |
| 0057.062 | *De praesagitione ex pulsibus*, 205–430 ; `n211` = p. 205 et porte le titre grec-latin. |
| 0057.063 | *Synopsis librorum suorum de pulsibus*, 431–533 ; pagination continue confirmée par le scandata. |
| 0057.065 | *De diebus decretoriis*, 769–941 ; `n775` = p. 769 et porte le titre grec-latin. |
| Source / droits | `BIUSante_45674x09` — [Internet Archive](https://archive.org/details/BIUSante_45674x09) ; *Galeni opera omnia*, IX, Kühn, Leipzig, Car. Cnoblochii ; IA date 1821/1833, le canon date le volume IX de 1825 ; [Licence ouverte Etalab](http://www.etalab.gouv.fr/licence-ouverte-open-licence). |
| JP2 / intégrité | `BIUSante_45674x09_jp2.zip` ; 455 183 874 octets ; SHA-1 `e2686299d2ba20dc07fe41bf0c7535f4a9a2582a` ; 951 images. |
| Scandata / qualité | `BIUSante_45674x09_scandata.xml` ; 338 096 octets ; SHA-1 `a9ed9d3536fd625da0b9c7cf7df2ee01e669a53b` ; PPI général absent, scans BIU lisibles (299 ppi dans les feuillets comparables). Aucun paquet JP2 original distinct publié. |

## Contrôles et action

`n7`, `n211` et `n775` ont été inspectés temporairement; les quatre JPEG téléchargés pour le repérage, le scandata et le répertoire temporaire ont été supprimés. Aucun OCR, PDF ni archive image n'a été conservé. Ajouter comme `REMOTE_ONLY` **READY** pour 0057.061–063 et 0057.065; ingestion image-only du volume complet, aucun dérivé OCR.
