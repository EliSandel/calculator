from tkinter import *

main = Tk()

main.title("simple calculator")

monitor = Entry(main , width=35 , borderwidth=5)
monitor.grid(row=0,column=0 , columnspan=4 , padx=10, pady=10)


def button_click(number):
    current = monitor.get()
    monitor.delete(0, END)
    monitor.insert(0, str(current) + str(number))
    

def clear_click():    
    monitor.delete(0, END)
      
    
def add_click():
    first_number = monitor.get()
    global math
    math = "addition"
    global first_num
    first_num = float(first_number)
    monitor.delete(0, END)    

def subtract_click():
    first_number = monitor.get()
    global math
    math = "subtraction"
    global first_num
    first_num = float(first_number)
    monitor.delete(0, END)    

def multiply_click():
    first_number = monitor.get()
    global math
    math = "multiplication"
    global first_num
    first_num = float(first_number)
    monitor.delete(0, END)    

def divide_click():
    first_number = monitor.get()
    global math
    math = "division"
    global first_num
    first_num = float(first_number)
    monitor.delete(0, END)    

def point_click():
    monitor.insert(END, ".")
    
def equal_click():
    second_number = monitor.get()
    monitor.delete(0, END)
    if math == "addition":
        monitor.insert(0, first_num + float(second_number))
    elif math == "subtraction":
        monitor.insert(0, first_num - float(second_number))
    elif math == "multiplication":
        monitor.insert(0, first_num * float(second_number))
    elif math == "division":
        monitor.insert(0, first_num / float(second_number))    
# define buttons

button_1 = Button(main, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(main, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(main, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(main, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(main, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(main, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(main, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(main, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(main, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(main, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_point = Button(main, text=".", padx=42, pady=20, command= point_click)
button_add = Button(main, text="+", padx=37, pady=20, command= add_click)
button_subtract = Button(main, text="-", padx=39, pady=20, command= subtract_click)
button_multiply = Button(main, text="*", padx=39, pady=20, command= multiply_click)
button_divide = Button(main, text="/", padx=39, pady=20, command= divide_click)
button_equal = Button(main, text="=", padx=86, pady=20, command= equal_click)
button_clear = Button(main, text="Clear", padx=28, pady=20, command= clear_click)





# put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1) 
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_point.grid(row=4, column=2)
button_clear.grid(row=1, column=3)
button_equal.grid(row=5, column=1,columnspan=2)

button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)



main.mainloop()