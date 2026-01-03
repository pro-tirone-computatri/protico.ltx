<!-- LTeX:Language=de-DE -->


#### <span style="color: green;">ÜBUNG</span> <span style="color:magenta;">CRX:FOSS:01:01</span>

* [ ] Stellen Sie fest, worin sich die MIT-Lizenz und die JSON-Lizenz unterscheiden.
* [ ] Stellen Sie fest, warum die JSON-Lizenz niemals eine Open-Source-Lizenz wird.

**Solution:**

* Die JSON-Lizenz ([https://www.json.org/license.html](https://www.json.org/license.html)) enthält - verglichen mit der MIT-Lizenz ([https://opensource.org/license/mit](https://opensource.org/license/mit)) - einen Satz mehr, nämlich die Forderung:
  
    *The Software shall be used for Good, not Evil.*

* Die *Open Source Definition* [https://opensource.org/osd](https://opensource.org/osd) fordert von Lizenztexten, 

    *(they) must not restrict anyone from making use of the program in a specific field of endeavor.* 
 
    Und der Ausschluss der schlechten Zwecke wäre so etwas.

#### <span style="color: green;">ÜBUNG</span> <span style="color:magenta;">CRX:FOSS:03:02</span>

* [ ] Ermitteln Sie, unter welchen Lizenzen *Visual-Studio-Code* (*VSCode*), *VSCodium*, *Drawio* und die *Powershell* veröffentlicht sind.
* [ ] Beschreiben Sie, warum und in welcher Hinsicht *VSCodium* eine Alternative zu *VSCode* ist.

**Solution:**

* *VSCode* :- 
  * Sourcecode in GitHub: MIT-Lizenz ([https://github.com/Microsoft/vscode](https://github.com/Microsoft/vscode))
  * Product :- proprietäre Lizenz ([https://code.visualstudio.com/license](https://code.visualstudio.com/license))
* *VSCodium* : MIT-Lizenz ([https://github.com/VSCodium/vscodium/blob/master/LICENSE](https://github.com/VSCodium/vscodium/blob/master/LICENSE))
* *Drawio* : Apache-Lizenz ([https://github.com/jgraph/drawio](https://github.com/jgraph/drawio))
* *Powershell* :- MIT-Lizenz ([https://github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell))

Problem :-

* Die VSCode-Binärversion vom Microsoft darf Extensionen vom *extension marketplace* installieren
* Die VSCode-Binärversion vom Microsoft darf auch Informationen der Nutzer sammeln.
* Wer das nicht will, muss die ganz freie Version *VSCodium* nutzen, die von der Community entwickelt wird.
* Aber: [die Microsoft Visual Studio Marketplace Terms](https://cdn.vsassets.io/v/M259_20250709.8/_content/Microsoft-Visual-Studio-Marketplace-Terms-of-Use.pdf) (Abschnitt 1) legen fest, dass die Binaries der Extensionen aus dem Marketplace für MS-Produkte sind - und implizit also nicht für fremde Produkte wie VSCodium