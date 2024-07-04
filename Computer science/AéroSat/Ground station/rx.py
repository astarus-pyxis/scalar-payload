"""
# SCALAR Va Charge Utile
# Programme de réception des données d'AéroSat

"""

# Importation du module LoRawan
from sx1262 import SX1262
import time

# Importation du module de la carte SD
import os
from machine import Pin, SPI
import sdcard

# Configuration de la carte SD
SD_CS_PIN = 5
SD_SCK_PIN = 6
SD_MOSI_PIN = 7
SD_MISO_PIN = 4
spi = SPI(0, baudrate=100000, sck=Pin(SD_SCK_PIN), mosi=Pin(SD_MOSI_PIN), miso=Pin(SD_MISO_PIN))

sd = sdcard.SDCard(spi, Pin(SD_CS_PIN))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')

# Configuration du LoRa Wan
sx = SX1262(spi_bus=1, clk=10, mosi=11, miso=12, cs=3, irq=20, rst=15, gpio=2)

# La fréquence d'émission du module est de 434MHz (norme EU433), avec un pas de 125kHz, un facteur d'étalement de 9,
# un taux de codage de 4/5, un mot de synchronisation de 0x12, une puissance de 10dBm, une limite de courant de 60mA,
# une longueur de préambule de 8 octets, une longueur d'implicite de 0xFF, un CRC activé, une modulation IQ désactivée,
# un TCXO de 1.6V, un régulateur LDO désactivé, et un mode bloquant.

# La puissance est limitée à 10dBm pour respecter le cahier des charges du CNES.
sx.begin(freq=434.0, bw=125.0, sf=9, cr=7, syncWord=0x12,
        power=10, currentLimit=60.0, preambleLength=8,
        implicit=False, implicitLen=0xFF,
        crcOn=True, txIq=False, rxIq=False,
        tcxoVoltage=1.6, useRegulatorLDO=False, blocking=True)

# Les données du GPS et du PMS sont enregistrées sur la carte SD, dans le fichier data.csv.
file = open('/sd/data.csv', 'a')
file.write("execution_time, WGS84 _latitude_parser, WGS84_latitude, WGS84_longitude_parser, WGS84_longitude, UTC_timestamp, Altitude, PM1.0, PM2.5, PM10, PM1.0, PM2.5, PM10, >0.3um in 0.1L air, >0.5um in 0.1L air, >1.0um in 0.1L air, >2.5um in 0.1L air, >5.0um in 0.1L air, >10um in 0.1L air\n") # En-tête du fichier CSV    
file.flush()

# boucle pricipale
while True:
    print("En attente d'un signal.\n")
    msg, err = sx.recv()
    if len(msg) > 0:
        error = SX1262.STATUS[err]
        print(msg) # Affichage du message reçu
        print(error) # Affichage de l'erreur

        # Enregistrement du message dans le fichier data.csv
        file.write(msg)
        file.write("\n")
        file.flush()
        time.sleep(0.1) # Attente de 0.1s pour éviter les erreurs de lecture/écriture

# Démontage de la carte SD
os.umount('/sd')

