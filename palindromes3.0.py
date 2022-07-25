def verpalindromos ():
    palindromos = list()
    noPalindromos = list()
    palabra=''
    
    while palabra != 'x':
        palabra=input('(---Para salir ingrese: x )Ingresa una palabra: ')
        if palabra == palabra[::-1] and palabra != 'x':
            print('Es palindromo!')
            palindromos.append(palabra)
            
        elif palabra == 'x':
            print('SALIDA')
        else:
            print('No es palindromo')
            noPalindromos.append(palabra)
    return {
        print('-- Palindromos:', ",".join(palindromos), 'Total:', len(palindromos)),
        print('-- No palindromos:', ",".join(noPalindromos), 'Total:', len(noPalindromos)),
        print(f'Total de palabras ingresadas: {len(palindromos)+len(noPalindromos)}')
    }

verpalindromos()