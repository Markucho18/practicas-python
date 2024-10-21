import random

def adivinar_numero_jugador():
  numero_random = random.randint(1, 100)
  prediccion = 0
  while prediccion != numero_random:
    prediccion = int(input("Ingresa un numero entre 1 y 100: "))
    if prediccion > numero_random:
      print("Ese numero es muy grande")
    elif prediccion < numero_random:
      print("Ese numero es muy pequeño")
  print(f"Haz adivinado el numero, era {numero_random}")

def adivinar_numero_computadora():
  minimo = 1
  maximo = 2
  numero_usuario = int(input("Introduzca un numero entre 1 y 100: "))
  while numero_usuario <= 0 or numero_usuario > 100:
    numero_usuario = int(input("Introduzca un numero valido: "))
  respuesta = ""
  print('Ingrese "a" si el numero es mayor')
  print('Ingrese "b" si el numero es menor')
  print('Ingrese "c" si el numero es correcto')
  while respuesta != "c":
    numero_computadora = random.randint(minimo, maximo)
    respuesta = input(f"Adivino el numero {numero_computadora}: ")
    if respuesta == "a":
      maximo = numero_computadora
    elif respuesta == "b":
      minimo = numero_computadora
    else:
      print("Ingrese un numero valido")
  print("He acertado el numero xd")
    
    
def adivinar_numero():
  juego = input("Que adivinara el numero tu(a) o la computadora(b)?: ")
  if juego == "a":
    adivinar_numero_jugador()
  elif juego == "b":
    adivinar_numero_computadora()

if __name__ == "__main__":
  adivinar_numero()
