<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### Aspekte der Datenanalyse **[→ ZP:Sheet:3]**

*Zweck von Daten*: Sie sollen

* Weltbeschreibungen liefern.
* zur Weltverbesserung anregen.

Aber: 

* Elektronische RAW-Daten sind nichts als Bits = Bytes = Zahlen
* Sie sagen für sich nichts.
* Sie müssen **syntaktisch** und **semantisch** interpretiert = **aufbereitet** werden.


### Begriffe / Definitionen

* **Interne Daten** :- 
  * entstehen bei der Ausführung / Durchführung firmeneigener Prozesse
  * mit firmeneigenen Systemen (ggfls. auch angemietet (Cloud))
  * mit Komponenten in firmeneigenen Netzen
* **Externe Daten** :- 
  * entstehen durch Fremdfirmenprozesse in firmenfremden Netzen
  * können frei angeboten werden (offizielle Statistiken)
  * können frei = legitim ausgelesen werden (Web-Crawler)
  * können von Fremdanbietern gekauft werden
* **Datenqualität** :-
    * meint die Güte der Daten, mit der sie einen Weltausschnitt abbilden und inwieweit sie weiterverwendet werden können:
    * wird nach gesonderten Kriterien begutachtet
    * **Vollständigkeit** :- 
      * *Erfassen die Daten den Weltausschnitt hinreichend umfassend*?
      * *Sind sie für die Weiterverarbeitung hinreichend komplett*?
    * **Korrektheit** :-
      * *Erfassen die Daten den Weltausschnitt hinreichend genau*?
      * *Ist die Datenerfassung transparent*?
      * *Sind Manipulationen ausgeschlossen*?
      * *Wie wahrscheinlich sind Ablesefehler*?
  
    
*Anmerkung*: Die Kriterien *Vollständigkeit* und *Korrektheit* stammen aus der KI/Mathematik:

* Ein Deduktionsalgorithmus ist vollständig, wenn er alle natürlichen Schlussfolgerung auch aus sich heraus ableitbar macht.
* Ein Deduktionsalgorithmus ist korrekt, wenn all seine auch sich heraus ableitbaren Schlüsse auch natürlich legitime Schlussfolgerungen sind.
* Ein vollständiger und korrekter Deduktionsalgorithmus ist z.B. der, den das Wissensrepräsentationssystem PROLOG verwendet.

*Beispiel:*

* Ein Algorithmus zur Auflistung der Schüler der Klasse 12ip/iv23 ist **korrekt**, wenn er nur Schülerinnen der Klasse 12ip/iv23 ausgibt.
* Ein Algorithmus zur Auflistung der Schüler der Klasse 12ip/iv23 ist **vollständig**, wenn er alle Schülerinnen der Klasse 12ip/iv23 ausgibt.
 
* Wäre er nur *vollständig*, könnte er - außer alle Schülerinnen der Klasse 12ip/iv23 - auch noch die der Klasse 12ia23 ausgeben.
* Wäre er nur *korrekt*, könnte er einige Schülerinnen der Klasse 12ip/iv23 und keine anderen ausgeben, müsste aber nicht alle auflisten. 
  

* **Konsistenz** :- meint Widerspruchsfreiheit
  * *innere Konsistenz* :- die innere Widerspruchsfreiheit der Daten (= die Daten dürfen nicht aussagen, dass 'etwas etwas in derselben Hinsicht zugleich zukommt und nicht zukommt') [Aristoteles]
  * *äußere Konsistenz* : die Daten stehen nicht mit anders gewonnenen Daten im Widerspruch.

*Beispiel*: 

Es gibt aktuell zwei Verfahren, die Gravitationskonstante zu messen. Die Verfahren wären für sich unbrauchbar, wenn sie in sich inkonsistente Messdaten lieferten. Die Daten der Verfahren widersprechen allerdings denen der anderen. Dies führt zwar zu einem Konflikt. Dessen Existenz allein desavouiert aber nicht die Datenqualität.

* **Redundanzfreiheit**
  * meint, dass dieselbe Tatsache in den Daten nicht mehrfach abgebildet/erfasst ist.
  * Problem im Hinblick auf Verarbeitungsaufwand
  * oft gefährdet bei der Zusammenführung (Mergen) von Daten
* **Verfügbarkeit**
  * *Sind die Daten technisch verarbeitbar?*
  * *Sind die Daten rechtlich nutzbar?*
* **Einheitlichkeit**
  * *Ist das syntaktische Format einer Datenmenge gleich?*
  * *Stimmt das syntaktische Format einer Datenmenge mit dem gleicher externer Daten überein?* = Standardkonform?

* **Datenverarbeitungsgrad**
  * **strukturierte Daten** haben festes, zu Bedeutung passendes Format und können auf/mit einer der Datenerfassungsformate repräsentiert werden, nämlich in/mit
    * JSON Dateien :- [https://de.wikipedia.org/wiki/JSON](https://de.wikipedia.org/wiki/JSON)
    * XML Dateien :- [https://de.wikipedia.org/wiki/Extensible_Markup_Language](https://de.wikipedia.org/wiki/Extensible_Markup_Language)
    * CSV Dateien :- [https://de.wikipedia.org/wiki/CSV_(Dateiformat)](https://de.wikipedia.org/wiki/CSV_(Dateiformat))
    * INI-Dateien (Schlüssel-Wert-Paare) :- [https://en.wikipedia.org/wiki/INI_file](https://en.wikipedia.org/wiki/INI_file)
    * YAML-Dateien :- [https://de.wikipedia.org/wiki/YAML](https://de.wikipedia.org/wiki/YAML)
    * → [protico.lessons](https://github.com/pro-tirone-computatri/protico.lessons/tree/main/download/lf.cx): lf.cx.Datafiles)
  * **semi-strukturierte Daten** haben Format, das die Bedeutung nicht vollständig repräsentiert [Bilder etc.]
  * **unstrukturierte Daten** = Sammlungen von Daten mit unterschiedlichen Formaten und unterschiedlicher Bedeutung.

*Vorwegnahme*:

In sehr großen Datenmengen machen obige Begriffe keinen Sinn mehr, weil das, worauf sie zielen, nicht mehr überprüfbar oder prozessual / technisch generierbar ist. Trotzdem sollen auch aus solchen Quellen Aussagen gewonnen werden. Dazu gibt es den **Cross Industry Standard Process for Data Mining** (= *CRISP-DM*):

* die Datengewinnung = das Geschäft verstehen
* Auswahl und Analyse der Daten, Bewertung im Hinblick auf Adäquatheit des zu erfassenden Geschäftsausschnittes
* (syntaktische) Datenaufbereitung
* Auswahl von Data-Mining-Methoden, Erstellung der Modellierung
* Evaluierung (exemplarischer Vergleich mit Weltausschnitten)
* Bereitstellung der Ergebnisse für eine Geschäftsverbesserung

### Sprung in die konkrete Datenanalyse **[→ ZP:Sheet:3]**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11C:Datenanalyse:01**</span>

* [ ] Laden Sie sich die Datei `dsp.alpha.xyz` herunter.
* [ ] Untersuchen Sie die darin enthaltenen Daten - notfalls mit einem HEX-Editor Ihrer Wahl.
* [ ] Stellen Sie eine Hypothese darüber auf, worum es bei diesen Daten geht.

<!-- uebung::end -->

---

*Lösung*: Blutdruckmessungen **[→ ZP:Sheet:4]**

Oder wie Mustafa sagte: "Ahh, der Herr Reincke hat Bluthochdruck".

### Phasen der Datenanalyse **[→ ZP:Sheet:5]**

Analyse von Daten folgt immer dem Schema:

1. **Strukturelle Aufbereitung**:
   1. *Datenanalyse auf Bytelayer*: Was befindet sich tatsächlich auf der Platte, dem Stick etc. (**HEX-Editor**)
   2. *Dateninterpretation auf Bytelayer*: Welche Bytes gehören zusammen und bilden welche Datentypen.
   3. *Datensatzanalyse auf Bytelayer*: Welche Bytes bilden zusammen einen Datensatz und was ist das typische Format der Elemente eines Datensatzes?
   4. *Syntaktische Datenbereinigung*: Können abweichende Formate in einzelnen Elementen an die typische Struktur angeglichen werden?
   5. *Datenkonverter*: Welcher Konverter kann die Daten in eines der Standardaustauschformate umformen? Wie programmiert man ihn am besten.
2. **Semantische Aufbereitung**:
   1. *Datenvisualisierung*: Welches Diagramm / Grafikformat präsentiert die Daten angemessen?
   2. *Datenevaluierung*: Was sollen die Daten erfassen? Gibt es Widersprüche? Dubletten? Inkonsistenzen?
   3. *Datenkorrektur*: Welche Abweichler beruhen wahrscheinlich auf Mess- oder Erfassungsfehlern? Was kann bereinigt werden?
   4. *Datenanalyse auf Inhaltsebene*: Was kann über das Verhalten der Daten gesagt werden?
   5. *Trendvisualisierung*: Tendenzen, Verhalten, Aussagen präsentabel machen?

*Anmerkung*:

* Ohne syntaktisch bereinigte Daten muss die semantische Aufbereitung scheitern.
* Ohne Konverter (digital bearbeitbare Daten), können keine Trends berechnet werden.
* Ohne semantische bereinigte Daten werden Aussagen zu Trends etc. verfälscht.


### Konverterarchitektur **[→ ZP:Sheet:6]**

Ein **Konverter**

* liest Daten aus einer Datei (bzw. von Stdin) ein,
* speichert sie in einer Zwischenrepräsentation uund
* schreibt sie im Zielformat in eine Datei (bzw. nach Stdout).
  
* kann Daten Datensatzweise einlesen, in ZRP-Form erfassen und sofort konvertieren.
  * *Vorteil*: auf große Datenmengen anwendbar
  * *Nachteil*: kontextsensitive Modifikationen i.d.R. nicht anwendbar
* kann Daten insgesamt einlesen, in ZRP-Form erfassen und dann durchgehend konvertieren.
  * *Vorteil*: kontextsensitive Modifikationen gut anwendbar 
  * *Nachteil*: Daten müssen insgesamt (oder in sehr großen Happen) 'in-memory' gehalten werden.

* verwendet eine Adapterarchitektur:
  * Jedes Inputformat hat einen Input-Adapter.
  * Verschiedene Input-Adapter lesen verschiedene syntaktische Formate in dieselbe ZRP ein.
  * Jedes Outputformat bekommt einen spezifischen Output-Adapter.

Beim **Konverterbau** nutzen wir günstigenfalls eine MVP-Strategie:

**MVP** = *Minimal Viable Product* 

> "[...] wörtlich ein 'minimal brauchbares oder existenzfähiges Produkt', ist die erste minimal funktionsfähige Iteration eines Produkts, die dazu dient, möglichst schnell aus Nutzerfeedback zu lernen und so Fehlentwicklungen an den Anforderungen der Nutzer vorbei zu verhindern."
> 
> (vgl. [https://de.wikipedia.org/wiki/Minimum_Viable_Product](https://de.wikipedia.org/wiki/Minimum_Viable_Product))

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11C:Datenanalyse:02**</span>

Was wäre das MVP für einen Konverter für gegebene Inputdaten im Format IF und gewünschten Outputformat OF? 

* [ ] Skizzieren Sie Ihre Möglichkeiten.
* [ ] Wählen Sie Ihre bevorzugte Variante und begründen Sie ihre Wahl

<!-- uebung::end -->

---

*Lösung*: Verschiedene Ansätze sind denkbar:

* ZPR mit INCODE-Daten + Outpout-Adapter (im selben Format wie Input Daten)
* Input-Adapter + ZPR + Outpout-Adapter
* Inpuit-Adapter allein
* ...

Das bester ZPR nimmt die wesentlichsten Merkmale der Ziellösung in Angriff und ist zugleich so kleine wie möglich,

Deshlab gibt es in diesem Fall ein von der Sache her geradezu zwingendes Verfahren:

**Konverter MVP.0**:

* [ ] Sichern Sie die Originaldaten. Entwickeln Sie Ihren Konverter nur auf Datenkopien.
* [ ] Spalten Sie einen kleinen, aber hinreichend großen Satz an Testdaten ab, der die tatsächliche strukturelle und semantische Komplexität repräsentiert.
* [ ] Spalten Sie von den Testdaten 3 möglichst komplexe Referenzdatensätze ab. (Nötigenfalls erhöhen Sie deren Komplexität)
* [ ] Entscheiden Sie sich für Ihre Zwischenrepräsentation und dokumentieren Sie sie.
* [ ] Erfassen Sie ihre Referenzdaten als In-Memory-Daten in Ihrem Konverterprogramm
* [ ] Programmieren Sie einen Output-Adapter, der Ihre In-Memory-Referenz-Daten in dem vorgegebenen Inputformat in eine Datei ausgibt.

**Konverter MVP.1**

* [ ] Erweitern Sie *MVP.0* um einen Input-Adapter, der Ihre Testdaten in die ZPR einliest.


**Konverter MVP.2**:

* [ ] Erweitern Sie *MVP.1* um einen Output-Adapter, der Ihre In-Memory-Referenz-Daten im Zielformat in eine Datei ausgibt.

usw. usw.


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11C:Datenanalyse:01**</span>

* [ ] Laden Sie sich die Datei `dsp.beta.xyz` herunter.
* [ ] Durchlaufen Sie mit diesen Daten die Schritte 1-5 der strukturellen Aufbereitung:
  * [ ] Finden Sie die Ordnung in den Dateien
  * [ ] Modifizieren Sie die Daten in der Datei syntaktisch so, dass sie diese Ordnung widerspiegeln, ohne die Aussage zu ändern.
  * [ ] Berichtigen Sie die Daten wo nötig syntaktisch.
  * [ ] Berichtigen Sie die Daten wo nötig auch semantisch.
* [ ] Programmieren Sie in Python einen Konverter, der diese Daten im INI-Format ausgibt:
  * [ ] Gehen Sie dabei gemäß MVP-Strategie vor.

Hinweis:

* Nutzen Sie für die Programmierung als Inspirationsquellen gerne

* lf.cx/cx.datafiles*
* lf.cx/cx.py2fr*
* lf.cx/cx.py2go*

<!-- uebung::end -->

---


