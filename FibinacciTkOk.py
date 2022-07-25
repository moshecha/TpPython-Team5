import sys
from tkinter import *

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
    
def susfib (x):
    lista = list ()
    for i in range (x):
        lista.append(fib(i))
    return (lista)#"".join
    

###
def hacer_click():
 try:
  _valor = int(entrada_texto.get())
  _valor = susfib(_valor )
  etiqueta.config(text=_valor)
 except ValueError:
  etiqueta.config(text="Introduce un numero!")


app = Tk()
app.title("Susecion de Fibonacci")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultados de Fibonacci")
etiqueta.grid(column=1, row=1, sticky=(W,E))

boton = Button(vp, text="ver susecion!", command=hacer_click)
boton.grid(column=2, row=2)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)

app.mainloop()
