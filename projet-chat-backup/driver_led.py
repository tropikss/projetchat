import grovepi
import time

LED_PIN = 7


def init():
    grovepi.pinMode(LED_PIN, "OUTPUT")

def ledon():
    grovepi.digitalWrite(LED_PIN, 1)
    
def ledoff():
    grovepi.digitalWrite(LED_PIN, 0)
