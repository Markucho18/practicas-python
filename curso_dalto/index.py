#ANOTACIONES 06/10/24
impares_hasta = lambda num : list(filter(lambda x : x % 2 != 0, range(num)))

print(impares_hasta(17))

#ANOTACIONES 05/10/24
""" num1 = 5

num2 = 6

def sumar(a , b):
  return a + b

print(sumar(num1, num2))

#PARAMETRO ARGS
def sumar_todo(*numeros):
  return sum(numeros)

print(f"La suma total de los numeros es {sumar_todo(num1, num2, 5, 7)}") """

#ANOTACIONES 03/10/24
""" numeros = [22, 33, 44, 56, 21, 12]

for numero in numeros:
  print(numero * 10)

suma_total = 0
sumas = list()
for numero in numeros:
  suma_total += numero
  sumas.append(suma_total)
  print(suma_total)
  print(sumas)

for numero, suma in zip(numeros, sumas):
  print(f"El numero {numero} sumado a la suma de los anteriores: es {suma}")

texto = "Hola amigos de youtube como estan"
lista_texto = texto.split(" ")
for i, palabra in enumerate(lista_texto):
  print(palabra)
  if i == len(lista_texto) - 1:
    for letra in palabra:
      print(letra) """

#ANOTACIONES 30/04/24
""" 
#DICCIONARIOS
persona = {
  'nombre': "Pancracio",
  'apellido': "Gutierrez",
}

division_baja = 24 // 6

print(division_baja)
print(f"{persona["nombre"]} {persona["apellido"]}")
print(type(persona))

numero = int(input("Ingrese un numero"))

if numero > 4:
  print("El numero es mayor que 4")
else:
  print("El numero es menor que 4") """

#ANOTACIONES 29/04/24
""" #Tema arrays/tuplas
frutas = ( "manzana", "banana", "naranja") #no se modifica
print(frutas[2])

#Sets (similar objetos)
conjunto = {"huevos", 2, True, 3.1416}

#La tabla del 3:
for i in range(0, 31, 3):
  print(i)

def sumar(a, b):
  return a + b

print(sumar(1, 2))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filtrar números pares usando comprensión de listas
pares = [num for num in numeros if num % 2 == 0]

print(pares)  # Resultado: [2, 4, 6, 8]

cadena = "Hola, mundo!"

# Recortar la cadena y tomar solo los primeros 5 caracteres
nueva_cadena = ""
for i in range(5):
    nueva_cadena += cadena[i]

print(nueva_cadena)  # Resultado: 'Hola,' """

