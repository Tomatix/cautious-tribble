import sys
import os
from Tkinter import *
from picamera import PiCamera

#import RPi.GPIO as GPIO
#import time

#GPIO.setWarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN)
#GPIO.setup(22, GPIO.OUT)

def start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Inside_display (root)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Inside_display (w)
    return (w, top)

def destroy_Inside_display():
    global w
    w.destroy()
    w = None




# class that creates the Inside display
class Inside_display:
    def __init__(self, top=None):
		

        # This class configures and populates the toplevel window.
        # top is the toplevel containing window.
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Times New Roman} -size 30 -weight normal "  \
                "-slant roman -underline 0 -overstrike 0"

        top.geometry("800x480")
        top.title("Jarvis")
        top.configure(background="#2b287a")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        
        def panic():
                pass
                        
        def talk():
                pass
                        
        def lock():
                pass
                        
        def unlock():
                pass

        # might not work `
        def display(x, y, h, w):
            global camera
            camera = PiCamera()
            camera.preview_fullscreen = False
            camera.resolution = (1920, 1080)
            camera.preview_window = (x, y, h, w)
            #camera.start_preview()

            take_picture_frame = Frame(width = x, height = x, bg = "white", cursor = "none")
            take_picture_frame.place(x = x, y = y)
            take_picture_frame.bind("Label1", take_picture())

        def take_picture():
            i = 0
            cwd = os.path.dirname(os.path.abspath(__file__))
            while os.path.exists(cwd + "/image%s.png" % i):
                i += 1
            camera.capture(cwd + "/image%s.png" % i)

##        # creates the out side of the gui
##        Frame1 = Frame(top)
##        Frame1.place(relx=0.01, rely=0.04, relheight=0.88, relwidth=0.92)
##        Frame1.configure(relief=GROOVE)
##        Frame1.configure(borderwidth="2")
##        Frame1.configure(relief=GROOVE)
##        Frame1.configure(background="#2b287a")
##        Frame1.configure(highlightbackground="#d9d9d9")
##        Frame1.configure(highlightcolor="black")
##        Frame1.configure(width=795)
        
        # creates and sets the video to the left side of the gui
        Label1 = Label(top)
        Label1.place(relx=0.0, rely=0.0, height=476, width=652)
        Label1.configure(activebackground="#f9f9f9")
        Label1.configure(activeforeground="black")
        Label1.configure(background="#686868")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=font11)
        Label1.configure(foreground="#000000")
        Label1.configure(highlightbackground="#d9d9d9")
        Label1.configure(highlightcolor="black")
        #Label1.configure(text='''Video''')
        # might not work
        display(0, 0, 476, 652)

        # creates the panic button at the top right of the gui
        Button1 = Button(top)
        # sets the button in it's appropriate place at its appropriate size
        Button1.place(relx=0.84, rely=0.04, height=93, width=96)
        # when the button is pressed the back ground changes color
        Button1.configure(activebackground="#d9d9d9")
        # sets the back ground color
        Button1.configure(background="black")
        # sets the width of the border
        Button1.configure(borderwidth="10")
        # when the button is pressed it calls the appropriate function 
        Button1.configure(command=lambda:panic())
        # when the mouse is over the button it changes the arrow to a hand 
        Button1.configure(cursor="hand2")
        _img1 = PhotoImage(file="sos.gif")
        Button1.configure(image=_img1)
        Button.image=_img1
        Button1.configure(pady="0")
        Button1.configure(text='''panic''')
        Button1.configure(width=96)
        
        # creates the Talk button under the panic button
        Button1_1 = Button(top)
        Button1_1.place(relx=0.84, rely=0.28, height=93, width=96)
        Button1_1.configure(activebackground="#d9d9d9")
        Button1_1.configure(background="#7a7a7a")
        Button1_1.configure(borderwidth="10")
        Button1_1.configure(command=lambda:talk())
        Button1_1.configure(cursor="hand2")
        _img2 = PhotoImage(file="Talk-icon.gif")
        Button1_1.configure(image=_img2)
        Button1_1.configure(pady="0")
        Button1_1.image=_img2
        Button1_1.configure(text='''Talk''')
        Button1_1.configure(width=96)
        
        # creates the unlock button under the talk button
        Button1_2 = Button(top)
        Button1_2.place(relx=0.84, rely=0.52, height=93, width=96)
        Button1_2.configure(activebackground="#d9d9d9")
        Button1_2.configure(background="#7a7a7a")
        Button1_2.configure(borderwidth="10")
        Button1_2.configure(command=lambda:lock())
        Button1_2.configure(cursor="hand2")
        _img3 = PhotoImage(file="Lock-icon.gif")
        Button1_2.configure(image=_img3)
        Button1_2.image=_img3
        Button1_2.configure(pady="0")
        Button1_2.configure(text='''unlock''')
        Button1_2.configure(width=96)
        
        # creates the lock button under the unlock button
        Button1_3 = Button(top)
        Button1_3.place(relx=0.84, rely=0.76, height=93, width=96)
        Button1_3.configure(activebackground="#d9d9d9")
        Button1_3.configure(background="black")
        Button1_3.configure(borderwidth="10")
        Button1_3.configure(command=lambda:unlock())
        Button1_3.configure(cursor="hand2")
        _img4 = PhotoImage(file="Unlock-icon.gif")
        Button1_3.configure(image=_img4)
        Button1_3.image=_img4
        Button1_3.configure(pady="0")
        Button1_3.configure(text='''lock''')
        Button1_3.configure(width=96)




if __name__ == '__main__':
    start_gui()


