'''
Ejemplos de los metodos center(), ljust() y rjust():
    1- pedimos al usuario que introduzca una palabra
    2- aplicamos el metodo center(), ljust() y rjust() para centrar, alinear a la izquierda y alinear a la derecha la palabra introducida
'''

palabra = "Hola"
print(f"La palabra introducida centrada               : {palabra.center(10, "-")}")
print(f"La palabra introducida alineada a la izquierda: {palabra.ljust(10, "_")}")
print(f"La palabra introducida alineada a la derecha  : {palabra.rjust(10, "=")}")

'''
Ejemplos de count():
    1- definimos una frase
    2- aplicamos el metodo count() para contar cuantas veces aparece la letra 'o' en la frase
'''
print("\nEjemplos de count():")
frase = "Hola, Buenos dias a todos"
print(frase)
print(f"La letra 'o' aparece {frase.count('o')} veces")

'''
 Ejemplos de startswith() y endswith():
    1- definimos una frase
    2- aplicamos el metodo startswith() y endswith() para verificar si la frase comienza o termina con la palabra 'Hola'
'''

print("\nEjemplos de startswith() y endswith():")
print(frase)
print(f"Buscando si la frase empieza por Hola: {frase.startswith("Hola")}")
print(f"Buscando si la frase termina pot todo: {frase.endswith("todo")}")

'''
Ejemplo find():
    1- definimos una frase
    2- aplicamos el metodo find() para buscar la posicion de la palabra 'Buenos' en la frase
'''

print("\nEjemplo de find():")
print(frase)
print(f"La palabra 'Buenos' empieza en la posicion {frase.find('Buenos')}")





