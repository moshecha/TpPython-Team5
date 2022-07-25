def contarpalabras(a):
    a = a.split()
    a = len(a)
    return print('---',a,'Palabras contadas en la frase')

def guardafrase (a,b):
    c = open(a, 'a')
    c.write(b + '\n')
    c.close()
    return print('--Frase Ingresada:',b)

def contarfrases(a):
    archivo = open(a)
    cant_frases =0
    
    for lineas in archivo:
        cant_frases += 1
    print('---En el archivo hay', cant_frases, 'frases')#cuantas frases hay?

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
    print('---En el archivo hay', numpalabras, 'palabras')#cuantas palabras hay en el archivo?
    
    
def imprimirFrases(a):
    print(' FRASES EN EL ARCHIVO --')
    archivo = open(a)
    for lineas in archivo:
        print ('-', lineas)
 
frase = ''       
while frase != 'salir' and frase != 'x':
    frase = input('ingrese frase: ')
    archivo = 'archivo.txt'
    guardafrase(archivo,frase)
    contarpalabras(frase)
    contarpalabrasArchivo(archivo)
    contarfrases(archivo)
    imprimirFrases(archivo)
