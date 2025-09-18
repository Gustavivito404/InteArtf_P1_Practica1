'''
Este codigo hase referencia a la leccion 16 de conversiones de tipos en python
la conversion de tipos se usa para cambiar un dato de un tipo a otro
'''

# convertir string a entero
num_str = "10"
num_int = int(num_str)
print(num_int)

# convertir string a float
num_str2 = "3.14"
num_float = float(num_str2)
print(num_float)

# convertir numero a string
edad = 20
edad_str = str(edad)
print(edad_str)

# convertir numero a bool
cero = 0
uno = 1
print(bool(cero))
print(bool(uno))

# convertir lista a tupla
lista = [1,2,3]
tupla = tuple(lista)
print(tupla)

# convertir tupla a lista
tupla2 = (4,5,6)
lista2 = list(tupla2)
print(lista2)

# convertir set a lista
colores = {"rojo","verde","azul"}
lista_colores = list(colores)
print(lista_colores)

# convertir lista a set
lista_colores2 = ["rojo","verde","rojo"]
set_colores = set(lista_colores2)
print(set_colores)

# existen tipos de conversiones como la implicita y la explicita
# la implicita la hace python automaticamente
numero_1 = 10
numero_2 = 20.5
print(numero_1 + numero_2) # el 10 se convierte a 10.0 automaticamente
# en este caso el resultado es float porque uno de los operandos es float
# si ambos operandos fueran int, el resultado seria int
# la explicita es la que hacemos nosotros con las funciones vistas como los ejemplos de arriba

# ¿Cómo saber el tipo de dato en Python?
print(type(num_int))
print(type(num_float))
# etc.


# cuidado con convertir strings que no sean numeros a int o float -> da error
# bool convierte 0, "", [], {} a False y todo lo demas a True

# ahora, un ejemplo practico que nos permite solucionar un problema que llegamos a ver antes
# el input() siempre devuelve un string
edad_input = input("Ingrese su edad: ") # si ingreso 20, edad_input es "20" (string)
print(type(edad_input))
# si quiero sumar 1 a la edad, no puedo hacer edad_input + 1 porque son tipos diferentes
# debo convertir edad_input a int
edad_int = int(edad_input)
nueva_edad = edad_int + 1
print("El año que viene tendras:", nueva_edad)

# incluso con matematicas mas complejas
numero_1 = float(input("Ingrese un numero: ")) # se realiza la conversion a float directamente
numero_2 = float(input("Ingrese otro numero: ")) # se realiza la conversion a float directamente
resultado = numero_1 + numero_2 # suma de floats
print("La suma es:", resultado)