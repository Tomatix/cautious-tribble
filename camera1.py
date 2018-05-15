from picamera import PiCamera
from time import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

camera = PiCamera()

camera.start_preview(fullscreen = False, window = (13,39, 645,480))
recording = False
history = 1

try:
        while True:
                i=GPIO.input(17)
                if i==1:                #When output from motion sensor is LOW
                        if recording:
                                print "Recording my brutah"
                                camera.wait_recording(0.1)
                        else:
                                camera.start_recording('/home/pi/Desktop/{}.h264'. format(history))
                                print "recording"
                                recording = True
                else:                   #When output from motion sensor is HIGH
                        if recording:
                                sleep(120)
                                camera.stop_recording()
                                if (history > 5):
                                        history = 1
                                        recording = False
                                else:
                                        history += 1
                                        recording = False
                        

except KeyboardInterrupt:
        GPIO.cleanup()
        camera.stop_preview()




