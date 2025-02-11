# Comentar una linea

'''
Este es un comentario de varias
lineas
'''
    
# Declaracion de las variables en python 
#Tambien existen numeros complejos que se declaran con la palabra complex
valor1 = int(3) 
decimal1 = float(5.6)
texto = str("Hola mundo")
Verdadero = bool(True)
num_complejo = complex(5)

# Print se utiliza para imprimir texto por pantalla
print(valor1, type(valor1))
print(decimal1, type(decimal1))
print(texto, type(texto))
print(Verdadero, type(Verdadero))
print(num_complejo, type(num_complejo))
print()

'''
Input sirve para pedirle datos al usuario
ejemplo = int(input("Texto que se va a mostrar"))
'''

# El += se utiliza para añadirle algun dato extra a la varible en este caso se utiliza para añadir un espacio y un nombre
mensaje = "Hola"
mensaje += " "
mensaje += "Alvaro"

print(mensaje,"\n") # \n hace un salto de linea

# Las variables en python son dinamicas y pueden cambiar 
print("concatenación:" )
mensaje = "Buenos"
espacio = " "
mensaje2 = "dias"

print(mensaje+espacio+mensaje2)

# Para buscar un dato en una cadena dentro de una variable para esto se utiliza el find
mensaje = "Buenas tardes"
buscar = mensaje.find("tardes")
print(buscar)

#Extraer una porcion de el mismo segun las posiciones que pongas dentro de los corchetes "[]"
mensaje = "Hola mundo"
extraer = mensaje[3:7]
print(extraer)    
