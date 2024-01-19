import time
import grovepi

class button:
    def __init__(self, pin):
        self.pin = pin
        grovepi.pinMode(pin, "INPUT")
        
    def state(self):
        return(grovepi.digitalRead(self.pin) == 1)