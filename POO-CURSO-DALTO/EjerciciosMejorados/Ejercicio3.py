from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def comer(self):
        pass
class Mamifero(ABC):
    @abstractclassmethod
    def amamantar(self):
        pass

class Ave(ABC):
    @abstractclassmethod
    def volar(self):
        pass
class Murcielago(Mamifero, Ave, Animal):
    def amamantar(self):
        print("Amamanta")
    def volar(self):
        print("Vuela")
    def comer(self):
        print("Comer")

murcielago=Murcielago()
murcielago.comer()
murcielago.volar()
murcielago.amamantar()

