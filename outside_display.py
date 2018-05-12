import sys
import RPi.GPIO as GPIO
import pygame
from time import *
from Tkinter import *


led = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)



def start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	global localtime
	root = Tk()
	top = Jarvis (root)
	App() 
	root.mainloop()

w = None
def create_Jarvis(root, *args, **kwargs):
	'''Starting point when module is imported by another program.'''
	global w, w_win, rt
	rt = root
	w = Toplevel (root)
	top = Jarvis (w)
	return (w, top)

def destroy_Jarvis():
	global w
	w.destroy()
	w = None





wrong_pin = []	
operater = 'Enter Passcode'	
Star_list = ''

class Jarvis:
	def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85' 
		_ana2color = '#d9d9d9' # X11 color: 'gray85' 
		font11 = "-family {Times New Roman} -size 30 -weight bold "  \
			"-slant roman -underline 0 -overstrike 0"
		font12 = "-family {Times New Roman} -size 24 -weight bold "  \
			"-slant roman -underline 0 -overstrike 0"
		font14 = "-family {Times New Roman} -size 36 -weight bold "  \
			"-slant roman -underline 0 -overstrike 0"
		font10 = "-family {Times New Roman} -size 20 -weight bold "  \
			"-slant roman -underline 0 -overstrike 0"
		font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
			"roman -underline 0 -overstrike 0"

		top.geometry("800x480")
		top.title("Jarvis")
		top.configure(background="#2b287a")
		top.configure(highlightbackground="#d9d9d9")
		top.configure(highlightcolor="black")

		display = StringVar()
		display.set(operater)
		
		# when any button is pressed it adds it to the display
		def buttonclick(num):
			global Star_list 
			global operater
			if (operater == "Alarm"):
				pass
			# if correct/incorrect/Enter Passcode are on the display it clears it and adds the button that was pressed
			# else it just adds the button pressed to the display
			elif ((operater == 'Correct') or (operater == 'Incorrect') or (operater == 'Enter Passcode')):
				operater = ''
				Star_list = ''
				Star_list += "*"
				operater = operater + str(num)
				display.set(Star_list)
			else:
				if (len(Star_list) < 8):
					Star_list += "*"
					operater = operater + str(num)
					display.set(Star_list)
		
		def talk():
			pass
		
		# when pressed checks the display for the correct passcode if correct it will change the display to correct and unlock the door
		# else it will display incorrect 
		def enter():
					global Star_list
					global operater
					global wrong_pin
					if (operater == str(12590)):
						sleep(.5)
						operater = 'Correct'
						wrong_pin = []
						display.set(operater)
##						GPIO.output(led, GPIO.HIGH)
##						sleep(10)
##						GPIO.output(led, GPIO.LOW)
					else:
						operater = 'Incorrect'
						wrong_pin.append('')
						if (len(wrong_pin) >= 5):
							operater = "Alarm"
							display.set(operater)
							alarm()
						else:
							display.set(operater)
		
		# when pressed the display will cleared, then set to Enter Passcode
		def clear():
			global operater
			global Star_list
			if (operater == "Alarm"):
				pass
			else:
				Star_list = ''
				operater = ''
				display.set('Enter Passcode')

		def ring_bell():
			pygame.init()
			pygame.mixer.Sound("door_bell.wav").play()
			
			
		def alarm():
			pygame.init()
			counter = 0
			while (counter < 25):			
				pygame.mixer.Sound("Air_Horn.wav").play()
				sleep(.5)
				pygame.mixer.Sound("Air_Horn.wav").play()
				counter += 1
				
	


		# creates the number 1 button
		Button1 = Button(top)
		# sets the button to the appropriate size and at the appropriate place
		Button1.place(relx=0.01, rely=0.29, height=68, width=175)
		# when pressed the button will change colors
		Button1.configure(activebackground="#6ec6d8", background="#d9d9d9",borderwidth="10", command=lambda:buttonclick(1), cursor="hand2", font=font14, pady="0", text='''1''')

		menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
		top.configure(menu = menubar)


		# same as above
		Button2 = Button(top)
		Button2.place(relx=0.25, rely=0.29, height=68, width=175)
		Button2.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(2), cursor="hand2", font=font14, pady="0", text='''2''')
		

		# same as above
		Button3 = Button(top)
		Button3.place(relx=0.5, rely=0.29, height=68, width=175)
		Button3.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(3), cursor="hand2", font=font14, pady="0", text='''3''')
		

		# same as above
		Button4 = Button(top)
		Button4.place(relx=0.01, rely=0.46, height=68, width=175)
		Button4.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(4), cursor="hand2", font=font14, pady="0", text='''4''')

		# same as above
		Button5 = Button(top)
		Button5.place(relx=0.25, rely=0.46, height=68, width=175)
		Button5.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(5), cursor="hand2", font=font14, pady="0", text='''5''')

		# same as above
		Button6 = Button(top)
		Button6.place(relx=0.5, rely=0.46, height=68, width=175)
		Button6.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(6), cursor="hand2", font=font14, pady="0", text='''6''')

		# same as above
		Button7 = Button(top)
		Button7.place(relx=0.01, rely=0.63, height=68, width=175)
		Button7.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(7), cursor="hand2", font=font14, pady="0", text='''7''')

		# same as above
		Button8 = Button(top)
		Button8.place(relx=0.25, rely=0.63, height=68, width=175)
		Button8.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(8), cursor="hand2", font=font14, pady="0", text='''8''')

		# same as above
		Button9 = Button(top)
		Button9.place(relx=0.5, rely=0.63, height=68, width=175)
		Button9.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(9), cursor="hand2", font=font14, pady="0", text='''9''')

		# same as above
		Clear_Button = Button(top)
		Clear_Button.place(relx=0.74, rely=0.80, height=68, width=175)
		Clear_Button.configure(activebackground="#6ec6d8", background="#ff0a0a", borderwidth="10", command=lambda:clear(), cursor="hand2", font=font14, pady="0", text='''Clear''')
		

		# same as above
		Button0 = Button(top)
		Button0.place(relx=0.25, rely=0.80, height=68, width=175)
		Button0.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick(0), cursor="hand2", font=font14, pady="0", text='''0''')

		# same as above
		Enter_Button = Button(top)
		Enter_Button.place(relx=0.74, rely=0.63, height=68, width=175)
		Enter_Button.configure(activebackground="#6ec6d8", background="#23d83b", borderwidth="10", command=lambda:enter(), cursor="hand2", font=font14, pady="0", text='''Enter''')

		# same as above
		Talk_Button = Button(top)
		Talk_Button.place(relx=0.74, rely=0.29, height=68, width=175)
		Talk_Button.configure(activebackground="#a32227", background="orange",borderwidth="10",command=lambda:talk(), cursor="hand2", font=font14, pady="0", text='''Talk''')

		# same as above
		Ring_Button = Button(top)
		Ring_Button.place(relx=0.74, rely=0.46, height=68, width=175)
		Ring_Button.configure(activebackground="#2c34a3", background="#4cd8d8", borderwidth="10", command=lambda:ring_bell(), cursor="hand2", font=font14, pady="0", text='''Ring''')

		# same as above
		Entry1 = Entry(top)
		Entry1.place(relx=0.22, rely=0.12,height=68, relwidth=0.29)
		Entry1.configure(background="#2b287a", borderwidth="0", disabledforeground="#a3a3a3", font=font12, foreground="white", highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black", insertborderwidth="1", justify=CENTER, selectbackground="#007878d7d777", selectforeground="#ffffffffffff", textvariable=display)
	

		# same as above
		Label1 = Label(top)
		Label1.place(relx=0.33, rely=0.0, height=46, width=242)
		Label1.configure(activebackground="#f9f9f9", background="#2b287a", font=font11, foreground="#4cd8d8", text='''Welcome''', width=242)


		# same as above
		Button_pound = Button(top)
		Button_pound.place(relx=0.5, rely=0.80, height=68, width=175)
		Button_pound.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick('#'), cursor="hand2", font=font14, foreground="#000000", pady="0", text='''#''')

		# same as above
		Button_star = Button(top)
		Button_star.place(relx=0.01, rely=0.80, height=68, width=175)
		Button_star.configure(activebackground="#6ec6d8", background="#d9d9d9", borderwidth="10", command=lambda:buttonclick('*'), cursor="hand2", font=font14, pady="0", text='''*''')
		
		

class App():
	def __init__(self):
			self.root = Tk()
			self.label = Label(text="")
			self.label.pack()
			self.update_clock()
			self.root.mainloop()

	def update_clock(self):
			now = strftime("%a \n%B %d %Y\n%X" )
			self.label.place(relx=0.82, rely=0.0, height=68, width=175)
			self.label.configure(text=now, background="#2b287a", font = 14, foreground = 'white')
			self.root.after(1000, self.update_clock)




			
if __name__ == '__main__':
	start_gui()




