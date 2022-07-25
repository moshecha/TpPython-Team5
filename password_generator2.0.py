import random

def elegir_caracteres():
    mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    minusculas = list('abcdefghijklmnopqrstuvwxyz')
    numeros = list('1234567890')
    especiales = list("+-%$&#")
    cantidad = (input('Ingrese longitud de clave a generar: '))
    if cantidad == '' or cantidad == '0':
        cantidad = 16
    else:
        cantidad = int(cantidad)
        
    hayMayuscula = input('Deseas que contenga Mayusculas? (si/no): ')
    hayMinuscula = input('Deseas que contenga Minusculas? (si/no): ')
    hayNumeros = input('Deseas que contenga Numeros? (si/no): ')
    hayEspeciales = input('Deseas que contenga Caracteres especiales? (si/no): ')
    
    clave = []
    var1 = 0  # va a sumar los tipos de caracteres para dividirlos

    caracteresAusar = list()
    # agregamos a la lista los caracteres a usar!
    if hayMayuscula == 'si':
        caracteresAusar += mayusculas
        var1 += 1
    if hayMinuscula == 'si':
        caracteresAusar += minusculas
        var1 += 1
    if hayNumeros == 'si':
        caracteresAusar += numeros
        var1 += 1
    if hayEspeciales == 'si':
        caracteresAusar += especiales
        var1 += 1
    if hayMayuscula != 'si' and hayMinuscula != 'si' and hayNumeros != 'si' and hayEspeciales != 'si':
        caracteresAusar = mayusculas + minusculas + numeros
    if var1 == 0:  # si no se elige los caracteres vale 1
        var1 = 1
    var2 = cantidad // var1  # divide la cantidad por los tipos de caracteres
    # en caso que falten caracteres los detectamos!
    var3 = cantidad - (var1 * var2)
    
        # ahora q tenemos las cantidades los elige random
    if hayMayuscula == 'si':
        for i in range(var2):
            clave.append(random.choice(mayusculas))
    if hayMinuscula == 'si':
        for i in range(var2):
            clave.append(random.choice(minusculas))
    if hayNumeros == 'si':
        for i in range(var2):
            clave.append(random.choice(numeros))
    if hayEspeciales == 'si':
        for i in range(var2):
            clave.append(random.choice(especiales))
    if hayMayuscula != 'si' and hayMinuscula != 'si' and hayNumeros != 'si' and hayEspeciales != 'si':  # en caso de no elegir nada
        for i in range(var2):
            clave.append(random.choice(caracteresAusar))

    #luego, agregamos si faltan
    if var3 > 0:
        for i in range(var3):
            clave.append(random.choice(caracteresAusar))


    random.shuffle(clave) #los mezcla una vez mas!
    
    #print('caracteres usados:', ",".join(caracteresAusar)) #opcional los usados
    print('')
    print('Clave: ', "".join(clave), '    Cantidad de Caracteres:', len(clave)) #join los muestra seguidos, y len muestra la cantidad
    return ''
    
    
print(elegir_caracteres())



