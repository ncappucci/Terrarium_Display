from tkinter import *
import tkinter as tk
import time
import Python_DHT
import RPi.GPIO as gpio
import time as tm

# GPIO Nummern angeben. Mit gpio.setmode(gpio.BOARD) müsste man PIN Nummern angeben
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
# Heizlampe: GPIO27, PIN 13
gpio.setup(27, gpio.OUT)
gpio.output(27, gpio.LOW)
gpio.setup(22, gpio.OUT)
gpio.output(22, gpio.LOW)
gpio.setup(5, gpio.OUT)
gpio.output(5, gpio.LOW)
gpio.setup(6, gpio.OUT)
gpio.output(6, gpio.LOW)

sensor = Python_DHT.DHT11
Feuchte, Temp = Python_DHT.read(sensor, 17)

# Definitionen zum Auslesen
def Temp_Auslesen():
    global temp
    Feuchte, Temp = Python_DHT.read_retry(11, 17)
    temp = Temp
    Temperatur.configure(text=str(temp) + " °C")
    Fenster.after(10000, Temp_Auslesen)

def Feuchte_Auslesen():
    global feuchte
    Feuchte, Temp = Python_DHT.read_retry(11, 17)
    feuchte = Feuchte
    Feuchtigkeit.configure(text=str(feuchte) + " %")
    Fenster.after(10000, Feuchte_Auslesen)

def Zeit_Auslesen():
    current_time = tm.strftime('%H:%M:%S')
    Zeit['text'] = current_time
    Fenster.after(200, Zeit_Auslesen)
    
def HLamp_Zustand():
    if ZustandHLamp.get():
        gpio.output(27, gpio.HIGH)
        AnzeigeHLamp.configure(text='AN', bg='green', width=4, height=1)
    else:
        gpio.output(27, gpio.LOW)
        AnzeigeHLamp.configure(text='AUS', bg='red', width=4, height=1)
        
def UVB_Zustand():
    if ZustandUVB.get():
        gpio.output(22, gpio.HIGH)
        AnzeigeUVB.configure(text='AN', bg='green', width=4, height=1)
    else:
        gpio.output(22, gpio.LOW)
        AnzeigeUVB.configure(text='AUS', bg='red', width=4, height=1)
        
def Tageslicht_Zustand():
    if ZustandTageslicht.get():
        gpio.output(5, gpio.HIGH)
        AnzeigeTageslicht.configure(text='AN', bg='green', width=4, height=1)
    else:
        gpio.output(5, gpio.LOW)
        AnzeigeTageslicht.configure(text='AUS', bg='red', width=4, height=1)
        
def Brunnen_Zustand():
    if ZustandBrunnen.get():
        gpio.output(6, gpio.HIGH)
        AnzeigeBrunnen.configure(text='AN', bg='green', width=4, height=1)
    else:
        gpio.output(6, gpio.LOW)
        AnzeigeBrunnen.configure(text='AUS', bg='red', width=4, height=1)
    
# Fenster erstellen:
Fenster = Tk()
# Variablen:
ZustandHLamp      = IntVar()
ZustandUVB        = IntVar()
ZustandTageslicht = IntVar()
ZustandBrunnen    = IntVar()
# Titel vom Fenster:
Fenster.title("Terrarium")
# Hintergrundfarbe des Fensters:
Fenster.config(background = 'gray63')

# Erstellen der "Felder"
# Zeit
ZeitText = Label(Fenster, text="Uhrzeit: ", bg='gray63')
Zeit = Label(Fenster, bg='gray63')
# Temperatur
TempText = Label(Fenster, text="Temperatur: ", bg='gray63')
Temperatur = Label(Fenster, bg='gray63')
# Luftfeuchtigkeit
HumiText = Label(Fenster, text="Luftfeuchtigkeit: ", bg='gray63')
Feuchtigkeit = Label(Fenster, bg='gray63')
# Heizlampe
HLamp = Label(Fenster, text = "Heizlampe", bg='gray63')
KnopfHLamp = Checkbutton(Fenster, text="AN/AUS",
                         indicatoron = 0,
                         variable = ZustandHLamp,
                         command = HLamp_Zustand )
AnzeigeHLamp = Label(Fenster, text='AUS', bg='red', width=4, height=1)
# UVB-Lampe
UVB = Label(Fenster, text="UVB-Lampe", bg='gray63')
KnopfUVB = Checkbutton(Fenster, text="AN/AUS",
                       indicatoron = 0,
                       variable = ZustandUVB,
                       command = UVB_Zustand)
AnzeigeUVB = Label(Fenster, text='AUS', bg='red', width=4, height=1)
# Tageslicht LED-Lampe
Tageslicht = Label(Fenster, text="Tageslicht-Lampe", bg='gray63')
KnopfTageslicht = Checkbutton(Fenster, text="AN/AUS",
                              indicatoron = 0,
                              variable = ZustandTageslicht,
                              command = Tageslicht_Zustand)
AnzeigeTageslicht = Label(Fenster, text='AUS', bg='red', width=4, height=1)
# Brunnen
Brunnen = Label(Fenster, text="Brunnen", bg='gray63')
KnopfBrunnen = Checkbutton(Fenster, text="AN/AUS",
                           indicatoron = 0,
                           variable = ZustandBrunnen,
                           command = Brunnen_Zustand)
AnzeigeBrunnen = Label(Fenster, text='AUS', bg='red', width=4, height=1)
# Winterschlaf Beginn Ende Eingabe
WS = Label(Fenster, text="Winterschlaf:", bg='gray63')
WSbegin = Label(Fenster, text="Beginn am ", bg='gray63')
Ebegin = Entry(Fenster, width = 30)
WSend = Label(Fenster, text="Ende am ", bg='gray63')
Eend = Entry(Fenster, width = 30)

# Anordnungen im GUI
ZeitText.grid(row=0, column=0, padx=5, pady=3)
Zeit.grid(row=0,column=2, padx=5, pady=3)
# Temperatur
TempText.grid(row=1, column=0, padx=5, pady=3)
Temperatur.grid(row=1, column=2, padx=5, pady=3)
# Luftfeuchtigkeit
HumiText.grid(row=2, column=0, padx=5, pady=3)
Feuchtigkeit.grid(row=2, column=2, padx=5, pady=3)
# Heizlampe
HLamp.grid(row=3, column=0, padx=5, pady=3)
KnopfHLamp.grid(row=3, column=1, padx=5, pady=3)
AnzeigeHLamp.grid(row=3, column=2, padx=5, pady=3)
# UVB-Lampe
UVB.grid(row=4, column=0, padx=5,pady=3)
KnopfUVB.grid(row=4, column=1, padx=5, pady=3)
AnzeigeUVB.grid(row=4, column=2, padx=5, pady=3)
# Tageslicht
Tageslicht.grid(row=5, column=0, padx=5, pady=3)
KnopfTageslicht.grid(row=5, column=1, padx=5, pady=3)
AnzeigeTageslicht.grid(row=5, column=2, padx=5, pady=3)
# Brunnen
Brunnen.grid(row=6, column=0, padx=5, pady=3)
KnopfBrunnen.grid(row=6, column=1, padx=5, pady=3)
AnzeigeBrunnen.grid(row=6, column=2, padx=5, pady=3)
# Winterschlaf
WS.grid(row=7, column=0, padx=5, pady=3)
WSbegin.grid(row=8, column=0, padx=5, pady=3)
Ebegin.grid(row=8, column=1, columnspan=3, padx=5, pady=3)
WSend.grid(row=9, column=0, padx=5, pady=3)
Eend.grid(row=9, column=1,columnspan=3, padx=5, pady=3)

# "Programm"-Durchführung
Zeit_Auslesen()
Temp_Auslesen()
Feuchte_Auslesen()

Fenster.mainloop()