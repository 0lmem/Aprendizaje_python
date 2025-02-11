'''
Calculadora simple
    1- Crear un menu de opciones
    2- Pedir al usuario que seleccione una opcion
    3- Pedir al usuario dos numeros
    4- Realizar la operacion seleccionada
'''

print("---------------------")
print("  Menu de opciones")
print("---------------------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto\n")

operador = int(input("Introduce la operacion deseada: "))
numero = float(input("Introduce el primer numero: "))

if operador == 1:
    numero += float(input("Introduce el segundo numero: "))
    print("La suma de los numeros es: ",numero)
elif operador == 2:
    numero -= float(input("Introduce el segundo numero: "))
    print("La resta de los numeros es: ",numero)
elif operador == 3:
    numero *= float(input("Introduce el segundo numero: "))
    print("La multiplicacion de los numeros es: ",numero)
elif operador == 4:
    numero /= float(input("Introduce el segundo numero: "))
    print("La division de los numeros es: ",numero)
elif operador == 5:
    numero //= float(input("Introduce el segundo numero: "))
    print("La division entera de los numeros es: ",numero)
elif operador == 6:
    numero **= float(input("Introduce el segundo numero: "))
    print("El exponente de los numeros es: ",numero)
elif operador == 7:
    numero %= float(input("Introduce el segundo numero: "))
    print("El resto de los numeros es: ",numero)
else:
    print("Ese numero no es una opcion, vuelva a intentarlo")
