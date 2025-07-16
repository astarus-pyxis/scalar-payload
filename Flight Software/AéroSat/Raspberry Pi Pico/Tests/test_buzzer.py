# Importations pour le buzzer
from buzzer import *

#Définition de la variable du buzzer
BUZZER_ENABLE = True

SetBuzzer(BUZZER_ENABLE, freq=2000, tps=1)
time.sleep(1)
SetBuzzer(False) 