<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1) Routingvarianten **[→ ZP:Sheet:2]**


Knüpft an Lösung der IPv4-Segmentierungsaufgabe *LF09:10* an

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:01**</span>

* [ ] Ermitteln Sie, wie viele Wege (ohne Schleifen) es vom Developer-Netz (192.168.1.64/26) ins Finance-Netz (192.168.1.128/27) gibt.  

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:3]**

---

### 2) Routing als Technik

**Router**

* informieren die ihnen benachbarten Router, 
  * welche Netze an sie angeschlossen sind
  * welche Netze die ihnen benachbarten Router kennen
* kommunizieren über Routingprotokolle
* berechnen mögliche Routen und schreiben sie in die eigenen Routingtabellen
* berücksichtigen mehrere Kriterien, um die beste Route zu finden
  * Anzahl der Hoppings
  * Durchsatzgeschwindigkeit
  * Auslastung

→ vgl. Schreiner: Computernetzwerke, 2014 (2014), S. 86f

Grundsatz:

* Sind mehrere Router in ein Netzwerk eingebunden
  * (= setzt es sich aus mehreren Broadcastdomains zusammen)
* gibt es
  * (sofern nicht durch Firewalls unterbunden)
* auch mehrere Wege (Hoppingsequenzen), einen Rechner auf Layer III-Ebene zu erreichen. 

**Routen**

* sind Wege, an die ein Router eine Frage weiterreicht, wenn er den Zielrechner nicht in seiner Broadcastdomäne findet
* werden manuell oder automatisiert in Routingtabellen eingetragen.
* die innerhalb eines segmentierten Netzes zu anderen Broadcastdomänen führen, müssen manuell oder automatisiert gepflegt werden.
* werden (auch) über Firewalls unterbunden

**Routingprotokolle**

existieren

* nutzen Router, um sich wechselseitig über die je nähere Umgebung zu informieren
* existieren, weil Anzahl und Vorkommen von Routern für Routingtabellen zu volatil ist
* werden in zwei Klassen eingeteilt
  * *Distance Vector Protokolle* tauschen Routingtabellen mit ihren Nachbarn aus.
  * *Link State Protokolle* senden Netzbeschreibungen an die Router einer Routerdomäne.

> Erst die Idee, dass Router sich wechselseitig über die je nähere Umgebung informieren,
> macht die "Vorgabe" erfüllbar, "[...] ein selbstkonvergentes, vermaschtes und weltweites
> Netzwerk zu entwickeln". 
>
→ vgl. Schreiner: Computernetzwerke, 2014 (2014), S. 88

* **Distance Vector Protokolle** 
  * tauschen ganze Tabellen aus 
  * erwarten, dass Empfänger das Tabellenformat verstehen 
  * (simpler + resourcensparend)
* **Link State Protkolle** 
  * beschreiben ihr Netz
  * erlauben es den Empfängern eigene Berechnung
  * können weitere Kreise bedienen 
  * (flexibel + rechenintensiv).

**Routingtypen**:

* **Dynamisches Routing** 
  * automatische Berechnung von Routen 
  * anhand von Informationen in den Routingtabellen 
  * mittels Austausche von Informationen.
* **Statisches Routing**
  * das manuelle Eintragen fester Routen an Routern
  * erfolgt meist an Grenzroutern
  * hat meist die Form *Route alles, das nicht zu Deinem Adressbereich gehört, übers
Interface X zu Router Y*
  * kann lokal auch die Form haben *Route alles [aus Subnetz X] an Subnetz Y über Router Z
  * z.B. via `ip route add 192.168.1.0/24 via 10.0.0.1`

Hinweise:

* *Statisches und Dynamisches Routing mit eigenen Weitverkehrsprotokollen wird auf
Providerebene dafür verwendet, um ganze Weitverkehrs-Routing-Domänen zu bilden.*
* Dynamisches Routing impliziert Umlernen von Netzwerkstrukturen.
* Klassische Routingprotokolle sind
  * RIP (Router Information Protocol)
  * OSPF (Open Shortest Path First)
  * IGRP Interior Gateway Routing Protocol
* Moderne Protokolle mit VLSM (Variable Length of Subnet Masks) können fast
beliebig segmentieren, ältere nicht.
* Viele Protokolle sind proprietär und NICHT unbedingt auf Kompatibilität ausgelegt.

Konsequenz: Trotz *Vendorenfalle*

> " [...] in dynamischen gerouteten Umgebungen lieber einen definierten Hersteller wählen 
> und [...] eine möglichst homogene Umgebung aufbauen“

→ vgl. Schreiner: Computernetzwerke, 2014 (2014), S. 88


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:02**</span>

Das Tool `ip` (LNX) bzw. `route` (W11) kann aktuelle Routen auslesen und neue Routen setzen

* [ ] Schreiben Sie für alle Routen im Beispiel *LF09:10* bei den zuständigen Routern die Routingkonfiguration

<!-- uebung::end -->

Lösung

---


### 3) Firewalling als Technik

**Firewalls** können (mindestens)

* anhand der IP-Adresse eines Rechners
  * dessen Zugriff auf eine IP-Adresse oder ein IP-Subnetz 
  * zulassen oder blockieren (Layer III)
* anhand der Netz-Adresse eines Sub-Netzes allen Rechnern des Netzes
  * dessen Zugriff auf eine IP-Adresse oder ein IP-Subnetz
  * zulassen oder blockieren (Layer III)
* Anfragen an einen Port zulassen oder blockieren (Layer IV)
* Anfragen anhand von Mustern (Häufigkeit der Anfrage, Anfrageinhalt, Protokoll) 
  zulassen oder blockieren (Layer III - VII)

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:03**</span>

* [ ] Ermitteln Sie, viele Firewalls Sie in diesem Netz mindestens wo brauchen, um alle Zugriffe
  steuern zu können.

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:4]**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:04**</span>

* [ ] Überlegen Sie, ob und wie Sie mit diesen Informationen über Routing- und Firewalltechniken
      die bisherige Lösung verfeinern können.
* [ ] Zeichnen Sie das 'kondensierte Netz', wenn möglich

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:5]**

---

