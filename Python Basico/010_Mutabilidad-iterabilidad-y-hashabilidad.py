'''
Este codigo ase referencia a la leccion de mutabilidad, iterabilidad y hashabilidad
en python. Aqui veremos que tipos de datos se pueden cambiar, cuales se pueden recorrer
y cuales se pueden usar como claves (por que son hashables). Todo con ejemplos simples.
'''

# --- mutabilidad ---
# mutable = se puede cambiar despues de crear
# inmutable = no se puede cambiar (si quieres otro valor, creas otro objeto)

# lista (mutable)
nums = [1,2,3]
print(nums)
nums[0] = 99  # cambiamos el primer valor
print(nums)

# tupla (inmutable)
t = (1,2,3)
print(t)
# t[0] = 99  # esto da error por que la tupla no se puede modificar

# string (inmutable)
s = "hola"
print(s)
# s[0] = "H"  # error, los string no se pueden modificar por indice
s2 = s.upper()  # creamos otro string basado en s
print(s2)

# set (mutable) -> conjuntos sin orden y sin repetidos
colores = {"rojo","verde","azul"}
print(colores)
colores.add("amarillo")
print(colores)
colores.discard("verde")
print(colores)

# dict (mutable) -> pares clave:valor
alumno = {"nombre":"gus","edad":20}
print(alumno)
alumno["edad"] = 21  # cambiamos valor
alumno["grupo"] = "6a"  # agregamos nueva clave
print(alumno)

# --- iterabilidad ---
# iterable = se puede recorrer con for (lista, tupla, string, dict, set, range)

for n in nums:
    print(n)

for c in s:
    print(c)

for k in alumno:
    print(k, alumno[k])

# tambien podemos usar iter() y next() manualmente
it = iter((10,20,30))  # un iterador sobre una tupla
print(next(it))
print(next(it))
print(next(it))
# next(it)  # si llamas otra vez sin elementos -> StopIteration

# --- hashabilidad ---
# hashable = se puede usar como clave en un dict o elemento en un set
# regla practica: inmutable y con __hash__ definido -> hashable
# (int, float, str, tuple de elementos hashables) son hashables
# (list, dict, set) no son hashables

# usar tupla como clave si sus elementos tambien son hashables
punto = (10, 20)
memo = {}
memo[punto] = "coordenada guardada"
print(memo)

# intentar usar lista como clave da error (descomenta para probar)
# lista_clave = [10, 20]
# memo[lista_clave] = "no se puede"  # TypeError: unhashable type: 'list'

# cuidado: una tupla es hashable solo si todos sus elementos lo son
ok = (1, "a", True)  # todo hashable
print(hash(ok))

no_ok = (1, [2,3])  # la lista interna no es hashable
# print(hash(no_ok))  # TypeError si intentas hashear

# ejemplo rapido con set: solo acepta elementos hashables
conjunto = set()
conjunto.add(1)
conjunto.add("x")
conjunto.add((2,3))  # tupla ok
print(conjunto)
# conjunto.add([2,3])  # error: la lista no es hashable

# resumen rapido (no exacto para todos los casos, pero ayuda):
# mutables: list, dict, set
# inmutables: int, float, bool, str, tuple
# iterables: casi todos los de coleccion (list, tuple, dict, set, str, range)
# hashables: int, float, bool, str, tuple(de hashables)
