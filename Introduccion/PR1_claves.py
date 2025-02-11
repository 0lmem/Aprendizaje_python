'''
Ejercicio 1:
    1- Pedir al usuario su nombre y la clave de empleado
    2- Pedir al usuario cuantos años lleva trabajando
    3- Crear una condicion para saber cuantos dias de vacaciones tiene el usuario
    4- Si la clave es 111 y lleva 1 año trabajando, tiene 6 dias de vacaciones
    5- Si la clave es 111 y lleva entre 2 y 6 años trabajando, tiene 14 dias de vacaciones
    6- Si la clave es 111 y lleva mas de 7 años trabajando, tiene 20 dias de vacaciones
    7- Si la clave es 222 y lleva 1 año trabajando, tiene 7 dias de vacaciones
    8- Si la clave es 222 y lleva entre 2 y 6 años trabajando, tiene 15 dias de vacaciones
    9- Si la clave es 222 y lleva mas de 7 años trabajando, tiene 22 dias de vacaciones
    10- Si la clave es 333 y lleva 1 año trabajando, tiene 10 dias de vacaciones
    11- Si la clave es 333 y lleva entre 2 y 6 años trabajando, tiene 20 dias de vacaciones
    12- Si la clave es 333 y lleva mas de 7 años trabajando, tiene 30 dias de vacaciones
'''
print("Dias de vacaciones disponibles \n")

nombre = str(input("Ingrese su nombre: "))
clave = int(input("Ingrese la clave de empleado: "))
años_trabajados = int(input("Ingrese cuantos años lleva trabajando: "))

if clave == 111:
    if años_trabajados == 1:
        print("Hola ",nombre,", Tiene 6 dias de vacaciones.")
    elif años_trabajados >= 2 or años_trabajados <= 6:
        print("Hola ",nombre,", Tiene 14 dias de vacaciones.")
    elif años_trabajados >= 7:
        print("Hola ",nombre,", Tiene 20 dias de vacaciones.")
    else:  
        print("Hola ",nombre,", No tiene vacaciones.")
elif clave == 222:
    if años_trabajados == 1:
        print("Hola ",nombre,", Tiene 7 dias de vacaciones.")
    elif años_trabajados >= 2 or años_trabajados <= 6:
        print("Hola ",nombre,", Tiene 15 dias de vacaciones.")
    elif años_trabajados >= 7:
        print("Hola ",nombre,", Tiene 22 dias de vacaciones.")
    else:  
        print("Hola ",nombre,", No tiene vacaciones.")
elif clave == 111:
    if años_trabajados == 1:
        print("Hola ",nombre,", Tiene 10 dias de vacaciones.")
    elif años_trabajados >= 2 or años_trabajados <= 6:
        print("Hola ",nombre,", Tiene 20 dias de vacaciones.")
    elif años_trabajados >= 7:
        print("Hola ",nombre,", Tiene 30 dias de vacaciones.")
    else:  
        print("Hola ",nombre,", No tiene vacaciones.")
else:
    print("La clave no existe.")