class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre= nombre
        self.edad= edad
        self.nacionalidad= nacionalidad
        
    def saludar(self):
        print(f"Hola buenas, mi nombre es: {self.nombre}")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad


class ArtistaPersona(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario= salario
        self.empresa= empresa

    def pruebaSelf(self):
        print("Prueba del self")

    def presentarme(self):
        # print(f"{super().saludar()} y mi habilidad es: {self} lo siguiente será una prueba: {self.pruebaSelf()}")
        super().saludar()  # Llama a Persona.saludar()
        print(f"Y mi habilidad es: {self.habilidad}")  # Llama a la propiedad heredada que esta DENTRO de la clase. Por eso el self
        print(f"La empresa en la que trabajo es: {self.empresa}")
        self.pruebaSelf()

ejemplo= ArtistaPersona("Ema", 17, "colombiano", "Dibujar", "80000000", "Glovant")
ejemplo.presentarme()