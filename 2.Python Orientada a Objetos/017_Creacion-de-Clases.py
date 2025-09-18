"""
Este codigo va a contemplar la Leccion 1 y 2 de la seccion de Python Orientada a Objetos
"""
# Para la generacion de clases se hace uso de la palabra reservada class
class MiClase:
    pass # La palabra reservada pass se utiliza para indicar que no hay nada en la clase
# y pass nos permite generar una clase vacia sin que el interprete de Python genere un error

# Las clases cuentan con parametros que se denominan atributos
# y pueden hacer uso de funciones que se denominan metodos
# los metodos permiten definir ciertas instrucciones que pueden ser utilizadas por los objetos
# y pueden hacer uso de los atributos de la clase

# Nota: Por convencion los nombres de las clases se escriben en CamelCase
class Toalla:
    # Atributos
    color = "Azul" # Los atributos pueden tener un valor por defecto
    humedad = 20.78
    usos_consecutivos = 5

    # Metodos
    def secar(self): # Se hace uso de self para definir que es un metodo de la clase
        # y este puede acceder a los atributos de la clase
        if self.humedad > 5.8: # para acceder a los atributos de la clase se utiliza self
            # con un . y el nombre del atributo y este se puede utilisar en opercaciones logicas
            # o en bucles
            print("La toalla esta secando")
        else:
            print("La toalla esta seca")

    def doblar(self):
        print("La toalla esta siendo doblada")

toalla_1 = Toalla() # Instancia de la clase Toalla o tambien llamado objeto
print(f'Toalla 1 color: {toalla_1.color}') # Accedemos al atributo color del objeto toalla_1 para mostrarlo en consola
toalla_1.secar() # Accedemos al metodo secar del objeto toalla_1 para ejecutarlo
toalla_1.doblar() # Accedemos al metodo doblar del objeto toalla_1 para ejecutarlo
# Nota: Por convencion los nombres de los objetos se escriben en snake_case

# Tambien se pueden crear multiples objetos de la misma clase
toalla_2 = Toalla()
toalla_2.color = "Roja" # Podemos cambiar el valor del atributo color del objeto toalla_2
print(f'Toalla 2 color: {toalla_2.color}') # Mostramos en consola el valor del atributo color del objeto toalla_2
toalla_2.humedad = 3.5 # Cambiamos el valor del atributo humedad del objeto toalla_2
toalla_2.secar() # Ejecutamos el metodo secar del objeto toalla_2

# Los atributos cuentan con las mismas propiedades que las variables
# y los metodos cuentan con las mismas propiedades que las funciones
# por lo que pueden recibir parametros y retornar valores, y tambien 
# podemos tener tuplas, listas, diccionarios, etc como atributos