# coding: utf-8
import smbus
import time

bus = smbus.SMBus(1)  # pour I2C-1 (0 pour I2C-0)

# Indiquez ici les deux adresses de l'ecran LCD
# celle pour les couleurs du fond d'ecran 
# et celle pour afficher des caracteres
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

def init():
	# couleur 
	bus.write_byte_data(DISPLAY_RGB_ADDR, 0x00, 0x00)
	time.sleep(0.1)
	bus.write_byte_data(DISPLAY_RGB_ADDR, 0x01, 0x00)
	time.sleep(0.1)

	# ecran
	bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, 0x01)
	time.sleep(0.1)
	bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, 0x0F)
	time.sleep(0.1)
	bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, 0x38)
	time.sleep(0.1)

def clear():
	bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, 0x01)
	time.sleep(0.05)

def background():
	bus.write_byte_data(DISPLAY_RGB_ADDR, 0x08, 0xAA)

# Completez le code de la fonction permettant de choisir la couleur
# du fond d'ecran, n'oubliez pas d'initialiser l'ecran
def setRGB(type):
	# rouge, vert et bleu sont les composantes de la couleur qu'on vous demande
	'''
	rouge = hex(rouge)
	vert = hex(vert)
	bleu = hex(bleu)
	
	print(rouge, bleu, vert)
	'''
	bleu = type[0]
	vert = type[1]
	rouge = type[2]

	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,rouge)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,vert)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,bleu)

# Envoie  a l'ecran une commande concerant l'affichage des caracteres
# (cette fonction vous est donnes gratuitement si vous
# l'utilisez dans la fonction suivante, sinon donnez 2000€
# a la banque et allez dictement en prison :)
def textCmd(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(cmd))
    time.sleep(0.01)

#cette fonction permet l'affichage d'un saut de ligne
def line():
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0xc0)

# Cette fonction affiche le texte sur l'écran, 16
#charactères sur 1 ligne. 

def setText(texte):
	for i in range(len(texte)):
		if(i == 16):
			line()
			time.sleep(0.01)
		textCmd(texte[i])
		time.sleep(0.01)

"""def setText(texte):
	TAILLE_LIGNE = 16
	c=0
	for i in texte:
		c=c+1
		l=0
		if c == 16 or i == "\n":
			line()
			l=1
			c=0
		if c > 1 :
			time.sleep(0.01)
			clear()
			l=0
			c=0
		textCmd(i)"""
