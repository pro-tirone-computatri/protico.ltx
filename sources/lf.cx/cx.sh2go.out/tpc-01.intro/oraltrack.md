<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

#### *Powershell 7.5.x als Tool für LF11a*

* *Nutzungsbegründung:* Nur Powershell 7 erlaubt Nutzung des WSL 2

**[→ Zur Geschichte](https://de.wikipedia.org/wiki/PowerShell):**

Windows

* enthielt ursprünglich nur die Command-Shell (`cmd`):
  * Suche in Windowssuche nach *cmd* oder *command*. 
  * Klicke angezeigte *Eingabeaufforderung* an
  * Windows startet die Command-Shell zum Starten einfacher Programme 
* Im Jahr 2003 hat Windows (Unix-)Admins eingeladen, um ihre Wünsche an eine bessere Admin-Shell zu erfahren. Ergebnis: So, wie unter UNIX/Linux.
* Daraufhin entstand die Powershell als eine auf den .NET-Framework aufsetzende Shell, auch mit eingebauten Befehlen.
  * Version 1.0 im Jahr 2006
  * Version 2.0 im Jahr 2008
  * Version 3.0 im Jahr 2012
  * Version 4.0 im Jahr 2013
  * Version 5.0 im Jahr 2015 zusammen mit Windows 10 (für ältere in Version 5.1 nachgereicht)
  * Version 6.0 im Jahr 2018 ist eine neue Open-Source-Version [Powershell-Core] (MIT) gehostet auf GitHub, die auch für LNX erhältlich ist.
  * Version 7.+x ist die aktuelle, 5.1 kriegt nur noch updates, 6 wird nicht weiterentwickelt, Basis ist jetzt die Version 7.x plattformübergreifend.

Hinweis: Linuxshells und Powershell unterscheiden sich trotzdem grundsätzlich: 

* PWSH arbeitet .NET basiert. Die meisten Kommandos sind als NET-Funktionalitäten im PWSH-Code implementiert.
* Linux-Shells dagegen stellen nativ die Programmlogik und Variablenauflösung bereit, ansonsten rufen sie externe Tools auf.
 
**Installation**

Powershell 7 ersetzt nicht vollständig Powershell 5. Deshalb existiert Powershell 5 auch noch nach der Installation von Powershell 7 und wird oft als defaultmäßig gestartet.

* Ermitteln der eigenen Version:
  * Powershell starten
  * `> $psVersionTable` eingeben
* Ggf. Powershell Version 7.5 installieren:
  * per Windowsstrore ohne Adminrechte. 
    * suche darin nach Powershell 7.
    * lasse es installieren
  * per [→ GitHub-Repository](https://github.com/PowerShell/PowerShell)
    * suche `PowerShell-7.5.2-win-x64.exe` unter [https://github.com/PowerShell/PowerShell/releases/tag/v7.5.2](https://github.com/PowerShell/PowerShell/releases/tag/v7.5.2)
    * Lade es runter in Deinen privaten App-Ordner.
    * Lasse dafür Link in Panel / Start anlegen
* Installation verifizieren:
  * Starte Powershell 5: 
    * In Appsuche nach *Powershell* (sic!) suchen und starten
    * `> $psVersionTable` eingeben
  * Starte Powershell 7: 
    * In Appsuche nach *pwsh* (sic!) suchen und starten oder
    * In gestarter Powershell 5 `pwsh` aufrufen
    * * `> $psVersionTable` eingeben

Hinweis: Powershell 7 (= pwsh) gibt es als Binaries auch für Linux und Mac. Allerdings: Die Powershell unter Microsoft arbeitet mit .NET-Funktionen, während die und Linux (und Mac?) meistens Tools des Betriebssystems aufrufen. Deshalb ist die `pwsh` streng gesehen nicht betriebssystem-übergreifend.

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LFCX:sh2go:01**</span>

* [ ] Installieren Sie die aktuellste Powershell auf Ihrem Windowsrechner.
* [ ] Verifizieren Sie ihre Installation

<!-- uebung::end -->

---
  
#### *Linux als Tool für LF09*

* *Nutzungsbegründung*: 
  * Shellprogrammierung erlaubt die Automatisierung Fernwartung der Rechner übers Netz.
  * Linux und Windows stellen aber unterschiedliche Shells zur Verfügung. Also sollte man deren Möglichkeiten kontrastiv erkunden / lernen


**Varianten der Bereitstellung**:

1. **auf einem zweiten Rechner/Laptop**
  * [ ] Ubuntu-24.04.03 LTS ISO-Datei von [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) herunterladen.
  * [ ] Mit Windowsmitteln einen bootfähigen USB-Stick erzeugen.
  * [ ] Rechner von USB-Stick booten.
  * [ ] Installationsanleitung folgen
2. **Dual Boot Installation**
  * [ ] Verfahren wie unter (1). 
  * [ ] Bei Installation 'neben Windows installieren' auswählen 
3. **in einer virtuellen Maschine unter Windows**
  * [ ] Virtualisierungssoftware auf Host *Windows* installieren
     * Empfohlen: [→Virtual Box]{https://www.virtualbox.org/}. Ist GPL v3 lizenziert = echte freie Software [→ https://www.virtualbox.org/wiki/Licensing_FAQ](https://www.virtualbox.org/wiki/Licensing_FAQ)
     * Abgeraten: VMware Workstation Player (kurz VMplayer) weil
       * [→ Vmware gekauft von Broadcom](https://www.heise.de/news/Broadcoms-VMware-Uebernahme-EU-Cloudanbieter-verklagen-die-Kommission-10499025.html). 
       * Broadcom monetarisiert die vorher (für den privaten Gebrauch) "freie" Software.
       * Lizenzen für VMware Workstation sind über diese Produktnummer nicht mehr erhältlich. Die Nachfolge-Lizenz war VMware Desktop Hypervisor Pro, diese ist aber auch im November 2024 nicht mehr erhältlich [→ https://www.software-express.de/hersteller/vmware/workstation/player/](https://www.software-express.de/hersteller/vmware/workstation/player/)
       * Antwort der Community: GitHub-Projekt zum Sammeln existierender Keys. [→ https://github.com/hegdepavankumar/VMware-Workstation-Pro-17-Licence-Keys](https://github.com/hegdepavankumar/VMware-Workstation-Pro-17-Licence-Keys).
       * Aber trotzdem keine seriöse Variante mehr.
  * [ ] Virtualisierungssoftware auf Host *MAC* von [→ https://ubuntu.com/download/desktop](https://mac.getutm.app/) installieren
  * [ ]  Ubuntu-24.04.03 LTS ISO-Datei von [→ https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) herunterladen.
  * [ ] In Virtualisierungssoftware als Start-/Bootmedium aktivieren
  * [ ] Virtuelle Maschine booten.
  * [ ] Installationsanleitung folgen 

4. **in einer virtuellen Maschine unter MacOs**
  * [ ] Virtualisierungssoftware auf Host *MacOs* installieren
     * mögliche: [→ Virtual Box]{https://www.virtualbox.org/}. Ist GPL v3 lizenziert = echte freie Software [→ https://www.virtualbox.org/wiki/Licensing_FAQ](https://www.virtualbox.org/wiki/Licensing_FAQ)
     * getestet: [→ iUTM]{https://mac.getutm.app/}. Ist Apache-v2 lizenziert = echte freie Software [→ https://github.com/utmapp/UTM](https://github.com/utmapp/UTM). Binaries auf Github und im AppleStore, dort aber angeblich gegen Geld.
4. **als Windows Subsystem Linux**
  * [ ] Über Windowssuchzeile nach *Features* suchen lassen
  * [ ] Button *Windows-Features aktivieren ...* anklicken
  * [ ] Im Dialog *Windows Subsystem für Linux* anwählen/aktivieren
  * [ ] Neustart
  * [ ] Powershell 7.5.x nach Windowsanleitung installieren [→ https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5)
  * [ ] Powershell (Adminmode) aufrufen
  * [ ] gemäß [→ Microsoftanleitung WSL-Aktivierung](https://learn.microsoft.com/de-de/windows/wsl/install) verfahren - bzw.
    * [ ] powershell: `wsl --install`     
    * [ ] powershell: `wsl --set-version UBUNTU 2` 

**Verifikation**:

* LNX (als virtuelle Maschine oder Dual-Boot etc.)
  * [ ] Linuxshell bzw. öffnen
  * [ ] `> ping 8.8.8.8` eingeben
  * Wenn Rückgabe *64 bytes from 8.8.8.8*, dann 
    * [ ] Zugriff auf Linuxtool *ping* (Linux läuft)
    * [ ] und Netzzugriff auf Google-Server (Netzzugang per NAT aktiviert)
* WSL auf Windows 11 Rechner:
  * Powershell öffnen
  * [ ] `> pwsh` eingeben (= Wechsel zu Powershell 7)
  * [ ] `> ping 8.8.8.8` eingeben (= Netzzugang verifizieren)
  * [ ] `> ipconfig` eingeben (= Windowsanalyse Netzwerkinterface)
  * [ ] `> wsl` eingeben (= WSL aktivieren)
  * [ ] `> ifconfig` eingeben (= Linuxanalyse Netzwerkinterface)

Hinweis: *Falls `ifconfig` oder gar `ping` unter LNX oder WSL fehlt, bitte in der Shell eingeben: `sudo apt-get install net-tools`

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LFCX:sh2go:02**</span>

* [ ] Installieren Sie eine Ihnen genehme Linux-Variante.
* [ ] Verifizieren Sie ihre Installation

<!-- uebung::end -->

---

#### *VSCODE als Tool für LF11a*

VSCODE

* wird von Microsoft zusammen mit der Community unter der MIT-Lizenz auf GitHub entwickelt [https://github.com/microsoft/vscode]https://github.com/microsoft/vscode()
* ist echte Open-Source-Software
* wird auch als Binärpaket für Windows, Linux und Mac bereitgestellt [→ https://code.visualstudio.com/download](https://code.visualstudio.com/download)
* kann mit Extensionen funktionell erweitert werden.

Hinweise:

* Die Binärpakete sind mit einer gesonderten Microsoft-Lizenz verbunden [→ https://code.visualstudio.com/license](https://code.visualstudio.com/license). Die erlaubt Windows, ihre Binärpakete mit 3rd-Party-Komponenten anzureichern. Außerdem sind Extensionen u.U. anders lizenziert.
* Wer Extensionen aus dem Windowsmarketplace installiert, stimmt den [→ Visual-Studio-Marketplace-Terms-of-Usex](https://cdn.vsassets.io/v/M259_20250709.8/_content/Microsoft-Visual-Studio-Marketplace-Terms-of-Use.pdf). Die besagen:

> *"Marketplace Offerings are intended for use only with In-Scope Products and Services and you may not install, reverse-engineer, import or use Marketplace Offerings in products and services except for the In-Scope Products and Services."* [S.2](https://cdn.vsassets.io/v/M259_20250709.8/_content/Microsoft-Visual-Studio-Marketplace-Terms-of-Use.pdf)

Das bedeutet, dass Extensionen aus dem Windowsmarketplace nur in den von Microsoft bereitgestellten Binaries integriert werden dürfen.

Die Community stellt aber unter dem Namen [→ VSCODIUM](https://vscodium.com/) eine Version ohne die Microsoft integrierten 3rd-Party-Komponenten. Deren Extension müssen konsequenterweise aus einem gesonderten Repository [[→ https://open-vsx.org/](https://open-vsx.org/) stammen. 


**Installation**

* VSCODE (Visual Studio Code) für 
  * [→ Windows](https://code.visualstudio.com/download) ([https://code.visualstudio.com/docs/setup/windows](https://code.visualstudio.com/docs/setup/windows)) 
  * [→ Linux](https://code.visualstudio.com/download) ([https://code.visualstudio.com/docs/?dv=linux64_deb](https://code.visualstudio.com/docs/?dv=linux64_deb))
  * [→ `VSCODIUM`](https://vscodium.com/) für 
    * [→ Windows](https://github.com/VSCodium/vscodium/releases) 
    * [→ Linux](https://github.com/VSCodium/vscodium/releases)
  * VS Plugins/Extensions jeweils über *Preferences/Extensions* installieren lassen. D.h. für
    * `VSCODE` erweitert aus [→ Visual Studio Marketplace](https://marketplace.visualstudio.com/):
      * PLUGINs für bash programming unter VSCODE: `shfmt`
      * PLUGINs für pwsh programming unter VSCODE: `pwsh`
    * `VSCODIUM` :
      * PLUGINs für bash programming unter VSCODIUM `shfmt`
      * PLUGINs für pwsh programming unter VSCODIUM: `pwsh`
  

**Verifikation**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LFCX:sh2go:03**</span>

* [ ] Öffnen Sie das Script `sh2go-00-happy-coding.sh` in Ihrer VS-Umgebung.
* [ ] Ersetzen Sie 'Happy Coding' durch eine Botschaft Ihrer Wahl.
* [ ] Sichern Sie das geänderte Script unter dem Namen `sh2go-00-mymsg.sh`
* [ ] Öffnen Sie in Ihrer Linux-Umgebung eine Commandshell (bash).
* [ ] Lassen sie das Script `sh2go-00-mymsg.sh` ausführen.

<!-- uebung::end -->

---

