import importlib
import importlib.util

# En este ficheros se ejecuta el codigo resuelto de cada ejercicio en orden secuencial
# Se utiliza la libreria importlib para utilizar el fichero con las funciones

route = "./05 Funciones/MI-APELLIDO_TP-05.py"
name_route = "my_lib"

spec = importlib.util.spec_from_file_location(name_route, route)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def print_separator(num):
    print("========================")
    print(f"Problema Nº{num}")

# Problema N1
print("Problema Nº1")
module.imprimir_hola_mundo()

# Problema N2
print_separator(2)
asw_2 = input("Por favor ingrese su nombre: ")
module.saludar_usuario(asw_2)

# Problema N3
print_separator(3)
lst = ["nombre", "apellido", "edad", "residencia"]

for i in range(4):
    asw_2 = input(f"Por favor, ingrese su {lst[i]}: ")
    lst[i] = asw_2

module.informacion_personal(lst[0], lst[1], lst[2], lst[3])    

# Problema N4
print_separator(4)
radio = float(input("Ingrese el radio del circulo: "))
print(f"Su area es de {module.calcular_area_circulo(radio)}")
print(f"Su perimetro es de {module.calcular_perimetro_circulo(radio)}")

# Problema N5
print_separator(5)
seg = float(input("Ingresar los segundos a convertir: "))
print(f"El equivalente en horas es de {module.segundos_a_horas(seg)}")

# Problema N6
print_separator(6)
multiplicador = int(input("Ingrese el número a mutiplicar: "))
module.tabla_multiplicar(multiplicador)

# Problema N7
print_separator(7)
print(module.operaciones_basicas(8, 2))

# Problema N8
print_separator(8)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros"))
print(f"Segun los datos proporcionados su IMC es de : {module.calcular_imc(peso, altura)}")

# Problema N9 
print_separator(9)
deg = float(input("Ingresar temperatura en grados celsius: "))
print(f"Su equivalente a fahrenheint es: {module.celsius_a_fahrenheit(deg)}")

# Problema N10
print_separator(10)

lst10 = []
for i in range(1, 4):
    asw = int(input(f"Ingrese Nº{i}: "))
    lst10.append(asw)

print(f"El promedio es: {module.calcular_promedio(lst10[0], lst10[1], lst10[2])}")