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
