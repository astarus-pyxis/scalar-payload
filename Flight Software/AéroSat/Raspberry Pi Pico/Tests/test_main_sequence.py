"""
# SCALAR Va Charge Utile
# Programme de test du programme complet d'AéroSat

"""


# Importations pour la carte SD
import os
from machine import Pin, SPI
import sdcard

# Importations pour le GPS
import time
from L76 import l76x
import math
import hashlib
from L76.micropyGPS.micropyGPS import MicropyGPS

# Importation pour le LoRa Wan
from sx1262 import SX1262

# Importations pour le PMS5003
from pms5003 import PMS5003

# Importations pour le buzzer
from buzzer import *

#Définition de la variable du buzzer
BUZZER_ENABLE = True

# Buzzer de début d'initialisation
SetBuzzer(BUZZER_ENABLE, freq=800, tps=1)
time.sleep(1)
SetBuzzer(False)





"""boucle"""

if __name__ == '__main__':



    # Configuration de la carte SD
    SD_CS_PIN = 5
    SD_SCK_PIN = 6
    SD_MOSI_PIN = 7
    SD_MISO_PIN = 4
    spi = SPI(0, baudrate=100000, sck=Pin(SD_SCK_PIN), mosi=Pin(SD_MOSI_PIN), miso=Pin(SD_MISO_PIN))

    sd = sdcard.SDCard(spi, Pin(SD_CS_PIN))
    vfs = os.VfsFat(sd)
    os.mount(vfs, '/sd')


    # Configuration du GPS Locosys LS20031, le code utilisé est celui du GPS L76
    UARTx = 0
    BAUDRATE = 57600 #Il s'agit du baudrate adapté au module Locosys, pour le module L76, prendre BAUDRATE = 9600
    gnss_l76b=l76x.L76X(uartx=UARTx,_baudrate = BAUDRATE)
    gnss_l76b.l76x_exit_backup_mode()
    gnss_l76b.l76x_send_command(gnss_l76b.SET_SYNC_PPS_NMEA_ON)
    parser = MicropyGPS(location_formatting='dd')
    sentence = ''


    # Configuration du LoRa Wan
    sx = SX1262(spi_bus=1, clk=10, mosi=11, miso=12, cs=3, irq=20, rst=15, gpio=2)

    sx.begin(freq=434.0, bw=125.0, sf=9, cr=7, syncWord=0x12,
            power=22, currentLimit=60.0, preambleLength=8,
            implicit=False, implicitLen=0xFF,
            crcOn=True, txIq=False, rxIq=False,
            tcxoVoltage=1.6, useRegulatorLDO=False, blocking=True)


    # Configuration du PMS5003
    pms5003 = PMS5003(uart=machine.UART(1, tx=machine.Pin(8), rx=machine.Pin(9), baudrate=9600),pin_enable=machine.Pin(19),pin_reset=machine.Pin(18),mode="active")


    # Les données du GPS et du PMS sont enregistrées sur la carte SD, dans le fichier data.csv.
    file = open('/sd/data.csv', 'a')
    file.write("execution_time, WGS84 _latitude_parser, WGS84_latitude, WGS84_longitude_parser, WGS84_longitude, UTC_timestamp, Altitude, PM1.0, PM2.5, PM10, PM1.0, PM2.5, PM10, >0.3um in 0.1L air, >0.5um in 0.1L air, >1.0um in 0.1L air, >2.5um in 0.1L air, >5.0um in 0.1L air, >10um in 0.1L air\n")    


    # Buzzer de fin d'initialisation
    SetBuzzer(BUZZER_ENABLE, freq=800, tps=0.2)
    time.sleep(0.6)

    # Initialisation du temps
    start_time = time.ticks_ms()

    while True:

        # Buzzer de vol
        SetBuzzer(BUZZER_ENABLE, freq=1500, tps=1)


        end_time = time.ticks_ms()
        execution_time = time.ticks_diff(end_time, start_time)/1000

        # Récupération des données GPS
        if gnss_l76b.uart_any():
            sentence = parser.update(chr(gnss_l76b.uart_receive_byte()[0]))
                
            if sentence:

                print('WGS84 Coordinate:Latitude(%c),Longitude(%c) %.9f,%.9f'%(parser.latitude[1],parser.longitude[1],parser.latitude[0],parser.longitude[0]))
                    
                sx.send(b"WGS84 Coordinate:Latitude(%c),Longitude(%c) %.9f,%.9f"%(parser.latitude[1],parser.longitude[1],parser.latitude[0],parser.longitude[0]))
                    
                print('UTC Timestamp:%d:%d:%d'%(parser.timestamp[0],parser.timestamp[1],parser.timestamp[2]))
                
                sx.send(b"UTC Timestamp:%d:%d:%d"%(parser.timestamp[0],parser.timestamp[1],parser.timestamp[2]))
                    
                #print fix status
                '''
                1 : NO FIX
                2 : FIX 2D
                3 : FIX_3D
                '''
                print('Fix Status:', parser.fix_stat)
                    
                print('Altitude:%d m'%(parser.altitude))
                print('Height Above Geoid:', parser.geoid_height)
                print('Horizontal Dilution of Precision:', parser.hdop)
                print('Satellites in Use by Receiver:', parser.satellites_in_use)
                print('')

                PMS_data = str(pms5003.read())
                print(PMS_data)

                sx.send(b"PMS data: %s"%PMS_data)

                # On écrit les données sur la carte SD
                file.write(str(execution_time) + "," + str(parser.latitude[1]) + "," + str(parser.latitude[0]) + "," + str(parser.longitude[1]) + "," + str(parser.longitude[0]) + "," + str(parser.timestamp[0]) + ":" + str(parser.timestamp[1]) + ":" + str(parser.timestamp[2]) + "," + str(parser.altitude) + "," + PMS_data + "\n")

                file.flush()

                    

    # On ferme le fichier et on démonte la carte SD
    os.umount('/sd')

                



