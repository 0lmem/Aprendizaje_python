'''
Ejercicio 6. Crear una tabla de multiplicar de un número ingresado por el usuario.
    1- Pedir al usuario que ingrese un número.
    2- imprimir la tabla de multiplicar de ese número.
    3- Preguntar al usuario si desea ver otra tabla de multiplicar.
    4- Si el usuario responde que sí, repetir los pasos 1 al 3.
    5- Si el usuario responde que no, terminar el programa.
'''
# declaramos las variables de control de los bucles
bucle = True
bucle_anidado = True
# bucle principal que se encarga de repetir el proceso de la tabla de multiplicar
while(bucle):   
    bucle_anidado = True
    numero = input("Ingrese un número: ")
# condicional que se encarga de validar si el valor ingresado es un número
    if numero.isnumeric() == False:
        print("El valor ingresado no es un número, vuelva a intentarlo")
        continue
# bucle que se encarga de imprimir la tabla de multiplicar del número ingresado
    for i in range(1,11):
        print(f"{numero} x {i} = {int(numero)*i}")
# bucle anidado que se encarga de preguntar al usuario si desea ver otra tabla de multiplicar
    while(bucle_anidado):
        respuesta = input("Desea ver otra tabla de multiplicar? (si/no): ")
        # condicionales que se encargan de validar la respuesta del usuario
        if respuesta == "si":
            bucle_anidado = False
        elif respuesta == "no":
            bucle = False
            bucle_anidado = False
        else:
            print("La respuesta no coincide, vuelva a intentarlo")

print("Fin del programa")
