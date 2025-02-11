'''
Ejericio 4: 
Realiza un programa que pida al usuario una frase y una palabra, y que elimine la primera ocurrencia de esa palabra en la frase.
    1- pedimos al usuario que introduzca una frase
    2- pedimos al usuario que introduzca una palabra que quiera buscar en la frase
    3- imprime la frase sin la primera ocurrencia de la palabra introducida
'''
frase = input("Introduce una frase: ")
frase= frase.lower()
buscar = str(input("Introduce la palabra que quieres buscar: "))
buscar = buscar.lower()
posicion = frase.find(buscar)
frase = frase[0:posicion] + frase[posicion + len(buscar) : ] 
print(frase)