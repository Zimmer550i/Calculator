from tkinter import *

root = Tk()
root.title("Sakif's Calculator")


e = Entry(root, width=10, borderwidth=5, font=("Helvetica", 32, "bold"))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#0 = +, 1 = -, 2 = *, 3 = /
#pyinstaller --onefile -w --icon='icon.ico' .\Calculator.py 

def button_print(num):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(num))

def button_clear():
	e.delete(0, END)

def button_a():
	global f_num 
	f_num = int(e.get())
	e.delete(0, END)
	global operator 
	operator = 0

def button_s():
	global f_num 
	f_num = int(e.get())
	e.delete(0, END)
	global operator 
	operator = 1

def button_m():
	global f_num 
	f_num = int(e.get())
	e.delete(0, END)
	global operator 
	operator = 2

def button_d():
	global f_num 
	f_num = int(e.get())
	e.delete(0, END)
	global operator 
	operator = 3

def button_e():
	s_num = int(e.get())
	e.delete(0, END)
	if operator==0:
		e.insert(0, f_num + s_num)
	if operator==1:
		e.insert(0, f_num - s_num)
	if operator==2:
		e.insert(0, f_num * s_num)
	if operator==3:
		e.insert(0, f_num / s_num)

#Button Declaration
button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_print(1), font=("Helvetica", 24, "bold"))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_print(2), font=("Helvetica", 24, "bold"))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_print(3), font=("Helvetica", 24, "bold"))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_print(4), font=("Helvetica", 24, "bold"))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_print(5), font=("Helvetica", 24, "bold"))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_print(6), font=("Helvetica", 24, "bold"))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_print(7), font=("Helvetica", 24, "bold"))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_print(8), font=("Helvetica", 24, "bold"))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_print(9), font=("Helvetica", 24, "bold"))
button_0 = Button(root, text="0", padx=20, pady=20, command=lambda: button_print(0), font=("Helvetica", 24, "bold"))
button_add = Button(root, text="+", padx=18.5, pady=20, command=button_a, font=("Helvetica", 24, "bold"))
button_sub = Button(root, text="-", padx=25, pady=20, command=button_s, font=("Helvetica", 24, "bold"))
button_mul = Button(root, text="X", padx=20, pady=20, command=button_m, font=("Helvetica", 24, "bold"))
button_div = Button(root, text="/", padx=27, pady=20, command=button_d, font=("Helvetica", 24, "bold"))
button_equal = Button(root, text="=", padx=66, pady=20, command=button_e, font=("Helvetica", 24, "bold"))
button_clear = Button(root, text="Clear", padx=28, pady=20, command=button_clear)


#Button Placement
button_clear.grid(row=0, column=3)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mul.grid(row=3, column=3)
button_0.grid(row=4, column=0)
button_div.grid(row=4, column=3)
button_equal.grid(row=4, column=1, columnspan=2)

root.resizable(False, False)

root.mainloop()