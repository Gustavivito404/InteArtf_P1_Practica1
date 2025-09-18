"""
Con base a la leccion 8 veremos como se utilizxan las cadenas de texto
o strings en Python
"""
frace_1= 'Hola, usted esta etrando a una nueva aventura '
frace_2= 'en el mundo de Python'
frace_3= 'y esperamos que sea muy divertido'

frace_completa= frace_1 + frace_2 + ' ' + frace_3 # El operador + concatena cadenas de texto
print(frace_completa)
# Pero si queremos agregar espacios entre frases debemos hacerlo concatenando un espacio ' ' entre las frases como se hizo entre frace_2 y frace_3
# O podemos agregar el espacio en la frace original, como se hizo en frace_1

# Para agregar comillas en una frace podemos usar \ antes de las comillas
print('El dijo: \'Hola, como estas?\'')

# O podemos utilizar diferentes comillas para encerrar la frace
print("El dijo: 'Hola, como estas?'")

# Otra forma de trabajar con strings es utilizando la sintaxis de f-strings
nombre= input('Cual es tu nombre? ')
print(f'Hola {nombre}, bienvenido a la aventura de Python!') # La f puede ser mayuscula y se puede usar cualquiera de las comillar
# En este estilo de trabajo podemos insertar variables dentro de las llaves {} y esto nos veneficia ya que no necesariamente tienen 
# que ser strings, pueden ser numeros o cualquier otro tipo de dato
edad= int(input('Cual es tu edad? '))
print(f'Hola {nombre}, bienvenido a la aventura de Python! Veo que tienes {edad} años, eso es genial!')
# Esto nos puede evitar errores al momento de concatenar diferentes tipos de datos
# Por ejemplo, si intentamos concatenar un string con un numero sin convertirlo a string

# En python contamos con utilidades ya que las string son un tipo de dato derivado de un objeto
# por lo que podemos usar metodos para trabajar con ellos
print(frace_completa.upper()) # Convierte toda la frace a mayusculas
print(frace_completa.lower()) # Convierte toda la frace a minusculas
print(frace_completa.capitalize()) # Convierte la primera letra de la frace a mayuscula