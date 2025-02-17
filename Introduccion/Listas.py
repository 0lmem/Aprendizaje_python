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
print(f"\nElementos de la lista: {lista_numerica}")
print(f"Primer elemento de la lista: {lista_numerica[0]}")
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

'''
Agregar elementos a una lista con el metodo append() e insert():
El metodo append() nos permite agregar un elemento al final de una lista.
El metodo insert() nos permite agregar un elemento en una posición específica de la lista.
'''
print("\nAgregar elementos a una lista con append():")
lista = ["Hola", "Mundo"]
print(f"\nLista original: {lista}")
lista.append("Python")
print(f"Lista con append: {lista}")

print("\nAgregar elementos a una lista con insert():")
lista = ["Hola", "Mundo"]
print(f"\nLista original: {lista}")
lista.insert(1, "Python")
print(f"Lista con insert: {lista}")

'''
Eliminar elementos de una lista con el metodo remove(), pop() y del:
El metodo pop() nos permite eliminar un elemento de una lista utilizando el índice del elemento.
El metodo remove() nos permite eliminar un elemento de una lista.
del nos permite eliminar un elemento de una lista utilizando el índice del elemento.
'''

print("\nEliminar elementos de una lista con pop(), remove() y del:")
lista = ["a", "b", "c", "d", "e"]
print(f"\nLista original: {lista}")
lista.pop(2)
print(f"Eliminamos el elemento en la posicion 2: {lista}")
lista.remove("b")
print(f"Eliminamos el elemento b: {lista}") 
lista.insert(1,"b")
lista.insert(2,"c")
print(f"Restauramos la lista: {lista}")
del lista[0:3]
print(f"Eliminamos los elementos de la posicion 0 a 3: {lista}")

'''
Invertir una lista con el metodo reverse():
El metodo reverse() nos permite invertir el orden de los elementos de una lista.
'''

print("\nInvertir una lista con reverse():")
lista = ["a", "b", "c", "d", "e"]
print(f"\nLista original: {lista}")
lista.reverse()
print(f"Lista invertida: {lista}")


'''
Ordenar una lista con el metodo sort():
El metodo sort() nos permite ordenar los elementos de una lista.
'''

print("\nOrdenar una lista con sort():")
lista = [4, 2, 1, 3, 5]
print(f"\nLista original: {lista}")
lista.sort()
print(f"Lista ordenada: {lista}")
lista.sort(reverse=True)
print(f"Lista ordenada de forma descendente: {lista}")

'''
Obtener la posición de un elemento con el metodo index():
El metodo index() nos permite obtener la posición de un elemento en una lista.
'''

print("\nObtener la posición de un elemento con index():")
lista = ["a", "b", "c", "d", "e"]
print(f"\nLista original: {lista}")
print(f"Posición del elemento 'c': {lista.index('c')}")
print(f"Posición del elemento 'e' a partir de la posición 3: {lista.index('e', 3)}")

'''
Concatenar listas con el metodo extend():
dado que las listas son mutables, podemos concatenar dos listas utilizando el metodo extend().
'''

print("\nConcatenar listas con extend():")
lista1 = ["a", "b", "c"]
lista2 = ["d", "e", "f"]
print(f"\nLista 1: {lista1}\nLista 2: {lista2}")
lista1.extend(lista2)
print(f"Lista concatenada: {lista1}")

'''
Sumar elementos de una lista con el metodo sum():
El metodo sum() nos permite sumar los elementos de una lista.
'''

print("\nSumar elementos de una lista con sum():")  
lista = [1, 2, 3, 4, 5]
print(f"\nLista original: {lista}")
suma = sum(lista)
print(f"Suma de los elementos de la lista: {suma}")
