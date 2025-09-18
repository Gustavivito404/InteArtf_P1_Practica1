'''
Este codigo ase referencia a la leccion 18 de condicionales y bucles en python (version extendida)
los condicionales ejecutan codigo si se cumple una condicion
los bucles repiten codigo varias veces
'''

# ---------------- condicionales ----------------
# if
x = 10
if x > 5:
    print("x > 5")
# if-else
y = 3
if y > 5:
    print("y > 5")
else:
    print("y no > 5")
# if-elif-else
edad = 18
if edad < 18:
    print("menor")
elif edad == 18:
    print("tienes 18")
else:
    print("mayor")

# operadores de comparacion: ==, !=, >, <, >=, <=
a = 7
b = 7
print(a == b)
print(a != b)
print(a >= b)

# operadores logicos: and, or, not
nota = 85
conducta = True
if nota >= 80 and conducta:
    print("pasa")

# valores true y false
# false comunes: 0, 0.0, "", [], {}, set(), None
vacio = ""
if not vacio:
    print("cadena vacia")

# nested if (if dentro de if)
temp = 30
lluvia = False
if temp > 25:
    if not lluvia:
        print("salir")

# ---------------- bucle while ----------------

contador = 0
while contador < 5:
    print("c:", contador)
    contador += 1

# while con break y continue
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # salta pares
    if n > 7:
        break     # corta al pasar 7
    print("impar:", n)

# ---------------- bucle for ----------------

frutas = ["manzana","pera","uva"]
for f in frutas:
    print(f)

# for sobre string
txt = "hola"
for ch in txt:
    print(ch)

# for con range: range(inicio, fin, paso)
for i in range(1, 10, 3):
    print(i)

# enumerate para tener indice y valor
for i, fruta in enumerate(frutas):
    print(i, fruta)

# recorrer diccionario
alumno = {"nombre":"gus","edad":20}
for k in alumno:
    print(k, alumno[k])

# tambien values() e items()
for v in alumno.values():
    print(v)
for k, v in alumno.items():
    print(k, v)

# notas:
# - if evalua expresiones booleanas
# - while repite mientras la condicion sea True
# - for recorre elementos de un iterable (lista, tupla, string, dict, range, etc)
# - break corta el bucle, continue salta a la siguiente iteracion
