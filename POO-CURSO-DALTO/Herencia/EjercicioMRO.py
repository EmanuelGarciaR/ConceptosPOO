"""
Ejercicio de herencia multiple y MRO:
Imagina que estás modelando animales en un zoológico. Crear tres clases: "Animal, "Mamifero" y "Ave"
La clase “Animal” debe tener un método llamado "comer". La clase "Mamifero” debe tener
un método llamado "amamantar" y la clase “Ave” un método llamado "volar".
Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto —
debe ser capaz de "amamantar y “volar”, además de “comer”.

Finalmente, juega con el orden de la herencia de la clase "Murcielago" y observa
como cambia el MRO y el comportamiento de los metodos al usar super().
"""

class Animal:
    def comer(self):
        print("Está Comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("Está amamantando")

class Ave(Animal):
    def volar(self):
        print("Está volando")

class Murcielago(Mamifero, Ave):
    pass

murcielagoA = Murcielago()
murcielagoA.comer()
murcielagoA.amamantar()
murcielagoA.volar()