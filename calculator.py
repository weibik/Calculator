#       JAKUB SZKOLA
#           2022
#        CALCULATOR 
#          TKINKER


from hashlib import new
import math
from string import hexdigits
from tkinter import *
from tkinter import ttk
from turtle import heading, width


def GUI():
   def display_text():
      global entry
      string = entry.get()
      display.configure(text = string)

   def button_click(number):
      current = entry.get()
      entry.delete(0, END)
      entry.insert(0, str(current) + str(number))

   def button_plus():
      first_num = entry.get()
      global f_num 
      global math
      math = "plus"
      f_num = int(float(first_num))
      entry.delete(0, END)

   def button_minus():
      first_num = entry.get()
      global f_num 
      global math
      math = "minus"
      f_num = int(float(first_num))
      entry.delete(0, END)

   def button_multi():
      first_num = entry.get()
      global f_num 
      global math
      math = "multiplication"
      f_num = int(float(first_num))
      entry.delete(0, END)
   
   def button_divi():
      first_num = entry.get()
      global f_num 
      global math
      math = "division"
      f_num = int(float(first_num))
      entry.delete(0, END)

   def button_result():
      new_num = entry.get()
      entry.delete(0, END)

      if math == "plus":
         entry.insert(0, f_num + int(new_num))
      if math == "minus":
         entry.insert(0, f_num - int(new_num))
      if math == "multiplication":
         entry.insert(0, f_num * int(new_num))
      if math == "division":
         entry.insert(0, f_num / int(new_num))
         


   window = Tk()
   window.title("Calculator")

   entry = Entry(window, width=10)
   display = Label(window)

   show = ttk.Button(window, text = "=", command = button_result)
   plus = ttk.Button(window, text = "+", command = button_plus)                      
   minus = ttk.Button(window, text = "-", command = button_minus)                        
   multi = ttk.Button(window, text = "*", command = button_multi)                                 
   divi = ttk.Button(window, text ="/", command = button_divi)                                
   close = ttk.Button(window, text ="Close", command=window.destroy)                                 

   button_1 = ttk.Button(window, text ="1", command = lambda: button_click(1))
   button_2 = ttk.Button(window, text ="2", command = lambda: button_click(2))
   button_3 = ttk.Button(window, text ="3", command = lambda: button_click(3))
   button_4 = ttk.Button(window, text ="4", command = lambda: button_click(4))
   button_5 = ttk.Button(window, text ="5", command = lambda: button_click(5))
   button_6 = ttk.Button(window, text ="6", command = lambda: button_click(6))
   button_7 = ttk.Button(window, text ="7", command = lambda: button_click(7))
   button_8 = ttk.Button(window, text ="8", command = lambda: button_click(8))
   button_9 = ttk.Button(window, text ="9", command = lambda: button_click(9))
   button_0 = ttk.Button(window, text ="0", command = lambda: button_click(0))

   display.grid(row=1, column = 0, pady = 5)
   entry.grid(row = 1, column = 1, columnspan = 2, sticky = W + E, pady = 5)
   show.grid(row=5, column = 3, pady = 5)
   plus.grid(row=2, column = 0, pady = 5)
   minus.grid(row=3, column = 0, pady = 5)
   multi.grid(row=4, column = 0, pady = 5)
   divi.grid(row=5, column = 0, pady = 5)
   close.grid(row=5, column = 1, pady = 5)

   button_1.grid(row=2, column = 1, pady = 5)
   button_2.grid(row=2, column = 2, pady = 5)
   button_3.grid(row=2, column = 3, pady = 5)
   button_4.grid(row=3, column = 1, pady = 5)
   button_5.grid(row=3, column = 2, pady = 5)
   button_6.grid(row=3, column = 3, pady = 5)
   button_7.grid(row=4, column = 1, pady = 5)
   button_8.grid(row=4, column = 2, pady = 5)
   button_9.grid(row=4, column = 3, pady = 5)
   button_0.grid(row=5, column = 2, pady = 5)

   window.mainloop()

GUI()






















































