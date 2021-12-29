from tkinter import *
import math
from PIL import Image, ImageTk

 

root = Tk()

root.title("Calculator")
icon = PhotoImage(file='calculator.png')

root.iconphoto(False,icon)


e = Entry(root, width = 50, borderwidth = 2, background = 'black', fg = 'white',font = ('sans serif',10,'bold','italic'))
e.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10)


def button_action(num):
	f = e.get()
	global g
	g = f
	global g2
	g2 = num
	e.delete(0,END)
	e.insert(0,str(f)+str(num))


def delete():
	e.delete(0,END)



def add():
	f_n = e.get()
	global cal
	global calculate
	calculate = int(f_n)
	cal = "Add"
	e.delete(0,END)

def sub():
	f_n = e.get()
	global cal
	global calculate
	calculate = int(f_n)
	cal = "Substraction"
	e.delete(0,END)

def mul():
   f_n = e.get()
   global cal
   global calculate
   calculate = int(f_n)
   cal = "Multiplication"
   e.delete(0,END)
def divide():
   f_n = e.get()
   global cal
   global calculate
   calculate = int(f_n)
   cal = "Divide"
   e.delete(0,END)   	

def mod():
	f_n = e.get()
	global cal
	global calculate
	calculate = int(f_n)
	cal = "Modulu"
	e.delete(0,END)

		
def result():
	last_num = e.get()
	e.delete(0,END)
	if cal == 'Add':
		e.insert(0,calculate + int(last_num))
	if cal == 'Substraction':
		e.insert(0,calculate - int(last_num))
	if cal == 'Multiplication':
		e.insert(0,calculate * int(last_num))
	if cal == "Divide":
		e.insert(0,calculate / int(last_num))
	if cal == "Modulu":
		e.insert(0,calculate % int(last_num))
	

button_1 = Button(root, text = "1", padx = 20,foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action(1)).grid(row = 3, column = 0)
button_2 = Button(root, text = "2", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action(2)).grid(row = 3, column = 1)
button_3 = Button(root, text = "3", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action(3)).grid(row = 3, column = 2)

button_4 = Button(root, text = "4", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action(4)).grid(row = 2, column = 0)
button_5 = Button(root, text = "5", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action('5')).grid(row = 2, column = 1)
button_6 = Button(root, text = "6", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'),command =lambda: button_action('6')).grid(row = 2, column = 2)

button_7 = Button(root, text = "7", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action('7')).grid(row = 1, column = 0)
button_8 = Button(root, text = "8", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action('8')).grid(row = 1, column = 1)
button_9 = Button(root, text = "9", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action('9')).grid(row = 1, column = 2)
button_0 = Button(root, text = "0", padx = 20, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command =lambda: button_action('0')).grid(row = 4, column = 0)

button_result = Button(root, text = "=", padx = 55,foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'),command = result).grid(row = 4, column = 1,columnspan = 2)
button_clear = Button(root, text = "Clear", padx = 50,foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'), command = delete).grid(row = 1, column = 3, columnspan = 2)

button_add = Button(root, text = "+", padx = 17, foreground = 'black',background = 'white', pady = 35, borderwidth = 2,font = ('sans serif',15,'bold'), command = lambda: add()).grid(row = 2, column = 4, rowspan = 2)
button_sub = Button(root, text = "-", padx = 15, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',13,'bold'),command = lambda: sub()).grid(row = 2, column = 3)
button_mul = Button(root, text = "*", padx = 15, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',13,'bold'),command = lambda: mul()).grid(row = 3, column = 3)
button_div = Button(root, text = "/", padx = 15, foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',13,'bold'),command = lambda: divide()).grid(row = 4, column = 3)
button_mod = Button(root, text = "Mod",padx = 15,foreground = 'black',background = 'white', pady = 5, borderwidth = 2,font = ('sans serif',10,'bold'),command = lambda: mod()).grid(row = 4, column = 4)



root.mainloop()