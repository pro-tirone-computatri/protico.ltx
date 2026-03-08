<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1. Allgemeines 

* **Suchen** meint, ein Element in einer Menge (unsortiert) oder Struktur 
   (sortiert) zu finden (und z.B. seine Position als Erfolgskriterium zurückzugeben):
  * **Lineare Suche**: finde das Suchelement in einer **unsortierten Liste**.
  * **Binäre Suche**: finde das Suchelement in einer **sortierten Liste**.
  * **Breitensuche**: finde das Suchelement in einem **gerichteten azyklischen Graph** (z.B. Baum), in dem jeweils - rekursiv - nach der Evaluation eines Vaterknotens erst der Reihe nach all seine Töchter überprüft werden, bevor es mit den Enkelinnenknoten weitergeht.
  * **Tiefensuche**: finde das Suchelement in einem **gerichteten azyklischen Graph** (z.B. Baum), in dem jeweils - rekursiv - nach der Überprüfung eines Knotens zuerst dessen Töchter überprüft werden, bevor es mit seinen Geschwisterknoten weitergeht.
  * **Wegesuche**: finde das Suchelement in einem (meist: gerichteten azyklischen) **Graph** (kein Baum!) den besten Weg zum Suchelement.
    * **A\*Algorithmus**
    * **Dijkstra's Algorithmus**
    * *weitere*: → [https://en.wikipedia.org/wiki/Pathfinding](https://en.wikipedia.org/wiki/Pathfinding)
* **Sortieren** meint, die richtigen Plätze für die Elemente einer unsortierten 
  Liste zu finden, sie geschickte dort zu platzieren (und die sortierte Menge
  als Erfolgskriterium zurückzugeben):
   * **Insertion Sort** : → [https://en.wikipedia.org/wiki/Insertion_sort](https://en.wikipedia.org/wiki/Insertion_sort)
   * **Selection Sort** : → [https://en.wikipedia.org/wiki/Selection_sort](https://en.wikipedia.org/wiki/Selection_sort)
   * **Bubble Sort** : → [https://en.wikipedia.org/wiki/Bubble_sort](https://en.wikipedia.org/wiki/Bubble_sort)
   * **Merge Sort**: → [https://en.wikipedia.org/wiki/Merge_sort](https://en.wikipedia.org/wiki/Merge_sort)
   * **Quick Sort**: → [https://en.wikipedia.org/wiki/Quicksort](https://en.wikipedia.org/wiki/Quicksort)
   * **Shell Sort**: → [https://en.wikipedia.org/wiki/Shellsort](https://en.wikipedia.org/wiki/Shellsort)
   * **Heap Sort**: → [https://en.wikipedia.org/wiki/Heapsort](https://en.wikipedia.org/wiki/Heapsort)
   * *weitere* : → [https://en.wikipedia.org/wiki/Sorting_algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)

### 2. Algorithmusbewertung

Es gibt 3 gängige Kriterien zum Vergleich der Such- bzw. Sortieralgorithmen untereinander:

* **Geschwindigkeit** (= Laufzeitverhalten), bezogen auf die Anzahl der Elemente (vermerkt in OH-Notation), ausgewiesen in *BestCase*, *Durchschnitt* und *WorstCase*
* **Ressourcenbedarf**: wie viel Memory braucht der Algorithmus zum Ausgangsmaterial
* **Stabilität**: garantiert der Algorithmus, dass die ursprüngliche Reihenfolge erhalten bleibt, sofern die Sortiervorgaben nicht ein Umpositionieren erzwingt? Beispiel bei Sortierung nach Nachnamen: 
  * stabil: `({Anton First},{Dorothea Last},{Bertram First})` => `({Anton First},{Bertram First},{Dorothea Last})`
  * instabil: `({Anton First},{Dorothea Last},{Bertram First})` => `({Bertram First},{Anton First},{Dorothea Last})`

### 3. Übliche Klassifizierung

Eine übliche Gegenüberstellungen sähe etwa so aus:

Agorithmus | Zeit (best case) | Zeit (avg. case) |	Zeit (worst case)	| Platz-bedarf | stabil |
---|---|---|---|---|---|
Insertion Sort	| O(n)	| O(n²)	| O(n²)	| O(1) | Ja
Selection Sort	| O(n²)	| O(n²)	| O(n²)	| O(1) | Nein
Bubble Sort	    | O(n)	| O(n²)	| O(n²)	| O(1) | Ja
Quicksort	      | O(n * log n) | O(n * log n)	| O(n²)	| O(log n) | Nein
Mergesort	      | O(n * log n) | O(n * log n) | O(n * log n) | O(n) | Ja
Heapsort        | O(n * log n) | O(n * log n) | O(n * log n) | O(1)	| Nein

nach 

* → [https://www.happycoders.eu/de/algorithmen/sortieralgorithmen/](https://www.happycoders.eu/de/algorithmen/sortieralgorithmen/)
* → [https://studyflix.de/informatik/sortieralgorithmen-1337](https://studyflix.de/informatik/sortieralgorithmen-1337)

Anmerkung:

Die 'Oh'-Notation besagt, dass bei jedem Fall von allen je konkreten Besonderheiten wie Rechnergeschwindigkeit, Speicherplatz oder Implementierung abstrahiert wird. So bleiben die Aussagen übrig, der Aufwand sei

* konstant: `O(1)`
* linear abhängig von der Anzahl der Elemente `n` 
* quadratisch / polynominal abhängig ist von der Anzahl der Elemente `n^2` 
* exponentiell abhängig von der Anzahl der Elemente `2^n`
* logarithmisch abhängig von der Anzahl der Elemente `n * log(n)`

Die Formeln zeigen:

```
'konstant = nicht abhängig von n' ist weniger als
  'linear abhängig von n' ist weniger als
    'logarithmisch abhängig von n' ist weniger als
      'quadratisch abhängig von n' ist weniger als 
        'exponentiell abhängig von n'
```

vgl. dazu

* → [https://www.happycoders.eu/de/algorithmen/o-notation-zeitkomplexitaet/](https://www.happycoders.eu/de/algorithmen/o-notation-zeitkomplexitaet/)
* → [https://de.wikipedia.org/wiki/Landau-Symbole](https://de.wikipedia.org/wiki/Landau-Symbole)
* → [https://en.wikipedia.org/wiki/Big_O_notation](https://en.wikipedia.org/wiki/Big_O_notation)

### 4. Implementierungen der Such- und Sortieralgorithmen.

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11a:sbj-01.sort-search:00**</span>

* [ ] Laden Sie sich aus Ihrem Downloadbereiche den Ordner `sbj-01.sort-search-snp.sose` herunter

---

Darin finden Sie Dateipaare nach dem Muster `sose-XYZ.py` und `sose-XYZ.sol.py`:

* Erstere enthält die Beschreibung der Aufgabe plus Hintergrundinformationen und Anregungen zur Implementierung.
* Letztere enthält darüber hinaus eine ablauffähige eine Lösung in Python. (`python3 sose-XYZ.sol.py` oder Aufruf von VisualStudioCode aus)


#### 4.A.
Suchalgorithmen

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11a:sbj-01.sort-search:01**</span>

* Lösen Sie die Aufgaben
  * [ ] `sose-00-sequential-search.py`, 
  * [ ] `sose-01-binary-search-iterative.py` 
  * [ ] `sose-01-binary-search-recursive.py`
* [ ] Vergleichen Sie Ihre Lösungen danach mit denen in den Dateien 
  * [ ] `sose-00-sequential-search.sol.py`, 
  * [ ] `sose-01-binary-search-iterative.sol.py` und 
  * [ ] `sose-01-binary-search-recursive.sol.py`

<!-- uebung::end -->

---

#### 4.B.
Einfache Sortieralgorithmen

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11a:sbj-01.sort-search:02**</span>

* Lösen Sie die Aufgaben
  * [ ] `sose-02-insertion-sort.py`, 
  * [ ] `sose-03-selection-sort.py`, 
  * [ ] `sose-04-bubble-sort.py`, 
* [ ] Vergleichen Sie Ihre Lösungen danach mit denen in den Dateien 
  * [ ] `sose-02-insertion-sort.sol.py`, 
  * [ ] `sose-03-selection-sort.sol.py`, 
  * [ ] `sose-04-bubble-sort.sol.py`, 

<!-- uebung::end -->

---

