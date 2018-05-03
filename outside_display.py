from threading import Timer
import sys
import time

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def vp_start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	global localtime
	root = Tk()
	top = Jarvis (root)
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


	
operater = ''	
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
		font15 = "-family {Times New Roman} -size 20 -weight bold "  \
			"-slant roman -underline 0 -overstrike 0"
		font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
			"roman -underline 0 -overstrike 0"

		top.geometry("948x677")
		top.title("Jarvis")
		top.configure(background="#2b287a")
		top.configure(highlightbackground="#d9d9d9")
		top.configure(highlightcolor="black")

		display = StringVar()

		

		def buttonclick(num):
			global Star_list 
			global operater
			if ((operater == 'Correct') or (operater == 'Incorrect')):
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
			
		def enter():
			global Star_list
			global operater
			if (operater == str(12590)):
				sleep(.5)
				operater = 'Correct'
				display.set(operater)
			else:
				sleep(.5)
				operater = 'Incorrect'
				display.set(operater)
			
		def clear():
			global operater
			global Star_list
			Star_list = ''
			operater = ''
			display.set('')

		def ring_bell():
			pass

		

		self.Button1_0 = Button(top)
		self.Button1_0.place(relx=0.01, rely=0.24, height=93, width=225)
		self.Button1_0.configure(activebackground="#6ec6d8")
		self.Button1_0.configure(activeforeground="#000000")
		self.Button1_0.configure(background="#d9d9d9")
		self.Button1_0.configure(borderwidth="15")
		self.Button1_0.configure(command=lambda:buttonclick(1))
		self.Button1_0.configure(cursor="hand2")
		self.Button1_0.configure(disabledforeground="#a3a3a3")
		self.Button1_0.configure(font=font14)
		self.Button1_0.configure(foreground="#000000")
		self.Button1_0.configure(highlightbackground="#d9d9d9")
		self.Button1_0.configure(highlightcolor="black")
		self.Button1_0.configure(pady="0")
		self.Button1_0.configure(takefocus="Tab")
		self.Button1_0.configure(text='''1''')

		self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
		top.configure(menu = self.menubar)



		self.Button1_1 = Button(top)
		self.Button1_1.place(relx=0.25, rely=0.24, height=93, width=225)
		self.Button1_1.configure(activebackground="#4cd8d8")
		self.Button1_1.configure(activeforeground="#000000")
		self.Button1_1.configure(background="#d9d9d9")
		self.Button1_1.configure(borderwidth="15")
		self.Button1_1.configure(command=lambda:buttonclick(2))
		self.Button1_1.configure(cursor="hand2")
		self.Button1_1.configure(disabledforeground="#a3a3a3")
		self.Button1_1.configure(font=font14)
		self.Button1_1.configure(foreground="#000000")
		self.Button1_1.configure(highlightbackground="#d9d9d9")
		self.Button1_1.configure(highlightcolor="black")
		self.Button1_1.configure(pady="0")
		self.Button1_1.configure(takefocus="Tab")
		self.Button1_1.configure(text='''2''')

		self.Button1_2 = Button(top)
		self.Button1_2.place(relx=0.5, rely=0.24, height=93, width=225)
		self.Button1_2.configure(activebackground="#6ec6d8")
		self.Button1_2.configure(activeforeground="#000000")
		self.Button1_2.configure(background="#d9d9d9")
		self.Button1_2.configure(borderwidth="15")
		self.Button1_2.configure(command=lambda:buttonclick(3))
		self.Button1_2.configure(cursor="hand2")
		self.Button1_2.configure(disabledforeground="#a3a3a3")
		self.Button1_2.configure(font=font14)
		self.Button1_2.configure(foreground="#000000")
		self.Button1_2.configure(highlightbackground="#d9d9d9")
		self.Button1_2.configure(highlightcolor="black")
		self.Button1_2.configure(pady="0")
		self.Button1_2.configure(takefocus="Tab")
		self.Button1_2.configure(text='''3''')

		self.Button1_3 = Button(top)
		self.Button1_3.place(relx=0.01, rely=0.38, height=93, width=225)
		self.Button1_3.configure(activebackground="#6ec6d8")
		self.Button1_3.configure(activeforeground="#000000")
		self.Button1_3.configure(background="#d9d9d9")
		self.Button1_3.configure(borderwidth="15")
		self.Button1_3.configure(command=lambda:buttonclick(4))
		self.Button1_3.configure(cursor="hand2")
		self.Button1_3.configure(disabledforeground="#a3a3a3")
		self.Button1_3.configure(font=font14)
		self.Button1_3.configure(foreground="#000000")
		self.Button1_3.configure(highlightbackground="#d9d9d9")
		self.Button1_3.configure(highlightcolor="black")
		self.Button1_3.configure(pady="0")
		self.Button1_3.configure(takefocus="Tab")
		self.Button1_3.configure(text='''4''')

		self.Button1_4 = Button(top)
		self.Button1_4.place(relx=0.25, rely=0.38, height=93, width=225)
		self.Button1_4.configure(activebackground="#6ec6d8")
		self.Button1_4.configure(activeforeground="#000000")
		self.Button1_4.configure(background="#d9d9d9")
		self.Button1_4.configure(borderwidth="15")
		self.Button1_4.configure(command=lambda:buttonclick(5))
		self.Button1_4.configure(cursor="hand2")
		self.Button1_4.configure(disabledforeground="#a3a3a3")
		self.Button1_4.configure(font=font14)
		self.Button1_4.configure(foreground="#000000")
		self.Button1_4.configure(highlightbackground="#d9d9d9")
		self.Button1_4.configure(highlightcolor="black")
		self.Button1_4.configure(pady="0")
		self.Button1_4.configure(takefocus="Tab")
		self.Button1_4.configure(text='''5''')

		self.Button1_5 = Button(top)
		self.Button1_5.place(relx=0.5, rely=0.38, height=93, width=225)
		self.Button1_5.configure(activebackground="#6ec6d8")
		self.Button1_5.configure(activeforeground="#000000")
		self.Button1_5.configure(background="#d9d9d9")
		self.Button1_5.configure(borderwidth="15")
		self.Button1_5.configure(command=lambda:buttonclick(6))
		self.Button1_5.configure(cursor="hand2")
		self.Button1_5.configure(disabledforeground="#a3a3a3")
		self.Button1_5.configure(font=font14)
		self.Button1_5.configure(foreground="#000000")
		self.Button1_5.configure(highlightbackground="#d9d9d9")
		self.Button1_5.configure(highlightcolor="black")
		self.Button1_5.configure(pady="0")
		self.Button1_5.configure(takefocus="Tab")
		self.Button1_5.configure(text='''6''')

		self.Button1_6 = Button(top)
		self.Button1_6.place(relx=0.01, rely=0.53, height=93, width=225)
		self.Button1_6.configure(activebackground="#6ec6d8")
		self.Button1_6.configure(activeforeground="#000000")
		self.Button1_6.configure(background="#d9d9d9")
		self.Button1_6.configure(borderwidth="15")
		self.Button1_6.configure(command=lambda:buttonclick(7))
		self.Button1_6.configure(cursor="hand2")
		self.Button1_6.configure(disabledforeground="#a3a3a3")
		self.Button1_6.configure(font=font14)
		self.Button1_6.configure(foreground="#000000")
		self.Button1_6.configure(highlightbackground="#d9d9d9")
		self.Button1_6.configure(highlightcolor="black")
		self.Button1_6.configure(pady="0")
		self.Button1_6.configure(takefocus="Tab")
		self.Button1_6.configure(text='''7''')

		self.Button1_7 = Button(top)
		self.Button1_7.place(relx=0.25, rely=0.53, height=93, width=225)
		self.Button1_7.configure(activebackground="#6ec6d8")
		self.Button1_7.configure(activeforeground="#000000")
		self.Button1_7.configure(background="#d9d9d9")
		self.Button1_7.configure(borderwidth="15")
		self.Button1_7.configure(command=lambda:buttonclick(8))
		self.Button1_7.configure(cursor="hand2")
		self.Button1_7.configure(disabledforeground="#a3a3a3")
		self.Button1_7.configure(font=font14)
		self.Button1_7.configure(foreground="#000000")
		self.Button1_7.configure(highlightbackground="#d9d9d9")
		self.Button1_7.configure(highlightcolor="black")
		self.Button1_7.configure(pady="0")
		self.Button1_7.configure(takefocus="Tab")
		self.Button1_7.configure(text='''8''')

		self.Button1_8 = Button(top)
		self.Button1_8.place(relx=0.5, rely=0.53, height=93, width=225)
		self.Button1_8.configure(activebackground="#6ec6d8")
		self.Button1_8.configure(activeforeground="#000000")
		self.Button1_8.configure(background="#d9d9d9")
		self.Button1_8.configure(borderwidth="15")
		self.Button1_8.configure(command=lambda:buttonclick(9))
		self.Button1_8.configure(cursor="hand2")
		self.Button1_8.configure(disabledforeground="#a3a3a3")
		self.Button1_8.configure(font=font14)
		self.Button1_8.configure(foreground="#000000")
		self.Button1_8.configure(highlightbackground="#d9d9d9")
		self.Button1_8.configure(highlightcolor="black")
		self.Button1_8.configure(pady="0")
		self.Button1_8.configure(takefocus="Tab")
		self.Button1_8.configure(text='''9''')

		self.Button1_9 = Button(top)
		self.Button1_9.place(relx=0.74, rely=0.68, height=93, width=225)
		self.Button1_9.configure(activebackground="#6ec6d8")
		self.Button1_9.configure(activeforeground="#000000")
		self.Button1_9.configure(background="#ff0a0a")
		self.Button1_9.configure(borderwidth="15")
		self.Button1_9.configure(command=lambda:clear())
		self.Button1_9.configure(cursor="hand2")
		self.Button1_9.configure(disabledforeground="#a3a3a3")
		self.Button1_9.configure(font=font14)
		self.Button1_9.configure(foreground="black")
		self.Button1_9.configure(highlightbackground="#d9d9d9")
		self.Button1_9.configure(highlightcolor="black")
		self.Button1_9.configure(pady="0")
		self.Button1_9.configure(takefocus="Tab")
		self.Button1_9.configure(text='''Clear''')

		self.Button1_10 = Button(top)
		self.Button1_10.place(relx=0.25, rely=0.68, height=93, width=225)
		self.Button1_10.configure(activebackground="#6ec6d8")
		self.Button1_10.configure(activeforeground="#000000")
		self.Button1_10.configure(background="#d9d9d9")
		self.Button1_10.configure(borderwidth="15")
		self.Button1_10.configure(command=lambda:buttonclick(0))
		self.Button1_10.configure(cursor="hand2")
		self.Button1_10.configure(disabledforeground="#a3a3a3")
		self.Button1_10.configure(font=font14)
		self.Button1_10.configure(foreground="#000000")
		self.Button1_10.configure(highlightbackground="#d9d9d9")
		self.Button1_10.configure(highlightcolor="black")
		self.Button1_10.configure(pady="0")
		self.Button1_10.configure(takefocus="Tab")
		self.Button1_10.configure(text='''0''')

		self.Button1_11 = Button(top)
		self.Button1_11.place(relx=0.74, rely=0.53, height=93, width=225)
		self.Button1_11.configure(activebackground="#6ec6d8")
		self.Button1_11.configure(activeforeground="#000000")
		self.Button1_11.configure(background="#23d83b")
		self.Button1_11.configure(borderwidth="15")
		self.Button1_11.configure(command=lambda:enter())
		self.Button1_11.configure(cursor="hand2")
		self.Button1_11.configure(disabledforeground="#a3a3a3")
		self.Button1_11.configure(font=font14)
		self.Button1_11.configure(foreground="black")
		self.Button1_11.configure(highlightbackground="#d9d9d9")
		self.Button1_11.configure(highlightcolor="black")
		self.Button1_11.configure(pady="0")
		self.Button1_11.configure(takefocus="Tab")
		self.Button1_11.configure(text='''Enter''')

		self.Button1_12 = Button(top)
		self.Button1_12.place(relx=0.74, rely=0.24, height=93, width=225)
		self.Button1_12.configure(activebackground="#a32227")
		self.Button1_12.configure(activeforeground="white")
		self.Button1_12.configure(activeforeground="#000000")
		self.Button1_12.configure(background="orange")
		self.Button1_12.configure(borderwidth="15")
		self.Button1_12.configure(command=lambda:talk())
		self.Button1_12.configure(cursor="hand2")
		self.Button1_12.configure(disabledforeground="#a3a3a3")
		self.Button1_12.configure(font=font14)
		self.Button1_12.configure(foreground="black")
		self.Button1_12.configure(highlightbackground="#d9d9d9")
		self.Button1_12.configure(highlightcolor="black")
		self.Button1_12.configure(pady="0")
		self.Button1_12.configure(takefocus="Tab")
		self.Button1_12.configure(text='''Talk''')

		self.Button1_13 = Button(top)
		self.Button1_13.place(relx=0.74, rely=0.38, height=93, width=225)
		self.Button1_13.configure(activebackground="#2c34a3")
		self.Button1_13.configure(activeforeground="white")
		self.Button1_13.configure(activeforeground="#000000")
		self.Button1_13.configure(background="#4cd8d8")
		self.Button1_13.configure(borderwidth="15")
		self.Button1_13.configure(command=lambda:ring_bell())
		self.Button1_13.configure(cursor="hand2")
		self.Button1_13.configure(disabledforeground="#a3a3a3")
		self.Button1_13.configure(font=font14)
		self.Button1_13.configure(foreground="black")
		self.Button1_13.configure(highlightbackground="#d9d9d9")
		self.Button1_13.configure(highlightcolor="black")
		self.Button1_13.configure(pady="0")
		self.Button1_13.configure(takefocus="Tab")
		self.Button1_13.configure(text='''Ring''')

		self.Entry1 = Entry(top)
		self.Entry1.place(relx=0.22, rely=0.07,height=94, relwidth=0.29)
		self.Entry1.configure(background="#2b287a")
		self.Entry1.configure(borderwidth="0")
		self.Entry1.configure(disabledforeground="#a3a3a3")
		self.Entry1.configure(font=font12)
		self.Entry1.configure(foreground="white")
		self.Entry1.configure(highlightbackground="#d9d9d9")
		self.Entry1.configure(highlightcolor="black")
		self.Entry1.configure(insertbackground="black")
		self.Entry1.configure(insertborderwidth="1")
		self.Entry1.configure(justify=CENTER)
		self.Entry1.configure(selectbackground="#007878d7d777")
		self.Entry1.configure(selectforeground="#ffffffffffff")
		self.Entry1.configure(textvariable=display)

		self.Label1 = Label(top)
		self.Label1.place(relx=0.33, rely=0.0, height=46, width=242)
		self.Label1.configure(activebackground="#f9f9f9")
		self.Label1.configure(activeforeground="#000000")
		self.Label1.configure(background="#2b287a")
		self.Label1.configure(disabledforeground="#a3a3a3")
		self.Label1.configure(font=font11)
		self.Label1.configure(foreground="#4cd8d8")
		self.Label1.configure(highlightbackground="#d9d9d9")
		self.Label1.configure(highlightcolor="black")
		self.Label1.configure(text='''Welcome''')
		self.Label1.configure(width=242)

		self.Label2 = Label(top)
		self.Label2.place(relx=0, rely=0.84, height=46, width=232)
		self.Label2.configure(activebackground="#f9f9f9")
		self.Label2.configure(activeforeground="#c6c6c6")
		self.Label2.configure(background="#2b287a")
		self.Label2.configure(disabledforeground="#a3a3a3")
		self.Label2.configure(font=font15)
		self.Label2.configure(foreground="white")
		self.Label2.configure(highlightbackground="#d9d9d9")
		self.Label2.configure(highlightcolor="black")
		self.Label2.configure(text= "localtime")
		self.Label2.configure(width=232)
		
		def update_localtime():
			localtime = datetime.today()
			self.Label2.configure(text = localtime)
			t = Timer(1.0, update_localtime)
			t.start()

		self.Button1_3 = Button(top)
		self.Button1_3.place(relx=0.5, rely=0.68, height=93, width=225)
		self.Button1_3.configure(activebackground="#6ec6d8")
		self.Button1_3.configure(activeforeground="#000000")
		self.Button1_3.configure(background="#d9d9d9")
		self.Button1_3.configure(borderwidth="15")
		self.Button1_3.configure(command=lambda:buttonclick('#'))
		self.Button1_3.configure(cursor="hand2")
		self.Button1_3.configure(disabledforeground="#a3a3a3")
		self.Button1_3.configure(font=font14)
		self.Button1_3.configure(foreground="#000000")
		self.Button1_3.configure(highlightbackground="#d9d9d9")
		self.Button1_3.configure(highlightcolor="black")
		self.Button1_3.configure(pady="0")
		self.Button1_3.configure(takefocus="Tab")
		self.Button1_3.configure(text='''#''')

		self.Button1_4 = Button(top)
		self.Button1_4.place(relx=0.01, rely=0.68, height=93, width=225)
		self.Button1_4.configure(activebackground="#6ec6d8")
		self.Button1_4.configure(activeforeground="#000000")
		self.Button1_4.configure(background="#d9d9d9")
		self.Button1_4.configure(borderwidth="15")
		self.Button1_4.configure(command=lambda:buttonclick('*'))
		self.Button1_4.configure(cursor="hand2")
		self.Button1_4.configure(disabledforeground="#a3a3a3")
		self.Button1_4.configure(font=font14)
		self.Button1_4.configure(foreground="#000000")
		self.Button1_4.configure(highlightbackground="#d9d9d9")
		self.Button1_4.configure(highlightcolor="black")
		self.Button1_4.configure(pady="0")
		self.Button1_4.configure(takefocus="Tab")
		self.Button1_4.configure(text='''*''')


if __name__ == '__main__':
    vp_start_gui()

