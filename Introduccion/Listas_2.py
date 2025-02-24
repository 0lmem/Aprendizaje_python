'''
El constructor list() se utiliza para convertir objetos iterables a listas
'''

# Introducir todos los datos del range dentro de una lista
lista = list(range(0, 100, 10))
print(lista)

print("Metemos un nombre dentro de una lista")
nombre = "Marcos Lopez"
lista_nombre = list(nombre)
print(nombre,"\n",lista_nombre)

'''
Ejemplo de lista anidadas

'''
print("Lista anidadas: ")
lista_anidada = [ [1, 2, 3 ],[4, 5, 6, [7, 8, 9 ] ], 10]
print(lista_anidada)
print(lista_anidada[1][3][1])

'''
Matrice
'''