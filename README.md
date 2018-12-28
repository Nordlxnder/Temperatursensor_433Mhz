# Temperatursensoren auszulesen die über die Frequenz 433 MHz senden 


## Hardware:
    Raspberry 3 B+
    USB Stick mit RTL2838 DVB-T
         
## Software: 
    OS Arch Linux mit Kernel 4.14.90-1-ARCH
       
       
       
## Schritt 1:

   #### Installation der Pakete um den Teiber zu kompilieren
    
    sudo pacman -S cmake community/rtl-sdr
    
## Schritt 2:
   
   #### Treiber installieren
   
    git clone https://github.com/merbanan/rtl_433.git
    cd rtl_433/
    mkdir build
    cd build/
    cmake ../
    make
    sudo make install
   
## Schritt 3: 
    
   #### Kerneltreiber deaktivieren( Datei wird während angelegt )
    
    /etc/modprobe.d/rtlsdr.conf
    
            # disable DVB drivers
            blacklist rtl2830
            blacklist rtl2832
            blacklist dvb_usb_rtl28xxu

   #### Neustart des Raspberrys
    
    sudo reboot
        
## Schritt 4:

   #### Start des Programm und auf Sender warten(dies kann einige Minuten dauern)
    
    rtl_433 -G 
