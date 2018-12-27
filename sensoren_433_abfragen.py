#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess ,shlex
from time import time as zeit

#ausgabe = subprocess.check_output('ip -details link show can0', shell=True)
#subprocess.call("sudo ip link set dev can0 down", shell=True)

def check_sdr_hardware():
    '''
    Funktion: Es wird gepüft ob die  benötigte Hardware RTL2838 von handen ist
              1  für vorhanden und 0 für nicht vorhanden
    '''

    cmd="lsusb | grep RTL2838"
    #cmd="lsusb | grep RTL2837"
    try:
        ausgabe = subprocess.check_output(cmd, shell=True,text=True, stderr=None)
        print("Ausgabe:\t",ausgabe)
        #hw_status="Geräte ist vorhanden!!!" 
        hw_status=1
    except subprocess.CalledProcessError:

        print('Fehler aufgetreten!!')
        #hw_status="!!! Gerät ist nicht vorhanden !!!"
        hw_status=0        
        pass
    return hw_status

def sensoren_auslesen():
    '''
    Funktion: Der Sensor empfängt etwa für 60 s Signale und schreibt 
              die Daten in die Datein info.txt
    '''
    startzeit=zeit()
    #print(startzeit)
    #cmd='rtl_433 -G -T 60 | tee >> info.txt '
    cmd='rtl_433 -R 12 -E | tee >> info.txt '
    cmd='rtl_433 -R 12 -E'
    werte=subprocess.run(cmd,shell=True,capture_output=True,check=True,text=True)
    
    ausgabeformat(werte)
    #werte_liste=werte.stdout.split("\n")

    #print(len(werte.stdout.split("\n")),werte.stdout.split("\n"))
    print("Dauer:\t",zeit()-startzeit,"Fertig")

    
    pass

def cputemp():
    cmd=shlex.split("/opt/vc/bin/vcgencmd  measure_temp")   
    cmd="/opt/vc/bin/vcgencmd  measure_temp"
    #cmd=["/opt/vc/bin/vcgencmd","measure_temp"]
    print(cmd)
    cpu_temp=subprocess.run(cmd, shell=True,capture_output=True,check=True,text=True).stdout
    print("CPU Temperatur:\t",cpu_temp)

def ausgabeformat(werte):
    '''
    Hier wird die Ausgabe des Befehls  cmd  formatiert und die benötigten Werte extrahiert
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    time      : 2018-12-27 08:44:45                    brand     : OS
    model     : THGR122N     House Code: 188
    Channel   : 1            Battery   : OK            Temperature: 22.90 C      Humidity  : 38 %
    
    :return:      Temperatur:              22.90 °C
                  Luftfeuchtigkeit:        38 %
 
    '''
    werte_liste=werte.stdout.split("\n")
    werte_liste2=werte_liste[3].split("     ")  

    temp=werte_liste2[-2].replace(" ","").split(":")
    phi=werte_liste2[-1].replace(" ","").split(":")

    print("\n")
    print("Temperatur:\t\t",(temp[1])[:-1], "°C")
    print("Luftfeuchtigkeit:\t",(phi[1][:-1]), "%")
    print("\n")

def hauptprogramm():

    cputemp()
    hw_status=check_sdr_hardware()
    if hw_status==1:
        print("Hardwarestatus:\t",hw_status)
        sensoren_auslesen()
    else:
        print("\n\n"\
              "\t###################################\n"\
              "\t#                                 #\n"\
              "\t#  Es ist ein Fehler aufgetreten! #\n"\
              "\t#  Die gesuchte Hardware ist      #\n"\
              "\t#  nicht vorhanden!               #\n"\
              "\t#                                 #\n"\
              "\t###################################\n")
    print("Das Hauptprogramm wurde ausgeführt!")


if __name__== "__main__":
    hauptprogramm()
