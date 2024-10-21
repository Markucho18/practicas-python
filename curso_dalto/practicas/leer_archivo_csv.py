import csv
import pandas as pd

#Puedo poner names={} para forzar columnas
df = pd.read_csv("./practicas/archivo.csv")

df_ordenados_nombre = df.sort_values("nombre")

for i, jugador in df:
  print(i, jugador)

print(df)

print(df_ordenados_nombre)

#MAAAAAAAAAAAAl
""" with open("./practicas/archivo.csv", encoding="UTF-8") as archivo:
  reader = csv.reader(archivo)
  for row in reader:
    print(row) """