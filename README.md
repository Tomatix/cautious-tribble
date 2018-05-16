# cautious-tribble
CYEN 132 project


While running the camera file, it has a key interrupt (Ctrl + C) that will stop running the code.

On the inside display there is a gui running in the back ground. This is done because the gui in the back ground is updating the time on the outside display.Do not close the gui in the background or else program will not run properly, you MUST use control+C keyboard interrupt to close the program, else you will be forced to terminate with alt+ctrl+delete.


On the outside display, we could not get the camera to display on the gui. So, we made two files one for the gui and one for the camera. The camera takes over the entire screen when it is displayed, with this we resized it to fit the proper spot on the gui. Now, it will appear to be one entire gui. 


Make sure Pi-Camera is intilaized if you want to do this project on your own on another pi. Native Pi-Camera support enable in settings and reboot. 
