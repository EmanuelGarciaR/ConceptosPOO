#Métodos que se utilizan cuando ocurre determinada cosa
class Persona():
    def __init__(self, nombre, edad): #__init__ es un método especial
        self.nombre= nombre
        self.edad= edad

    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'

    def __add__(self, otro):
        nuevo_valor= self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)

ema= Persona("Ema", 17)
shawn= Persona("Shawn", 23)
nueva_persona = ema + shawn

print(nueva_persona.nombre)