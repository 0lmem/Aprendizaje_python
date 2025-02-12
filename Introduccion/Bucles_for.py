'''
 Ejemplo de bucle for:
    1- Se define una variable llamada frase con el valor "Hola Mundo"
    2- Se recorre la frase letra por letra
    3- Se imprime cada letra
'''
#El bucle for recorre la cadena letra por letra.
#En cada iteración, la variable letra toma el valor del carácter actual de la cadena y se imprime.
print("Ejemplo de for: ")
frase = "Hola Mundo"

for letra in frase:
    print(letra)

'''
Ejemplo de bucle for con range:
    1- Se define un bucle for con la funcion range
    2- Se imprime el valor de i
    3- La funcion range tiene la siguiente sintaxis:
        range(inicio, fin, paso)
        inicio: valor inicial
        fin: valor final
        paso: incremento
'''
print("Ejemplo de for con range: ")
for i in range(1, 10, 2):
    print(i)
