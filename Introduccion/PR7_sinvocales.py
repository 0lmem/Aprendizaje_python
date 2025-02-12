'''
Ejericio 7. Programa que pide una cadena de texto y elimina las vocales de la cadena.
    1- Pedir una cadena de texto.
    2- Eliminar las vocales de la cadena.
    3- Mostrar la cadena sin vocales.
'''

# Pedimos una cadena de texto
cadena = input("Introduce una cadena de texto: ")
cadena_min = cadena.lower()

# Recorremos la cadena y eliminamos las vocales
for caracter in cadena_min:
    if caracter == "a":
        continue
    elif caracter == "e":
        continue
    elif caracter == "i":
        continue
    elif caracter == "o":
        continue
    elif caracter == "u":
        continue
    else:
        print(caracter, end="")