
from datetime import datetime

date_heure_actuelles = datetime.now()
nom = date_heure_actuelles.strftime("%H:%M:%S")

h = date_heure_actuelles.strftime("%H")
m = date_heure_actuelles.strftime("%M")
s = date_heure_actuelles.strftime("%S")

print(h, m, s)