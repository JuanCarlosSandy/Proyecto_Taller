import pymongo
from Comida import *

class RegistroComida:
    def __init__(self) -> None:

        MONGO_HOST="localhost"
        MONGO_PUERTO="27017"
        MONG_TIEMPO_FUERA=1000

        MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

        MONGO_BD="Restaurante"
        MONGO_COLECCION="Menu"
        self.cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONG_TIEMPO_FUERA)
        self.baseDatos=self.cliente[MONGO_BD]
        self.coleccion=self.baseDatos[MONGO_COLECCION]

    def mostrarMenu(self):
        for documento in self.coleccion.find():
            print(str(documento["idComida"])+" "+documento["nombreComida"])

    def crearRegistroComida(self,idComida,nombreComida):
        documento = {"idComida":idComida,"nombreComida":nombreComida}
        self.coleccion.insert_one(documento)

    def actualizarComida(self,idComida,nombreComida):
        self.coleccion.update_one({"idComida":idComida},{"$set":{"nombreComida":nombreComida}})

    def eliminarComida(self, idComida):
        self.coleccion.delete_many({"idComida":idComida})

class Menu:
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

    def actualizarComida(self):
        id = input("id del plato: ")
        newnombre = input("Nuevo Nombre del Plato: ")
        self.food.actualizarComida(id, newnombre)

    def eliminarComida(self):
        id = input("Id de la comida que desea eliminar: ")
        self.food.eliminarComida(id)

food = Menu()
food.resigistroComida()
food.enviarDatosComida()
verfood = RegistroComida()
verfood.mostrarMenu()
food.actualizarComida()
verfood.mostrarMenu()
food.eliminarComida()
verfood.mostrarMenu()