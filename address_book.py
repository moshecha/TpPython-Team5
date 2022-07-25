import csv
import random
from datetime import date

def fecha():
    today = date.today() #Para la fecha
    return (f'{format(today.day)}/{format(today.month)}/{(today.year)}') 

def guardar_contacto (archivo,contacto):
    with open(archivo, "a+", newline ='\n') as csvfile:
        wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator='')
        wr.writerow(contacto)
        wr.writerow('\n')
    print('Nuevo contacto Ingresado:',','.join(contacto[:-1]))#el -1 le saca el ,'\n'
    
def ID ():
    Id = []
    idnumeros = list('1234567890')
    for i in range(5):
        Id.append(random.choice(idnumeros)) #Elige numeros para el id / o .extend
    random.shuffle(Id) #los mezcla
    Id = (f'Id:{"".join(Id)}')  #ordena en un str
    return Id



nombre = input('Nombre y Apellido: ')
direccion = input('Direccion: ')
numero = 'Tel: '+input('Telefono: ') 

archivo = 'addresses.csv'
newContacto = [nombre.title(),direccion.title(),numero,fecha(),ID()]#,'\n' 

guardar_contacto(archivo,newContacto)
