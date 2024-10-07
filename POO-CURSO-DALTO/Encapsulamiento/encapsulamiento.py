class MiClase: #Atributos protegidos
    def __init__(self):
        self._atributoProtegido = "Valor" #Se puede seguir accediendo, pero se usa para tener cuidado y manejar como privado

ejemplo= MiClase()
print(ejemplo._atributoProtegido) #Permite acceder, pero debemos tratarlo como si no lo fuera

class ClassPriv:
    def __init__(self):
        self.__atributoPrivado = "Privado"
    
    def __metodoPrivado(self): #Tambien se puede usar en metodos
        print("Uso de metodo privado")

priv= ClassPriv()
print(priv.__atributoPrivado)#No lo permite, ya que es privado

# Para acceder a estas propiedades y metodos, debemos hacer uso de los getters y setters