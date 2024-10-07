class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, newName):
        self.__nombre = newName

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, newAge):
        self.__edad = newAge

Ema = Persona("Ema", 10)
nombre = Ema.nombre
edad = Ema.edad
print(nombre)  # Salida: Ema
print(edad)    # Salida: 10

Ema.nombre = "Pepito"
nombre = Ema.nombre
print(nombre)  # Salida: Pepito

Ema.edad = 2000
edad = Ema.edad
print(edad)# Salida: 2000

#Los setters no llevan return: Los setters solo deben asignar el valor, no devolverlo.