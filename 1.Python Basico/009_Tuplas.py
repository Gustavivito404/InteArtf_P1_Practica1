'''
Este codigo hace referencia a la leccion 12 de tuplas
una tupla es una coleccion ordenada e inmutable
se escribe entre parentesis () y se puede acceder a sus valores por indices
no se pueden modificar despues de crearlas pero si se pueden leer sus valores
'''

# tupla basica
colores = ("rojo","verde","azul")
print(colores)

# tupla con diferentes tipos de datos
mi_tupla = ("gus",6,True,3.14)
print(mi_tupla)

# tupla de un solo elemento (tiene que llevar coma al final)
una_sola = ("unico",)
print(una_sola)
print(type(una_sola))

# acceder a elementos por indices
print(colores[0])
print(colores[2])
print(colores[-1])

# slicing (cortes de la tupla)
print(colores[0:2])
print(colores[1:])
print(colores[:2])

# inmutabilidad de las tuplas
#colores[0] = "amarillo"  # esto da error porque no se puede cambiar

# metodos de lectura
repetidos = ("rojo","verde","rojo","amarillo","rojo")
print(repetidos.count("rojo"))
print(repetidos.index("verde"))

# si buscamos un valor que no existe con index dara error
# print(repetidos.index("morado"))

# operaciones utiles
print(len(colores))
print("verde" in colores)
print("negro" in colores)

# convertir lista a tupla y al reves
lista_temporal = list(colores)
lista_temporal.append("amarillo")
tupla_nueva = tuple(lista_temporal)
print(tupla_nueva)

# desempaquetado de tuplas
numeros = (10,20,30,40)
a,b,c,d = numeros
print(a,b,c,d)

# desempaquetado con *
x,y,*resto = numeros
print(x,y,resto)

primero,*centro,ultimo = (1,2,3,4,5,6)
print(primero,centro,ultimo)

# cuando usar tuplas
# - cuando no queremos que los datos cambien
# - para representar coordenadas o valores fijos
# - se pueden usar como claves en diccionarios

# diferencia entre tupla y lista
# tupla es inmutable, se escribe con ()
# lista es mutable, se escribe con []
