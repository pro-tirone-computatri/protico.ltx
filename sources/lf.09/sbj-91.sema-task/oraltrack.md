<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:91**</span>

Ausgangspunkt ist ein **Netz mit zwei getrennten, jeweils voll-verswitchten Broadcast-Domänen**.
Darin werde eine Nachricht von `RA2` zu `RB1` übertragen und von `RB1` an `RA2` beantwortet.

Das Netz bestehe in der Broadcastdomäne *A* aus den Rechnern `RA1`, `RA2` und dem
Layer-II-Switch `SWA`, in der Broadcastdomäne *B* aus den Rechnern `RB1`, `RB2` und dem
Layer-II-Switch `SWB`.  Die Broadcastdomänen *A* und *B* werden durch einen Router `RAB`
verbunden, der über sein eines Interface auch in Broadcastdomäne *A* und über
sein eines Interface auch in Broadcastdomäne *B* gehört.


* [ ] Erstellen Sie ein Drawio-Aktivitätsdiagramm für dieses Szenario
* [ ] Gehen Sie dabei davon aus, dass `RB` 1 Minute benötigt, um die Antwort zu berechnen.
* [ ] Erstellen Sie das dazu passende Drawio-Sequenzdiagramm

Laden Ihr Dateien im Datenaustauschbereich hoch. Benennen Sie Ihre Dateienpaar analog zu 

* `exa-YYYYMMDD-name-act.drawio` 
* `exa-YYYYMMDD-name-seq.drawio`

<!-- uebung::end -->

---


Lösung: Analog zu sbj-06.arp-router-zenprese.pdf / Folie 06


---

<!-- uebung::start -->

Benotung pro Diagramm:

* 2 Punkte, wenn wesentliche Handlungsabschnitte bzw. Kommunikationsschritte mit den im Prinzip richtigen Diagrammsymbolen erfasst sind
* 2 Punkte, wenn alle Handlungsabschnitte bzw. Kommunikationsschritte mit den richtigen Diagrammsymbolen erfasst sind.
* 2 Punkte, wenn alle Handlungsabschnitte bzw. Kommunikationsschritte mit den richtigen Diagrammsymbolen optisch sauber und einsichtig dargestellt sind.
* 6 Punkte, wenn die Aktion des Umschreibens als Handlung im Aktivitätsdiagramm und als Parameter im Sequenzdiagramm richtig erfasst sind.

| Punkte | Note | Punkte | Note | Punkte | Note | Punkte | Note | Punkte | Note |
|---|---|---|---|---|---|---|---|---|---|
| 16+x | 1 | 12 | 2 | 11 | 2,3 | 10 | 2,7 
|   |  | 9 | 3 | 8 | 3,3 | 7 | 3,7 |
|   |  | 6 | 4  |  5 | 4,3  | 4 | 4,7 | ... | ... |

<!-- uebung::end -->

---

