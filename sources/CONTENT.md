<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->

<!-- LTeX:Language=de-DE -->

`sources/ltx.etc` enthält Lehr- und Lernmittelquellen im Format [.tex (LaTeX), .md, .drawio] samt zugehöriger Bilder, build-Skripte und Makefiles - gruppiert nach Lernfeldern, Themen und Aspekten. Die Ordnerstruktur nutzt folgende Systematik:

1. `3ps` :- 3rd-Party-Software, die zum Kompilieren der Lehr- und Lernmittel aus den Quellen benötigt wird.
2. `bib.gl` :- Biber-Latex basierte globale Literaturverwaltung
3. `bin` :- Scripte zum Kompilieren der Lehr- und Lernmittel aus den Quellen
4. `cfg.gl`:- globale Konfigurationsdateien zum Kompilieren der Lehr- und Lernmittel aus den Quellen
5. `img.gl` :- alle verwendeten Bilder samt json-Info über Quellen und Rechte
6. `lf.crx` :- lernfeldübergreifende Stunden.
7. `lf.tpl` :- Template zur Instantiierung / Initialisierung eines neu hinzuzufügenden Lernfelds

Ziel ist es, zu jedem Lernfeld fertig nutzbare Unterrichtsmaterialien anbieten zu können, die alle Themen und Aspekte des Lernfeldes abdecken.

