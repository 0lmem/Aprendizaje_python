'''
Ejemplo de los metodos title() e istitle()
    1- pedimos al usuario que introduzca su nombre y apellido
    2- concatenamos el nombre y apellido en una sola variable
    3- aplicamos el metodo title() para que la primera letra de cada palabra sea mayuscula
    4- aplicamos el metodo istitle() para comprobar si la primera letra de cada palabra es mayuscula
    5- aplicamos el metodo title() de forma permanente
'''
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")

#f-string sirve para concatenar variables con texto en una sola linea
nombre_completo = (f"{nombre} {apellido}")
print(f"Su nombre completo sin ningun metodo es: {nombre_completo}")

#Metodo title() convierte la primera letra de cada palabra en mayuscula
print(f"Su nombre completo con el metodo title() es: {nombre_completo.title()}")

#Metodo istitle() devuelve True si la primera letra de cada palabra es mayuscula
print(f"El metodo istitle() devuelve: {nombre_completo.istitle()}")

#aplicamos el metodo title() de forma permanente
nombre_completo = nombre_completo.title()
print(f"Su nombre completo es: {nombre_completo}")
print(f"El metodo istitle() devuelve: {nombre_completo.istitle()}\n")

'''
Ejemplo de los metodos upper() e isupper() y lower() e islower()
    1- pedimos al usuario que introduzca una palabra
    2- aplicamos el metodo isupper() para comprobar si la palabra introducida es mayuscula o islower() para comprobar si la palabra introducida es minuscula
    3- aplicamos el metodo upper() para convertir la palabra en mayusculas o lower() para convertir la palabra en minusculas
'''
palabra = input("Introduce una palabra: ")
print(f"El metodo isupper() devuelve: {palabra.isupper()}")
print(f"La palabra introducida con el metodo upper() es: {palabra.upper()}")
print(f"El metodo islower() devuelve: {palabra.islower()}")
print(f"La palabra introducida con el metodo lower() es: {palabra.lower()}")

'''
Ejemplo de los metodos swapcase() y capitalize()
    1- pedimos al usuario que introduzca una palabra
    2- aplicamos el metodo swapcase() para convertir las mayusculas en minusculas y viceversa
    3- aplicamos el metodo capitalize() para convertir la primera letra de la palabra en mayuscula y el resto en minusculas
'''

palabra = input("\nIntroduce una palabra: ")
print(f"La palabra introducida con el metodo swapcase() es: {palabra.swapcase()}")
print(f"La palabra introducida con el metodo capitalize() es: {palabra.capitalize()}")