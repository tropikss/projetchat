import grovepi
import time

grovepi.set_bus("RPI_1")

ultrasonic_ranger = 2

def getValue():
    return(grovepi.ultrasonicRead(ultrasonic_ranger))

