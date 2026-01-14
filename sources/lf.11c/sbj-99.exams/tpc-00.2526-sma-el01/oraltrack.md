<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

---

<!-- uebung::start -->
<span style="color: green;">_Aufgabe_</span> <span style="color:magenta;">**LF11c:Klausurersatzleistung:Allgemein**</span>

Sie erhalten im Folgende 7 aufeinander aufbauende und ineinandergreifende Teilaufgaben. Auf's Ganze gesehen sollen Sie in Python einen Konverter vom gegebenen Input-Format ins JSON-Format programmieren. Die Einzelaufgaben brechen diese Aufgabe in Teilschritte herunter.

Wenn Sie dabei

* ein Ergebnis beschreiben sollen, dann fügen Sie diese Beschreibung als Kommentar in Ihren Programmcode ein.
* die einzulesende Daten vor der Verarbeitung modifizieren, fügen Sie Ihre Version als Input-Datendatei Ihrer Lösung hinzu.
* Testdaten zusammenstellen, fügen Sie die als (zweite) Input-Datendatei Ihrer Lösung hinzu.
* Daten, Funktionen oder Klassen programmieren, fügen Sie in einer einzigen Programmdatei Ihrer Lösung bei.

Laden Sie Ihre Dateien zum Schluss in den Ordner hoch, in den Sie auch alle bisherigen Übungen hochgeladen haben. Nutzen Sie dabei das bekannte Namensschema:

* Ihre Programmdatei ende bitte auf die Extension `.py`
* Ihre Input-Datendatei(en) verwenden bitte die entsprechenden Dateiextensionen.  

Ich bewerte Ihre Lösung nach den Merkmalen (Teilschritten), die ich im Folgenden mit einer Punktzahl versehen habe.

Es sind 32 Punkte erreichbar (plus 4 Zusatzpunkte)

Punkte | Zensur
---|---
32 | 1
31 | 1,2
30 | 1,4
29 | 1,6
28 | 1,9
27 | 2,1
... | gemäß [ihk-notenschluessel](https://www.lehrerfreund.de/notenschluesselrechner/form-ihk-notenschluessel)

<!-- uebung::end -->

---

**_Lösung zu Step 02:_**


---

<!-- uebung::start -->
<span style="color: green;">_Aufgabe_</span> <span style="color:magenta;">**LF11c:Klausurersatzleistung:Step:01**</span>

* [ ] Laden Sie die Datei `dsp.teta.xyz` herunter.
* [ ] Machen Sie sich mit den Daten vertraut.
* [ ] Finden Sie die Ordnung der Daten.
* [ ] Modifizieren Sie die Daten so, dass jeder Datensatz in einer eigenen Zeile steht. **(2P)**
* [ ] Beschreiben Sie die Datensatzstruktur. **(1P)**

<!-- uebung::end -->

---

**_Lösung zu Step 02:_**

---

<!-- uebung::start -->
<span style="color: green;">_Aufgabe_</span> <span style="color:magenta;">**LF11c:Klausurersatzleistung:Step:02**</span>

* [ ] Bereinigen Sie die Daten syntaktisch, wo es die Einheitlichkeit gebietet. **(2P)**
* [ ] Beschreiben Sie, welche Datensätze wie und warum syntaktisch bereinigt werden mussten. **(1P)**

<!-- uebung::end -->

---

**_Lösung zu Step 02:_**

---

<!-- uebung::start -->
<span style="color: green;">_Aufgabe_</span> <span style="color:magenta;">**LF11c:Klausurersatzleistung:Step:03**</span>

* [ ] Bereinigen Sie die Daten semantisch, wo es die Konsistenz gebietet. **(2P)**
* [ ] Beschreiben Sie, welche Datensätze wie und warum semantisch bereinigt werden mussten. **(1P)**

<!-- uebung::end -->


---

**_Lösung zu Step 03:_**

---

<!-- uebung::start -->
<span style="color: green;">_Aufgabe_</span> <span style="color:magenta;">**LF11c:Klausurersatzleistung:Step:04**</span>

* [ ] Programmieren Sie in Python einen Konverter, der die (syntaktisch und semantisch bereinigten) Daten in dem Format aus einer Datei einliest, das Sie in Step 1 festgelegt haben, und sie in demselben Format in eine andere Datei zurückschreibt. Verfolgen Sie dabei nachvollziehbar dem Minimal-Viable-Produkt-Prinzip:
  * [ ] **MVP-0**:
    * [ ] Extrahieren Sie 3 Datensätze aus den von Ihnen bereinigten Daten als Testdaten. **(1P)**
    * [ ] Definieren Sie eine Zwischenrepräsentation.
    * [ ] Initialisieren Sie im Programm eine entsprechende Datenstruktur mit 2 Datensätzen aus Ihren Testdaten. **(2P)**
    * [ ] Progammieren Sie einen Output-Adapter für Ihren Konverter, der die interne Datenstruktur im selbst in Step 1 festgelegten Format in eine Datei schreibt. **(4P)**
  * [ ] **MVP-1**:
    * [ ] Programmieren Sie einen Input-Adapter des Konverters, der Ihre Testdaten einliest und in eine interne Datenstruktur gemäß Ihrer Zwischenrepräsentation umwandelt. **(4P)**
    * [ ] Überprüfen Sie Ihr Programm, ob es die bereinigte Gesamtdatendatei [Format (Step 1)] einlesen und im gleichen Format in eine andere Datei ausgibt.
    * [ ] Kommentieren Sie Ihre Programm kurz, aber aussagekräftig. **(1P)**

<!-- uebung::end -->

---

**_Lösung zu Step 04:_**

---

<!-- uebung::start -->
<span style="color: green;">_Aufgabe_</span> <span style="color:magenta;">**LF11c:Klausurersatzleistung:Step:05**</span>

* [ ] Programmieren Sie in Python einen Konverter, der bereinigten Gesamtdaten [Format (Step 1)] aus einer Datei einliest und in anderen Formate in eine andere Datei ausgibt.
  * [ ] **MVP-2**:
    * [ ] Progammieren Sie einen zweiten Output-Adapter für Ihren Konverter, der die interne Datenstruktur im CSV-Format in eine Datei schreibt. **(1P)**
  * [ ] **MVP-3**:
    * [ ] Progammieren Sie einen dritten Output-Adapter für Ihren Konverter, der die interne Datenstruktur im JSON-Format in eine Datei schreibt. **(4P)**
    * [ ] Modifizieren Sie Ihren Konverter so, dass er seinen Nutzer das Ausgabeformat wählen lässt. **(1P)**
    * [ ] Überprüfen Sie Ihr Programm, ob es die bereinigte Gesamtdatendatei [Format (Step 1)] einlesen und im JSON-Format in eine andere Datei ausgibt.
    * [ ] Kommentieren Sie Ihr Programm kurz, aber aussagekräftig. **(1P)**

<!-- uebung::end -->

---

**_Lösung zu Step 05:_**

---

<!-- uebung::start -->
<span style="color: green;">_Aufgabe_</span> <span style="color:magenta;">**LF11c:Klausurersatzleistung:Step:06**</span>

* [ ] Ergänzen Sie Ihren Konverter um einen Output-Adapter, der die Datenmenge (Anzahl der Bytes) ohne Datenverlust deutlich reduziert.
  * **MVP-4**:
    * [ ] Beschreiben Sie Ihre Verbesserungsideen. **(2P)**
    * [ ] Programmieren Sie dafür exemplarisch einen vierten Output-Adapter. **(2P)**

<!-- uebung::end -->

---

**_Lösung zu Step 06:_**

---

<!-- uebung::start -->
<span style="color: green;">_Aufgabe_</span> <span style="color:magenta;">**LF11c:Klausurersatzleistung:Step:07**</span>

* [ ] Beschreiben Sie, wovon die Daten in `dsp.teta.xyz` handeln, will sagen: welchen Weltausschnitt sie erfassen. (2ZP)
* [ ] Beschreiben Sie eine auffällige Eigenart der beteiligten Person. (2ZP)

<!-- uebung::end -->

---

**_Lösung zu Step 07:_**



