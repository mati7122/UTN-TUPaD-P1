from datetime import datetime 

''' 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. '''

user_year = 0

user_year = int(input("Por favor, ingrese su edad: "))
if user_year >= 18:
    print("El usuario es mayor de edad.")

'''
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”
'''

user_note = 0

user_note = float(input("Ingrese su nota: "))
if user_note >= 6:
    print("Aprobado!")
else:
    print("Desaprobado")

'''
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.

'''

par_number = 0

par_number = int(input("Ingrese un número par: "))
if par_number % 2 == 0:
    print("Ah ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

'''
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
'''

user_year2 = 0

user_year2 = int(input("Ingrese su edad: "))

if user_year2 >= 0 and user_year2 <= 12:
    print("Niño/a: menor de 12 años.")
elif user_year2 >= 12 and user_year2 < 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif user_year2 >= 18 and user_year2 < 30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif user_year2 >= 30:
    print("Adulto/a: mayor o igual que 30 años.")

'''
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
'''

password = ''

password = input("Ingrese una contraseña válida(Entre 8 y 14 caracteres): ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

'''
6) Escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
'''

from statistics import median, mode, mean
import random  

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Se encuentra un sesgo positivo o a la derecha.")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Se encuentra un sesgo negativo o a la izquierda.")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("No se ha encontrado ningún sesgo.")


'''
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla
'''

text = input("Ingresa una frase o palabra: ")
vowels = "aeiouAEIOU"

if text[-1] in vowels:
    text += "!" 

print(text)


'''
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
'''
user_name = ''
option = 0

user_name = input("Ingrese su nombre: ")

print("Ingrese un número según...")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra mayúscula")
option = int(input("Ingrese un numero: "))

match option:
    case 1:
        print(user_name.upper())
    case 2:
        print(user_name.lower())
    case 3:
        print(user_name.capitalize())

'''
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
'''

scale = 0

scale = float(input("Ingrese la magnitud del terremoto: "))

if scale < 3:
    print("Muy leve (imperceptible)")
elif scale >= 3 and scale < 4:
    print("Leve (ligeramente perceptible)")
elif scale >= 4 and scale < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif scale >= 5 and scale < 6:
    print("Fuerte (Puede causar daños en estructuras débiles)")
elif scale >= 6 and scale < 7:
    print("Muy fuerte (Puede causar daños significativos)")
elif scale >= 7:
    print("Extremo (Puede causar graves daños a gran escala)")

'''
10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
'''

hemisphere = ''

hemisphere = input("Ingrese en que hemisferio se encuentra(N/S) :")
hemisphere = hemisphere.upper()

if hemisphere != 'N' and hemisphere != 'S':
    while hemisphere == hemisphere != 'N' and hemisphere != 'S':
        hemisphere = input("Por favor, ingrese un valor válido")

date_day = int(input("Ingrese el día: "))
date_month = int(input("Ingrese el mes: "))
date_year = int(input("Ingrese el año: "))

converted_date = datetime(date_year, date_month, date_day)

if converted_date >= datetime(date_year - 1, 12, 21) and converted_date <= datetime(date_year, 3, 20):
    if hemisphere == 'N':
        print("Usted se encuentra en invierno")
    else:
        print("Usted se encuentra en verano")
elif converted_date >= datetime(date_year, 3, 21) and converted_date <= datetime(date_year, 6, 20):
    if hemisphere == 'N':
        print("Usted se encuentra en primavera")
    else:
        print("Usted se encuentra en otoño")
elif converted_date >= datetime(date_year, 6, 21) and converted_date <= datetime(date_year, 9, 20):
    if hemisphere == 'N':
        print("Usted se encuentra en verano")
    else:
        print("Usted se encuentra en invierno")
elif converted_date >= datetime(date_year, 9, 21) and converted_date <= datetime(date_year, 12, 20):
    if hemisphere == 'N':
        print("Usted se encuentra en otoño")
    else:
        print("Usted se encuentra en Primavera")

