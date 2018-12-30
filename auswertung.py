#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


# Globale Variablen

dateiname="log.csv"

class DatenBank:

    def __init__(self):
       self.DB={}

    def daten_in_die_DB_schreiben(self,daten):
       #self.DB[daten[0]]=daten[1]
       #print(daten[0])
       pass

def auslesen():
    '''
    
    '''
    
    file = open(dateiname, "r")
    csv_reader = csv.reader(file, delimiter=",")
    # Kopfzeile auslesen und in eine Liste schreiben 
    beschreibung_liste=csv_reader.__next__()
    
    #print(dir(csv_reader))
    #print(type(csv_reader))
    #print(dir(csv_reader.__doc__))
    DB=DatenBank()
    for row in csv_reader:
       sensor=zeile_auswerten(row)
       # Sensordaten  einordnen
       print(sensor)
       if sensor[5] in sensor:
           DB.daten_in_die_DB_schreiben([sensor[5],sensor[3]])
       else:
           pass
       #dict_erstellen(sensor)
       
    file.close()
    #print(DB.keys())
def zeile_auswerten(zeile):
    pos=0
    sensor={}
    for e in zeile:
        if len(e) >0:
            sensor[pos]=e
        pos += 1    
    return sensor


def dict_erstellen(sensordaten):
    '''
    Aufbau der Datenbank
    {seriennummer:{name: name1,}}
    
    '''
    print(sensordaten)
    # prüfen ob eine Seriennummer vorhanden ist
    #if sensordaten[2][0]==5:
    #    for e in sensordaten:
    #       print(e)
    #    #print(len(sensordaten))
    #else:
    #    print(sensordaten)
    pass

def hauptprogramm():
    
    auslesen()

    print("Das Hauptprogramm wurde ausgeführt!")


if __name__== "__main__":
    hauptprogramm()
