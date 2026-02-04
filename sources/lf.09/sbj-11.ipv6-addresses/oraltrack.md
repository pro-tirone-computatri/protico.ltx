<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1) IPv6-Adresse [→ ZP:Sheet:2]


* bestehen aus 128 Bits (= 16 Bytes)
* werden zur Verschriftlichung in 8 Blöcke zu je 2 Bytes aufgeteilt.
* jedes Bytes hexadezimal notiert
* 2 benachbarte Bytes bilden ein Paar und werden vom folgenden durch einen \texttt{:} abgetrennt.
* Die Bytes werden mit abnehmender Wertigkeit von links nach rechts ausgegeben.
* Führende Nullen in einem Byte-Paar weglassbar. 
* Einmal in einer zusammenhängenden Gruppe von Null-Blöcken alle 0 weglassbar

Beispiel:

* 2001:0db8:0000:08d3:0000:8a2e:0070:7344 
* → 2001:db8:0:8d3:0:8a2e:70:7344
* → 2001:db8::8d3:0:8a2e:70:7344
* [ → [https://de.wikipedia.org/wiki/IPv6](https://de.wikipedia.org/wiki/IPv6) ]

Anmerkung:

* In IPv6-Adressen gibt es keine Netzmaske! Der Netzanteil wird ausschließlich in CIDR-Notation markiert 
* Verteilung: 
  * Provider bekommt von [https://www.ripe.net/](https://www.ripe.net/) z.B. \texttt{2001:0db8::/32} zur weiteren Verteilung. 
  * Kunde bekommt vom Provider z.B. \texttt{2001:0db8:0000:0001/64} 
* Grundsatz: Jede bekommt mindestens `2^{64}` IPv6-Adressen mindestens

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">LF09:11:IPv6:01</span>

Finden Sie mit `ipconfig` bzw.  `ifconfig` Ihre IPv6-Adresse im Schulnetz

* [ ] Finden Sie mit `ipconfig` bzw.  `ifconfig` Ihre IPv6-Adresse im Schulnetz
* [ ] Geben Sie die IPv6-Netzadresse des Schulnetzes an.
  
<!-- uebung::end -->

---


**[→ ZP:Sheet:3]**

* Zahlenmäßig stünden mit 16 Bytes `2^{128}` = `3,4 * 10^{38}` = `340 Sextillionen` IPv6-Adressen zur Verfügung
* $3,402823669*10^{38}$ ist so groß, dass mein Taschenrechner 
- wenn ich davon die $8.000.000.000$ Erdbewohnerinnen abziehen lasse - immer noch denselben Wert ausgibt.

### 2) IPv6-Adressklassen [→ ZP:Sheet:4]

### 3) IPv6-MacAdresseb [→ ZP:Sheet:5]

Grundfrage: Könnte man eine Mac-Adresse (weltweit eindeutig) n icht als IPv6-Adresse verwenden?

Ausgang:

* MAC-Adresse hat 6 Bytes
* Die erste 3 spezifizieren den Hardwarehersteller
* Die letzten drei sind die Interfacenummer = Netzwerkkarten-ID. 
  
MAC-Adresse sollte als in eine IPv6 *Link Local Unicast Address* umgewandelt werden können

* Mac-Adresse (Hex-Notation) in zwei 3-Byte-Blöcke aufteilen:
  * `(52:74:f2:b1:a8:7f` → `52:74:f2 und b1:a8:7f)`
* Dazwischen den Wert FF:FE einfügen: 
  * `(52:74:f2 + FF:FE + b1:a8:7f` → `52:74:f2:FF:FE:b1:a8:7f)`
* Ergebnis in die IPv6-Format umformen: 
  * `(52:74:f2:FF:FE:b1:a8:7f` → `5274:f2ff:feb1:a87f )`
* Das erste Oktett in Binärnotation umwandeln und das 7. Bit invertieren
  * `(52` → `01010010` → `01010000)`
* Binärwert in Hex-Code umwandeln
  * `(01010000` → `50)`
* Das erste Oktet durch den neuen Wert ersetzen:
  * `(5274:f2ff:feb1:a87f` → `5074:f2ff:feb1:a87f)`
* Dem Ganzen das Link-Local-Prefix `fe80::` voransetzen:
  *  `( 5074:f2ff:feb1:a87f` → `fe80::5074:f2ff:feb1:a87f)`

Warum die Bit-Konvertierung? 

* Um der Begrenzung der traditionellen Mac-Adresse zu kommen, ist das EUI-64 Format für Mac-Adressen erfunden worden.
* Im EUI-64 Format soll das 7 Bit (wie im alten 48-Bit-Format) anzeigen, ob die MAC-Adresse 
  global unique = administriert ist, oder lokal generiert worden ist. 
* Algorithmus verändert eine global administrierte MAC-Adresse lokal: ergo muss sie den uniquen Status verlieren. 
* Deshalb die Inversion der 7. Bits.
*  [ → [https://ben.akrin.com/mac-address-to-ipv6-link-local-address-online-converter/](https]://ben.akrin.com/mac-address-to-ipv6-link-local-address-online-converter/)]
*  [ → [https://community.cisco.com/t5/networking-knowledge-base/why-we-flip-the-7th-bit-in-eui-64-a-comprehensive-analysis/ta-p/4951015](https://community.cisco.com/t5/networking-knowledge-base/why-we-flip-the-7th-bit-in-eui-64-a-comprehensive-analysis/ta-p/4951015)]