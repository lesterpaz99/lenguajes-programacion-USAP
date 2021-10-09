# DEVELOPER: Obed Paz - USAP

from Tkinter import *
import ttk
import tkFont 
import tkMessageBox 
import os
import time
import subprocess

# Crea ventana principal
main_window = Tk()
main_window.title("Control I/O")
main_window.geometry("600x400+0+0")

# Configura fuente para ventana principal
text1 = tkFont.Font(family="Helvetica", size=1)
text2 = tkFont.Font(family="Arial", size=14)

# Agrega titulo a la ventana principal
title = Label(main_window, text="Control GPIO", font=text1).place(x=100, y=10)

# Crea funciones de apagado y encendido
def on():
    print('on')
    os.system("sudo /./home/lesterpaz99/Documents/myFirstAppUSAP/turn_on.sh")

def off():
    print('off')
    os.system("sudo /./home/lesterpaz99/Documents/myFirstAppUSAP/turn_off.sh")

# Crea y agrega botones a la ventana principal
btn_on = Button(main_window, text="Turn on", command=on).place(x=100,y=100)
btn_off = Button(main_window, text="Turn off", command=off).place(x=100,y=150)

def update():
    pointer_file = open("/home/lesterpaz99/Documents/gpio_state.txt", "r")
    for line in pointer_file:
      field = line.split("\n")
      value = field[0]

      if (value == "1"):
        label_on = Label(main_window, text="ON", font=text1).place(x=100, y=200)
        main_window.after(1000, update)

      if (value == "0"):
        label_off = Label(main_window, text="OFF", font=text1).place(x=100, y=200)
        main_window.after(1000, update)

update()

def toplevel():
    # Variables globales
    global initial_hour
    global initial_min
    global final_hour
    global final_min

    window_time = Toplevel()
    window_time.title("Programacion de tiempo")
    window_time.geometry("400x300+180+100")

    # Define las variables globales como tipo cadena
    initial_hour.StringVar()
    initial_min.StringVar()
    final_hour.StringVar()
    final_min.StringVar()

    # Configura fuente para la venta del tiempo
    t1 = tkFont.Font(family="Helvetica", size=11, weight="bold")
    t2 = tkFont.Font(family="Arial", size=9, weight="bold")

    # Etiquetas / Labels
    subtitle_label = Label(window_time, text="Horario de activacion").place(x=10, y=10)
    label_ih = Label(window_time, text="Hora inicial", font=t2).place(x=10, y=50)
    label_im = Label(window_time, text="Minuto inicial", font=t2).place(x=10, y=100)
    label_fh = Label(window_time, text="Hora final", font=t2).place(x=10, y=150)
    label_fm = Label(window_time, text="Minuto inicial", font=t2).place(x=10, y=200)

    # Cajas de texto / Text boxes
    textbox_ih = Entry(window_time, textvariable=initial_hour, width=5).place(x=100, y=50)
    textbox_im = Entry(window_time, textvariable=initial_min, width=5).place(x=100, y=100)
    textbox_fh = Entry(window_time, textvariable=final_hour, width=5).place(x=100, y=150)
    textbox_fm = Entry(window_time, textvariable=final_min, width=5).place(x=100, y=200)

    # Botones / Buttons
    btn_save = Button(window_time, text="Guardar", command=save).place(x=100, y=250)

    window_time.mainloop()


main_window.mainloop()