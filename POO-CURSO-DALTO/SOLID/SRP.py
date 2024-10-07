# class Auto():
#     def __init__(self):
#         self.posicion = 0
#         self.combustible= 100

#     def mover(self, distancia):
#         if self.combustible> distancia/2:
#             self.posicion += distancia
#             self.combustible -= distancia/2
#         else:
#             print("El combustible no es suficiente")

#     def agregar_combustible(self, cantidad):
#         self.combustible += cantidad

#     def obtener_combustible(self):
#         return self.combustible
# No resperta SRP porque la clase Auto se está encargando del movimiento del auto (mover) como tambien del combustible
# (agregar_combustible) y (obtener_combustible)

class Auto():
    def __init__(self, tanque):
        self.posicion = 0 #Atributo estático
        self.tanque= tanque #Atributo de instancia

    def mover(self, distancia):
        if self.tanque.obtener_combustible()>= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            return "Has movido el auto"
        else:
            return "El combustible no es suficiente"

    def obtener_posicion(self):
        return self.posicion

class TanqueDeCombustible():
    def __init__(self):
        self.combustible= 100

    def agregar_combustible(self, cantidad):
        self.combustible+= cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

tanque= TanqueDeCombustible()
autito= Auto(tanque)
print(autito.obtener_posicion())
print(autito.mover(30))
print(autito.obtener_posicion())

