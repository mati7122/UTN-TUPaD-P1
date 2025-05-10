# Trabajo práctico N5

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range

list01 = range(1, 101, 4) # Esta línea no crea una lista propiamente, crea un elemento range.

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

list02 = [1, 2, 3, 4, 5]

print("Penúltimo ", list02[3])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:

lista_vacia = []

lista_vacia.append("mozo")
lista_vacia.append("computadora")
lista_vacia.append("heladera")

print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[3] = "oso"

print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7] # Se crea una variable de tipo lista para almacenar 5 valores diferentes de tipo integer
numeros.remove(max(numeros)) # La función max nos devuelve el números más grande
# dentro de nuestra lista y luego la función remove elimina el retorno de la anterior función mencionada
# print(numeros)  

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

list06 = range(10, 31, 5)

print(list06[0], list06[1])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = [ "sedan", "polo", "suran", "gol"]

autos[1] = "BMW"
autos [2] = "Buggati"

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

# ===========================================================================

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a)Agregar "jugo" a la lista del tercer cliente usando append.

compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.

compras[1][1] = "tallarines"
 
# c) Eliminar "pan" de la lista del primer cliente.

compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla

print(compras)

# ===========================================================================

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]

print(lista_anidada)