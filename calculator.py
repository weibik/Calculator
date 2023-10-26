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

   show = ttk.Button(window, text="=", command=button_result)
   plus = ttk.Button(window, text="+", command=button_plus)
   minus = ttk.Button(window, text="-", command=button_minus)
   multi = ttk.Button(window, text="*", command=button_multi)
   divi = ttk.Button(window, text="/", command=button_divi)
   close = ttk.Button(window, text="Close", command=window.destroy)

   buttons_list = []
   for i in range(10):
      buttons_list.append(ttk.Button(window, text =f"{i}", command = lambda i=i: button_click(i)))

   display.grid(row=1, column = 0, pady = 5)
   entry.grid(row = 1, column = 1, columnspan = 2, sticky = W + E, pady = 5)
   show.grid(row=5, column = 3, pady = 5)
   plus.grid(row=2, column = 0, pady = 5)
   minus.grid(row=3, column = 0, pady = 5)
   multi.grid(row=4, column = 0, pady = 5)
   divi.grid(row=5, column = 0, pady = 5)
   close.grid(row=5, column = 1, pady = 5)

   buttons = [
      ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
      ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
      ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
      ("0", 5, 2)
   ]
   row_num, col_num = 2, 1
   buttons_list.append(ttk.Button(window, text="0", command=lambda: button_click(0)))
   for button in buttons_list:
      button.grid(row=row_num, column=col_num, pady=5)
      col_num += 1
      if col_num > 3:
         col_num = 1
         row_num += 1

   window.mainloop()

GUI()