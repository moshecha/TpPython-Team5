# Import Module
from tkinter import *

def es_palindromo(x):
    return x == x[::-1]

def no_es_palindromo(x):
    return x != x[::-1]

lista_de_palindromos = []
lista_de_no_palindromos = []

# Create Object
root = Tk()
root.title('Verificando Capicuas')
#root.configure(bg='green')
# Set geometry
#root.geometry('400x500')
  
# Information List
datas = []
  
# Add Information
def add():
    global datas
    datas.append([Name.get()]) #,address.get(1.0, "end-1c")
    
    Label(frame3,foreground="blue", background="white", text = Name.get(), font='arial 12 bold').pack(side=LEFT)
    if len(Name.get())>=2:
        #lista_palabras.append([Name.get()])
        if Name.get() == Name.get()[::-1]:
            lista_de_palindromos.append(Name.get())  
            etiqueta.config(text=(f"{Name.get()}: Es Palindromo") ,foreground="green", background="white", )
        else:
            lista_de_no_palindromos.append(Name.get())
            etiqueta.config(text=(f"{Name.get()}: No es palindrmo"),foreground="red", background="white",)
    else:
        etiqueta.config(text=(f"Ingrese una palabra"),foreground="red", background="white",)
    listpali = (f"Palindromos ok: {','.join(lista_de_palindromos)}   En total: {len(lista_de_palindromos)}")
    listnopali = (f"No Palindromos: {','.join(lista_de_no_palindromos)}   En total:{len(lista_de_no_palindromos)}")
    
    etiqueta1.config(text=listpali)
    etiqueta2.config(text=listnopali)
    Name.set('') #limpia la barra de ingreso de palabras

# Add Buttons, Label, ListBox
Name = StringVar()
  
frame = Frame() #ingreso de palabras
frame.pack(pady=10)

etiqueta = Label( text="Ingrese una palabra!!!!") #imprime si o no palin
etiqueta.pack()

Button(root,text="Verificar",font="arial 12 bold",command=add).pack()

etiqueta1 = Label( text="Palabras palindromas!!!!",foreground="blue")
etiqueta1.pack()

etiqueta2 = Label( text="Palabras no palindromas!!!!",foreground="blue")
etiqueta2.pack()

frame3 = Frame() # imprime las palabras ingresadas
frame3.pack(pady=5)

Label(frame, text = 'Palabra', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=50).pack()
  
  #Resultados
Label(frame3, text = 'Palabras Ingresadas:', font='arial 12 bold').pack(side=TOP)

# Execute Tkinter
root.mainloop()