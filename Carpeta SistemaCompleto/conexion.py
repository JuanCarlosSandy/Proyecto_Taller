from os import system
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
        system("cls")
        print('='*5,"MENU",'='*5)
        for documento in self.coleccion.find():
            print(str(documento["idComida"])+" "+documento["nombreComida"])
        print("="*40)
        input("ENTER PA CONTINUAR")

    def crearRegistroComida(self,idComida,nombreComida):
        documento = {"idComida":idComida,"nombreComida":nombreComida}
        self.coleccion.insert_one(documento)

    def actualizarComida(self,idComida,nombreComida):
        self.coleccion.update_one({"idComida":idComida},{"$set":{"nombreComida":nombreComida}})

    def eliminarComida(self, idComida):
        self.coleccion.delete_many({"idComida":idComida})

class Login:
    def __init__(self) -> None:
        MONGO_HOST="localhost"
        MONGO_PUERTO="27017"
        MONG_TIEMPO_FUERA=1000

        MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

        MONGO_BD="Restaurante"
        MONGO_COLECCION="Usuario"
        self.cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONG_TIEMPO_FUERA)
        self.baseDatos=self.cliente[MONGO_BD]
        self.coleccion=self.baseDatos[MONGO_COLECCION]

    def crearUsuario(self,usuario,contraseña):
        documento = {"Usuario":usuario,"Contraseña":contraseña}
        self.coleccion.insert_one(documento)

    def verificarUsuario(self, usuario, contraseña):
        self.coleccion.find_one({"Usuario":usuario,"Contraseña":contraseña})

class Orden:
    def __init__(self) -> None:
        MONGO_HOST="localhost"
        MONGO_PUERTO="27017"
        MONG_TIEMPO_FUERA=1000

        MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

        MONGO_BD="Restaurante"
        MONGO_COLECCION="Pedidos"
        self.cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONG_TIEMPO_FUERA)
        self.baseDatos=self.cliente[MONGO_BD]
        self.coleccion=self.baseDatos[MONGO_COLECCION]

    def crearPedido(self,idPedido, nombreCliente, Comida, Nota, dondeConsume):
        documento = {"idPedido":idPedido,"nombreCliente":nombreCliente,"Comida":Comida,"Nota":Nota,"dondeConsume":dondeConsume}
        self.coleccion.insert_one(documento)

    def mostrarPedido(self):
        system("cls")
        contador = 1
        for documento in self.coleccion.find():
            print("="*4,"PEDIDO #",contador,"="*4)
            print("idPedido: "+str(documento["idPedido"])+"\nNombre del cliente: "+documento["nombreCliente"]+"\nComida: "+documento["Comida"]+"\nNota: "+documento["Nota"]+"\nLlevar o Mesa: "+documento["dondeConsume"])
            contador += 1
            print("="*40)
        input("ENTER PA CONTINUAR")

    def actualizarPedido(self,idPedido,nombreComida, nota, dondeConsume):
        self.coleccion.update_one({"idPedido":idPedido},{"$set":{"Comida":nombreComida,"Nota":nota,"dondeConsume":dondeConsume}})

    def eliminarPedido(self, idPedido):
        self.coleccion.delete_many({"idPedido":idPedido})
