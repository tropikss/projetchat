#coding : utf-8    f
from grovepi import *
from time import *

# retourne la position
# 0 = bas, 1 = droite, 2 = haut, 3 = gauche, 4 = centre
def read5way(adresse=0x03)
	sleep(0.1)
	lect = read_i2c_block(adresse)
	if lect[3] == 128:
		for i in range(4:10)
			if lect[i]=0:
				return i-4  
	return -1
