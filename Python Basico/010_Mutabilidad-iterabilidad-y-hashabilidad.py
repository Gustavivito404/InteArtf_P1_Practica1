'''
Este codigo ase referencia a la leccion 13 de mutabilidad, iterabilidad y hashabilidad
en python
'''

# --- mutabilidad ---

# lista mutable
nums = [1,2,3]
print(nums)
nums[0] = 99
print(nums)

# tupla inmutable
t = (1,2,3)
print(t)
# t[0] = 99  # error: no se puede cambiar

# string inmutable
saludo = "hola"
print(saludo)
# s[0] = "H"  # error: no se puede cambiar
print(saludo.upper())

# --- iterabilidad ---

for n in nums:
    print(n)

for c in saludo:
    print(c)

# nota: todos los tipos de coleccion son iterables (listas, tuplas, strings, dict, set, etc)

# --- hashabilidad ---

# para ver si un objeto es hashable, se puede usar la funcion hash()
# solo se puede usar hash() en objetos inmutables como tuplas, strings, numeros, etc
# si se intenta usar hash() en un objeto mutable, dara un error
punto = (10,20)
print(hash(punto))

# nota: int, float, str, bool, y tuplas de hashables si son hashables
# nota: list, dict y set no son hashables
# nota: solo los hashables se pueden usar como clave en un dict o como elemento en un set
