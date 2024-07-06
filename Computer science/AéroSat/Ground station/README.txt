## Codes de réceptiond des données de télémétrie d'AéroSat
## Par Florian Topeza

Pour recevoir les données d'AéroSat, il faut une Raspberry Pi Pico, un module Lorawan SX1262, une carte micro SD et son connecteur.

La librairie sdcard ainsi que les trois librairies sx du Lorawan doivent être téléversées sur la Pico.

Le module Lorawan se fixe sous la Pico, avec l'indicateur USB du côté du connecteur USB de la Pico.

Le pin GND du connecteur doit êter branché à l'un des pins GND de la Pico.
Le pin VCCC doit être branché au pin VBUS.
Le pin CS doit être branché au GPIO5.
Le pin SCK doit être branché au pin GPIO6.
Le pin MOSI doit être branché au pin GPIO7.
Le pin MISO doit être branché au pin GPIO4.

Lancer ensuite le programme rx.py depuis Thonny avec la Pico connectée. La console affiche "En attente d'un signal" jusqu'à recevoir des données.
