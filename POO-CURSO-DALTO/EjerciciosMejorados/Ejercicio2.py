from abc import ABC, abstractclassmethod
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def saludo(self):
        return f"Me llamo {self.nombre} y mi edad es {self.edad}"
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def grado(self):
        super().saludo()
        print(f"Estoy en el grado {self.grado}")

ema= Estudiante("Ema", 17, 11)
print(ema.grado)