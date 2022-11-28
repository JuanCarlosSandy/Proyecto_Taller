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
    
    def crearRegistroComida(self,idComida,nombreComida):
        documento = {"idComida":idComida,"nombreComida":nombreComida}
        self.coleccion.insert_one(documento)