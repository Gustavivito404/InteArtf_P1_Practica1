"""
Con base a la Leccion 3, 4 y 5 de la seccion de Python Orientada a Objetos
vamos a ver el uso de los constructores en las clases y el uso de self
"""

# Los constructores son metodos especiales que se ejecutan al momento de crear un objeto
# y se utilizan para inicializar los atributos del objeto en base a los parametros que se le pasan
# al momento de crear el objeto
# esto nos ahorra tener que asignar los valores de los atributos despues de crear el objeto

class Toalla:
    # Constructor
    def __init__(self, color, humedad, usos_consecutivos):
        # El metodo constructor siempre debe llamarse __init__ (por convencion)
        # y debe recibir al menos un parametro que es self
        # que hace referencia al objeto que se esta creando
        self.color = color # Asignamos el valor del parametro color al atributo color del objeto
        self.humedad = humedad # Asignamos el valor del parametro humedad al atributo humedad del objeto
        self.usos_consecutivos = usos_consecutivos # Asignamos el valor del parametro usos_consecutivos al atributo usos_consecutivos del objeto

    # Metodos
    def secar(self):
        if self.humedad > 5.8:
            print("La toalla esta secando")
        else:
            print("La toalla esta seca")

    def doblar(self):
        print("La toalla esta siendo doblada")

toalla_1 = Toalla("Azul", 20.78, 5) # Al crear el objeto toalla_1 le pasamos los valores de los atributos
print(f'Toalla 1 color: {toalla_1.color}') # Mostramos en consola el valor del atributo color del objeto toalla_1
toalla_1.secar() # Ejecutamos el metodo secar del objeto toalla_1

toalla_2 = Toalla(usos_consecutivos=2, color='Amarilla', humedad=3.5) # Tambien podemos pasar los parametros por nombre como en las funciones
print(f'Toalla 2 color: {toalla_2.color}') # Mostramos en consola el valor del atributo color del objeto toalla_2
toalla_2.secar() # Ejecutamos el metodo secar del objeto toalla_2

# Nota: El uso de self es obligatorio en los metodos de las clases
# y siempre debe ser el primer parametro de los metodos
# no puedesponer mas parametros en el constructor de los que necesites

# Pero a mi me da curiosidad y quiero intentar crear un objeto con 
# 2 constructores como la sobre definicion o no recuerdo como se llama

class Operacion:
    # En Python no se pueden tener dos constructores distintos como en C++ o Java (donde haces overloading de __init__ con diferentes parámetros).
    # En Python, solo puede existir un __init__ por clase.
    # Si defines otro, el último sobreescribe al anterior.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __init__(self, a, b, c): # Este constructor sobreescribe al anterior
        self.a = a
        self.b = b
        self.c = c

    def sumar(self):
        if self.c != 0:
            return self.a + self.b + self.c
        else:
            return self.a + self.b
        
# operacion_1 = Operacion(2, 3) # Esto va a generar un error porque el constructor con 2 parametros no existe
# print(f'Operacion 1 suma: {operacion_1.sumar()}')
# operacion_1.c = 4 
# print(f'Operacion 1 suma con c: {operacion_1.sumar()}')


operacion_2 = Operacion(2, 3, 4) # Esto si funciona porque el constructor con 3 parametros si existe
print(f'Operacion 2 suma: {operacion_2.sumar()}')

# una forma de esto es tomar el parametro como una tupla o lista y hacer que el constructor
# maneje la cantidad de parametros que se le pasen

class OperacionFlexible:
    f = 3 # Atributo de clase
    # A los atributos de fuera (tipo_usuario y publicidad), les doy un valor en la clase, 
    # este no cambia al crear el objeto. Es decir, yo le puedo dar al objeto un nid, un alias, 
    # un nombre y apellidos al instanciarlo, pero no puedo cambiar los valores de tipo_usuario y 
    # publicidad, al menos durante la creación del objeto.

    def __init__(self, *args): # El asterisco permite recibir una cantidad variable de argumentos
        if len(args) == 0:
            self.a = 0
            self.b = 0
            self.c = 0
        elif len(args) == 1:
            self.a = args[0]
            self.b = 0
            self.c = 0
        elif len(args) == 2:
            self.a = args[0]
            self.b = args[1]
            self.c = 0
        elif len(args) == 3:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]

    def sumar(self):
        return self.a + self.b + self.c + self.f
    
# Numeros para operar
numlist = [4, 60, 15]
numtup = (8, 10, 3)

operacion_flexible_1 = OperacionFlexible() # Sin parametros
print(f'Operacion Flexible 1 suma: {operacion_flexible_1.sumar()}')

operacion_flexible_2 = OperacionFlexible(5) # Con un parametro
print(f'Operacion Flexible 2 suma: {operacion_flexible_2.sumar()}')

operacion_flexible_3 = OperacionFlexible(5, 10) # Con dos parametros
print(f'Operacion Flexible 3 suma: {operacion_flexible_3.sumar()}')

operacion_flexible_4 = OperacionFlexible(5, 10, 15) # Con tres parametros
print(f'Operacion Flexible 4 suma: {operacion_flexible_4.sumar()}')

operacion_flexible_5 = OperacionFlexible(*numlist) # Con una lista desempaquetada
print(f'Operacion Flexible 5 suma: {operacion_flexible_5.sumar()}')

operacion_flexible_6 = OperacionFlexible(*numtup) # Con una tupla desempaquetada
print(f'Operacion Flexible 6 suma: {operacion_flexible_6.sumar()}')

# podemos agregar un atributo unicamente a un solo objeto
operacion_flexible_6.d = 100
print(f'Operacion Flexible 6 atributo d: {operacion_flexible_6.d}')

