
def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
    
print('                 ---Para salir ingrese: -1   ------')
cant = int(input('(Salir con -1) Ingrese la cantidad de fibonacci que queres ver: '))
while cant != -1:
    
    
    if cant > 0:
        for x in range(cant):
            print(x+1,'º:',fib(x))
        cant = int(input('(Salir con -1) Ingrese la cantidad de fibonacci que queres ver: '))
        
    else:
        print('Ingrese un numero mayor a 0')
        cant = int(input('(Salir con -1) Ingrese la cantidad de fibonacci que queres ver: '))
    