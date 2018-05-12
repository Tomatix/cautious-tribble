from picamera import PiCamera
from time import *

camera = PiCamera()

camera.start_preview(fullscreen = False, window = (13,39, 645,480))
try:
        while True:
                sleep(1)

except KeyboardInterrupt:
        camera.stop_preview()




