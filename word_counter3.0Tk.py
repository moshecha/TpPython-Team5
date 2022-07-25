from tkinter import *
root = Tk()
root.geometry("550x550")
root.title('Guardando y contando Frases!!!')
def contarpalabras(a):
    a = a.split()
    a = len(a)
    et1=Label(root, text=(f"--- {a} Palabras contadas en la frase")).pack()#grid(row=4, column=0)
    
    
def guardafrase (a,b):
    c = open(a, 'a')
    c.write(b + '\n')
    c.close()
    et2 = Label(root,font="arial 14 bold", text=(f"--- Frase Ingresada: '{b}'")).pack()#grid(row=3, column=0)
    
    
def contarfrases(a):
    archivo = open(a)
    cant_frases =0
    
    for lineas in archivo:
        cant_frases += 1
    et3 = Label(root, text=(f"--- En el Archivo hay {cant_frases} frases")).pack()#grid(row=5, column=0)

    
def contarpalabrasArchivo(a):
    numpalabras = 0
    simbolos = ['¿', '?', '.', ',', ';', ':', '¡', '!']
    with open(a) as fichero:
        for linea in fichero:
                for simbolo in simbolos:
                    # remplaza los simbolos por espacios
                    linea = linea.replace(simbolo, ' ')
                palabras = linea.split()  # hace una lista de palabras

                for palabra in palabras:
                    numpalabras += 1
    et4 =  Label(root, text=(f"--- En el Archivo hay {numpalabras} palabras")).pack()#grid(row=6, column=0)
#cuantas palabras hay en el archivo?
    
def imprimirFrases(a):
    Label(ventana_nueva1, text=(f"FRASES GUARDADAS")).grid(row=7, column=1)
    archivo = open(a)
    renglon = 8
    for lineas in archivo:
        et5 = Label(ventana_nueva1, text=(f"- {lineas}")).grid(row=renglon, column=1)
        renglon +=1
        




fras = StringVar()
texto0 = Label(root, text="Archivando Frases",font="arial 20 bold").pack()#grid(row=0, column=1)
texto1 = Label(root,font="arial 14 bold", text="Ingrese una Frase:").pack()
ingresofrase = Entry(root,textvariable=fras)
ingresofrase.pack()#grid(row=1, column=1)
#grid(row=1, column=0)
archivo = 'archivo.txt'

def click_boton():
        #texto = Label(root, text='¡Se envío correctamente!').pack()#grid(row=0, column=0)
        frase = fras.get()
        archivo = 'archivo.txt'
        guardafrase(archivo,frase)
        contarpalabras(frase)
        contarpalabrasArchivo(archivo)
        contarfrases(archivo)
        imprimirFrases(archivo)
        fras.set('')
        return 0 

ventana_nueva1 = Toplevel()
#ventana_nueva1.geometry("300x200")
ventana_nueva1.title("Frases Guardadas")

boton1 = Button(root,
				text="Guardar",
				foreground="red",
				padx=30,
				pady=5,
                font="arial 12 bold",
				command=click_boton).pack()#grid(row=1, column=3)

root.mainloop()