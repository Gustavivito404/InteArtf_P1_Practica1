'''
En el codigo existen reglas en los lenguajes y tambien existen
convenciones que se deben seguir para nombrar las variables.
Las diferencias serian que las reglas son necesarias para que
la sintaxis del lenguaje sea correcta y las convenciones son
recomendaciones para que el codigo sea mas legible y entendible.
o lo que serian buenas practicas.

'''
#Ejemplos de nombres de variables válidos en Python:
numero_1 = 10  # Es recomendable usar guion bajo en el nombre de la variable
numero = 20 
numeroUno = 30

#Ejemplos de nombres de variables inválidos en Python (Reglas):
# 1numero ->Los nombres de variables en Python, no pueden empezar por un valor numérico. A partir del segundo carácter del nombre, puedes poner los que quieras, pero el primero, debe ser sí o sí, un guion bajo o una letra.
# $resultado -> Los nombres de variables en Python, no pueden empezar por un símbolo de dólar.
# nombre-usuario -> Los nombres de variables en Python, no pueden contener guiones.
# _n0c3e -> Los nombres de variables en Python, no pueden empezar por un guion bajo seguido de un número.
# a1_b2_c3 -> Los nombres de variables en Python, no pueden contener números en la primera posición.

#Recomendacion de nombres de variables (Convenciones):
# 1. Usa nombres descriptivos: El nombre de la variable debe describir claramente su propósito o contenido.
#Un ejemplo de como no hacerlo seria
fecha = "Hola"
nombre = 7
a = 10034.5657
#Un ejemplo de como hacerlo seria
saludo = "Hola"
numero = 7
numero_preciso = 7.5657

# 2. Usa minúsculas y guiones bajos: En Python, la convención es usar minúsculas y guiones bajos para separar palabras en nombres de variables.
#Un ejemplo de como hacerlo seria
nombre_usuario = "Juan"
fecha_nacimiento = "01/01/2000"
# Este estilo es conocido como "snake_case".

# 3. Hacer uso de mayusculas para constantes: Las constantes son variables cuyo valor no cambia a lo largo del programa. Por convención, se escriben en mayúsculas y se separan las palabras con guiones bajos.
#Un ejemplo de como hacerlo seria
PI = 3.14159
GRAVEDAD = 9.81

# 4. Evita usar palabras reservadas: No uses palabras reservadas del lenguaje como nombres de variables.

# 5. Evutar acentos y caracteres especiales: Es recomendable evitar el uso de acentos y caracteres especiales en los nombres de variables para asegurar la compatibilidad y legibilidad del código.