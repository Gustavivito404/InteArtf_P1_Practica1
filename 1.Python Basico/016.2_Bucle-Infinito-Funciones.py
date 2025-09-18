'''
Este codigo muestra un ejemplo de bucle infinito (secuencia infinita)
con menu y funciones
'''
import os

amigos = ['Jasso','Eduardo','Mercado','Yavhe']

# ---------- funciones ----------

def mostrar_menu():
    os.system('cls')  # limpia la consola (en linux seria "clear")
    print("Menu:")
    print("1. Quieres saber quienes son mis amigos?")
    print("2. Quieres saber cuantos amigos tengo?")
    print("3. Que opino de Jasso?")
    print("4. Agregar un nuevo amigo")
    print("5. Eliminar un amigo")
    print("6. Salir")

def opcion1():
    amigo = input("Ingresa el nombre de alguno de mis amigos -> ")
    if amigo in amigos:
        print(f"{amigo} es uno de mis amigos")
    else:
        print(f"{amigo} no es uno de mis amigos")
    input("\t\nPresiona Enter para continuar...")

def opcion2():
    cantidad = len(amigos)
    print(f"Tengo {cantidad} amigos")
    print("Mis amigos son:")
    for amigo in amigos:
        print(f"\t- {amigo}")
    input("\t\nPresiona Enter para continuar...")

def opcion3():
    if 'Jasso' in amigos:
        print("Jasso es un gran amigo, siempre esta ahi para ayudar")
    else:
        print("No conozco a Jasso")
    input("\t\nPresiona Enter para continuar...")

def opcion4():
    new_amigo = input("Ingresa el nombre de un nuevo amigo -> ")
    amigos.append(new_amigo)
    print(f"{new_amigo} ha sido agregado a la lista de amigos")
    input("\t\nPresiona Enter para continuar...")

def opcion5():
    del_amigo = input("Ingresa el nombre del amigo que quieres eliminar -> ")
    if del_amigo in amigos:
        amigos.remove(del_amigo)  # remove elimina de lista
        print(f"{del_amigo} ha sido eliminado de la lista de amigos")
    else:
        print(f"{del_amigo} no se encuentra en la lista de amigos")
    input("\t\nPresiona Enter para continuar...")

# ---------- programa principal ----------

while True:
    mostrar_menu()
    opcion = input("Ingresa el numero relacionado con la opcion del menu -> ")

    match opcion:
        case "1":
            opcion1()
        case "2":
            opcion2()
        case "3":
            opcion3()
        case "4":
            opcion4()
        case "5":
            opcion5()
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida")
            input("\t\nPresiona Enter para continuar...")
