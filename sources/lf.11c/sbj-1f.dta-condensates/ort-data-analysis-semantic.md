<!-- LTeX:Language=de-DE -->

### Data Analysis (Semantik) 

#### A
Begriffe / Definitionen

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
  

* **Konsistenz** :- meint Widerspruchsfreiheit
  * *innere Konsistenz* :- die innere Widerspruchsfreiheit der Daten (= die Daten dürfen nicht aussagen, dass 'etwas etwas in derselben Hinsicht  zugleich zukommt und nicht zukommt') [Aristoteles]
  * *äußere Konsistenz* : die Daten stehen nicht mit anders gewonnenen Daten im Widerspruch.

*Beispiel*: Es gibt aktuell zwei Verfahren, die Gravitationskonstante zu messen. Die Verfahren wären für sich unbrauchbar, wenn sie in sich inkonsistente Messdaten lieferten. Die Daten der Verfahren widersprechen allerdings denen der anderen. Dies führt zwar zu einem Konflikt. Dessen Existenz allein desavouiert aber nicht die Datenqualität.

* **Redundanzfreiheit**
  * meint, dass dieselbe Tatsache in den Daten nicht mehrfach abgebildet/erfasst ist.
  * Problem im Hinblick auf Verarbeitungsaufwand
  * oft gefährdet bei der Zusammenführung (Mergen) von Daten
* **Verfügbarkeit**
  * *Sind die Daten technisch verarbeitbar?*
  * *Sind die Daten rechtlich nutzbar?*
* **Einheitlichkeit**
  * *Ist das syntaktische Format einer Datenmenge gleich?*
  * *Stimmt  syntaktische Format einer Datenmenge mit dem gleicher externer Daten überein?* = Standardkonform?

* **Datenverarbeitungsgrad**
  * **strukturierte Daten** haben festes, zu Bedeutung passendes Format und können auf/mit einer der Datenerfassungsformate repräsentiert werden, nämlich in/mit
    * JSON Dateien :- [https://de.wikipedia.org/wiki/JSON](https://de.wikipedia.org/wiki/JSON)
    * XML Dateien :- [https://de.wikipedia.org/wiki/Extensible_Markup_Language](https://de.wikipedia.org/wiki/Extensible_Markup_Language)
    * CSV Dateien :- [https://de.wikipedia.org/wiki/CSV_(Dateiformat)](https://de.wikipedia.org/wiki/CSV_(Dateiformat))
    * INI-Dateien (Schlüssel-Wert-Paare) :- [https://en.wikipedia.org/wiki/INI_file](https://en.wikipedia.org/wiki/INI_file)
    * YAML-Dateien :- [https://de.wikipedia.org/wiki/YAML](https://de.wikipedia.org/wiki/YAML)
  * **semi-strukturierte Daten** haben Format, das die Bedeutung nicht vollständig repräsentiert [Bilder etc.]
  * **unstrukturierte Daten** = Sammlungen von Daten mit unterschiedlichen Formaten und unterschiedlicher Bedeutung.

Anmerkung:

In sehr großen Datenmengen machen obige Begriffe keinen Sinn mehr, weil das, worauf sie zielen, nicht mehr überprüfbar oder prozessual / technisch generierbar ist. Trotzdem sollen auch aus solchen Quellen Aussagen gewonnen werden. Dazu gibt es den **Cross Industry Standard Process for Data Mining** (= *CRISP-DM*):

* die Datengewinnung = das Geschäft verstehen
* Auswahl und Analyse der Daten, Bewertung im Hinblick auf Adäquatheit des zu erfassenden Geschäftsausschnittes
* (syntaktische) Datenaufbereitung
* Auswahl von Data-Mining-Methoden, Erstellung der Modellierung
* Evaluierung (exemplarischer Vergleich mit Weltausschnitten)
* Bereitstellung der Ergebnisse für ein Geschäftsverbesserung

#### B
(semantische) Methoden der Datenanalyse

* **Visualisierung** = grafische Aufbereitung zur Ableitung von Erkenntnissen über die Datenqualität mittels
  * **Linien- und Flächendiagramme** :- zur Darstellung des Werteverlaufs über die Zeit
  * **Balkendiagramme** :- konfrontative Darstellung von erreichten Werten pro Werteträger (= Wahlergebnisse)
  * **Tortendiagramme** : Darstellung von Anteilen an einer Gesamtanzahl
  * **Streudiagramm** : Verteilung von zweidimensionalen Messungen zweck Einteilung in Gruppen
  * **Blasendiagramm** : Verteilung von dreidimensionalen Messungen
  * **Wortwolken** : assoziative Begriffsdarstellung mit Gewichtung per Größe.

* **Statistische Analyse**
  * **Beispielbasis**: 
  * SYST :- | `[ 182, 158, 179, 170]` | sort(SYST) :- `[ 158, 170, 179, 182 ]`
  * PULS :- `[ 66, 75, 67, 78]` | sort(PULS) :- `[ 66, 67, 75, 78]`
 
  * **Minimum** = kleinster Wert einer Datenreihe = `min(SYST)= sort(SYST)[0] = 158`
  * **Maximum** = größter Wert einer Datenreihe = `max(SYST)= sort(SYST)[3] = 182`
  * **Spannweite** = Maximum - Minimum = `max(SYST)-min(SYST) = 182-158 = 34`
  * **Mittelwert**
    * addiere alle Werte und Teile die Summe durch die Anzahl der addierten Werte
    * *aussagekräftig* für gleichmäßig verteilten Werte
    * SYST
      * `SUM(SYST)/sizeof(SYST) = (158+170+179+182)/4`
      * = `689/4 = 172,25 ~= 172`
    * PULS
      * `SUM(PULS)/sizeof(PULS) = (66+75+67+78)/4` 
      * =`268/4 = 71,5 ~= 72`
  
  * **Median**
    * sortiere alle Werte und wähle den Wert, sodass gleich viel Werte oberhalb und unterhalb liegen. (*Bei einer ungeraden Anzahl von Messungen ist der Wert, der genau in der Mitte der Liste liegt. Bei einer gerade Anzahl der Messungen ist es der Mittelwert der beiden Werte, die die Mitte der Liste bilden.*)
    * Ausreißer fallen nicht so ins Gewicht [Problem der Gehaltsanpassung]
    * SYST
      * `average(midpair(sort(SYST))) = average(170,179)` 
      * = `(170+179) / 2` = 174,5
 
  * **Varianz**
    * gibt die durchschnittliche Abweichung vom Mittelwert an
    * Berechnung:
      * subtrahiere von jedem Wert einer Datenreihe den Mittelwert und quadriere das Ergebnis.
      * addiere die so berechneten Werte und teile sie durch die Anzahl 
      * SYST:
        * `( (158-172)^2 + (170-172)^2 + `
          * \+ `(179-172)^2 + (182-172)^2 ) / 4`
        * = `( -14^2 + -2^2 + 7^2 + 10^2 ) / 4` 
        * = `(196 + 4 + 49 + 100) / 4` = `349 / 4` = `87,25` ~= **87**
      * PULS:
        * `( (66-72)^2 + (75-72)^2) + `
           * \+ ` (67-72)^2) + (78-72)^2 ) / 4`
        * = `( -6^2 + 3^2 + -5^2 + 6^2 ) / 4`
        * = `( 36 + 9 + 25 + 36 ) / 4` = `106 / 4` = `26,5` ~= **27**
  
  * **Standardabweichung**
    * alternative Form der durchschnittlichen Abweichung vom Mittelwert =(das Quadrat wird wieder 'rausgerechnet)
    * wird wegen Ähnlichkeit zu den 'gemessenen' Werten oft bevorzugt
    * **je kleiner Standardabweichung, desto kleiner Abweichung vom Mittelwert im Durchschnitt** *= desto 'gleichförmiger' die Messungen*
    * Berechnung:
      * bilde zweite Wurzel aus der Varianz
      * `sqrt(87)` ~= *9,32* 
      * `sqrt(27)` ~= *5,2*
 
  * **Kovarianz** nach [https://www.scribbr.de/statistik/kovarianz/](https://www.scribbr.de/statistik/kovarianz/) 
    * "gibt Auskunft über den Zusammenhang von zwei metrischen Variablen".
    *  ist "ein nichtstandardisiertes Zusammenhangsmaß ist und damit nur begrenzt vergleichbar."
    *  "Ein positiver Wert der Kovarianz sagt dir, dass wenn die eine Variable steigt, dies auch für die andere der Fall ist. Gleichermaßen zeigt ein negatives Vorzeichen, dass wenn die eine Variable steigt, die andere sinkt."
    * Berechnung:
      * Bestimme das arithmetische Mittel jeder Wertereihe.
      * Subtrahiere von jedem Wert einer jeden Wertereihe das jeweilige arithmetische Mittel
      * multipliziere die so gewonnenen Ergebnisse paarweise
      * Addiere die so gewonnenen Werte 
      * Dividiere den so gewonnenen Wert duch die Anzahl (4) - 1

    | SYST | PULS | SYST-am(SYST) | PULS-am(PULS) | ... |
    |---|---|---|---|---|
    | | | | | (SYST-am(SYST)) *
    | | | | | * (PULS-am(PULS)) 
    | 182 | 66 | 182 - 172 = 10 | 66 - 71 = -5 | - 50 |
    | 158 | 75 | 158 - 172 = -14 | 75 - 71 = 3 | - 42 |
    | 179 | 67 | 178 - 172 = 6 | 67 - 71 = -4 | - 24 |
    | 170 | 78 | 170 - 172 = - 2| 78 - 71 = -7 | 14 |
    | | | | | = -112 / 4 = **-28**

    am(SYST) ~= 172, am(PULS) ~= 71

  * **Korrelationskoeffizient** nach [https://www.scribbr.de/statistik/kovarianz/](https://www.scribbr.de/statistik/kovarianz/) 
    * "gibt die standardisierte Kovarianz an" :- normiert das Ergebnis auf einen Bereich zwischen -1 und +1;
      * ~0 : es gibt keinen Zusammenhang
      * \>0 : Je größer die Kovarianz, desto größer die Wahrscheinlichkeit, dass der zweite Wert auch steigt, wenn der erste Wert steigt .
      * <0 : Je kleiner die Kovarianz, desto **größer!** die Wahrscheinlichkeit, dass der zweite Wert auch steigt, wenn der erste Wert sinkt
    * Berechnung
      * Berechne die Standardabweichungen zweier Datenspalten einer Datenmessung 
        * SYST: *9,32*
        * PULS: *5,2*
      * Berechne die Kovarianz bezogen auf diese Datenspalten: *-112*
      * Dividiere die Kovarianz durch das Produkt beider Standardabweichungen 
      * `-28/(9,32*5,2)` = `-28/4846` ~= **`-0,57`**


  * **Entropie**
    * meint in der Physik (Thermodynamik) den ohne Hinzufügen äußerer Energue irreversiblen Prozess des Ausgleiches von Temperaturunterschieden = Geschwindigkeiten der Partikel.
    * gibt in der Informatik den Grad des Informationsgehaltes einer Messung an: je unwahrscheinlicher ein Ereignis (der Wert einer Messung) p(x), desto höher der Informationsgehalt h(x) = sie sind umgekehrt proportional zu einander :- `h(x) = -log(p(x))`
    * Die Shannon Entropie gibt den Informationsgehalt einer Zufallsvariable X  (einer Menge von Symbolen aus einem Alphabet) mit k Zuständen an :- `H(x) = -H(x) = - SUM(ki * log(p(ki)))`
    * *Beispiel*:
    * Gesetzt, wir haben ein Alphabet von 4 Buchstaben 'A, B, C, D'
     * Gesetzt, in unserer Sprache über dem Alphabet kommt in der Gesamtheit aller Wörter der Buchstabe *A* doppelt so häufig wie *B* und *B* doppelt so häufig wie *C* und *D*.
    * Da die Wahrscheinlichkeit der verwendeten Buchstaben zusammen 1 ergeben muss (es erscheint an jeder Stelle einer der Buchstaben 'A oder B oder C oder D'), ergibt sich `p('A') = 0,5`, `p('B') = 0,25`, `p('C') = 0,125` `p('D') = 0,125`
    * Bezogen auf dieses Alphabet und diese Sprache haben die Buchstaben für sich genommen jeweils einen Informationsgehalt von 
    * `h('A') = -(log(p('A'))) = -(log(0,5)) ~= -(-0,30) =~ 0,3`
    * `h('B') = -(log(p('B'))) = -(log(0,25)) ~= -(-0,60) =~ 0,6`
    * `h('C') = -(log(p('C'))) = -(log(0,125)) ~= -(-0,90) =~ 0,9`
    * Bezogen auf dieses Alphabet und diese Sprache hat
    *  das Wort 'ABBA' einen (statischen) Informationsgehalt von `h('A') + h('B') + h('B') + h('A') = 0,3 + 0,6 + 0,6 + 0,3 = 1,8`
    * das Wort 'ACDC' einen (statistischen) Informationsgehalt von `h('A') + h('C') + h('D') + h('C') = 0,3 + 0,9 + 0,9 + 0,9 = 3,0`

* [https://www.studienkreis.de/mathematik/varianz-standardabweichung/](https://www.studienkreis.de/mathematik/varianz-standardabweichung/)
* [https://de.wikipedia.org/wiki/Entropie_(Informationstheorie)](https://de.wikipedia.org/wiki/Entropie_(Informationstheorie))


**Defects per Million Opportunities** (*DPMO*)
  * gibt an, wie viel falsche (falsch erfasste, repräsentierte, ...) Daten pro 1 Millionen Möglichkeiten
  
    *DPMO represents the number of defects that could occur per million opportunities in any given process, thus providing a standardized measure for evaluating process performance and quality across different industries and scales of operation.* vgl. [https://www.sixsigmaonline.org/defects-per-million-opportunities-dpmo-six-sigma](https://www.sixsigmaonline.org/defects-per-million-opportunities-dpmo-six-sigma)

  * wird berechnet aus:
    * Anzahl der gemessenen Fehler = D
    * Anzahl der produzierten / verglichenen Einheiten (units) = N
    * Anzahl der *möglichen* Fehler pro produzierter / verglichener Einheit = O(opportunities)
    * Formel **`DPMO=(D/(N*O))×1,000,000`**
  * wird praktisch ermittelt durch
    * definiere, was als produzierten / verglichene Einheit gilt
    * definiere die relevanten Fehlermöglichkeiten 
    * zählen
    * vgl. [https://six-sigma-deutschland.de/defects-per-million-opportunities-dpmo/](https://six-sigma-deutschland.de/defects-per-million-opportunities-dpmo/)
**Six Sigma** (*6S*)
  * meint Qualität eines Prozesses
  * ist definiert als 3.4 defects per million


**Hinweis:** DPMO und 6Sigma sagt etwas über den Datenerhebungsprozess aus.

#### C
Methoden der Datenaufbereitung

* **Codierung** :- nicht computererfasste Daten werden digitalisiert = in einem Zahlenmodell repräsentiert 
* **Vereinheitlichung** :- Daten aus unterschiedlichen Quellen werden in dasselbe Format gebracht
  * *syntaktisch* = Systole und Diastole werden einheitlich als Paar <Sys/Dia> erfasst
  * *semantisch* = Tempreaturwerte werden als Celsius-Werte dargestellt 
* **Reduzierung** = Entfernung von Kontext bedingt irrelevanten Aspekten
  * *syntaktisch* = Abbildung von Texten auf Hashwerte bei Unterschiedsvergleichen
  * *semantisch* = Entfernung von Farbwerten aus Buchstabenbildern
* **Konvertierung** = Überführung in ein anderes, 'besser verarbeitbares' Format 
* **Klassifizierung** = Einteilung in Klassen, Bildung von Generalisierungen


**Unterscheidung**

* **Rohdaten** - Daten, wie erfasst
* **Analysedaten** - aufbereitete Daten nach Fehlerbereinigung
* **Data Lake** - Repository mit Rohdaten

**Überschneidung**

* *ACID* ist eine 'Technik' bei Datenbankmanagementsystemen: Eine Folge von Datenbank-Operationen (= Transaktion) wird so genannt, wenn diese Folge 
  * **atomar** ist = ganz ausgeführt wird oder gar nicht [= gibt es bei einem Schritt einen Fehler, kommt es zum Rollback '->' *Andere Zugriffe auf die Daten sehen nur den Ausgangsstatus oder den zu erreichenden Endtstatus, nicht aber die möglicherweise invaliden Zwischenstände*]
  * **consistent** ist = eine durchgeführte Transaktion hinterlässt einen konsistenten Datenbankzustand, sofern die Datenbank davor auch konsistent war
  * **isoliert** ist = Zwischenzustände während der Transaktion werden anderen Zugriffen gegenüber versteckt = isoliert
  * **dauerhaft** ist = der Endzustand wird sicher in der Datenbank gespeichert.

(vgl. [https://de.wikipedia.org/wiki/ACID][https://de.wikipedia.org/wiki/ACID])
