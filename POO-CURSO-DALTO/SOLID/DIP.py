"""
Módulos de alto nivel no deben depender de los de bajo nivel.
Ambos tienen que depender de las abstracciones

-No tenemos que depender de implementaciones especificas
"""
from abc import ABC, abstractclassmethod
class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        #Lógica para verificar palabra
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Lógica para verificar palabra si está en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificado = verificador

    def corregir_texto(self, texto):
        #usamor el verificador para corregir texto
        pass