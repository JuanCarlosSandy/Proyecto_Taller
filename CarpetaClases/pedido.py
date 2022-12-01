class Pedido():
    def __init__(self,idPedido, nombre, comida, cambios, dondeconsume) -> None:
        self.idPedido = idPedido
        self.nombre = nombre
        self.comida = comida
        self.cambios = cambios
        self.dondeconsume = dondeconsume

    def getIdPedido(self):
        return self.idPedido

    def getNombre(self):
        return self.nombre

    def getComida(self):
        return self.comida

    def getCambio(self):
        return self.cambios

    def getDondeconsume(self):
        return self.dondeconsume

    def __str__(self) -> str:
        return 'Id: '+str(self.idPedido)+'\nNombre: '+self.nombre+'\nComida: '+'\nPersonalizar pedido: '+self.cambios+'\nDonde Consume: '+self.dondeconsume