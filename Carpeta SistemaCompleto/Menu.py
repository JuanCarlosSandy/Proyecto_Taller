from Comida import *
from conexion import *

class Menu:
    def __init__(self) -> None:
        self.listacomida = []
        self.food = RegistroComida()

    def resigistroComida(self):
        self.food.mostrarMenu()
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
        print("="*20)
        print("PLATO REGISTRADO")
        print("="*20)
        input("ENTER PARA CONTINUAR")

    def actualizarComida(self):
        self.food.mostrarMenu()
        id = input("id del plato: ")
        newnombre = input("Nuevo Nombre del Plato: ")
        self.food.actualizarComida(id, newnombre)
        print("="*20)
        print("PLATO ACTUALIZADO")
        print("="*20)
        input("ENTER PARA CONTINUAR")

    def eliminarComida(self):
        self.food.mostrarMenu()
        id = input("Id de la comida que desea eliminar: ")
        self.food.eliminarComida(id)
        print("="*20)
        print("PLATO ELIMINADO")
        print("="*20)
        input("ENTER PARA CONTINUAR")
