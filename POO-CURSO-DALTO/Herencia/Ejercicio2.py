#Ejercicio de Herencia y uso de Super()
"""Crear sistema para una escuela. En este sistema, vamos a tener 2 clases Principales:
Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y un metodo 
que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona
y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def imprimirNombre(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")

class Estudiante (Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def imprimirGrado(self):
        print(f"Estoy en el grado {self.grado}")

    def presentacion(self):
        super().imprimirNombre()
        self.imprimirGrado()

jaimito= Estudiante("Jaimito", 10, 6)
jaimito.presentacion()

print(f"""==ATRIBUTOS===\n {jaimito.nombre}\n {jaimito.edad}\n {jaimito.grado}""")
