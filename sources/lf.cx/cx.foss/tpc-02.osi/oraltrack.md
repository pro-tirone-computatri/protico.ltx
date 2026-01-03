<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->

<!-- LTeX:Language=de-DE -->

### (II) CRX / FOSS / OSI *Tonspur*

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LFCX:FOSS:01**</span>

* [ ] Stellen Sie fest, worin sich die MIT-Lizenz und die JSON-Lizenz unterscheiden.
* [ ] Stellen Sie fest, warum die JSON-Lizenz niemals eine Open-Source-Lizenz wird.

<!-- uebung::end -->

---

*Lösung:*

* Die JSON-Lizenz ([https://www.json.org/license.html](https://www.json.org/license.html)) enthält - verglichen mit der MIT-Lizenz ([https://opensource.org/license/mit](https://opensource.org/license/mit)) - einen Satz mehr, nämlich die Forderung:

    *The Software shall be used for Good, not Evil.*

* Die *Open Source Definition* [https://opensource.org/osd](https://opensource.org/osd) fordert von Lizenztexten,

    *(they) must not restrict anyone from making use of the program in a specific field of endeavor.*

    Und der Ausschluss der schlechten Zwecke wäre so etwas.


**_Frage A_: Wer entscheidet eigentlich, wann Software Open-Source-Software ist?**

* Früher häufige Antwort: _Open-Source-Software ist Software, zu der der Quellcode zugänglich ist_.
* Geschichtlich gesehen, ist es anders:

**Randbemerkung (I): Entstehung des Begriffs 'Open-Source(-Software) [→ ZP:Sheet:19]**

Heute:

* unverbrüchlich mit Begriff *Open-Source(-Software)* verknüpft: Nutzungsrechte
* = Zugriff auf den Code bzw. das Programm erlaubt (gewisse) Nutzungen,
* für die man nicht mehr extra zahlen muss
 
Früher:
  
* 1995 - 1998: Netscape Navigator weltweit meist genutzter Internetbrowser.
* Ende der 1990er Jahre: Microsoft bündelt Internet-Explorer mit Windows.
* `=>` 'Browserkrieg' zwischen Microsoft (Internet-Explorer) und Netscape (Netscape Navigator)
* 1998 verliert Netscape massiv Umsatz. Reaktion: Netscape
  * gibt Quellcode seines Navigators zur Nutzung frei
  * gründet die Mozilla (= Mosaic Killer) Foundation zur Weiterentwicklung
    * Hintergrund: Mosaic war ein früher Browser, vertrieben von der Firma *Spyglas*. Die hat MS gekauft und seinen IE darauf aufgebaut [https://de.wikipedia.org/wiki/NCSA_Mosaic](https://de.wikipedia.org/wiki/NCSA_Mosaic)
  * entwickelt die Mozilla Public License
  * aus dem Code entsteht zuletzt der Firefox
  * 1998 erfindet *Bruce Perens* den Begriff *Open-Source-Software* als geschäftsfreundliche Alternative zum stärker programmatisch/politisch gefärbten Begriff *Free Software*
* 2001 versucht Microsoft die neue 'Open-Source-Bewegung' zu 'kapern' bzw. zu 'unterlaufen', indem es
  * die 'Shared Source Initiative' gründet
  * den Windowscode unter NDA-Bedingungen bestimmten Nutzer zugänglich macht
  * damit aber gerade keine Nutzungsrechte verknüpft (außer dem reinen Leserecht)
  * argumentiert, dass das ja auch offene Software ist. 
  * (MS hat sich um 2015 gewendet und ist heute der größte FOSS-Contributor)

* → 
  * [https://de.wikipedia.org/wiki/Netscape_Navigator](https://de.wikipedia.org/wiki/Netscape_Navigator)
  * [https://de.wikipedia.org/wiki/Mozilla_Firefox](https://de.wikipedia.org/wiki/Mozilla_Firefox)
  * [https://de.wikipedia.org/wiki/Open_Source_Initiative](https://de.wikipedia.org/wiki/Open_Source_Initiative)
  * [https://en.wikipedia.org/wiki/Shared_Source_Initiative](https://en.wikipedia.org/wiki/Shared_Source_Initiative)

Aus dem ersten Abschnitt über KTJ-Salat wissen wir:

**_Antwort zu Frage A_:**

> **_Software wird Open-Source-Software, wenn die Copyright-Inhaber der Quellcode per Lizenzierungsstatement mit einer Open-Source-Lizenz verknüpfen._**

---

**_Frage B_: Wer entscheidet, wann eine Lizenz eine Open-Source-Lizenz ist?**

**Variante a: Freie Software: [→ ZP:Sheet: 20]**

Aus dem ersten Abschnitt über KTJ-Salat wissen wir auch:

* *[Free Software Foundation](https://fsf.org)* erwartet, dass freie Software unverbrüchlich mit Freiheiten verknüpft ist, nämlich die Freiheit (das Recht), die Software

  * zu **verwenden**
  * zu **verstehen**
  * zu **verbreiten**
  * zu **verbessern**

> Ziel: *Wer die Software hat, soll das tun dürfen*.

Die FSF hat einen *festen Bestand an Freie-Software- bzw. GNU-Lizenzen*: 

* die **GPL**: GNU General Public License (starkes Copyleft)
* die **LGPL**: GNU Lesser General Public License (schwaches Copyleft)
* die **AGPL**: GNU Affero General Public License (starkes Copyleft in Cloud)
* die **GFDL**: GNU Free Documentation License (Copyleft für Dokumente)

Andere Lizenzen betrachtet (und listet) die FSF vom Standpunkt der Kompatibilität her: 

> *Kompatibel lizenzierte Software liegt vor, wenn die Lizenz der Komponente, Bibliothek etc. die Wirkung für GNU-Lizenz nicht aufhebt!* 

**Randbemerkung (II): Zusammenhang von GNU und FSF**

* Das *GNU-Projekt* ist das Projekt, das *Richard Stallmann* 1983 ins Leben gerufen hat, um eine freie Alternative zu Unix zu entwickeln. 
* *Frei* meint ein Unix, das frei im obigen Sinne ist. (Unix ist nicht in dem Sinne frei. Deshalb das Wortspiel *__GNU__* = *`GNU`* `is not Unix`)
* Zur Durchsetzung der Ziele: Gründung *Free-Software-Foundation* gegründet.

**_Antwort 1 zu Frage B_:**

> * Freie Software im strengen Sinne ist unter einer GNU-Lizenz lizenziert.
> * Frei Software im erweiterten Sinne ist unter einer GNU-kompatiblen Lizenz lizenziert.


* → 
  * [https://www.gnu.org/philosophy/free-sw.html](https://www.gnu.org/philosophy/free-sw.html)
  * [https://fsfe.org/freesoftware/freesoftware.de.html](https://fsfe.org/freesoftware/freesoftware.de.html)
  * [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)
  * [https://www.gnu.org/licenses/license-compatibility](https://www.gnu.org/licenses/license-compatibility)
  * [https://www.gnu.org/licenses/license-list.de.html](https://www.gnu.org/licenses/license-list.de.html)
  * [https://www.gnu.org/software/software.de.html](https://www.gnu.org/software/software.de.html)
  * [https://de.wikipedia.org/wiki/Richard_Stallman](https://de.wikipedia.org/wiki/Richard_Stallman)


**Variante b: Open-Source-Software: [→ ZP:Sheet:21]**

[Bruce Perens](https://de.wikipedia.org/wiki/Bruce_Perens) hat 1998

* den Begriff *"Open-Source-Software"* als Alternative zum politisch aufgeladenen Begriff *"Free Software"*
  
* die *Open Source Initiative* = **OSI** mit gegründet
* die *Open Source Definition* = **OSD** zentral mit geschrieben.

Idee:

* Open-Source-Software ist, was unter einer Open-Source-Lizenz lizenziert ist.
* Es gibt 10 Bedingungen, die eine Lizenz erfüllen muss, um eine Open-Source-Lizenz sein zu können. (**OSD**)
* Ob eine Lizenz die **OSD** erfüllt, entscheidet ein Review- (früher: Approval-)Prozess der **OSI**.
* Ist eine Lizenz 'approved', wird sie in die Liste der Open-Source-Lizenzen aufgenommen.

**_Antwort 2 zu Frage B_:**

> * Software ist Open-Source-Software, wenn sie unter einer Open-Source-Lizenz lizenziert ist.
> * Ob eine Lizenz eine Open-Source-Lizenz ist, entscheidet die **OSI** mittels eines Approval-Prozesses.

* →
  * [https://opensource.org/](https://opensource.org/)
  * [https://opensource.org/osd](https://opensource.org/osd)
  * [https://opensource.org/licenses/review-process](https://opensource.org/licenses/review-process)
  * [https://opensource.org/licenses](https://opensource.org/licenses)


**Randbemerkung (III): OSD-Bedingungen**

* **Free Redistribution** :- die Lizenz darf niemanden pekuniär oder organisatorisch behindern, die Software an Dritte weiterzugeben.
* **Source Code** :- die Lizenz muss die Weitergabe in Form von Quell- und Binärcode erlauben.
* **Derived Works** :- die Lizenz muss Modifikationen und abgeleitete Werke und deren Weitergabe erlauben
* **Integrity of The Author’s Source Code** :- die Lizenz darf von abgeleiteten Werken fordern, dass sie unter anderem Namen weitergegeben werden.
* **No Discrimination Against Persons or Groups** :- die Lizenz darf keine Person von der Nutzung der Software ausschließen.
* **No Discrimination Against Fields of Endeavor** :- die Lizenz darf keine Verwendungszecke ausschließen
* **Distribution of License** :- Die Lizenz muss die Rechte allen gewähren und darf dazu keine zusätzliche Lizenz nötig machen
*  **License Must Not Be Specific to a Product** :- Die Lizenz darf andere Software nicht begrenzen / ausaschließen, die zusammen mit der lizenzierten Software weitergegeben wird.
* **License Must Be Technology-Neutral** :- Die Lizenz darf Technologiekontexte nicht ausschließen.

**Randbemerkung (IV): Unterschiede Open-Source- zu Free-Software**

* Technologisch und konzeptionell gibt es zwischen *Freier Software* und *Open-Source-Software* **keinen** Unterschied:
  * die vier konstitutiven Freiheiten bei *Freier Software* sind von der *OSD* abgedeckt.
* Politisch wollte und will die FSF die *Freie Software* zum Standard machen. *Closed Software* gilt ihr als Übel. Entsprechend ist sie von kommerziellen Entwicklern angegangen worden.
* *Open-Source-Software* wollte ein Begriff ohne diese Konnotation sein.
* Heute wird allgemein der Begriff *Open-Source-Software* verwendet.
* Kompromissbegriff: FOSS bzw. FLOSS = Free/Libre Open Source Software [https://de.wikipedia.org/wiki/Free/Libre_Open_Source_Software]https://de.wikipedia.org/wiki/Free/Libre_Open_Source_Software()


**Randbemerkung (V): Vorteil OSI-Vorgehen**

> Beide, Lizenzgeber und Nutzer (Lizenznehmer) brauchen kein Geld mehr für die anwaltliche Prüfung auszugeben, ob der Lizenztext die intendierten Rechte gewährt bzw. ob man die benötigten Rechte wirklich hat.

> *Aber: Jeder Nutzer muss die Pflichten aus den einzelnen Lizenzen entnehmen und erfüllen. Zusammenfassende Darstellungen sind immer Vereinfachungen. Auch die Darstellung in Abschnitt I.* 

---

**_Frage C_: Wie passt das zu dem, was man sonst so darüber hört?  [→ ZP:Sheet:22]**

** = 7 Mythen über _Open Source Software_**

> *__Disclaimer__: Mythen habe __wahren Kern__ + __Unsinn drumherum__* 


* **Mythos 1.A**: *Mit Open Source darf man kein Geld verdienen!*
  * ist **falsch**: denn Open-Source-Nutzer haben immer schon mit Open-Source-Geschäftsfällen Geld verdient
    * Richard Stallman hat seinen Emacs mittels Bändern vertrieben.
    * Red Hat (und SuSe) haben sich sehr früh für die Zusammenstellung und Vorkompilation passender Software in Distributionen bezahlen lassen.
    * Heute ist die Firma SerNet Weltmarkführer im Vertrieb der Komponenten *Samba* und *Verinice*, obwohl sie jedes ihrer Produkte unter der AGPL vertreibt. [https://www.sernet.de/](https://www.sernet.de/): Ihr Geld verdienen sie damit, die Software bei/in Firmen zu installieren, entsprechend zu konfigurieren und Updates zu liefern
  * hat einen **wahren** Kern: Keine OS-Lizenz erlaubt das Geschäftsmodell ‚Nutzungsgebühr‘

> "1. Free Redistribution: [...] The license shall not require a royalty or other fee for such sale"

* **Mythos 1.B**: *Das Gegenteil von OS Software ist kommerzielle Software!*
  * ist **falsch**: Denn man darf auch mit Open-Source-Software ein Geschäft betreiben.
  * hat einen **wahren** Kern: das Lizenzgeschäft ist ausgeschlossen

* **Mythos 1.C**: *Open Source Software ist kostenlos!*
  * ist **falsch**: Denn tatsächlich kann man das Recht, OS Software zu nutzen, nicht kaufen. Man 'erhält' die Nutzungsrechte nach dem Prinzip ‚Paying by Doing‘  
    * = alle OS Lizenzen erwarten ein lizenzadäquates Verhalten. Das muss umgesetzt werden, was kostet.
  * hat einen **wahren** Kern: Man zahlt niemals Gebühren für das bloße Recht, sie zu nutzen

* **Mythos 2**: *Open Source ist nur was für Gutmenschen!*
  * ist **falsch**: denn die OSI-Definition schließt jede Begrenzung des Verwendungszwecks aus - auch die Begrenzung auf moralisch unanfechtbare Zwecke
    * No Discrimination Against Persons or Groups
    * No Discrimination Against Fields of Endeavor
  * hat einen **wahren** Kern: dem frei(giebig)en Austausch haftet immer etwas Altruistisches an!

* **Mythos 3**: "Verbesserte Open-Source-Software muss man immer veröffentlichen!"
  * ist **falsch**: denn
    * die permissiven Lizenzen verlangen das gerade nicht
    * bei den anderen gilt die Weitergabe als Trigger: 
      * = Software, die man nicht weitergibt, kann man verbessern, ohne den verbesserten Code weitergeben zu müssen
  * hat einen **wahren**: Denn zum Spirit des Open-Source-Biotops / der Community gehört es, dafür, dass man sich frei daran bedienen kann, etwas zurückzugeben.
  
* **Mythos 4**: *"Verbesserte Open-Source-Software muss man **weltweit** veröffentlichen!"*
  * ist **falsch**: denn die Lizenz fordern nur, dass der, der die Software erhält, auch den Code erhält. 
  * hat den **wahren** Kern, dass bei einem Downloadservice (weltweit) auch der Code (weltweit) downloadbar sein muss.
  
* **Mythos 5**: *Software ist entweder Open-Source-Software oder proprietär.*
  * ist **falsch**: Nach dem Urhebergesetz **gehört** Open-Source-Software den Entwicklern. Darauf baut das Rechtemanagement auf. [https://www.gnu.org/licenses/copyleft.en.html](https://www.gnu.org/licenses/copyleft.en.html)
  * hat den **wahren** Kern, dass für andere Entwickler das Konzept 'Eigentum' viel deutlicher hervorgehoben wird (EULA-Texte)

* **Mythos 6**: *Veröffentlichte Open-Source-Software bleibt für immer Open-Source!*
  * ist **falsch**, weil alle Rechteinhaber zusammen eine Relizenzierung beschließen können.
  * hat den **wahren** Kern, dass die bis dahin veröffentlichten Versionen nicht nachträglich 'relizenziert' werden können (rückwirkende einseitige Vertragsänderung sind nicht legal.)

**Randbemerkung (V):**

> **Open Source schützt Ihr Geschäftsmodell vor Lizenzänderung,** die sonst Gebührenerhöhungen sind, denen der Hersteller ausgeliefert ist, weil er auf ein Closed-Source-Vorprodukt setzt.


* **Mythos 7**: Dynamisches Linken einer Bibliothek befreit von der Pflicht zur Veröffentlichung der Verbesserungen!
  * ist **falsch**, weil die *LGPL* und ihr schwaches Copyleft immer noch die Weitergabe des verbesserten Bibliothekcodes an die Produktempfänger fordert
  * hat den **wahren** Kern, dass die *LGPL* den starken Copylefteffekt bei dynamisch gelinkten Programme zugunsten des schwachen Copylefteffekts aufhebt.

**Summary**

* `--(I)` Mit Open Source darf man kein Geld verdienen? 
  * Doch!  - nur eben keine Lizenz-/Nutzungsgebühren.
* `-(II)` Open Source ist nur was für Gutmenschen? 
  * Nein! – die Nutzungsszenarien dürfen nicht begrenzt werden.
* `(III)` Modifizierte Open-Source-Software muss man wieder veröffentlichen?
  * Nein! - nur manchmal. Und 'dürfen' kann man es immer.
* `-(IV)` Modifizierte Open-Source-Software muss man weltweit freigeben? 
  * Nein! - nur diejenige müssen die bekommen, denen man das entsprechende Binary gegeben hat.
* `--(V)` OS Software ist entweder Open-Source-Software oder proprietär?
  * Nein! – beides gehört (weiter) den (Nutzungsrechts-) Inhabern. 
* `-(VI)` Publizierte Open-Source-Software muss man immer wieder veröffentlichen? 
  * Nein! – (die) Copyrightinhaber (zusammen) dürfen das Lizenzmodell ändern.
* `(VII)`  Dynamisches Linken befreit von der Pflicht zur  Veröffentlichung?
  * Nein! - das ist Entwicklerlatein!!!


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LFCX:FOSS:02**</span>

* [ ] Ermitteln Sie, unter welchen Lizenzen *Visual-Studio-Code* (*VSCode*), *VSCodium*, *Drawio* und die *Powershell* veröffentlicht sind.
* [ ] Beschreiben Sie, warum und in welcher Hinsicht *VSCodium* eine Alternative zu *VSCode* ist.

<!-- uebung::end -->

---

