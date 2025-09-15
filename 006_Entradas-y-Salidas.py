'''
En este punto de la leccion 7 nos muestran como leer 
y escribir datos en la consola usando las funciones input() 
y print().
'''

# Entrada de datos
# La funcion input() permite leer datos desde la consola
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
# Nota: La funcion input() siempre devuelve un string

# Salida de datos
print("Hola", nombre, "tienes", edad, "años.")

# pero que pasa si queremos hacer operaciones con la edad
# Si intentamos sumar 10 a la edad, obtendremos un error

#edad_mas_diez = edad + 10
#print("En 10 años tendras:", edad_mas_diez) 
# Esto generara un error

# El error ocurre porque estamos intentando sumar un string (edad) con un entero (10)
# Para solucionar esto, necesitamos convertir la edad a un entero usando int()

# Convertir tipos de datos
# Si necesitamos que la edad sea un numero entero, podemos convertirla usando int()
edad = int(edad)
edad_mas_diez = edad + 10 
# Tambien podemos convertir a float() si necesitamos un numero decimal
print("En 10 años tendras:", edad_mas_diez)

# pero si intentamos sumar dos numeros string lo que hace es una concatenacion y el
# comando input() siempre devuelve un string
numero1 = input("Ingrese un numero: ")
numero2 = input("Ingrese otro numero: ")
suma = numero1 + numero2
print("La suma es (Sin convertir):", suma)

# Para solucionar esto, necesitamos convertir los numeros a enteros usando int()
numero1 = int(numero1)
numero2 = int(numero2)
suma = numero1 + numero2
print("La suma es: (Convirtiendo)", suma)

# De la misma forma que lo hicimos con la edad para poder manipularla como un numero