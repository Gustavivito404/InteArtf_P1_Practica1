'''
Este codigo ase referencia a la leccion de expresiones de logica booleana en python
las expresiones booleanas devuelven True o False
'''

# operadores logicos basicos: and, or, not

a = True
b = False

print(a and b)  # solo es True si ambos son True
print(a or b)   # es True si al menos uno es True
print(not a)    # not invierte el valor

# comparaciones logicas
x = 10
y = 5

print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x == 10)
print(x != y)

# se pueden combinar comparaciones con operadores logicos
print(x > 5 and y < 10)
print(x < 5 or y == 5)
print(not(x < y))

# nota: == es igualdad, = es asignacion
# nota: != es diferente
# nota: las expresiones booleanas son muy usadas en condicionales (if)
