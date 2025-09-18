'''
Este codigo muestra un ejemplo de bucle infinito (secuencia infinita)
'''
import os

amigos = ['Jasso','Eduardo','Mercado','Yavhe']

while True:
    os.system('cls') # limpia la consola
    print("Menu:")
    print("1. Quieres saber quienes son mis amigos?")
    print("2. Quieres saber cuantos amigos tengo?")
    print("3. Que opino de Jasso?")
    print("4. Agregar un nuevo amigo")
    print("5. Eliminar un amigo")
    print("6. Salir")
    match input("Ingresa el numero relacionado con la opcion del menu -> "):
        case "1":
            amigo = input("Ingresa el nombre de alguno de mis amigos -> ")
            if amigo in amigos: # in recorre cada elemento de la lista y funciona como un booleano comparando si el elemento existe o no
                print(f"{amigo} es uno de mis amigos")
            else:
                print(f"{amigo} no es uno de mis amigos")
            input("\t\nPresiona Enter para continuar...")

        case "2":
            cantidad = len(amigos)
            print(f"Tengo {cantidad} amigos")
            print(f"Mis amigos son: ")
            for amigo in amigos: # in recorre cada elemento de la lista y funciona como un booleano
                print(f"\t- {amigo}")
            input("\t\nPresiona Enter para continuar...")

        case "3":
            if 'Jasso' in amigos:
                print("Jasso es un gran amigo, siempre esta ahi para ayudar")
            else:
                print("No conozco a Jasso")
            input("\t\nPresiona Enter para continuar...")

        case "4":
            new_amigo = input("Ingresa el nombre de un nuevo amigo -> ")
            amigos.append(new_amigo) # append agrega un elemento al final de la lista
            print(f"{new_amigo} ha sido agregado a la lista de amigos")
            input("\t\nPresiona Enter para continuar...")

        case "5":
            del_amigo = input("Ingresa el nombre del amigo que quieres eliminar -> ")
            if del_amigo in amigos:
                amigos.discard(del_amigo) # discard elimina un elemento de la lista y si no existe no da error
                print(f"{del_amigo} ha sido eliminado de la lista de amigos")
            else:
                print(f"{del_amigo} no se encuentra en la lista de amigos")
            input("\t\nPresiona Enter para continuar...")

        case "6":
            print("Saliendo del programa...")
            break

        case _:
            print("Opcion no valida")