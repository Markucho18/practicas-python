import random
from palabras import palabras

def jugar():
  palabra_random = random.choice(palabras)
  palabra_oculta = ["_"] * len(palabra_random)
  print(" ".join(palabra_oculta))
  palabra_correcta = False
  fallos = 0
  while palabra_correcta == False:
    letra = input("Ingrese una letra porfavor: ")
    if letra in palabra_random:
      for i, letra_palabra in enumerate(palabra_random):
        if(letra_palabra == letra):
          palabra_oculta[i] = letra
      print("La letra se encuentra en la palabra")
    else:
      fallos = fallos + 1
      print(f"Le letra no se encuentra en la palabra, tienes {fallos}/5 fallos")
    if "_" not in palabra_oculta:
      print(f"Has acertado!, la palabra era {palabra_random}")
      palabra_correcta = True
      break
    if fallos == 5:
      print("Haz cometido 5 fallos y haz perdido!")
      break
    print(" ".join(palabra_oculta))

if __name__ == "__main__":
  jugar()