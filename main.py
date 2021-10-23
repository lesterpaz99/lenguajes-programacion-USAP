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

# Declarar imagenes
# El parametro file busca la imagen desde el directorial actual
img_on = PhotoImage(file="../on.gif")
img_off = PhotoImage(file="../off.gif")

# Configura fuente para ventana principal
text1 = tkFont.Font(family="Helvetica", size=16)
text2 = tkFont.Font(family="Arial", size=14)

# Agrega titulo a la ventana principal
title = Label(main_window, text="Control GPIO", font=text1).place(x=20, y=20)

# EXAMEN
# ------
def update():
    # actualiza el label / etiqueta del estado

    pointer_file = open("/home/lesterpaz99/Documents/gpio_state.txt", "r")
    for line in pointer_file:
        field = line.split("\n")
        value = field[0]

        if (value == "1"):
            #label = Label(main_window, text="ON  ", font=text1)
            #label.place(x=540, y=20)
            label2 = Label(main_window, image=img_on)
            label2.place(x=140, y=100)

        if (value == "0"):
            #label = Label(main_window, text="OFF", font=text1)
            #label.place(x=540, y=20)
            label2 = Label(main_window, image=img_off)
            label2.place(x=140, y=100)

        main_window.after(1000, update)

update()

# Esta funcion es repetitiva, he agregado la imagen en la funcion update original (arriba) 
def update2():
    # actualiza el label / etiqueta del estado

    pointer_file = open("/home/lesterpaz99/Documents/gpio_state2.txt", "r")
    for line in pointer_file:
        field = line.split("\n")
        value = field[0]

        if (value == "1"):
            label = Label(main_window, image=img_on)
            label.place(x=260, y=100)

        if (value == "0"):
            label = Label(main_window, image=img_off)
            label.place(x=260, y=100)

        main_window.after(1000, update2)

update2()

def update3():
    # actualiza el label / etiqueta del estado

    pointer_file = open("/home/lesterpaz99/Documents/gpio_state3.txt", "r")
    for line in pointer_file:
        field = line.split("\n")
        value = field[0]

        if (value == "1"):
            label = Label(main_window, image=img_on)
            label.place(x=380, y=100)

        if (value == "0"):
            label = Label(main_window, image=img_off)
            label.place(x=380, y=100)

        main_window.after(1000, update3)

update3()

# --------------
# FIN DEL EXAMEN
def save():
    # Inserta la configuracion a los archivos en cron
    
    print('Saved')
    ih = initial_hour.get()
    im = initial_min.get()
    fh = final_hour.get()
    fm = final_min.get()
    tab = " "
    month = day = year = "*"
    user = "root"
    path1 = "/home/lesterpaz99/Documents/myFirstAppUSAP/turn_on.sh"
    path2 = "/home/lesterpaz99/Documents/myFirstAppUSAP/turn_off.sh"
    
    # tc stands for time-config
    string_tc1 = str(im+tab+ih+tab+day+tab+month+tab+year+tab+user+tab+path1)
    string_tc2 = str(fm+tab+fh+tab+day+tab+month+tab+year+tab+user+tab+path2)
    
    # agrega full permisos y escribe en archivos
    os.system("sudo chmod -R 777 /etc/cron.d/process1")    
    file_pointer1 = open("/etc/cron.d/process1", "w")
    file_pointer1.write(string_tc1)
    file_pointer1.write("\n")
    file_pointer1.close()
    
    os.system("sudo chmod -R 777 /etc/cron.d/process2")
    file_pointer2 = open("/etc/cron.d/process2", "w")
    file_pointer2.write(string_tc2)
    file_pointer2.write("\n")
    file_pointer2.close()
    
    # Revertir permisos
    os.system("sudo chmod -R 755 /etc/cron.d/process1")
    os.system("sudo chmod -R 755 /etc/cron.d/process2")
    
    # Reinia el servicio
    os.system("sudo /etc/init.d/cron restart")

# Crea funciones de apagado y encendido
def on():
    print('on')
    os.system("sudo /./home/lesterpaz99/Documents/myFirstAppUSAP/turn_on.sh")

def off():
    print('off')
    os.system("sudo /./home/lesterpaz99/Documents/myFirstAppUSAP/turn_off.sh")

def toplevel():
    # Maqueta la ventana para la configuracion del tiempo
    
    # Variables globales
    global initial_hour
    global initial_min
    global final_hour
    global final_min
    
    window_time = Toplevel()
    window_time.title("Programacion de tiempo")
    window_time.geometry("400x300+180+100")
    
    # Define las variables globales como tipo cadena
    initial_hour = StringVar()
    initial_min = StringVar()
    final_hour = StringVar()
    final_min = StringVar()
    
    # Configura fuente para la venta del tiempo
    t1 = tkFont.Font(family="Helvetica", size=11, weight="bold")
    t2 = tkFont.Font(family="Arial", size=9, weight="bold")
    
    # Etiquetas / Labels
    subtitle_label = Label(window_time, text="Horario de activacion", font=t1)
    subtitle_label.place(x=10, y=10)
    label_ih = Label(window_time, text="Hora inicial", font=t2)
    label_ih.place(x=10, y=50)
    label_im = Label(window_time, text="Minuto inicial", font=t2)
    label_im.place(x=10, y=100)
    label_fh = Label(window_time, text="Hora final", font=t2)
    label_fh.place(x=10, y=150)
    label_fm = Label(window_time, text="Minuto final", font=t2)
    label_fm.place(x=10, y=200)
    
    # Cajas de texto / Text boxes
    textbox_ih = Entry(window_time, textvariable=initial_hour, width=5)
    textbox_ih.place(x=100, y=50)
    textbox_im = Entry(window_time, textvariable=initial_min, width=5)
    textbox_im.place(x=100, y=100)
    textbox_fh = Entry(window_time, textvariable=final_hour, width=5)
    textbox_fh.place(x=100, y=150)
    textbox_fm = Entry(window_time, textvariable=final_min, width=5)
    textbox_fm.place(x=100, y=200)
    
    # Botones / Buttons
    btn_save = Button(window_time, text="Guardar", command=save)
    btn_save.place(x=100, y=250)
    
    window_time.mainloop()

# Crea y agrega botones a la ventana principal
btn_on = Button(main_window, text="Turn on", command=on).place(x=20,y=100)
btn_off = Button(main_window, text="Turn off", command=off).place(x=20,y=150)
btn_window_time = Button(main_window, text="Configurar tiempo", command=toplevel).place(x=20,y=200)


main_window.mainloop()