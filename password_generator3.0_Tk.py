from tkinter import *
import random
from tkinter.ttk import Separator

root = Tk()
root.title("GCA (Generar Clave Automatica)")
root.geometry("450x450")

mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
minusculas = list('abcdefghijklmnopqrstuvwxyz')
numeros = list('1234567890')
especiales = list("+-%$&#")
clave = list()
var1 = 0  # va a sumar los tipos de caracteres para dividirlos
caracteresAusar = []

def seleccion():
    clave = list()
    var1 = 0
    if cantidad.get() == 0:
        cantidad.set(16)
    
    if control1.get()==1:
        var1 += 1
    if control2.get()==1:
        var1 += 1
    if control3.get()==1:
        var1 += 1
    if control4.get()==1:
        var1 += 1
    
    if var1 == 0:
        var1 = 3  
    var2 = cantidad.get() // var1  
    
    if control1.get()==1:
        caracteresAusar.append(mayusculas)
        for i in range(var2):
            clave.append(random.choice(mayusculas))
            
    if control2.get()==1:
        caracteresAusar.append(minusculas)
        for i in range(var2):
            clave.append(random.choice(minusculas))
    if control3.get()==1:
        caracteresAusar.append(numeros)
        for i in range(var2):
            clave.append(random.choice(numeros))
    if control4.get()==1:
        caracteresAusar.append(especiales)
        for i in range(var2):
            clave.append(random.choice(especiales))
    
    if control1.get()!=1 and control2.get()!=1 and control3.get()!=1 and control4.get()!=1:
        for i in range(var2):
            clave.append(random.choice(mayusculas))
        for i in range(var2):
            clave.append(random.choice(minusculas))
        for i in range(var2):
            clave.append(random.choice(numeros))
    
    var3 = cantidad.get() % var1
    if var3 >=1 :#or 
        if control1.get()==1:
            for i in range(var3):
                clave.append(random.choice(mayusculas))
        elif control2.get()==1:
            for i in range(var3):
                clave.append(random.choice(minusculas))
        elif control3.get()==1:
            for i in range(var3):
                clave.append(random.choice(numeros))
        elif control4.get()==1:
            for i in range(var3):
                clave.append(random.choice(especiales))
        else:
            for i in range(var3):
                clave.append(random.choice(numeros)) 
    
    random.shuffle(clave)
   
    etiqueta4 = Label(root, text= clave).pack()
    etiqueta5 = Label(root, text=(f'cantidad de caracteres: {len(clave)} ')).pack()
    cantidad.set(0)
cantidad = IntVar()

control1 = IntVar()
control2 = IntVar()
control3 = IntVar()
control4 = IntVar()

# cant = Spinbox(root, from_=0, to=20, wrap=True,textvariable=cantidad ,state='readonly')
# cant.pack()
etiqueta2 = Label(root, text= "Cuantos caracteres deseas que contega la clave?",foreground="white", background="blue",
                               borderwidth=5, anchor="e").pack()
ingresecantidad = Entry(root, width=5,textvariable= cantidad).pack()
#cantidad.insert(0, "Escriba aquí...")
#cantidad.grid(row=0, column=0)
etiqueta1 = Label(root, text= 'Marca lo que deseas que contenga:').pack()

opcion_1 = Checkbutton(root,
                      text="Mayusculas",
                      variable=control1,
                      onvalue=1,
                      offvalue=0)
opcion_1.pack()
opcion_1.deselect()

opcion_2 = Checkbutton(root,
                      text="Minusculas",
                      variable=control2,
                      onvalue=1,#caracteresAusar.append(minusculas)
                      offvalue=0)

opcion_2.pack()
opcion_2.deselect()

opcion_3 = Checkbutton(root,
                      text="Numeros",
                      variable=control3,
                      onvalue=1,#caracteresAusar.append(numeros)
                      offvalue=0)
opcion_3.pack()
opcion_3.deselect()

opcion_4 = Checkbutton(root,
                      text="Simbolos",
                      variable=control4,
                      onvalue=1,#caracteresAusar.append(especiales)
                      offvalue=0)
opcion_4.pack()
opcion_4.deselect()

muestra_seleccion = Button(root, text="Generar Clave", command=seleccion).pack()
separ1 = Separator(root, orient=HORIZONTAL).pack()
boton1 = Button(root, text="Salir", command=quit) .pack()
mainloop()