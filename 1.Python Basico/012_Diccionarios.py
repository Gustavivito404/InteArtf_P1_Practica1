'''
Este codigo ase referencia a la leccion 15 de diccionarios en python
un diccionario es una coleccion de pares clave:valor
se escribe con llaves {}
'''

# diccionario basico
alumno = {"nombre":"gus","edad":20,"grupo":"6a"}
print(alumno)

# acceder a valores por la clave
print(alumno["nombre"])
print(alumno["edad"])

# modificar un valor
alumno["edad"] = 21
print(alumno)

# agregar nueva clave
alumno["materia"] = "python"
print(alumno)

# eliminar clave con del
del alumno["grupo"]
print(alumno)

# tambien se puede usar pop
alumno.pop("materia")
print(alumno)

# recorrer diccionario
for clave in alumno:
    print(clave, alumno[clave])

# metodos utiles
print(alumno.keys())   # devuelve las claves
print(alumno.values()) # devuelve los valores
print(alumno.items())  # devuelve pares clave:valor

# tambien se puede borrar un diccionario entero con del o con clear()
del alumno
# si hago print(alumno) da error porque ya no existe

# y del es una palabra reservada de python
# incluso se puede utilisar en listas, tuplas y sets

# diccionario vacio
vacio = {}
print(vacio)

# nota: las claves deben ser hashables (str, int, tuple hashable)
# nota: los diccionarios son mutables (se pueden cambiar)
