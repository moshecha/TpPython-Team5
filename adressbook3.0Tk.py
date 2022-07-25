from tkinter import *
import csv
import random
from datetime import date

# Create Object
root = Tk()
  
# Set geometry
root.geometry('500x500')
root.title('Nuevo Contacto')

def fecha():
    today = date.today() #Para la fecha
    return (f'{format(today.day)}/{format(today.month)}/{(today.year)}') 

def guardar_contacto (archivo,contacto):
    with open(archivo, "a+", newline ='\n') as csvfile:
        wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator='')
        wr.writerow(contacto)
        wr.writerow('\n')
    #print('Nuevo contacto Ingresado:',','.join(contacto[:-1]))#el -1 le saca el ,'\n'
    
def ID ():
    Id = []
    idnumeros = list('1234567890')
    for i in range(5):
        Id.append(random.choice(idnumeros)) #Elige numeros para el id / o .extend
    random.shuffle(Id) #los mezcla
    Id = (f'Id:{"".join(Id)}')  #ordena en un str
    return Id


def click_boton ():
    Label(root, text=(f"Nuevo contacto:{nombre.get().title()}, Tel:{telefono.get()}, Direccion: {direccion.get().title()}")).pack()
    Label(root, text=(f"{fecha()}, {ID()} ")).pack()

    archivo = 'addresses.csv'
    newContacto = [nombre.get().title(),direccion.get().title(),telefono.get(),fecha(),ID()]#,'\n' 

    guardar_contacto(archivo,newContacto)


nombre = StringVar()
telefono = StringVar()
direccion = StringVar()

frame = Frame()
frame.pack()

frame1 = Frame()
frame1.pack()
  
frame2 = Frame()
frame2.pack()
  
Label(frame, text = 'Nombre', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = nombre,width=50).pack()
  
Label(frame1, text = 'Telefono', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = telefono,width=50).pack()
  
Label(frame2, text = 'Direccion', font='arial 12 bold').pack(side=LEFT)
Entry(frame2, textvariable = direccion,width=50).pack()

boton1 = Button(root,
				text="Guardar",
				bg="red",
				padx=30,
				pady=5,
                font="arial 12 bold",
				command=click_boton).pack()



root.mainloop()