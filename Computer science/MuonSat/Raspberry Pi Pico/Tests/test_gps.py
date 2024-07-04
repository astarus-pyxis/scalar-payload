"""
# SCALAR Va Charge Utile
# Programme de test de réception des données GPS brutes

"""


from machine import UART
import time

# Configuration du port UART
adaGPS = UART(0, baudrate=9600, bits=8, parity=None, stop=1)

# Initialisation du fichier d'écriture des données
#file = open("gps_data.csv", "a")
#file.write("UTC, latitude, NS, longitude, EW, satellites_used, MSL_altitude, course_over_ground, speed_kmh\n")

# Lecture des données GPS
while True:

    data = adaGPS.read()
    if data is not None:
        print("Raw data:", data)
    else:
        print("none")
#        print("decoded data:", data.decode('ascii'))
#         # Traitement des données GPS
#         # Attention, comme ce programme n'utilise pas de parser pour gérer les erreurs de réception, il s'arrête dès qu'une phrase
#         # reçue est corrompue.
#         for line in decoded_data.split('\r\n'):
#             # Lecture de la phrase GGA
#             if line.startswith("$GPGGA"):
#                 # On déoupe les champs de la phrase
#                 fields = line.split(',')
#                 # Extraction des données utiles
#                 UTC = fields[1]  # UTC time
#                 latitude = fields[2] #Latitude
#                 NS = fields[3] #N/S indicator
#                 longitude = fields[4] #Longitude
#                 EW = fields[5] #E/W indicator
#                 satellites_used = fields[7] #Nombre de satellites utilisés
#                 MSL_altitude = fields[9] #MSL altitude
#                 file.write("{},{},{},{},{},{},{},".format(UTC, latitude, NS, longitude, EW, satellites_used, MSL_altitude))
#                 file.flush()
#                 
#                 print("UTC:", UTC)
#                 print("Latitude:",latitude)
#                 print(NS)
#                 print("Longitude:", longitude)
#                 print(EW)
#                 print("Satellites in use:", satellites_used)
#                 print("MSL altitude:", MSL_altitude)
#                 
#             # Lecture de la phrase GPVTG
#             if line.startswith("$GPVTG"):
#                 fields = line.split(',')
#                 course_over_ground = fields[1] #orientation mesurée en degrés
#                 speed_over_ground = fields[7] #vitesse en km/h
#                 file.write("{},{}\n".format(course_over_ground, speed_over_ground))
#                 file.flush()
#                 
#                 print("Course over ground:", course_over_ground)
#                 print("Speed over ground (km/h):", speed_over_ground)
#                 
#                 print("\n")

                




