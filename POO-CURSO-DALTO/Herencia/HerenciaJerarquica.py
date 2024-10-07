class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def llamado (self):
        print(f"Hola {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, grado):
        super().__init__(nombre, edad, nacionalidad)
        self.grado = grado

class Jefe(Persona):
    def __init__(self, nombre, edad, nacionalidad, cargo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.cargo= cargo
        self.salario= salario
    def llamado(self):
        print(f"Eres el jefe {self.nombre}")

Ema = Jefe("Emanuel", 17, "colombiano", "Arquitecto de Software", 15000000)
Ema.llamado()
print(Ema.salario)