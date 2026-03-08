<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

---

### 4.) Produktbacklog

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
* [ ] { } **Systemarchitektur erstellen**
    * [ ] Übertragung (Protokoll, Port, Software) von Sensor zur Data-Aggregatur konzipiert/dokumentiert 
    * [ ] Übertragung im Data-Aggregatur zu MQTT-Broker (Protokoll, Port, Software) konzipiert/dokumentiert
    * [ ] Übertragung vom MQTT-Broker zu persistentes Datenhaltungssystem (Protokoll, Port, Software) konzipiert/dokumentiert
    * [ ] Datenstzruktur im Datenhaltungssystem konzipiert/dokumentiert
    * [ ] Übertragung vom Datenhaltungssystem zum Datenevaluator (Protokoll, Port, Software) konzipiert/dokumentiert
    * [ ] Datenevaluator (Software, Rechner) konzipiert/dokumentiert
    * [ ] Übertragung vom Datenevaluator zu Datenpräsentatoren (Protokoll, Port, Software) konzipiert/dokumentiert
    * [ ] Gesamtleitbild ist erstellt.
* { } Data-Aggregator zum MQTT-Broker machen (auf MQTT umstellen) mit (eclipse-mosquitto)
* { } Datenhaltungssystem implementieren und anschließen
* { } Sensorik auf Temperatur und Luftfeuchtigkeit erweitern.
* { } Übertragung zum Data-Aggregator auf Temperatur und Luftfeuchtigkeit erweitern.
* { } Prozess der Datenerhebung designen und dokumentieren in BPMN
* { } Datenevaluation auf Durchschnitt, Median erweitern
* { } Auslieferung an Data-Visualizer auf Durchschnitt, Median erweitern
* { } Berechnungen auf weitere Aussagen erweitern
  * ...
* { } Berechnung der Prozessgüte erweitern  

### 5) Projektabschluss




