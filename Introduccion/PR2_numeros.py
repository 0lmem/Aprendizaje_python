'''
Ejercicio 2:
    1- Pedir al usuario 3 numeros
    2- Crear una condicion para saber cual de los 3 numeros es el mas grande
'''
print("Que numero es mas grande")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 > num2:
    if num1 > num3:
        print("El numero ",num1," es el numero mas grande")
elif num2 > num3:
        print("El numero ",num2," es el numero mas grande")
else:
        print("El numero ",num3," es el numero mas grande")
