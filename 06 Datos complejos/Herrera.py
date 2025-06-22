#1) Dado el diccionario precio_frutas

precios_frutas = {'Banana':1200, 'Ananá':2500, 'Melón':3000, 'Uva':1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado el en punto anterior,
# actualizar los precios de las siguientes frutas:

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Siguiedo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios

precios_frutas_lista = ['Banana', "Ananá", "Melón", "Uva", "Naranja", "Manzana", "Pera"]

# 4) Escribí un programa que permita almacenar y consultar números telefónicos
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

# Crear diccionario vacío para guardar los contactos
agenda = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i + 1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

# Consultar un contacto
consulta = input("\n¿A quién querés buscar? Ingresá el nombre: ")

if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontró ningún contacto con el nombre '{consulta}'.")

# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas(usando un set)
# un diccionario con la cantidad de veces que aparece cada palabra

# Solicitar una frase al usuario
frase = input("Ingresá una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# Obtener palabras únicas con un set
palabras_unicas = set(palabras)

# Contar la cantidad de veces que aparece cada palabra
frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Mostrar resultados
print("\nPalabras únicas:")
print(palabras_unicas)

print("\nFrecuencia de palabras:")
for palabra, cantidad in frecuencia_palabras.items():
    print(f"{palabra}: {cantidad}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# Diccionario para guardar alumnos y sus notas
alumnos = {}

# Cargar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno #{i + 1}: ")
    print(f"Ingresá las 3 notas de {nombre} (separadas por espacio):")
    notas = tuple(map(float, input().split()))
    
    # Validar que haya exactamente 3 notas
    while len(notas) != 3:
        print("Por favor ingresá exactamente 3 notas:")
        notas = tuple(map(float, input().split()))
    
    alumnos[nombre] = notas

# Mostrar promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:

Parcial1 = ('Sofia', 'Rodrigo', 'Lautaro')
Parcial2 = ('Sofia', 'Federico', 'Lucia') 
print(Parcial1 + Parcial2)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

# Diccionario inicial de productos con su stock
stock_productos = {
    "manzanas": 10,
    "naranjas": 5,
    "bananas": 8
}

# Mostrar productos disponibles
print("Productos disponibles:", list(stock_productos.keys()))

# Solicitar producto al usuario
producto = input("\nIngresá el nombre del producto que querés consultar: ").lower()

if producto in stock_productos:
    print(f"Stock actual de '{producto}': {stock_productos[producto]} unidades")

    # Consultar si quiere agregar más unidades
    opcion = input("¿Querés agregar unidades al stock? (s/n): ").lower()
    if opcion == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de '{producto}': {stock_productos[producto]} unidades")
else:
    print(f"El producto '{producto}' no existe en el inventario.")
    # Consultar si quiere agregarlo
    opcion = input("¿Querés agregarlo como nuevo producto? (s/n): ").lower()
    if opcion == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")

# Mostrar inventario final
print("\nInventario actualizado:")
for prod, cant in stock_productos.items():
    print(f"{prod}: {cant} unidades")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# las capitales sean las claves, los países sean los valores

original= {"Argentina":"Buenos Aires", "Chile": "Santiago", "España": "Madrid", "Alemania": "Berlin"}
invertido = {"Buenos Aires":"Argentina", "Santiago":"Chile", "Madrid":"España", "Berlin":"Alemania"}