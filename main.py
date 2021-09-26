# DEVELOPER: Obed Paz - USAP

from Tkinter import *
import ttk
import os
import time
import tkFont
import tkMessageBox

# Crear ventana
window = Tk()
window.title("Control E/S")
window.geometry("400x300+0+0")

def on():
  print('on')

def off():
  print('off')

# Crear botones
btn_on = Button(window, text="Turn on", command=on).place(x=100,y=100)
btn_off = Button(window, text="Turn off", command=off).place(x=100,y=150)


window.mainloop()