
import time
import grovepi
import openCV

import driver_ultrasonic as ultrasonic
import driver_led as led
import grove_rgb_lcd as lcd
import driver_button
import driver_camera as picam
import drive 
import os

from datetime import datetime

wait = [0, 0, 255]
process = [255, 255, 0]
done = [0, 255, 0]
error = [255, 0, 0]

# --------------------------------- INITIALISATION ----------------------------------

picam.initPhoto(640, 480)			# camera

led.init()							# led 1 et 2

#lcd.init()							# ecran lcd
#lcd.background()

# ----------------------------------- LIBRAIRIE ---------------------------------------
	
def message(type, message):
	shift = 128

	r = type[0]-shift
	g = type[1]-shift
	b = type[2]-shift

	lcd.setRGB(r,g,b)
	lcd.setText(message)

def delete(chemin_fichier):
    """
    Supprime le fichier spécifié par le chemin_fichier.
    """
    try:
        # Vérifie si le fichier existe avant de le supprimer
        if os.path.exists(chemin_fichier):
            # Supprime le fichier
            os.remove(chemin_fichier)
            print(f"deleted : {chemin_fichier}")
        else:
            print(f"Le fichier {chemin_fichier} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression du fichier {chemin_fichier}: {e}")

def deleteAll():
	repertoire = "photo/"
	try:
		# Liste de tous les fichiers dans le répertoire
		fichiers = os.listdir(repertoire)

		# Parcourir la liste et supprimer chaque fichier
		for fichier in fichiers:
			chemin_fichier = os.path.join(repertoire, fichier)
			if os.path.isfile(chemin_fichier):
				os.remove(chemin_fichier)
				print(f"Fichier supprimé : {fichier}")

		print("Tous les fichiers ont été supprimés avec succès.")
	except Exception as e:
		print(f"Une erreur s'est produite : {e}")

def uploadAll(directory_path):
	try:
		# Obtient la liste de fichiers dans le répertoire
		files = os.listdir(directory_path)

		# Parcourt tous les fichiers dans le répertoire
		for file_name in files:
			# Construit le chemin complet du fichier
			file_path = os.path.join(directory_path, file_name)

			# Vérifie si le chemin correspond à un fichier
			if os.path.isfile(file_path):
				# Appelle la fonction pour traiter le fichier
				drive.upload(file_path)
				delete(file_path)

	except Exception as e:
		print(f"Une erreur s'est produite : {e}")

last = None

def compare(repertoire):
	# Liste des fichiers dans le répertoire
	fichiers = os.listdir(repertoire)

	# Filtrer les fichiers pour ne conserver que les fichiers (pas les répertoires)
	fichiers = [fichier for fichier in fichiers if os.path.isfile(os.path.join(repertoire, fichier))]

	# Vérifier s'il y a au moins deux fichiers
	if len(fichiers) == 2:
		# Récupérer les deux premiers fichiers
		p1, p2 = os.path.join(repertoire, fichiers[0]), os.path.join(repertoire, fichiers[1])

		print("p1 : "+str(p1))
		print("p2 : "+str(p2))

		global last
		if last is None :
			last = p1

		if(openCV.mouvement(p1, p2)) :
			
			print("                                     MOUVEMENT")
			led.on()
			if(p1 == last):
				drive.upload(p2)
			else :
				drive.upload(p1)
		
		else :
			led.off()
			print("                                     AUCUN MOUVEMENT")
		
		if(p1 == last):
			delete(last)
			last = p2
		elif(p2 == last):
			delete(last)
			last = p1

	elif(len(fichiers) < 2):
		print("Pas assez de fichier")
	else :
		deleteAll()
		print("deleteAll")

def shoot():
	date_heure_actuelles = datetime.now()
	nom = date_heure_actuelles.strftime("%H:%M:%S")

	picam.shoot(nom)
	time.sleep(1)

	return(nom)

def shoot_upload():

	date_heure_actuelles = datetime.now()
	nom = date_heure_actuelles.strftime("%H:%M:%S")

	message(error, "Ne bougez plus !")
	picam.shoot(nom)

	message(process, "Upload en cours")
	time.sleep(2)
	drive.upload(nom)

	message(done, "Upload termine")

distance = 100
n = 10

ultrasonicTab = [distance] * n

i = 0

def moy(tab):
	res = 0
	for i in range(len(tab)-1):
		res += tab[i]
	return int(res/(len(tab)-1))

def moyUltrasonic():

	global i

	u = ultrasonic.getValue()

	if(i >= 10):
		i = 0
		u += 1

	ultrasonicTab[i] = u

	i += 1

	print(str(ultrasonicTab)+" - "+str(moy(ultrasonicTab))+" - "+str(ultrasonic.getValue()))
	return moy(ultrasonicTab)

# ----------------------------------- DEBUT CODE -------------------------------------------------

while True:
	date_heure_actuelles = datetime.now()
	nom = date_heure_actuelles.strftime("%H:%M:%S")

	h = date_heure_actuelles.strftime("%H")
	m = date_heure_actuelles.strftime("%M")
	s = date_heure_actuelles.strftime("%S")

	message(done,nom)

	print("shoot start")
	shoot()
	print("shoot end")

	time.sleep(0.5)

"""while True: 
	
	date_heure_actuelles = datetime.now()
	nom = date_heure_actuelles.strftime("%H:%M:%S")

	h = date_heure_actuelles.strftime("%H")
	m = date_heure_actuelles.strftime("%M")
	s = date_heure_actuelles.strftime("%S")

	led.led1on()
	lcd.setRGB(0, 0, 100)
	lcd.setText(nom)

	time.sleep(0.5)

	led.led1off()

	time.sleep(0.5)

	shoot()
	compare("photo/")
	time.sleep(2)
	"""

