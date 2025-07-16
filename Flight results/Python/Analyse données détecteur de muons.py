"""

SCALAR V-a Charge utile
Analyse des données de vol du détecteur de muons


"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from math import floor

# Ouverture du fichier csv des données de vol
data = pd.read_csv("D:/SCUBE/SCALAR/SCALAR 5/Données de vol/Données de vol détecteur de muons/Données de vol détecteur de muons.csv", delimiter=" ", keep_default_na=False, encoding='latin-1')

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

# Analyse de la répartition des amplitudes des signaux des détections
Amplitudes = [100*x for x in range(25)]
Répartition = [0]*25
nb_total = 10509 # Nombre total de détections
for x in SiPM:
    i = floor(x/100)
    Répartition[i] += 1

Répartition = [x / nb_total * 100 for x in Répartition]

plt.bar(Amplitudes, Répartition, width=100, align='edge')
plt.xlabel('Signals amplitude (mV)')
plt.ylabel('Percentage of detections')
# plt.title('Distribution of the amplitudes of the detections')
plt.show()

# Analyse de la répartition des niveaux des détections sur l'ADC
Niveaux = [i for i in range(1024)]
Répartition = [0 for i in range(1024)]
nb_total = 10509 # Nombre total de détections
for x in ADC:
    Répartition[x] += 1

Répartition = [x / nb_total * 100 for x in Répartition]

plt.bar(Niveaux, Répartition, width=1, align='edge')
plt.xlabel('ADC levels')
plt.ylabel('Percentage of detections')
# plt.title('Distribution of the ADC levels of the detections')
plt.show()

# Analyse des propriétés statistiques des amplitudes des signaux

# Conversion de SiPM en array numpy pour faciliter les calculs
SiPM_array = np.array(SiPM)

# Calcul des propriétés statistiques
moyenne = np.mean(SiPM_array)
variance = np.var(SiPM_array)
ecart_type = np.std(SiPM_array)
quartiles = np.percentile(SiPM_array, [25, 50, 75])  # Quartiles Q1, médiane (Q2), Q3
min = np.min(SiPM_array)
max = np.max(SiPM_array)

# Affichage des résultats
print(f"Moyenne: {moyenne}")
print(f"Variance: {variance}")
print(f"Écart-type: {ecart_type}")
print(f"Quartiles: Q1={quartiles[0]}, Médiane={quartiles[1]}, Q3={quartiles[2]}")
print(f"Minimum: {min}")
print(f"Maximum: {max}")

# Analyse des propriétés statistiques des niveaux sur l'ADC

# Conversion de adc en array numpy pour faciliter les calculs
ADC_array = np.array(ADC)

# Calcul des propriétés statistiques
moyenne = np.mean(ADC_array)
variance = np.var(ADC_array)
ecart_type = np.std(ADC_array)
quartiles = np.percentile(ADC_array, [25, 50, 75])  # Quartiles Q1, médiane (Q2), Q3
min = np.min(ADC_array)
max = np.max(ADC_array)


# Affichage des résultats
print(f"Moyenne: {moyenne}")
print(f"Variance: {variance}")
print(f"Écart-type: {ecart_type}")
print(f"Quartiles: Q1={quartiles[0]}, Médiane={quartiles[1]}, Q3={quartiles[2]}")
print(f"Minimum: {min}")
print(f"Maximum: {max}")

# Répartition du temps entre desux détections

time_shifted = time[1:]
time_diff = time_shifted - time[:-1]
time_diff *= 60 # Conversion en secondes

plt.hist(time_diff, bins=100)
plt.xlabel('Time between two detections (s)')
plt.ylabel('Number of detections')
# plt.title('Distribution of the time between two detections')
plt.show()
