'''
Ejericio 5. Invertir un string
    1- pedir un string por teclado
    2- Crear un bucle for que reciba un string y devuelva el string invertido.
'''

# Solicitamos una frase al usuario
frase = input("Introduce una frase: ")

# Recorremos la frase de forma inversa con la tecnica de slicing
for i in frase[::-1]:
    print(i, end="")
print("\nFin del programa")

# La tecnica slicing o rebanado consiste en indicar el inicio y fin de la cadena y el paso de la iteracion, 
# para este caso se indica -1 para que recorra la cadena de forma inversa

'''
Otra forma de hacerlo es:

string = input("Introduce una frase: ") # agregamos la palabra "Hola"
string_invertido = ""
for letra in string:
    string_invertido = letra + string_invertido #En la primera iteracion el string_invertido tendra la letra "H" 
                                                 en la segunda iteracion se agrega la letra "o" 
print(string_invertido)                          y asi hasta terminar de recorrer la palabra "Hola"

# Al final dentro de la variable string_invertido se almacenara la cadena "aloH"
# porque al sumar las letras se hac de esta manera "H" + "" = "H" luego "o" + "H" = "oH" y asi sucesivamente

En este ejemplo vamos agregando los caracteres de la cadena string a la variable string_invertido para que se
almacene de forma inversa gracias a que con el bucle for vamos pasando letra por letra y se va agregando a string-invertido
al reves y al final imprimimos la cadena invertida.

'''