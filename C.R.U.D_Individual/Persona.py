class Persona:
    def __init__(self,nombre="",edad=0,genero=0,codigo=0,telefono=0):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.codigo=codigo
        self.telefono=telefono
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getGenero(self):
        return self.genero
    def getCodigo(self):
        return self.codigo
    def getTelefono(self):
        return self.telefono



    def setNombre(self,nombre):
        self.nombre=nombre

    def setEdad(self,edad):
        self.edad=edad
    def setGenero(self,genero):
        self.genero=genero  
    def setCodigo(self,codigo):
        self.codigo=codigo
    def setTelefono(self,telefono):
        self.telefono=telefono
    def __str__(self):
        return "\nNombre: "+self.nombre+"\nEdad: "+str(self.edad)+"\nGenero: "+self.genero+"\nCodigo:"+str(self.codigo)+"\nTelefono:"+str(self.telefono)