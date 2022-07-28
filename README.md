# EJERCICIOS A RESOLVER

- Contador de Palabras: Crear un algoritmo que permita realizar el conteo de
palabras de una frase ingresada por el usuario. Además, debe almacenar o registrar
las frases ingresadas en un archivo de texto. Cada vez que ejecuta el algoritmo,
debe mostrar un resumen con la cantidad de frases ingresadas y el total de
palabras, siempre y cuando el archivo de texto contenga información previa. Se
debe ingresar frases hasta que se ingrese una palabra o frase clave de salida (debe
contemplar ambas). Por ejemplo, el algoritmo termina si se ingresa alguna de las
siguientes frases: “abra cadabra”, “show time”, “the end”.

  - Nombre del script: word_counter.py
  - Nombre del archivo de texto: phrases.txt

- Palíndromos: Crear un algoritmo que permita identificar si una palabra ingresada
por el usuario es o no un palíndromo. Un palíndromo es una palabra que puede
leerse tanto de izquierda a derecha como de derecha a izquierda. Por ejemplo:
neuquen, a3l3a, okonoko, 153351. El programa finaliza cuando se ingresa alguna
palabra clave, como por ejemplo “aloha”, “bye”. Al finalizar el programa, se debe
presentar un resumen con la cantidad de palabras ingresadas, cuantas eran
palíndromos y cuantas no eran palíndromos.

  - Nombre del script: palindromes.py

- Fibonacci: Crear un algoritmo que permita ingresar un número entero, y muestre en
pantalla la sucesión fibonacci con la cantidad de elementos igual al número
ingresado. Por ejemplo, si se ingresa el número 3, se deberían mostrar los primeros
3 elementos de la serie: 1, 1, 2. Se debe controlar que el número ingresado sea
mayor que 0 y mostrar un mensaje informativo al respecto para que el usuario
ingrese otro número válido.

  - Nombre del script: fibonacci.py

- Generador de Contraseñas: Crear un algoritmo que permita generar una
contraseña aleatoria, solicitando al usuario la longitud de la misma, si desea que
tenga mayusculas, minusculas, numeros y/o caracteres especiales (tomaremos
únicamente los caracteres +, -, %, $, &, #). Por defecto, si el usuario no escoge
ninguna de las opciones propuestas, se debe generar una contraseña de 16 dígitos
alfanuméricos (letras mayúsculas, minúsculas y números).

  - Nombre del script: password_generator.py

- Libreta de Direcciones: Crear un algoritmo que permita registrar información de
una dirección en un archivo csv (valores separados por coma) con los siguientes
campos: ID (generado aleatoriamente), nombre identificatorio, dirección, teléfono,
fecha de registro (este último debe generarse automáticamente al realizar el
registro).

  - Nombre del script: address_book.py
  - Nombre del archivo de texto: addresses.csv

# Integrantes:

1. Moshe chami
2. Sharu Romano
3. Levcovich Uriel
4. Rubi Chaio
5. Integrante 5??? no aparece

# Correcciones

- Ejercicio __'contador de palabras'__: No mostrar el contenido del archivo cada vez que el usuario ingresa una nueva frase, solo mostrar la cantidad de frases y palabras. No se debe contar la palabra clave en el archivo ni tampoco sumarla en el conteo final.

- Ejercicio __'fibonacci'__: El primer valor de la serie de fibonacci es 1, no 0. La serie de fibonacci comienza con 1, 1, 2, 3, 5, 8, 13 ....

- Ejercicio __'libreta de direcciones'__: Se deben hacer algunas correcciones, solo almacenar las variables sin ningun agregado. Ver los comentarios en el archivo address_book.py

- Agregar los integrantes del grupo en la seccion Integrantes de este documento
