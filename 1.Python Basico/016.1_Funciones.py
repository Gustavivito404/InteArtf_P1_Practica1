'''
Este codigo ase referencia a la leccion 19 de funciones en python
una funcion es un bloque de codigo que se puede reutilizar
se define con la palabra def
'''

# funcion sin parametros
def saludar():
    print("hola gus")

saludar()

# funcion con parametro
def saludar_persona(nombre):
    print("hola", nombre)

saludar_persona("juan")
saludar_persona("ana")

# funcion con return
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)

# funcion con valores por defecto
def presentar(nombre, edad=18):
    print("me llamo", nombre, "y tengo", edad)

presentar("pedro")
presentar("maria", 25)

# funcion con varios parametros
def mostrar_datos(nombre, edad, ciudad):
    print("soy", nombre, "tengo", edad, "y vivo en", ciudad)

mostrar_datos("gus", 20, "gdl")
mostrar_datos(ciudad="cdmx", nombre="luis", edad=30) # se pueden usar parametros nombrados
# aun cuando no los metas en orden si el parametro esta nombrado se acomoda correctamente

# nota: def crea la funcion
# nota: return devuelve un valor
# nota: se pueden usar valores por defecto en los parametros
# nota: las funciones ayudan a organizar y reutilizar codigo
