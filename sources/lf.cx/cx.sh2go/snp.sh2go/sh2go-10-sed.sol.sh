#!/bin/sh
#
# This file is part of the Open Source project 'proTironeComputatri'
# (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

# Lesehinweis: 
# In spitzen Klammern schreibe ich stets Tools und ihre Parameter.
# Die Tools stellt Ihnen Betriebssystem zur Verfügung.
#
# Beipiel: 
# Rufen Sie <echo dies> auf, meint, dass Sie an der
# Kommandozeile echo dies eingeben. Wo sich das Tool, hier
# <echo> bei Ihnen befindet, können Sie mit <which echo> erfragen

EXC=sh2go-10
echo "executing Uebung $EXC"

# (1) Schreiben Sie wieder das heutige Datum mit dem Format +'%Y%m%d" in eine Datei. Nutzen Sie dafür das Tool <date> 
# (2) Hängen Sie wieder aus dem Skript heraus die Zeile '2024 war besser' an Ihre Datei
# (3) Ersetzen Sie mit dem Streameditor automatisiert aus dem Skript heraus jede Jahreszahl durch das Jahr 3030


# Hintergrund: 
#
# (A) Eine Pipe (Symbol '|') nimmt den Output des vorgehenden Tools und reicht in als Input an das nachfolgende Tool weiter.
# (B) cat nimmt einem Dateiname und liest den Inhalt der Datei ein und gibt ihn zeilenweis aus.
# (C) sed (= Stream-Editor) liest von stdin Zeile für Zeile ein. 
# (D) sed nimmt als Parameter einen (Ersaetzungs)Befehl der Form "s/RegEx/Neu/" und wendet den auf jede Zeile an.
# (E) Als Stream-Editor erwartet der Editor die zu modifizierenden Zeilen von stdin. Deshalb muss der
#     Inhalt einer Datei zuvor mit cat eingelesen und mit | zu sed gepipet werden.

echo `date +'%Y%m%d'` > mf.txt
echo '2024 war besser' >> mf.txt
cat mf.txt | sed "s/202[45]/3030/"