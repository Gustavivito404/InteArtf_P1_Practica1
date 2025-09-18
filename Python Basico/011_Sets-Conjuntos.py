'''
Este codigo ase referencia a la leccion 14 de conjuntos (sets) en python
un set es una coleccion sin orden y sin elementos repetidos
se escribe con llaves {}
'''

# set basico
colores = {"rojo","verde","azul"}
print(colores)

# un set no tiene orden
# cada vez que lo imprimimos puede salir en orden diferente

# no acepta elementos repetidos
colores2 = {"rojo","verde","azul","rojo","azul"}
print(colores2)

# agregar elementos
colores.add("amarillo")
print(colores)

# eliminar con remove
colores.remove("rojo")
print(colores)

# eliminar elementos con discard (no da error si no existe el elemento)
colores.discard("rojo")  # no da error
print(colores)

# como mencionamos, tambien se puede usar remove (da error si no existe el elemento)
# colores.remove("rosa")  # error si el elemento no esta

# el uso de len() funciona igual que con listas y tuplas
print(len(colores))
# esta funcion tambien sirve con listas, tuplas y cadenas

# vaciar set
colores.clear()
print(colores)

# crear set vacio (nota: {} crea un dict, no un set)
vacio = set()
print(vacio)

# operaciones de conjuntos
a = {1,2,3,4}
b = {3,4,5,6}
print(a.union(b))       # union de a y b
print(a.intersection(b))# interseccion de a y b
print(a.difference(b))  # diferencia a - b
print(b.difference(a))  # diferencia b - a
print(a.symmetric_difference(b)) # elementos que no se repiten en ambos

#La funcion max() y min() tambien funcionan con sets
print(max(a)) # maximo elemento
print(min(a)) # minimo elemento

# en el caso de strings funciona con el orden lexicografico

#tambien existen los fronzensets (sets inmutables)
fs = frozenset([1,2,3,4])
# si intentas modificarlo dara error
# fs.add(5)  # error
print(fs)

# nota: los sets son mutables (se pueden modificar)
# nota: solo se pueden guardar elementos hashables (int, str, tuple hashable)
