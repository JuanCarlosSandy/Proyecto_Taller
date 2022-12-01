from os import system
import pymongo
from pymongo import MongoClient
from CarpetaClases.Comida import *

class RegistroComida:
    def __init__(self) -> None:

        MONGO_HOST="localhost"#SE CONECTA A LA RUTA DE LOCALHOST
        MONGO_PUERTO="27017"
        MONG_TIEMPO_FUERA=1000

        MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

        MONGO_BD="Restaurante"#creamos la base de datos
        MONGO_COLECCION="Menu"
        self.cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONG_TIEMPO_FUERA)#con esto podemos realizar las operaciones que necesitamos
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
    def verificarUsuario(self):
        print('='*5,"INICIO DE SESION",'='*5)
        validador=False
        usuario=input("Ingrese su nombre de usuario:")
        contraseña=input("Ingrese su contraseña:")
        for documento in self.coleccion.find():
            usuarioRegistrado=(documento["Usuario"])
            contraseñaRegistrado=(documento["Contraseña"])
        #print(usuarioRegistrado,contraseñaRegistrado)
        #input(">>ENTER")
            if (usuarioRegistrado==usuario) and (contraseñaRegistrado==contraseña):
                validador=True
                return validador
        if (usuarioRegistrado==usuario) and (contraseñaRegistrado==contraseña):
                validador=True
                return validador
        print("DATOS INCORRECTOS")
        input("ENTER PARA VOLVER A INICIO")
    def mostrarUsuario(self):
        print('='*5,"USUARIOS",'='*5)
        contador=1
        for documento in self.coleccion.find():
            print("usuario:"+str(contador))
            contador =contador+1
            print(str(documento["Contraseña"])+" "+documento["Usuario"])
        print("="*40)
        input("ENTER PA CONTINUAR")
    def eliminarUsuario(self):
        usuario1=input("Ingrese el usuario:")
        contraseña1=input("Ingrese la contraseña:")
        dirreccion={"Contraseña":contraseña1,"Usuario":usuario1}
        x=self.coleccion.delete_many(dirreccion)
        print(x.deleted_count,"Usuario eliminado")
        print("="*20)
        input("ENTER PARA CONTINUAR")        
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
            print("PEDIDO #",contador)
            print("idPedido: "+str(documento["idPedido"])+"\nNombre del cliente: "+documento["nombreCliente"]+"\nComida: "+documento["Comida"]+"\nPedido personalizado: "+documento["Nota"]+"\nLlevar o Mesa: "+documento["dondeConsume"])
            print("="*40)
            contador += 1

    def actualizarPedido(self,idPedido,nombreComida, nota, dondeConsume):
        self.coleccion.update_one({"idPedido":idPedido},{"$set":{"Comida":nombreComida,"Nota":nota,"dondeConsume":dondeConsume}})

    def eliminarPedido(self, idPedido):
        self.coleccion.delete_many({"idPedido":idPedido})
