<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 0.) Context

* Themen seitens des Rahmenlehrplans **[→ ZP:Sheet:2]**
* Topic-Checkliste für 11c / Anfang 2. Halbjahr
* Topic-Checkliste für 11d / Anfang 2. Halbjahr

Wer ist 'voraus'?

### 1.) Zeithorizont **[→ ZP:Sheet:3]**

* Wochenliste im Überblick
* Constraint: 'AP2-Termin'
* Constraint: 'Zensurfestlegung'

→ 5 Wochen à 3 Tage à 4 Doppelstunden

**Gordischer Knoten der Anforderungen**: **[→ ZP:Sheet:4]**

### 2.) Verfahren **[→ ZP:Sheet:5]**

* 5 Wochensprints a je 3 Tagen mit je 4 Doppelstunden.
* Sprint-Planning (45min.) am 1. Tag des Sprints
* Daily (15.min) morgens am 2. und 3. Tag
* Sprint-Review (25min.) am Ende 3. Tag
* Sprint-Retro (20min.) am Ende 3. Tag

* gelegentlich 'Zwischensprints' zwecks konzeptioneller Klärung als Vorarbeit für die Verfeinerung des Product-Backlogs


* Digitale Vernetzer: Aufbau des Systems incl. Sensorik und Datenhaltung
* Daten- u. Prozessanalytiker: automatisierte Auswertung der Daten inkl. Codeimplementierung und Darstellung
* 
### 3.) Scopestatement **[→ ZP:Sheet:6]**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF12cd:Mikroklima:01**</span>

Bitte bauen Sie ein Mikroklima-Reportsystem:

* Im Lehrerzimmer, in 2 Klassenräumen und im Flur sollen Temperatur, Luftfeuchtigkeit und Luftdruck gemessen werden.
* Die erhobenen Daten sollen auf einem 'Data-Aggregator' gesammelt und strukturiert gehalten werden.
* Für den 'Data-Aggregator' soll eine Datensicherung eingeplant sein.
* Der 'Data-Aggregator' soll Daten auf Anfrage an einen 'Data-Evaluator' liefern können.
* Der 'Data-Aggregator' soll Aussagen über die Datenlage ableiten, z.B. (aber nicht nur): 
  * Was ist Minimum, was Maximum, wo liegt der Median. 
  * Wie hängen Luftfeuchtigkeit und Temperatur zusammen? 
  * Gibt es einen Zusammenhang zwischen Schüleranwesenheit?
  * Ist ein Lüftungskonzept zu erkennen? Sinkt die Temperatur in den Pausen?
  * Gibt es eine schulweite Nachtabsenkung?
  * ...
* Der 'Data-Aggregator' soll Übersichten an optische und textuelle Clients liefern.

Bitte realisieren Sie das Projekt so, dass Vorgehen und Resultate es auf der 175 Jahr-Feier gezeigt werden können.

<!-- uebung::end -->

---

### 4.) Product-/Sprintbacklog **[→ einzelne Docs]**

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF12cd:Mikroklima:02**</span>

#### Sprint A
Durchstichsvariante

* [ ] Schätzen Sie die zur Durchstichsvariante gehörenden Storys (Planning Poker)
* [ ] Schätzen Sie Ihre Sprintkapazität in Storypoints
* [ ] Füllen Sie Sprintbacklog-A mit entsprechend vielen Storys.
* [ ] Setzen Sie das Sprintbacklog-A um.

<!-- uebung::end -->

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF12cd:Mikroklima:03**</span>

#### Sprint B Zwischensprint
Systemarchitektur

* [ ] Beantworten Sie in einem Tag (4 Stunden) die Systemarchitektur gehörenden Fragen
* [ ] Entscheiden Sie sich bei offenen Punkten für eine Lösung.
* [ ] Dokumentieren Sie Ihre Entscheidungen in/mit einer Systemarchitektur.

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:7]**

* Die Mikrokontroler / Sensoren übertragen Daten per MQTT an MQTT-Broker. (Unvermittelte Direktverbindung zum MQTT-Broker).
  * MQTT-Broker lauscht ohne TLS/SSL aus Standardport 1883 (nicht: 8883)
* Der Daten-Aggregator bezieht als Subscriber alle erhobenen Daten vom MQTT-Broker. (Entkoppelung von Datenerhebung und Datensicherung).
* Die empfangenen Daten werden in Ordnern des Daten-Aggregators persistent gehalten.
  * Nachfragen:
    * [ ] Woraus besteht ein Datensatz / eine Datenmessung? 
    * [ ] Sind die zu einem Typ erhobenen voneinander unabhängig?
    * [ ] Werden die Daten eines Typus nacheinander in einer Datei gespeichert? Zeilenbasiert? Mit Format MESSDATUM | MESSWERT?
    * [ ] Gibt es für jedes erhobene Datum eine Datei (mit Format MESSDATUM | MESSWERT)?
    * [ ] Ist sichergestellt, dass die Anzahl der während der Messperiode erstellten Dateien die Zahl der vom Filesystem maximal zulässigen nicht überschreiten?
    * [ ] Ist sichergestellt, dass die Gesamtgröße der während der Messperiode erhobenen Dateien den vorhanden Plattenplatz nicht übersteigen?
* Der Daten-Aggregator erhält als Auslieferungskomponente einen NGINX HTTP-Server.
  * Aggregator-NGINX lauscht ohne TLS/SSL auf Standardport 80 (nicht 443)
* Die Datenauslieferung wird als Rest-API gestaltet.
* Die Daten erfragenden Evaluatoren können in der Anfrage mitgeben, welchen Daten aus welchem Zeitraum und welchen Typs sie benötigen.
* Die Evaluatoren (HTTP-Clients) sollen Frageparameter in HTTP(GET)- und HTTP(POST)-Anfragen mitgeben können.
* Die Evaluatoren erfragen und erhalten nur die zur Berechnung benötigten Daten, und löschen die geholten Daten danach wieder.
* Die Evaluatoren stellen ihre Ergebnisse selbst als HTTP-Server zur Verfügung.
* Die Evaluatoren sind im Kern Skripte (CGI/Python-Module)?
* Evaluator-NGINX lauscht ohne TLS/SSL auf Standardport 80 (nicht 443).
  * Nachfragen:
    * [ ] Stellt NGINX ein Pythonmodul zur Verfügung?
    * [ ] Stellt NGINX ein CGI-modul zur Verfügung?
    * [ ] Wenn nicht: Wäre es sinnvoll an den zwei Web-Server-Postion einmal NGINX und einmal Apache zu nutzen?
* Die Daten werden mit einer Weboberfläche präsentiert.
* Die Evaluationen werden i.d.R. fest vorberechnet. 
* Einige Berechnungen sollen adhoc in der Weboberfläche parametrisiert (INPUT) und 'on-the-fly' berechnet werden.
* Die Evaluatoren arbeiten als Skripte (CGI/python-Module)?



---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF12cd:Mikroklima:04**</span>

#### Sprint C
Implementierung I

* [ ] 
* [ ] 
* [ ] 

<!-- uebung::end -->

Lösung:

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF12cd:Mikroklima:05**</span>

#### Sprint D
Implementierung II

* [ ] 
* [ ] 
* [ ] 

<!-- uebung::end -->

Lösung:

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF12cd:Mikroklima:06**</span>

#### Sprint E
Systemtest

* [ ] 
* [ ] 
* [ ] 

<!-- uebung::end -->

Lösung:

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF12cd:Mikroklima:07**</span>

#### Sprint F
Datenerhebung und Auswertung

* [ ] 
* [ ] 
* [ ] 

<!-- uebung::end -->

---

### 6) Projektabschluss




