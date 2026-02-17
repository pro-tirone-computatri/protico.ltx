<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

<!-- uebung::start -->

## Block 1: 'Netzwerkarchitekturen'

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:90:1**</span>

*Netzwerksysteme werden auch nach der Art ihrer Struktur klassifiziert.*

* 1.1 __Skizzieren Sie (sprachlich und/oder per Diagramm) eine Client-Server-Architektur.__ (3P)
* 1.2 __*Skizzieren Sie (sprachlich und/oder per Diagramm) eine Peer-To-Peer-Architektur.*__ (1ZP)

<!-- uebung::end -->

---

<!-- uebung::start -->

## Block 2: MAC-Adressen 

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:90:2**</span>

MAC-Adressen dienen zur weltweit eindeutigen Nummerierung von Netzwerkinterfaces/-karten:

* 2.1: __Beschreiben Sie, wie viele Bytes eine MAC-Adresse hat und welche Bytes davon (standardmäßig) zum Vendorencode gehören.__ (3P)
* 2.2: __*Rechnen Sie vor, wie viele verschiedene MAC-Adressen es maximal geben kann.*__ (1ZP)

Hinweis: Exponentialzahl reicht als Lösung.

<!-- uebung::end -->

Lösung: 

* MAC-Adresse = 6 Bytes, 3 für Vendorencode, 3 für vendoren spezifische Nummerierung
* `2^8 * 2^8 * 2^8 * 2^8 * 2^8 * 2^8 = 2^(6*8) = 2^48`
 
---

<!-- uebung::start -->

## Block 3: IPv4-Adressen

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:90:3**</span>

IPv4-Adressen haben eine innere Struktur und definieren im Verbund ein Netz.

* 3.1 __Beschreiben Sie, wie viele Bytes eine IPv4-Adresse hat__ (2P)
* 3.2 __*Berechnen Sie mit Bitoperatoren aus der IPv4-Adresse '192.168.110.42' und der Subnetzmaske '255.255.255.0' die folgenden Adressen:*__
  * _Netzadresse_ (1ZP)
  * _Broadcastadresse_ (1ZP)
  * _eine der üblicherweise genutzten Gatewayadressen_* (1ZP)

Hinweis: Beschreiben Sie Ihren Rechenweg.

<!-- uebung::end -->

Lösung:

* IPv4-Adresse = 4 Bytes
* `192.168.110.42 & 255.255.255.0 = 192.168.110.0`
* `192.168.110.0 | 0.0.0.255 = 192.168.110.255`
* a) `192.168.110.0 + 1 = 192.168.110.1` 
* b) `192.168.110.255 - 1 = 192.168.110.254`

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:90:4**</span>

Außerdem sind IPv4-Adressen in Gruppen mit speziellen Zwecken geordnet.

* 3.3. __Beschreiben Sie, wozu man private IPv4-Adressen nutzt.__ (2P)
* 3.4. __*Beschreiben Sie, wozu und wie man (wer?) APIPA-Adressen nutzt.*__ (2ZP)
 
<!-- uebung::end -->

---

Lösung:

* Zum Aufbau eines privaten Netzes, dessen IP-Adressen nicht ins Internet geroutet werden.
* Darf sich ein Rechner übergangshalber aus dem APIPA-Pool frei nehmen, wenn DHCP-Server nicht erreichbar

---

Bewertung:

* 10 Standardpunkte (P) + 7 Zusatzpunkte (ZP) möglich.
* 10 Punkte insgesamt = 2.0
* ab 12 Punkte insgesamt = 1.0
* Rest: [https://www.lehrerfreund.de/notenschluesselrechner/form-ihk-notenschluessel] mit dem Höchstwert 12
  
---



