"""
Este codigo hace referencia a la Leccion 6 que trabaja con la herencia en 
clases
"""

class Persona:
    def __init__(self, estatura, peso, edad):
        self.estatura = estatura
        self.peso = peso
        self.edad = edad

    def caminar(self):
        print("Estoy caminando")

    def dormir(self):
        print("Estoy durmiendo")

    def calcular_IMC(self):
        imc = self.peso / (self.estatura ** 2)
        return imc

# Al declarar una nueva clase podemos hacer que herede de otra clase
# para ello se pone el nombre de la clase padre entre parentesis
class Estudiante(Persona):
    def __init__(self, carrera, semestre):
        self.carrera = carrera
        self.semestre = semestre

    def estudiar(self):
        print("Estoy estudiando")

    def warframe(self):
        print("Estoy jugando Warframe")

# Al declarar estudinte tomamos el constructor de Estudiante
estudiante1 = Estudiante("Ingenieria en Sistemas", 5)

# esto nos permite modificar los valores de peso, estatura y edad
# pero para poder modificar los atributos de la clase heredada desde el 
# contructor necesitamos otro elemento
estudiante1.peso = 70
estudiante1.estatura = 1.75
estudiante1.edad = 20

# tambien podemos acceder a los metodos de la clase heredada
estudiante1.caminar()
estudiante1.dormir()
estudiante1.warframe()
estudiante1.estudiar()
estudiante1.calcular_IMC()
print(estudiante1.calcular_IMC())
