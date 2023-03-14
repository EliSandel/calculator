from tkinter import *

main = Tk()

main.title("simple calculator")

monitor = Entry(main , width=35 , borderwidth=5)
monitor.grid(row=0,column=0 , columnspan=3 , padx=10, pady=10)

index2 =0
index =0
first_num =0
second_num =0
def button_click(number):
    global index
    global index2
    current = monitor.get()
    monitor.delete(0, END)
    monitor.insert(0,str(current) + str(number))
    index += 1
    index2 += 1

def clear_click():
    global index
    global index2
    index = 0
    index2 = 0
    monitor.delete(0, END)
      
    
def add_click():
    global index
    global index2
    index2 = 0
    global first_num
    first_number = int(monitor.get())
    first_num = first_number
    monitor.insert(END, "+")
    index += 1
    
def equal_click():
    global index
    global index2
    global second_num
    second_number = monitor.get()
    second_number = second_number[index-index2:]
    second_number = int(second_number)
    monitor.delete(0, END)
    addition = first_num+second_number
    monitor.insert(0, addition)
    index2 =0
    index =0
    return        

 
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
button_add = Button(main, text="+", padx=39, pady=20, command= add_click)
button_equal = Button(main, text="=", padx=86, pady=20, command= equal_click)
button_clear = Button(main, text="Clear", padx=77, pady=20, command= clear_click)





# put buttons on screen
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1) 
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1,columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)



print("hello")


main.mainloop()
