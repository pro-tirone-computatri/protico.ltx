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

EXC=sh2go-14
echo "executing Uebung $EXC"

# Erstellen Sie Script, dass eine Datei zeilenweise einliest und i
# die Zeilen sortiert in ein Duplikatsdatei schreibt

# Hintergrund: 
#
# Das Tool 'sort' alle Zeilen einer Datei oder von stdin  ein
# sortiert sie alphabetisch, sobald sie alle eingelesen hat
# und gibt sie nach stout wieder aus.
#
# Zum Testen können Sie gut die den Output von sh2go-13 verwenden. 


cat list-of-sh2go-tasks.txt | sort > list-of-sh2go-tasks.dup

