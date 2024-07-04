"""
# SCALAR Va Charge Utile
# Programme de test de d'enregistrement des données du capteur d'aérosols
# Fait appel au programme __init__.py modifié du PMS5003 pour que les données soient retournées sous forme de
# chaîne de caractères pour être enregistrées dans un fichier csv sur la carte SD

"""


import time
from pms5003 import PMS5003

# Importations pour la carte SD
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


# Configure the PMS5003 for Enviro+
pms5003 = PMS5003(
    uart=machine.UART(1, tx=machine.Pin(8), rx=machine.Pin(9), baudrate=9600),
    pin_enable=machine.Pin(19),
    pin_reset=machine.Pin(18),
    mode="active"
)

file = open('/sd/data.csv', 'w')
file.write("PM1.0, PM2.5, PM10, PM1.0, PM2.5, PM10, >0.3um in 0.1L air, >0.5um in 0.1L air, >1.0um in 0.1L air, >2.5um in 0.1L air, >5.0um in 0.1L air, >10um in 0.1L air\n")  

while True:
    PMS_data = str(pms5003.read())
    print(PMS_data)
    print("\n")
    file.write(PMS_data)
    file.flush()
    print(PMS_data)
    time.sleep(1.0)
    
# Unmount SD card
os.umount('/sd')
