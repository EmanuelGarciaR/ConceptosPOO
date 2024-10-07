from abc import ABC, abstractclassmethod

class Persona(ABC): #Esto hace que sea una clase abstracta
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod  #Con este decorador creamos el metodo abstracto. En las siguientes classes que se hereden, DEBEN INCLUIRLO
    def hacer_actividad(self):
        pass
    
    def presentar(self): #Este método, todas las personas lo pueden realziar con normalidad, ya que no cambiará por su actividad
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

# Ema=Persona("Ema", 17, "Masculino", "Programacion") NO SE PUEDE, ya que las clases abstractas es la PLANTILLA PARA CLASES, NO INSTANCIAS
class Estudiante(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self): #Hacemos el método que pusimos abstracto
        super().presentar()
        print(f"Soy estudiante de: {self.actividad}")
ema= Estudiante("Ema", 17, "Masculino", "Programación")
ema.hacer_actividad()

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self): #Hacemos el método que pusimos abstracto
        super().presentar()
        print(f"Trabajo en {self.actividad}")

shawn= Trabajador("Shawn", 23, "Masculino", "Cantante")
shawn.hacer_actividad()

#hacer_actividad al ser abstracto, es un método obligatorio. Todas las clases deben llevar ese metodo
#Cuando aseguramos abstracción, estamos haciendo también polimorfismo.