<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

---

### Produktbacklog

**Sprint A:**

* [X] **MVP-Teil-A**
  * {2} exemplarische Datenerhebung mit einem Sensor 
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist mit Sensor gemessen
  * {5} Übertragung der Daten an den 'Data-Aggregator'
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Aggregator'-Datenbereich abgelegt
* [X] **MVP-Teil-B**
  * {5} Konzeption des Datenhaltungssystems
    * [X] DoD: Technisches Datenhaltungssystem läuft mit einem Test-Datensatz
  * {3} exemplarische Integration der erhaltenen Daten von **MVP-Teil-A**
    * [X] DoD: Technisches Datenhaltungssystem läuft mit dem Mess-Datensatz
* [X] **MVP-Teil-C**
  * {8} exemplarische Datenlieferung an Daten-Evaluator
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Evaluator'-Datenbereich abgelegt
  * {1} Berechnung eines initialen Markanten (Durchschnitt)
    * [X] DoD: Temperaturdurchschnitt ist automatisiert berechnet.
* [X] **MVP-Teil-D**
  * {13} exemplarischer Abruf eines Ergebnisses in einem Client
    * [X] DoD: Aussage über Messung und Temperaturdurchschnitt kann in einem Client abgerufen werden.
* [X] **MVP (Durchstichsvariante)**
  * {0} 1 Messung automatisiert über die ganze Kette schicken
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist mit Sensor gemessen
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Aggregator'-Datenbereich abgelegt
    * [X] DoD: Technisches Datenhaltungssystem läuft mit dem Mess-Datensatz
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Evaluator'-Datenbereich abgelegt
    * [X] DoD: Temperaturdurchschnitt ist automatisiert berechnet.
    * [X] DoD: Aussage über Messung und Temperaturdurchschnitt kann in einem Client abgerufen werden.

---

**Sprint B (Zwischensprint)**

* [X] **Systemarchitektur erstellen**
    * [X] Übertragung (Protokoll, Port, Software) von Sensor zur Data-Aggregatur konzipiert/dokumentiert 
    * [X] Übertragung im Data-Aggregatur zu MQTT-Broker (Protokoll, Port, Software) konzipiert/dokumentiert
    * [X] Übertragung vom MQTT-Broker zu persistentes Datenhaltungssystem (Protokoll, Port, Software) konzipiert/dokumentiert
    * [X] Datensatzstuktur im Datenhaltungssystem konzipiert/dokumentiert
    * [X] Übertragung vom Datenhaltungssystem zum Datenevaluator (Protokoll, Port, Software) konzipiert/dokumentiert
    * [X] Datenevaluator (Software, Rechner) konzipiert/dokumentiert
    * [X] Übertragung vom Datenevaluator zu Datenpräsentatoren (Protokoll, Port, Software) konzipiert/dokumentiert
    * [X] Gesamtleitbild ist erstellt.

---

**Heap**

---

* [ ] MQTT-Broker aktivieren
  * { } MQTT-Broker installieren (eclipse-mosquitto) 
  * * [ ] DoD1: mosquitto ist installiert, Server läuft, 
    * [ ] DoD2: Anlieferung ist per `mosquitto_pub` verifiziert,
    * [ ] DoD3: Auslieferung ist per `mosquitto_sub` verifiziert,
  * { } hinreichend großen Testdatensatz pro Sensortyp erstellen.
    * [ ] DoD1: Für alle Sensorentypen sind 10 Testwerte + Messzeitpunkt definiert.
    * [ ] DoD2: Wenn mit Messreihen gearbeitet wird, sind 10 Testdatensätze definiert.
  * { } Testdatensatz-Publishing simulieren per Skript  mit/für `mosquitto_pub`
    * [ ] DoD: Der Testdatensatz ist per `mosquitto_pub` zum MQTT-Broker übertragen
  * { } Testdatensatz-Subscribing simulieren per Skript mit/für `mosquitto_sub`
    * [ ] DoD: Der Testdatensatz ist per `mosquitto_sub` vom MQTT-Broker abgeholt
  * { } Daten(file)format im Aggregator festlegen
    * [ ] DoD: In einer Spezifikation ist festgelegt, wie die Daten im Aggregator abgelegt werden
  * { } Testdatensatz im Aggregator bei Eintreffen im Daten(file)format ablegen
    * [ ] DoD1: MQTT-Subscription-Client ist in Python programmiert
    * [ ] DoD2: MQTT-Subscription-Client legt die Daten gemäß Spezifikation als Datei(en) ab

---

* [ ] Datenauslieferung aktivieren
  * { } HTTP-Anfrage vom Evaluator an Aggregator designen (Parameter)
    * [ ] DoD: Es ist spezifiziert, was Evaluatoren-Clients als Datenparameter vorgeben können. 
  * { } Aggregator-HTTP-Server installieren (nginx) 
    * [ ] DoD1: `nginx` ist installiert und konfiguriert
    * [ ] DoD2: `nginx` kann auf Datenbereich zugreifen
    * [ ] DoD3: `nginx` liefert Beispieldaten über Browser aus
  * { } Datenzugriffsmodul programmieren
    * [ ] DoD1: Auslieferungsmodul ist programmiert + empfängt Datanausschnittsparameter
    * [ ] DoD2: Auslieferungsmodul stellt Datenausschnitt gemäß Parameter zusammen
    * [ ] DoD3: `nginx` liefert erfragten Datenausschnitt über Browser aus.
  * { } HTTP-Client mit Request und Ablage im Fileformat in Python programmieren
    * [ ] DoD1: HTTP-Client ist in Python programmiert
    * [ ] DoD2: HTTP-Client holt die Datenausschnitte ab
    * [ ] DoD3: gemäß Spezifikation als Datei(en) ab

---

* [ ] Sensorik erweitern
  * { } Sensorik auf Temperatur und Luftfeuchtigkeit erweitern.
    * [ ] DoD: Sensoren für Temperatur, Luftdruck und Luftfeuchtigkeit liefern Daten
  * { } Sensoren testweise aktivieren
    * [ ] DoD: Datensätze für Temperatur, Luftdruck und Luftfeuchtigkeit sind über MQTT-Broker und MQTT-Subscription-Client abgeholt und abgelegt
  * { } Daten(file)format für Aggregator mitbestimmen
    *  [ ] DoD: Daten(file)format ist final spezifiziert

---

* [ ] Datenevaluation aktivieren
  * { } Annahmeformat der Testdaten im/für Evaluator festlegen
    * DoD: In einer Spezifikation ist festgelegt, wie die Daten im Evaluator ankommen und wo sie wie übergangshalber abgelegt werden
  * { } Testdaten im/für Evaluator im Annahmeformat bereitstellen
    * DoD: Testdaten sind wie spezifiziert zur Evaluation abgelegt
  * { } Datenevaluationsmodule in Python designen und programmieren
    * DoD: Framework für ein Evaluationsmodul ist programmiert
    * DoD: Basic-Evaluation 'Datensatzanzahl' ist programmiert
  * { } Grundlegende Auswertungen (Durchschnitt, Median) implementieren
    * Median-Evaluation-Modul ist programmiert
    * Durchschnitt-Evaluation-Modul ist programmiert

---

* { } Regelmäßig Datensicherung im/für Aggregator implementieren.
* { } Prozess der Datenerhebung designen und dokumentieren in BPMN
* { } Datenanalyse auf Bestand gemäß `lf.11c/sbj-04.dta-evaluation` erweitern
* { } Analyse der Prozessgüte auf Bestand gemäß `sbj-02.prc-analysis` erweitern
 





