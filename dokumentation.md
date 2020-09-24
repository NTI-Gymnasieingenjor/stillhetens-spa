# Dokumentation

**Krav**: Python

## Validering 
Navigera in i tests\validation\ mappen med valfri kommandotolk.

Kör: 
```python
python cssValidering.py
``` 
eller 
```python
python htmlValidering.py
``` 
Detta kör valideringen lokalt.

## Tester i selenium

### Kör Tester
Navigera in i tests\webtests\ mappen med valfri kommandotolk.
Kör 
```python
python run.py
``` 
Detta kör testerna lokalt.
### Skapa tester

## Testa upplösningar
### Hur man testar upplösningar
1. Navigera till sidan som ska testas. <br>
1. Inspektera element (CTRL+Skift+I eller F12).
1. Toggle device toolbar i inspektera element (CTRL+Skift+M).
1. I dropdown-menyn i mitten på toolbaren kan man välja sina enheter som man vill testa upplösningar i.

### Hur man lägger till upplösningar (Chrome)
1. Längst ned i dropdown-menyn på toolbaren så finns det en **Redigera** knapp, klicka på denna.
1. Till höger sida kommer det fram en meny med enheter. I denna kan man lägga till enheter genom att klicka på **Lägg till Anpassade Enheter** knappen.
1. Inmata valfritt namn till enheten. Lägg sedan till enhetens bredd, höjd samt Pixel ratio.
1. Sedan spara din enhet. Den ska nu gå att hitta i dropdown-menyn på toolbaren.


### Upplösningar som vi testar
**Dator** <br> 
2560x1440 <br>
1920x1080 <br>
1280x720 <br>

**Mobil** <br>
iPad [768x1024] Pixel ratio[2] <br>
iPhone X [375x812] Pixel ratio[3]<br>
iPhone 7 [375x667] Pixel ratio[2]<br>
iPhone 5 [320x568] Pixel ratio[2]<br>
Galaxy S5 [360x640] Pixel ratio[3]<br>
Galaxy S10 [412x869] Pixel ratio [3.5]<br>
Galaxy Fold [280x653] Pixel ratio[2.625]<br>
Galaxy Fold Landscape [586x820] Pixel ratio[2.625] <br>

Länk till att hitta de flesta av vanliga enheters upplösningar och pixel ratio. <br>
https://www.danhendricks.com/2018/04/adding-iphone-galaxy-chrome-mobile-emulated-devices