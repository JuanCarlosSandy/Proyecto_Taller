from Comida import *
from conexion import *

class Restaurant:
    def __init__(self) -> None:
        self.listacomida = []
        self.food = RegistroComida()

    def resigistroComida(self):
        idComida = input("id: ")
        nombreComida = input("Nombre del plato: ")
        plato = Comida(idComida, nombreComida)
        self.listacomida.append(plato)

    def enviarDatosComida(self):
        for i in self.listacomida:
            id = i.getidComida()
            nombre = i.getnombreComida()
            self.food.crearRegistroComida(id, nombre)
        self.listacomida.clear()

    def abrirRestauran(self):
        estado = True
        while estado == True:
            opc = self.menuAdminPLato()
            if opc == 1:
                self.resigistroComida()
                self.enviarDatosComida()
            elif opc == 0:
                estado = False

restaurant = Restaurant()
restaurant.abrirRestauran()