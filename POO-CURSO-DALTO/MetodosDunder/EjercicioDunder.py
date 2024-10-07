"""
Crear un juego de Fusión

El juego consiste en crear personajes en un juego y que esos personajes se puedan fusionar
para formar personajes más poderosos que tengan más poder

Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes
se fusiones, salga un nuevo personaje con habilidades mejoradas.

Una posible fórmula es: el promedioo de las habildiades de ambos al cuadrado!
"""
class Personaje():
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre= nombre
        self.fuerza= fuerza
        self.velocidad= velocidad
    
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro):
        promedioHabilidadesFuerza= ((self.fuerza + otro.fuerza)/2)**2
        promedioHabilidadesVelocidad= ((self.velocidad + otro.velocidad)/2)**2
        return Personaje(self.nombre + otro.nombre, promedioHabilidadesFuerza, promedioHabilidadesVelocidad)

goku= Personaje("Goku", 100, 100)
veggeta= Personaje("Veggeta", 99, 99)
gogetta= goku + veggeta
print(gogetta)

jiren= Personaje( "Jiren", 130, 140)
jireta= jiren + gogetta
print(jireta)