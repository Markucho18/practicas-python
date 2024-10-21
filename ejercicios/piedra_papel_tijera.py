import random

jugadas = {
  "a": "piedra",
  "b": "papel",
  "c": "tijera"
}

def comprobar(opciones):
  if "a" in opciones and "b" in opciones:
    return opciones.index("b")
  elif "a" in opciones and "c" in opciones:
    return opciones.index("a")
  elif "b" in opciones and "c" in opciones:
    return opciones.index("c")

def jugar():
  print('Piedra = "a", Papel = "b", Tijera = "c"')
  print("Gana el mejor de 3")
  opciones = ["a", "b", "c"]
  victorias_usuario = 0
  victorias_maquina = 0
  while victorias_usuario < 3 and victorias_maquina < 3:
    opcion = input("Que juegas: ").lower()
    while opcion not in opciones:
      opcion = input("Ingrese una pocion valida: ").lower()
    opcion_maquina = random.choice(opciones)
    print(f"Jugaste {jugadas[opcion]} y la maquina jugó {jugadas[opcion_maquina]}")
    if opcion == opcion_maquina:
      print("Fue un empate!")
    else:
      ganador = comprobar([opcion, opcion_maquina])
      if ganador == 0:
        victorias_usuario = victorias_usuario + 1
        print(f"El usuario ha ganado la ronda, lleva {victorias_usuario} victorias")
      if ganador == 1:
        victorias_maquina = victorias_maquina + 1
        print(f"La maquina ha ganado la ronda, lleva {victorias_maquina} victorias")
  if victorias_usuario == 3:
    print("El usuario ha ganado el juego")
  elif victorias_maquina == 3:
    print("La maquina ha ganado el juego")

if __name__ == "__main__":
  jugar()