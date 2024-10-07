"""
Si la clase B es una subclase de A
La clase A debería poder utilizarse eb todos los lugares
donde B pueda utilizarse
"""
# class Ave:
#     def volar (self):
#         return "Estoy volando"

# class Pinguino (Ave):
#     def volar(self):
#         return "No puedo volar"

# def hacer_volar(ave=Ave):
#     return ave.volar()
# print(hacer_volar(Pinguino())) #El pinguino no puede hacer lo que puede hacer Ave "volar"

class Ave: #ponemos parametros de las aves CLASE BASE
    pass
class AveVoladora(Ave): #Ponemos parametros de aves voladoras tambien SUBCLASE DE AVE
    def volar(self):
        return "Estoy volando"
class AveNoVoladora(Ave): #Ponemos parametros de aves no voladoras tambien   SUBCLASE DE AVE
    pass
#Hemos craedo una clase base y hemos subdividido sus características en otras clases.