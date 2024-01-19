
import time
import random as r

distance = 100
n = 10

ultrasonicTab = [distance] * n + [0]

i = 0

def moy(tab):
	res = 0
	for i in range(len(tab)-1):
		res += tab[i]
	return int(res/(len(tab)-1))

def moyUltrasonic():

	global i
	u = r.randint(0, 255)

	if(i >= 10):
		i = 0
		u += 1

	ultrasonicTab[i] = u
	ultrasonicTab[10] = moy(ultrasonicTab)

	i += 1

	print(ultrasonicTab)

while True: 
	moyUltrasonic()
	time.sleep(0.05)

