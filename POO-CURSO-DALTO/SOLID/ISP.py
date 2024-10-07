"""
Ningún cliente tiene que ser forzado a depender de interfaces que no tuiliza. 
Elimina las dependencias que no vamos a utilizar
"""
#En este caso la interfaz es la abstract class
from abc import ABC, abstractclassmethod
class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass
class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass
class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("Humano come")
    def dormir(self):
        print("Humano duerme")
    def trabajar(self):
        print("Humano trabaja")

class Robot(Trabajador): #Un robot no duerme ni come
    def trabajar(self):
        print("Robot trabaja")

robot= Robot()
ema= Humano()
print(robot.trabajar())

#Pregunta: Por qué a pesar de que Robot hereda a Trabajador que es una clase abstracta. Solo se llama el método trabajar?
#No deberían llamarse todos los metodos que se heredan al ser abstractos?.
