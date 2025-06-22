'''
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

'''
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
'''

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

'''
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general.
'''

def potencia(n, m):
    if m <= 0:
        return 1
    else:
        return n * potencia(n, m-1)
    
print(potencia(4,2))

'''
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
'''

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(25))

'''
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto
sin espacios ni tildes, y devuelva True si es un palindromo o False si no lo es.
Requisitos: La solución debe ser recursiva, No se debe usar [::-1] ni la función reversed()'''

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

print(es_palindromo("reconocer"))


'''
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo
y devuelva la suma de todos sus digitos.
Restricciones: No se puede convertir el número a string, usá operaciones matemáticas(%, //) y recursión.
'''

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
print(suma_digitos(89))

'''
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
'''

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(25))

'''
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
'''

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

print(contar_digito(234243223, 2))