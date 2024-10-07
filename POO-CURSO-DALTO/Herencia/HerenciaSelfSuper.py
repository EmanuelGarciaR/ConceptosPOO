class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre= nombre
        self.edad= edad
        self.nacionalidad= nacionalidad
        
    def saludar(self):
        print(f"Hola buenas, mi nombre es: {self.nombre} y estas desde la clase PERSONA")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad


class ArtistaPersona(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario= salario
        self.empresa= empresa

    def saludar(self):
        print(f"Hola trabajo en {self.empresa} y estas en la clase ARTISTAPERSONA")

    def presentarme(self):
        # return self.saludar() #Self cuando se llama dentro de la misma clase
        return super().saludar() #Cuando llamamos desde la clase Padre

ejemplo= ArtistaPersona("Ema", 17, "colombiano", "Dibujar", "80000000", "Glovant")
ejemplo.presentarme()