'''
Ejemplo de break y continue
    el break se utiliza para salir de un bucle o terminar un bucle y el continue se utiliza para saltar 
    a la siguiente iteracion de un bucle

    Ejemplo del break:
    1- se crea un bucle while que imprime los numeros del 1 al 10
    2- utilizamos el break para salir del bucle cuando el numero sea igual a 5

    Ejemplo del continue:
    1- Creamos otro bucle while que imprime los numeros del 1 al 10
    2- utilizamos el continue para saltar a la siguiente iteracion cuando el numero sea igual a 5
'''   

print("Ejemplo de break:")
num = 0
while num < 10:
    num += 1
    if num == 5:
        break
    print(num, end=" ")

print("\nFin de programa")

print("Ejemplo de continue:")
num = 0
while num < 10:
    num += 1
    if num == 5: 
        continue
    print(num, end=" ")

print("\nFin de programa")
