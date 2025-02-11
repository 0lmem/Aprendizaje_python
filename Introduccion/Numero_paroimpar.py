'''
Ejericio 3: Crear un programa que identifique si un numero es par o impar.
    1- Pedir al usuario un numero entero
    2- Crear una condicion para saber si el numero es par o impar
'''

print("Identificar si el numero es par o impar")

numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")