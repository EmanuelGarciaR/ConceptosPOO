class Gato:
    def sonido(self):
        return "miaw"

class Perro:
    def sonido(self):
        return "guau"

def hacer_sonido(animal):
    print(animal.sonido())

perro= Perro()
gato= Gato()
hacer_sonido(gato) #---> Polimorfismo de función. Cambia el argumento
print(perro.sonido())#-> Cambiamos la instancia (objeto) creado