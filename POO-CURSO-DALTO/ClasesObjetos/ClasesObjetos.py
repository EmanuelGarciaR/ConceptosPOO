class Autos:
    def __init__(self, marca, modelo, velocidad, costo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.costo = costo

#Metodos
    def mostrarVelocidad(self):
        print(f'La velocidad del {self.marca} {self.modelo} es: {self.velocidad}')

auto1 = Autos("Porshe", "Spyder 911", "300km/h", 300000)
# print(auto1.costo)
auto1.mostrarVelocidad()