# DEVELOPER: Obed Paz - USAP

from Tkinter import *
import ttk
import tkFont 
import tkMessageBox 
import os
import time

# Crear ventana
window = Tk()
window.title("Control I/O")
window.geometry("600x400+0+0")

# Configurar texto
text1 = tkFont.Font(family="Helvetica", size=1)
text2 = tkFont.Font(family="Arial", size=14)

def update():
  pointer_file = open("/home/lesterpaz99/Documents/gpio_state.txt", "r")
  for line in pointer_file:
    field = line.split("\n")
    value = field[0]

    if (value == "1"):
      label_on = Label(window, text="ON", font=text1).place(x=100, y=200)
      window.after(1000, update)

    if (value == "0"):
      label_off = Label(window, text="OFF", font=text1).place(x=100, y=200)
      window.after(1000, update)

update()

def on():
  print('on')
  os.system("sudo /./home/lesterpaz99/Documents/myFirstAppUSAP/turn_on.sh")

def off():
  print('off')
  os.system("sudo /./home/lesterpaz99/Documents/myFirstAppUSAP/turn_off.sh")

# Title
title = Label(window, text="Control GPIO", font=text1).place(x=100, y=10)

# Crear botones
btn_on = Button(window, text="Turn on", command=on).place(x=100,y=100)
btn_off = Button(window, text="Turn off", command=off).place(x=100,y=150)


window.mainloop()