"""

SCALAR V-a Charge utile
Affichage des données de vol du détecteur de muons


"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Ouverture du fichier csv des données de vol
data = pd.read_csv("D:/SCUBE/Scalar/Données de vol/Données de vol détecteur de muons/Données de vol détecteur de muons.csv", delimiter=" ", keep_default_na=False, encoding='latin-1')

# Détections
data['Event'] = data['Event'].astype(int) # Conversion en flottant
Event = data['Event'].tolist() # Conversion en liste

# Temps
data['Ardn_time[ms]'] = data['Ardn_time[ms]'].astype(float) # Conversion en flottant
time = data['Ardn_time[ms]'].tolist() # Conversion en liste
time = np.array(time) / 60000 # Conversion du temps en minutes

# ADC
data['ADC[0-1023]'] = data['ADC[0-1023]'].astype(int) # Conversion en flottant
ADC = data['ADC[0-1023]'].tolist() # Conversion en liste

# SiPM
data['SiPM[mV]'] = data['SiPM[mV]'].astype(float) # Conversion en flottant
SiPM = data['SiPM[mV]'].tolist() # Conversion en liste

# Température
data['Temp[C]'] = data['Temp[C]'].astype(float) # Conversion en flottant
Temp = data['Temp[C]'].tolist() # Conversion en liste

# Température au cours du temps
plt.scatter(time, Temp, marker='+', s=10, linewidths=0.5)
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (C)')
#plt.title('Temperature through time in the muon detector compartment')
plt.show()

# Amplitude des signaux à chaque détection
plt.scatter(Event, SiPM, marker='+', s=20, linewidths=1)
plt.xlabel('Detections')
plt.ylabel('Amplified signal (mV)')
#plt.title('Amplitude of the signals of the detections')
plt.show()

# Niveau sur l'ADC à chaque détection
plt.scatter(Event, ADC, marker='+', s=20, linewidths=1)
plt.xlabel('Detections')
plt.ylabel('ADC level')
#plt.title('ADC level of the detections')
plt.show()

# Nombre de muons détectés au cours du temps
plt.scatter(time, Event, marker='+', s=10, linewidths=0.5)
plt.xlabel('Time (minutes)')
plt.ylabel('Number of detections')
#plt.title('Number of muons detected through time')
plt.show()

plt.scatter(ADC, SiPM, marker='+', s=20, linewidths=1)
plt.xlabel('ADC value')
plt.ylabel('Amplified signal (mV)')
#plt.title('Amplitude of the signals of the detections')
plt.show()