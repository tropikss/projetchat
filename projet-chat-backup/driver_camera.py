

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import time

picam = Picamera2()

def initPhoto(w, h):
    conf = picam.create_still_configuration(main={"size": (w, h)})
    picam.configure(conf)
    picam.start()
    print("init picam")

def shoot(nom):
    picam.capture_file("photo/"+nom+".jpg", quality = 50)

