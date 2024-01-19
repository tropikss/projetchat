
import time
import grovepi

import driver_ultrasonic as ultrasonic
import driver_led as led
import driver_ecran as lcd
import driver_button
import driver_camera as picam
import drive 

from datetime import datetime

wait = [0, 0, 255]
process = [255, 255, 0]
done = [0, 255, 0]
error = [255, 0, 0]


picam.initPhoto(640, 480)
led.init()
lcd.init()
	
def message(type, message):
	shift = 128

	for i in range(len(type)):
		type[i] = type[i]-shift

	lcd.clear()
	lcd.setRGB(type)
	lcd.setText(message)

def shoot_upload():

	date_heure_actuelles = datetime.now()
	nom = date_heure_actuelles.strftime("%Y-%m-%d %H:%M:%S")

	message(error, "Ne bougez plus !")
	picam.shoot(nom)

	message(process, "Upload en cours")
	time.sleep(2)
	drive.upload(nom)

	message(done, "Upload termine")

lcd.background()
displayed = False
distance = 100

delay = 0.1
times = 1
n = times/delay
res = 0
last = 0
i = 0

while True:
	v = ultrasonic.getValue()
	print("v:"+str(v))
	close = v < distance
	 
	if(close):
		message(error, "stop")
	else :
		message(wait, "Attente...")
	

	v = v/n
	res += v
	res -= last
	last = v
	print("res: "+str(res))
	i += 1

	if(i >= times/delay):
		if(v < distance):
			print("someone close")
			led.on()
			shoot_upload()
	
	# delai pour pas tout cramer
	time.sleep(0.1)
