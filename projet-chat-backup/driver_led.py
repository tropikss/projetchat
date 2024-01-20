import grovepi
import time

LED_PIN1 = 7
LED_PIN2 = 8

def init():
    grovepi.pinMode(LED_PIN1, "OUTPUT")
    grovepi.pinMode(LED_PIN2, "OUTPUT")

def led1on():
    grovepi.digitalWrite(LED_PIN1, 1)
    
def led1off():
    grovepi.digitalWrite(LED_PIN1, 0)

def led2on():
    grovepi.digitalWrite(LED_PIN2, 1)
    
def led2off():
    grovepi.digitalWrite(LED_PIN2, 0)
