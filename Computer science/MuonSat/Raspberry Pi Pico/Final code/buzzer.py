# Berryrocket project
# Buzzer management
# Licence CC-BY-NC-SA
# Louis Barbier

import time
from machine import Pin,PWM,Timer

# Declaration d'un PWM pour le buzzer
buzzer = PWM(Pin(21))

# Declaration timer pour le buzzer et son extinction
timerBuzzer = Timer()
timerOffBuzzer = Timer()

# Variables pour le buzzer
freqBuzzer  = 500
tempsBuzzer = 0

# Management buzzer
def MgtBuzzer(timer):
    buzzer.freq(freqBuzzer)
    buzzer.duty_u16(32768) # Set to 50%
    timerOffBuzzer.init(freq=1.0/0.1, mode=Timer.ONE_SHOT, callback=SetOffBuzzer) # Ring the buzzer for this time (0.1s)

def SetOffBuzzer(timer):
    buzzer.duty_u16(0) # Set to 0%

# Mets en marche le buzzer pour la fréquence et la période indiquées
def SetBuzzer(enable=True, freq=500, tps=5.0):
    """Set the buzzer with a frequency and a time between ring"""
    global freqBuzzer
    freqBuzzer = freq
    timerBuzzer.deinit()
    if enable is True:
        timerBuzzer.init(freq=1.0/tps, mode=Timer.PERIODIC, callback=MgtBuzzer)
