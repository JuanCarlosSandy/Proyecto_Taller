from CarpetaClases.Comida import *
from CarpetaBD.conexion import *

class Menu:
    def __init__(self) -> None:
        self.listacomida = []
        self.food = RegistroComida()
        self.usuario=Login()

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
        print(" ","="*26)
        print("『ᴘʟᴀᴛᴏ ʀᴇɢɪsᴛʀᴀᴅᴏ ᴄᴏɴ ᴇxɪᴛᴏ』√")
        print(" ","="*26)
        input("ENTER PARA CONTINUAR")

    def actualizarComida(self):
        id = input("id del plato: ")
        newnombre = input("Nuevo Nombre del Plato: ")
        self.food.actualizarComida(id, newnombre)
        print(" ","="*27)
        print("『ᴘʟᴀᴛᴏ ᴀᴄᴛᴜᴀʟɪᴢᴀᴅᴏ ᴄᴏɴ ᴇxɪᴛᴏ』√")
        print(" ","="*27)
        input("ENTER PARA CONTINUAR")

    def eliminarComida(self):
        id = input("Id de la comida que desea eliminar: ")
        self.food.eliminarComida(id)
        print(" ","="*27)
        print("『ᴘʟᴀᴛᴏ ᴇʟɪᴍɪɴᴀᴅᴏ ᴄᴏɴ ᴇxɪᴛᴏ』⚗_⚗")
        print(" ","="*27)
        input("ENTER PARA CONTINUAR")