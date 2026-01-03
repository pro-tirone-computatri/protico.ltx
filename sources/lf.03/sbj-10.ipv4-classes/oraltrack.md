<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1) IPv4-Adressklassen [→ ZP:Sheet:2]

Historisch gesehen wurden die 4.294.967.296 möglichen IPv4-Adressen auf 5 Klassen aufgeteilt:

1. **Klasse-A-Netze**:
   1. CIDR-Suffix: `/8` → `2^24` Adressen pro Klasse A-Netz
   2. Bereich: `0.0.0.0` (= `0x00000000`) - `127.255.255.255` (= `0x7FFFFFFF`)
   3. Bit-Erkennungsprefix: `0b0` gefolgt von 31 weiteren Bits: `0b0[01]{31}`
2. **Klasse-B-Netze**
   1. CIDR-Suffix: `/16` → `2^16` Adressen pro Klasse B-Netz
   2. Bereich: `128.0.0.0` (= `0x80000000`) - `191.255.255.255` (= `0xBFFFFFFF`)
   3. Bit-Erkennungsprefix: `0b10` gefolgt von 30 weiteren Bits: `0b10[01]{30}`
3. **Klasse-C-Netze**
   1. CIDR-Suffix: `/24` → `2^8` Adressen pro Klasse C-Netz
   2. Bereich: `192.0.0.0` (= `0xC0000000`) - `223.255.255.255` (= `0xDFFFFFFF`)
   3. Bit-Erkennungsprefix: `0b110` gefolgt von 29 weiteren Bits: `0b110[01]{29}`
4. **Klasse-D-Netze**
   2. Bereich: `224.0.0.0` (= `0xE0000000`) - `239.255.255.255` (= `0xEFFFFFFF`)
   3. Bit-Erkennungsprefix: `0b1110` gefolgt von 28 weiteren Bits: `0b1110[01]{28}`
5. **Klasse-E-Netze**
   2. Bereich: `240.0.0.0` (= `0xF0000000`) - `255.255.255.255` (= `0xFFFFFFFF`)
   3. Bit-Erkennungsprefix: `0b1111` gefolgt von 28 weiteren Bits: `0b1110[01]{28}`


**Exkurs: Regular Expressions [→ ZP:Sheet:3]**

* deutsch: Reguläre Ausdrücke
* abgekürzt: RegEx
* meint: eine grammatische Beschreibung erlaubter Sprachkonstrukte

1. An Position erlaubte Zeichen erscheint literal.
2. An einer Position erlaubte Varianten erscheinen in eckigen Klammern  (`[A-Zabc]`):
   * Bereiche werden durch Bindestriche erfasst (`A-Z` meint alle Großbuchstaben).
   * Ansonsten werden alle Varianten direkt hintereinander geschrieben (`abc` meint nur `a`oder `b` oder `c`).
3. Quantoren werden danach in geschweiften Klammern erfasst (`[A-Zabc]`){2,5}:
   * 2 Zahlen werden als `min` bis `max`gelesen.
   * 1 Zahl bestimmt das genaue Vorkommen.
   * 1 Zahl gefolgt von Komma meint `mindestens, aber gern auch mehr`.
   * 0,n meint beliebig viele, aber höchstens n
4. Sonderquantoren werden ohne geschweifte Klammern direkt ans Zeichen angehängt (`A+`):
   * `?` meint 0 oder einmal (= {0,1})
   * `+` mindestens 1 mal, aber sonst beliebig viele male (= {1,})
   * `*` beliebig oft, aber auch gar nicht (= {0,})

Hinweis: Manche Programme verwenden eine abgewandelte Syntax. `grep` z.B. gibt es auch als Tool `egrep`, was für *expanded global/regular expression" steht. 

vgl.:

* [https://de.wikipedia.org/wiki/Regulaerer_Ausdruck](https://de.wikipedia.org/wiki/Regulärer_Ausdruck)
* [https://en.wikipedia.org/wiki/Regular\_expression](https://en.wikipedia.org/wiki/Regular_expression)
* [https://de.wikipedia.org/wiki/Grep](https://de.wikipedia.org/wiki/Grep)


Es gilt: **[→ ZP:Sheet:4]**
   
1. Adressen aus **Klasse-A-Netzen** = frei routbar - außer
   1. `0.0.0.0` :- reserviert als kontextsensitiver Platzhalter
   2. `10.0.0.0` (= `0x0A000000`)- `10.255.255.255` (= `0x0AFFFFFF` ) :- privat 
   3. `127.0.0.0` (= `0x7F000000`)- `127.255.255.255` (= `0x7FFFFFFF`) :- superprivat 
2. Adressen aus **Klasse-B-Netzen** = frei routbar - außer
   1. `169.254.0.1` (= `0xA9FE0001`) - `169.254.255.255` (= `0xA9FEFFFF`) :- APIPA = DHCP-Fallback
   2. `172.16.0.0` (= `0xAC100000`) - `172.31.255.255` (= `0xAC1FFFFF`) :- privat 
3. Adressen aus **Klasse-C-Netzen** = frei routbar - außer
   1. `192.168.0.0` (= `0xC0A80000`) - `192.168.255.255` (= `0xC0A8FFFF`) :- privat 
4. Adressen aus **Klasse-D-Netzen** = Multicastadressen / dürfen nicht als Rechneridentifikatoren genutzt werden
5. Adressen aus **Klasse-E-Netzen** = Testadressen / dürfen nicht ins Internet geroutet werden.

Legende:

* **frei routbar** :-  können netzübergreifend als IP-Adresse / 'Rechnername' verwendet werden
* **privat** :- dürfen Adressen in einem privaten Netz eingesetzt, aber nicht ins Internet geroutet werden
* **superrivat** :- dürfen innerhalb eines Rechners als Loopbackadressen für seine Interfaces eingesetzt, aber nicht nach außen geroutet werden, auch nicht in private Netze
* **APIPA** :- steht für *Automatic Private IP Addressing*. Erlaubt Rechnern beim DHCP-Ausfall eine Adresse aus diesem Pool zu nehmen. Doppelte IP-Adresse werden in Kauf genommen: besser als gar nicht kommunizieren zu können. 

**IPv4-Adressen** werden

* von der **IANA** (= Internet Assigned Numbers Authority [https://www.iana.org/](https://www.iana.org/)) (meist blockweise) an *Registrare* vergeben
* von **Registraren** als Blöcke an *Provider* weitergereicht
* von **Providern**  einzeln, als Mengen oder als Blöcke (an Kunden) weitergereicht

**Regeln**:

* Wer einen IPv4-Adressblock delegiert, 
  * spezifiziert den Block mittels der (Sub)Netzwerkadresse und der zugehörigen (Sub)Netzmaske 
  * stellt via IP-Adresse u.a. ein Gateway zur Verfügung, an den Router aus dem verteilten Adressbereich ihre unzustellbaren ’Weiterleitungsaufträge’ abgeben können.
* Wer einen IPv4-Adressblock empfängt, darf
  * diesen weiter segmentieren. 
  * die neuen Segmente weiterreichen (Netzwerkadresse + erweiterte Subnetzmaske), sofern er seinen ’Kunden’ ein Gateway anbietet.

### 2) IPv4-Segmentierung [→ ZP:Sheet:5]

* Ausgangspunkt einer Segmentierung sind Netzadresse und Subnetzmaske: 
  - z.B. `192.168.1.0/24` bzw. 
  - `192.168.1.0` \& `255.255.255.0`
* __Subnetze können nur in `2^x`-Segmente vom Netzbereich abgespalten__ werden [→ ZP:Sheet:6]: 
  * z.B. `192.168.1.0/25` bzw. `192.168.1.0` \& `255.255.255.128`
  * z.B. `192.168.1.128/25` bzw. `192.168.1.128` \& `255.255.255.128`
* Eine **symmetrische Netzwerksegmentierung** teilt den Adressbereich in gleich große Subnetze auf.
* Eine **asymmetrische Netzwerksegmentierung** spaltet vom verbliebenen Adressbereich verschieden große Subnetze ab: 
  * Zuerst den größten Bereich abspalten;
  * danach sukzessive die je kleineren Bereiche
* Die Anzahl der in einem Subnetz prinzipiell zuweisbaren IPv4-Adressen ist `2^n - 2`: 
  - Netzadresse und Broadcastadresse dürfen nicht zugewiesen werden.
* Das kleinste sinnvoll abspaltbare Subnetz hat die Größe `2^2` mit 
  * 1 Netzadresse
  * 1 Broadcastadresse
  * 1 Router-/Gatewayadresse
  * 1 Adresse für einen Arbeitsrechner

**Beispiel im großen Aufriss [→ ZP:Sheet:7]**

* Klasse C-Netz `192.168.42.y` aufgespalten in 1 `\25` und 2 `\26` Subnetze
  * `192.168.42.0/25`
  * `192.168.42.128/26` 
  * `192.168.42.192/26` 
* Achtung:
  * Aufspaltung hat nichts mit Hopping zu tun

**Hinweis:**

1. Eine korrekte **Segmentierung** verlängert die gegebene Subnetzmake (Bits hinzufügen):
   1. Sie darf diese nie verkürzen (Bits aus der gegebenen Maske entfernen (damit im Netz keine Dubletten von IP-Adressen auftreten.)
   2. = *CIDR-Suffix* nur erhöhen, nicht verringern.
2. Wer wie viele ’Gatewayrouter’ wem mit welcher Verfügbarkeit zur Verfügung stellt, ist eine Frage der je bilateralen Verträge:
   1. Der oberstere Provider könnte alle Router aus allen neu segmentierten Subnetzen in sein übergeordnetes Netzmit mit Gateway einbinden.
   2. Der oberstere Provider könnte seinem Kunden, der Subnetze heraussegmentiert, anbieten, einen speziellen Kunden-Router bei sich einzubinden: Dann bräuchte der Segmentierer ein gesondertes Netz, in das alle Router seiner Subnetze als normalen Mitglieder eingebunden sind und in dem der Kunden-Router als Gateway fungiert.

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF03:10:Segmentierung:01**</span>

Nehmen wir an, ich hätte überraschend doch noch 256 routbare, unverbrauchte IPv4-Adressen 'gefunden', nämlich `192.110.0.0/24`. Die würde ich dann gerne in Teilblöcken an Sie weitergeben:

* [ ] Segmentieren Sie die Bereiche so, dass
  * [ ] ich ein kleines Verwaltungsnetz bekomme, in das ich meinen Router nach außen als Gateway für innen, einen eigenen Rechner und die je für Ihre Subnetze zuständigen Router einbinden kann
  * [ ] jeder von Ihnen ein möglichst großes Subnetz bekommt
* [ ] Erstellen Sie mit *drawio* ein Netzdiagramm. Geben Sie dabei alle Netzspezikikatoren und verwendeten IPv4-Adressen an.
  
<!-- uebung::end -->

---
