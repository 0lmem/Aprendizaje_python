'''
Ejemplos de las funciones len() y format()
    1- utilizamos la funcion len() para contar los caracteres de una cadena
    2- utilizamos la funcion format() para formatear una cadena 
'''

print("Hola tiene", len("Hola"), "caracteres")

longitud = len("Programacion")
print("Programacion tiene", longitud, "caracteres\n")

#Ejemplo de format()
#La función format() se utiliza para formatear una cadena.

#ejemplo 1
nombre = "Juan"
edad = 25
print("Hola, mi nombre es {} y tengo {} años".format(nombre, edad))

#ejemplo 2

print("\nHola, mi nombre es {0} y tengo {1} años".format(nombre, edad))

#ejemplo 3

print("\nHola, mi nombre es {nombre} y tengo {edad} años".format(nombre="Marcos", edad=30))