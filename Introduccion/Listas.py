'''
Ejemplo de listas en Python:
Las listas son un tipo de dato que nos permite almacenar varios valores en una sola variable.
Las listas se crean utilizando corchetes [] y separando los elementos con comas.
y el primer elemento de la lista tiene el índice 0.
'''
print("Lista de números:")
lista_numerica = [1, 2, 3, 4, 5]
print(lista_numerica)

print("\nLista de strings:")
lista_strings = ["Hola", "Mundo", "Python"]
print(lista_strings)

'''
Acceder a los elementos de una lista:
Para acceder a los elementos de una lista se utiliza el índice del elemento.
'''
print("\nAcceder a elementos de una lista:")
lista_numerica = [1, 2, 3, 4, 5]
print(f"\nPrimer elemento de la lista: {lista_numerica[0]}")
print(f"Muestra varios elementos de la lista: {lista_numerica[:3]}")
print(f"Último elemento de la lista: {lista_numerica[-1]}")
print(f"Muestra todos los elementos de la lista: {lista_numerica[:]}")

'''
Cambiar elementos de una lista:
Para cambiar el valor de un elemento de una lista se utiliza el índice del elemento.
'''

print("\nCambiar elementos de una lista:")
lista = ["a","e","i","o","u"]
print(f"Lista original: {lista}")
lista[0] = "A"
print(f"Cambiamos la primera letra: {lista}")
lista[1:3] = ["E", "I"]
print(f"Modificamos de la posicion 1 a 3: {lista}")
lista[:5] = ["a", "e", "I", "O"]
print(f"Modificamos de la posicion 0 a 5: {lista}")

