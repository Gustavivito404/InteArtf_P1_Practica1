"""
En este codigo mas que nada es una prueba de como usar input y trabajar con 
un tipo de cadena de texto mas larga.con f-strings.
y tomare este espacio para explicar sobre la Leccion 9 y los valores literales de cadena
de varias lineas.
"""
nombre= input('Cual es tu nombre? ')
edad= int(input('Cual es tu edad? '))
print("\n")
print(f'Hola {nombre.capitalize()} mucho gusto, veo que tienes {edad} años. Espero que te guste este cuento chiquito. \n\nHabia una vez un programador llamado {nombre.capitalize()}, que tenia {edad} años. \nUn dia, decidió aprender Python y se embarcó en una aventura emocionante. \nA medida que avanzaba en su aprendizaje, descubrió el poder de la programación y cómo podía crear cosas increíbles\ncon solo unas pocas líneas de código.\nAl final de su viaje, {nombre.capitalize()} se convirtió en un experto en Python y logro crear un programa que le \nayudaba a ver sus sueños en un entorno virtual, esto aun que parezca algo bueno fue muy malo\nya que dejo de distingir entre la realidad y la fantasia, solo vengo a recordarte {nombre.capitalize()} no pierdas\nde vista tus sueños y no te sientas vacio por lo que haces o lo que no haces, \naun puedes lograr todos tus sueños, aun tienes {edad} años bien vividos y los que faltan. :)\n\nFin.')

# Una cadena literal se trata de una cadena la cual sabemos el valor y podemos remplazar por otro 
# en el codigo sin problema. Pero una cadena no lineal es una cadena cuyo valor no podemos conocer, como 
# el nombre de una persona o su edad, ya que esto puede cambiar segun el input del usuario y el caso del 
# texto que se muestra para el imput es un texto no lineal ya que ese dato no lo podemos modificar y se quedara estatico las veces que se muestre
# ya que el dato que se guarda es el del usuario.