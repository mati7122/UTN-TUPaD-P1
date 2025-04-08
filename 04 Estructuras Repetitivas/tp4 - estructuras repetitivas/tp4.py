'''
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
'''

for i in range(0, 101):
    print(i)

'''
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
'''

number = 0

number = input("Ingrese un número entero: ")

print("La cantidad de digitos que contiene el número ingresado es: ", len(number))

'''
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
'''

number_two = 0
result = 0

number_one = int(input("Ingrese el primer valor: "))
number_two = int(input("Ingrese el segundo valor: "))

for i in range(number_one+1, number_two):
    result = result+i

print(result)

'''
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
'''


total = 0
print("Ingresa 0 para finalizar el sumador.")
user_input = int(input("Ingrese un número: "))

while user_input != 0:
    total += user_input
    user_input = int(input("Ingrese un nuevo número: "))

print("El resultado es: ", total)

'''
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
'''

from random import randint

random_number = randint(0, 9)
tries = 1
print(random_number)

print("Ingrese un número a adivinar por el algoritmo")
user_input = int(input("Ingrese un valor: "))

while user_input != random_number:
    tries += 1
    user_input = int(input("Ingrese un nuevo valor: "))

print("El número es: ", random_number)
print("Le ha tomado al usuario ", tries, " intento(s) adivinar el número")

'''
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
'''

for i in range(1, 100+1):
    if i % 2 == 0:
        print(i)

'''
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
'''

user_input = int(input("Ingrese un número entero positivo: "))
total = 0

for i in range(0, user_input+1):
    total += i

print("El total es: ", total)

'''
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
'''
count = 0
user_input = 0
limit = 10 # límite para finalizar el algoritmo

# acumuladores de cada tipo de número
pair_number = 0
odd_number = 0
pos_number = 0
neg_number = 0

while count < limit:
    user_input = int(input("Ingresa un número entero: "))

    if user_input % 2 == 0 and user_input != 0:
        pair_number += 1
    elif user_input % 2 != 0 and user_input != 0:
        odd_number += 1
    
    if user_input > 0:
        pos_number += 1
    elif user_input < 0: 
        neg_number += 1

    count += 1

print("Estos son los resultados")
print("Números pares ingresado: ", pair_number)
print("Números impares ingresado: ", odd_number)
print("Números positivos ingresado: ", pos_number)
print("Números negativos ingresado: ", neg_number)

'''
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
'''

user_input = 0
limit = 10
counter = 0 
total = 0

print("El programa se detendra cuando usted ingrese ", limit, " números.")

while counter < limit:
    user_input = float(input("Ingrese un valor al acumulador: "))
    total += user_input
    counter += 1

print(total)
print("El valor del total es de: ", total / limit)

'''
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
'''

print("Ingrese un número a invertir su orden")
raw_number = input("Ingrese un número: ")
inverted_number = []
string_number = ''

for i in range(len(raw_number)-1, -1, -1):
    inverted_number.append(raw_number[i])

for i in range(0, len(raw_number), 1):
    string_number += inverted_number[i]

print("El número invertido es ", string_number)