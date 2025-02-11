'''
Ejemplos de condicionales en Python
    1- pedir al usuario su nombre y tres notas
    2- calculamos el promedio de las notas
    3- si el promedio es mayor o igual a 8, felicitamos al usuario
    4- si el promedio es mayor o igual a 5, le decimos que está bien
    5- si el promedio es menor a 5, le decimos que está mal
'''

print("Calculo de media: ")

nombre = str(input("¿Como se llama? "))

print("Hola ",nombre)
nota1 = int(input(" ¿Cual es su nota de matematicas? "))
nota2 = int(input(" ¿Cual es su nota de biologia? "))
nota3 = int(input(" ¿Cual es su nota de educacion fisica? "))
promedio = float((nota1 + nota2 + nota3) / 3)

# Es importante indentar correctamente el código dentro de los condicionales (if, elif, else) para asegurar que las condiciones se evalúen
# y ejecuten correctamente. La indentación en Python define el bloque de código que pertenece a cada condición.
if promedio >= 8:
    print("Felicidades ",nombre, ", su media es de: ",promedio)
elif promedio >= 5:
    print("Muy bien ",nombre, "su media es de: ",promedio)
else:
    print("Muy mal ",nombre,", su media es de: ",promedio)

