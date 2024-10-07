class Persona:
    def __init__(self, nombre, edad):
        self._nombre= nombre
        self._edad= edad
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, newAge):
        self._edad= newAge
        return self._edad

Ema= Persona("Ema",10)
nombre= Ema.get_nombre()
print(nombre)

edad= Ema.get_edad()
print(edad)

newEdad = Ema.set_edad(20)
print(newEdad)