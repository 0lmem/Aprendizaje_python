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