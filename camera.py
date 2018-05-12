from picamera import PiCamera
from time import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

camera = PiCamera()

camera.start_preview(fullscreen = False, window = (13,39, 645,480))
try:
        while True:
                i=GPIO.input(17)
                if i==0:                 #When output from motion sensor is LOW
                        print "No intruders"
                        camera.start_recording('/home/pi/Desktop/video.h264')
                        sleep(0.1)
                elif i==1:               #When output from motion sensor is HIGH
                        print "Intruder detected"
                        camera.stop_recording()
                        sleep(0.1)
                #sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()
        camera.stop_recording()
        camera.stop_preview()




