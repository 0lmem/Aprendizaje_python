'''
Ejercicio 9. Eliminar de una lista los caracteres que se le indiquen.
La lista original es la siguiente: ["A","a","B","b","C","c","D","d","E","e"]
Deberás pedir al usuario que introduzca un caracter y eliminar de la lista original todas las ocurrencias de ese caracter.
'''
# Declaracion de variables
lista_original = ["A","a","B","b","C","c","D","d","E","e"]

# Imprimimos la lista original.
print(f"\nLista original: {lista_original}")
# Pedimos al usuario que introduzca el caracter que quiere eliminar de la lista.
charelim = input("Introduce el caracter que quieres eliminar de la lista: ")
# Eliminamos el caracter que el usuario introdujo. 
# el bucle while pasara por toda la lista elminando el caracter que el usuario introdujo.
while charelim in lista_original:
    lista_original.remove(charelim.lower())
    lista_original.remove(charelim.upper())

# Imprimimos la lista sin el caracter que el usuario introdujo.
print(f"Lista sin el caracter {charelim}: {lista_original}")