# DEVELOPER: Obed Paz - USAP

from Tkinter import *
import ttk
import tkFont 
import tkMessageBox 
import os
import time

# Crear ventana
window = Tk()
window.title("Control E/S")
window.geometry("400x300+0+0")

def on():
  print('on')
  os.system("sudo /./home/lesterpaz99/Documents/myFirstAppUSAP/turn_on.sh")

def off():
  print('off')
  os.system("sudo /./home/lesterpaz99/Documents/myFirstAppUSAP/turn_off.sh")

# Crear botones
btn_on = Button(window, text="Turn on", command=on).place(x=100,y=100)
btn_off = Button(window, text="Turn off", command=off).place(x=100,y=150)


window.mainloop()