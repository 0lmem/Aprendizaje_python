'''
Ejemplos de operadores logicos en Python
    1- Crear dos variables con valores numericos
    2- Crear una condicion con el operador logico and
    3- Crear una condicion con el operador logico or
    4- Crear una condicion con el operador logico not 

'''
num1 = int(5)
num2 = int(7)

# Con el operador logico and los dos condiciones tienes que ser verdaderas
if num1 >= 5 and num2 >= 5:
    print("Ambas condiciones se han cumplido")
else:
    print("No se ha cumplido una o las dos condiciones")

# Con el operador logico or solo una de las condiciones tiene que ser verdadera    
if num1 >= 5 or num2 <= 5:
    print("Una o ambas condicions se han cumplido")
else:
    print("Ninguna condicion se ha cumplido")

# COn el operador logico not se alterna la condicion
if not num2 > 6:
    print("La condicion se invirtio y se cumple al ser un numero menor a 6")
else:
    print("No se cumple la condicion porque el numero es mayor a 6")