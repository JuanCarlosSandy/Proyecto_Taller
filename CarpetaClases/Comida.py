class Comida:
    def __init__(self, idComida, nombreComida):
        self.idComida = idComida
        self.nombreComida = nombreComida

    def getidComida(self):
        return self.idComida

    def getnombreComida(self):
        return self.nombreComida

    def setidComida(self, idComida):
        self.idComida = idComida

    def setnombreComida(self, nombreComida):
        self.nombreComida = nombreComida

    def __str__(self) -> str:
        return 'id Comida: '+str(self.idComida)+'\nNombre del Plato: '+self.nombreComida