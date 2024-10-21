sumar = lambda x, y : x + y
restar = lambda x, y : x - y
multiplicar = lambda x, y : x * y
dividir = lambda x, y : x / y

def calcular ():
  continuar = True
  while continuar:
    continuar = input("Desea realizar calculos? ").lower() == "s"
    if not continuar:
      print("Saliendo...")
      break
    print("1: Sumar")
    print("2: Restar")
    print("3: Multiplicar")
    print("4: Dividir")
    operacion = int(input("Que operacion desea realizar? "))
    if operacion > 0 and operacion < 5:
      num1 = int(input("Digame el primer numero: "))
      num2 = int(input("Digame el segundo numero: "))
      if operacion == 1:
        print(f"El resultado de su suma es: {sumar(num1, num2)}")
      elif operacion == 2:
        print(f"El resultado de su resta es: {restar(num1, num2)}")
      elif operacion == 3:
        print(f"El resultado de su multiplicacion es: {multiplicar(num1, num2)}")
      elif operacion == 4:
        print(f"El resultado de su division es: {dividir(num1, num2)}")
    else:
      print("Ese numero de operacion no es valido")

if(__name__ == "__main__"):
  calcular()