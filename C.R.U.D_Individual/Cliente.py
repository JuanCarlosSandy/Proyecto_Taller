from Persona import *
class Cliente(Persona):
    def __init__(self, nombre="", edad=0, genero=0, codigo=0, telefono=0,correo=""):
        super().__init__(nombre, edad, genero, codigo, telefono)
        self.correo=correo
    
    def getCorreo(self):
        return self.correo
    def setCorreo(self,correo):
        self.correo=correo
    
    def __str__(self):
        return super().__str__()+"\nCorreo: "+self.correo