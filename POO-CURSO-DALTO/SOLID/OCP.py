#Agregar nuevas funcionalidades sin tener que cambiar el código fuente de la clase o de las entidades
class Notificador:
    def __init__(self, mensaje, usuario):
        self.mensaje= mensaje
        self.usuario= usuario
    def notificar (self):
        raise NotImplementedError #cualquier clase que herede de Notificador debe proporcionar su propia implementación del método notificar.
#No modificamos esta clase

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Mensaje en Email {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Mensaje en SMS {self.usuario.sms}")