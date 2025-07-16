## SCALAR Va Charge Utile - Descriptif des programmes Raspberry Pi Pico MuonSat ##

# Codes sources originaux #

Ce dossier contient les codes sources tels qu'ils ont été téléchargés.

lib contient les codes sources pour écrire des données sur une carte SD.
micropySX126X contient les codes sources pour utiliser le module LoRa Wan.
Pico-GPS-L76B_Code2 contient les codes sources pour utiliser le GPS L76B. Ces codes fonctionnent également pour utiliser le GPS Locosys LS20031, avec un baudrate de 57600 bauds pour la Raspberry Pi Pico.

# Tests #

Ce dossier contient des fichiers pour tester le GPS, le LoRa Wan et la carte SD. La plupart sont issus des dossiers des codes sources originaux.

test_gps sert à tester l'envoi de données par le GPS Locosys LS20031
test_main sert à tester la réception, l'écriture et l'envoi des données GPS.
test_main_sequence est un test du code complet utilisé pour le lancement réel, il reprend les tests de test_main et intègre également l'utilisation du buzzer, la détection du décollage et de l'atterrissage.

# Code source final #

Ce dossier contient les librairies nécessaires au bon fonctionnement des appareils du Cansat et le code main utilisé au cours du vol.







