'''
Ejercicio 10. Hacer un programa que elimina el primer y ultimo numero de una lista
Y despues que imprima la lista con elementos borrados mas otra lista con los elementos que se han borrado 
'''

# Declaramos las lista que vamos a utilizar
lista = [1,2,3,4,5,6,7,8,9,10]
lista_borrador = []

# Imprimimos la lista original
print(f"Lista original: {lista}")

# Agregamos el primer y ultimo elemento de la lista a "lista_borrador"
lista_borrador.append(lista[0])
lista_borrador.append(lista[-1])

# Eliminamos los elementos de la lista original
lista.pop()
lista.pop(0)

#Imprimimos las dos listas 
print(f"Lista sin el primer ni ultimo numero: {lista}")
print(f"Lista de los numero borrados: {lista_borrador}")

