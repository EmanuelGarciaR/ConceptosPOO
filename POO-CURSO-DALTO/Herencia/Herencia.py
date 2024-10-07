class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionaldad= nacionalidad

#Como un empleado es una persona, debemos heredar de la clase persona.
#Lo hacemos de la siguiente manera:
class Empleado(Persona):
    #El metodo pass hace que no haga nada, hace que cuando se ejecute, no salte error.
    pass
Shawn = Empleado("Shawn", 20, "canadiense")
print(Shawn.nacionaldad)