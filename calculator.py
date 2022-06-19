#       JAKUB SZKOLA
#           2022
#        CALCULATOR 
#          TKINKER


from string import hexdigits
from tkinter import *
from tkinter import ttk
from turtle import heading


def display_text():
   global entry
   string = entry.get()
   display.configure(text = string)

window = Tk()
window.title("Calculator")

entry = Entry(window)
entry.grid(row = 1, column = 1,pady = 5)


display = Label(window)
display.grid(row=1, column = 0, pady = 5)

show = ttk.Button(window, text = "=", width = 10, command = display_text)
show.grid(row=1, column = 3, pady = 5)

plus = ttk.Button(window, text = "+", width = 10)                         
plus.grid(row=2, column = 0, pady = 5)

minus = ttk.Button(window, text = "-", width = 10)                        
minus.grid(row=3, column = 0, pady = 5)

multi = ttk.Button(window, text = "*", width = 10)                                 
multi.grid(row=4, column = 0, pady = 5)

divi = ttk.Button(window, text ="/",  width = 10)                                
divi.grid(row=5, column = 0, pady = 5)

close = ttk.Button(window, text ="Close", width = 10)                                 
close.grid(row=5, column = 3, pady = 5)

button_1 = ttk.Button(window, text ="1", width = 10)
button_1.grid(row=2, column = 1, pady = 5)

button_2 = ttk.Button(window, text ="2", width = 10)
button_2.grid(row=2, column = 2, pady = 5)

button_3 = ttk.Button(window, text ="3", width = 10)
button_3.grid(row=2, column = 3, pady = 5)

button_4 = ttk.Button(window, text ="4", width = 10)
button_4.grid(row=3, column = 1, pady = 5)

button_5 = ttk.Button(window, text ="5", width = 10)
button_5.grid(row=3, column = 2, pady = 5)

button_6 = ttk.Button(window, text ="6", width = 10)
button_6.grid(row=3, column = 3, pady = 5)

button_7 = ttk.Button(window, text ="7", width = 10)
button_7.grid(row=4, column = 1, pady = 5)

button_8 = ttk.Button(window, text ="8", width = 10)
button_8.grid(row=4, column = 2, pady = 5)

button_9 = ttk.Button(window, text ="9", width = 10)
button_9.grid(row=4, column = 3, pady = 5)





window.mainloop()




























































