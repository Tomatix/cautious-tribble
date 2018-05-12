from picamera import PiCamera
from time import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

camera = PiCamera()

camera.start_preview(fullscreen = False, window = (13,39, 645,480))
recording = False
try:
        while True:
                i=GPIO.input(17)
                if i==1:                 #When output from motion sensor is LOW
                        if recording:
                                camera.wait_recording(0.1)
                        print "No intruders"
                        camera.start_recording('/home/pi/Desktop/video.h264')
                        recording = True
                elif i==0:               #When output from motion sensor is HIGH
                        print "Intruder detected"
                        camera.stop_recording()
                        recording = False
                        sleep(0.1)

except KeyboardInterrupt:
        GPIO.cleanup()
        if recording:
                camera.stop_recording()
        camera.stop_preview()




