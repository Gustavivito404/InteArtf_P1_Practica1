'''
Convase a la leccion 6 de matematicas basicas
Veamos como se realizan diferentes operaciones matematicas en python
'''
# Nota inicial: Cualquiera de las operaciones que realices sobre un print(), las podrás guardar de la misma forma en una variable.
a=10
b=6
print("Valores iniciales: a =",a,", b =",b)

# Suma
# La suma funciona solo de 2 operandos en 2, por lo que 
# inicia sumando 3 + 2 = 5 y luego 5 + 1 = 6
operacion_suma = a + b
print("Resultado suma:",operacion_suma)

# Resta
operacion_resta = a - b
print("Resultado resta:",operacion_resta)

# Multiplicacion
# La multiplicación funciona de la misma manera que la suma y la resta.
operacion_multiplicacion = a * b
print("Resultado multiplicacion:",operacion_multiplicacion)

# Division
# La división funciona de la misma manera que las otras operaciones.
operacion_division = a / b
print("Resultado division:",operacion_division)
# Nota: La division siempre devuelve un numero decimal flotanmte, aunque el resultado sea un numero entero.

# Operaciones multiples y misxtas
# En este caso, python sigue la jerarquia de operaciones matematicas
operacion_compleja = a + b * a - b / a
print("Resultado operacion compleja (a + b * a - b / a):",operacion_compleja)

# Operar con nombres de variables
# En este caso, se resta el resultado de la multiplicacion menos el resultado de la division
operacion_con_variables = operacion_multiplicacion - operacion_division
print("Resultado operacion con variables (multiplicacion - division):",operacion_con_variables)

# Operador modulo
# El operador modulo devuelve el resto de una division entre 2 numeros
# o lo que seria el residuo de una division
operacion_modulo = a % b
print("Resultado operacion modulo:",operacion_modulo)
# Nota: Siempre regresa enteros y si uno de los datos es flotante
# el resultado sera un flotante
operacion_modulo_flotante = a % b
print("Resultado operacion modulo flotante:",operacion_modulo_flotante)

# Operador division entera
operacion_division_entera = a // b
print("Resultado operacion division entera:",operacion_division_entera)
# El operador de division entera devuelve el cociente de una division

# Operador potencia
operacion_potencia = a ** b
print("Resultado operacion potencia (a elevado a b):",operacion_potencia)
# El operador de potencia devuelve el resultado de elevar un numero a otro

# Calculos con parentesis
operacion_parentesis = (a + b) * (a - b) / a
print("Resultado operacion con parentesis ( (a + b) * (a - b) / a ):",operacion_parentesis)

# Numeros largos
# Python soporta numeros largos de manera nativa, sin necesidad de librerias adicionales
numero_largo = 123456789012345678901234567890
print("Numeros largos:",numero_largo)

# Guiones bajos en numeros largos
# Python permite el uso de guiones bajos en numeros largos para mejorar la legibilidad
numero_largo_con_guiones = 123_456_789_012_345_678_901_234_567_890
print("Numeros largos y guiones:",numero_largo_con_guiones)
# Esto tambien incluye el uso de numeros decimales
numero_decimal_con_guiones = 123_456.789_012_345
print("Numeros decimales y guiones:",numero_decimal_con_guiones)
