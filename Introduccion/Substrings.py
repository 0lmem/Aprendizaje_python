'''
Ejemplo de como obtener todos los substrings de una cadena
    1- declaramos una variable de tipo string
    2- declaramos una variable de tipo string para almacenar los substrings
    3- Obtenemos los substrings de la cadena de diferentes formas
'''

Cadena = "Hola mundo, adios mundo"
substrings = ""

#obetenemos los substrings de la cadena
substrings = Cadena[2]
print (f"subcadena con indice en la posicion [2]: {substrings}")

substrings = Cadena[5:10]
print (f"subcadena con indice en la posicion [5:10]: {substrings}")

substrings = Cadena[-5]
print (f"subcadena con indice en la posicion [-5]: {substrings}")

substrings = Cadena[1:3:9]
print (f"subcadena con indice en la posicion y salto [1:3:9]: {substrings}")

substrings = Cadena[::3]
print (f"subcadena con indice en la posicion y salto [::2]: {substrings}")