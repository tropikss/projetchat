import grovepi
import time

LED_PIN = 7

def init():
    grovepi.pinMode(LED_PIN, "OUTPUT")

def on():
    grovepi.digitalWrite(LED_PIN, 1)
    
def off():
    grovepi.digitalWrite(LED_PIN, 0)
