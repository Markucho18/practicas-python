contenido_original = ""

with open("archivo.txt", encoding="UTF-8") as archivo:
  contenido_original = archivo.read()
  print("El contenido del archivo es: ")
  print(contenido_original)
  longitud = len(contenido_original)
  print(f"La cantidad de caracteres del archivo es: {longitud}")
  archivo.seek(0)
  primeros_diez = archivo.read(10)
  print(f"Los primeros 10 caracteres son: {primeros_diez}")
  archivo.seek(0)
  lista_lineas = archivo.readlines()
  lista_alreves = []
  for i, linea in enumerate(reversed(lista_lineas)):
    lista_alreves.append(linea)
  print("Las lineas del archivo al reves son: ")
  for linea in lista_alreves:
    print(linea.strip())


with open("archivo.txt", "w", encoding="UTF-8") as archivo:
  nuevo_texto = input("Ingrese el texto a escribir: ")
  archivo.write(f"{nuevo_texto}\n")
  lineas = []
  continuar = 1
  while continuar == 1:
    continuar = int(input("Desea escribir una linea en el archivo? 0/1: "))
    if continuar != 1:
      print("saliendo...")
      break
    nueva_linea = input("Ingrese la linea: ")
    lineas.append(f"{nueva_linea}\n")
  archivo.writelines(lineas)

with open("archivo.txt", "a", encoding="UTF-8") as archivo:
  continuar = 1
  while continuar == 1:
    continuar = int(input("Desea escribir una jugador en el archivo? 0/1: "))
    if continuar != 1:
      print("saliendo...")
      break
    jugador = f"{input("Ingrese el jugador: ")}\n"
    archivo.write(jugador)

with open("archivo.txt", "r", encoding="UTF-8") as archivo:
  contenido = archivo.read()
  print(f"El resultado final del archivo es: {contenido}")


#Hola amigos de youtube como estan xd
#hoy os voy a enseñar a descargar el gta san andres full crack español 100% real no fake