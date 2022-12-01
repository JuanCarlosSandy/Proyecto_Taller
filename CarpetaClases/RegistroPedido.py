from CarpetaClases.pedido import *
from CarpetaBD.conexion import *

class Pedidos():
    def __init__(self) -> None:
        self.listaPedidos= []
        self.pedido = Orden()

    def registrarPedido(self):
        id = int(input("Id Pedido: "))
        user = input("Nombre: ")
        comida = input("Comida: ")
        cambios = input("Personalizar pedido: ")
        dondeconsume = input("Para llevar o Mesa: ")
        pedido = Pedido(id, user, comida, cambios, dondeconsume)
        self.listaPedidos.append(pedido)

    def enviarDatosPedido(self):
        for i in self.listaPedidos:
            id = i.getIdPedido()
            nombre = i.getNombre()
            comida = i.getComida()
            cambios = i.getCambio()
            dondeConsume = i.getDondeconsume()
            self.pedido.crearPedido(id,nombre,comida,cambios,dondeConsume)
        self.listaPedidos.clear()
        print("="*20)
        print("PEDIDO REGISTRADO")
        print("="*20)
        input("ENTER PARA CONTINUAR")

    def actualizarPedido(self):
        id = int(input("id del Pedido: "))
        newComida = input("Nueva Comida: ")
        newCambio = input("Nuevos Cambios: ")
        newDondeConsume = input("Llevar o Mesa: ")
        self.pedido.actualizarPedido(id, newComida, newCambio, newDondeConsume)
        print("="*20)
        print("DATO ACTUALIZADOS")
        print("="*20)
        input("ENTER PARA CONTINUAR")

    def eliminarPedido(self):
        idPedido = int(input("Id del Pedido que desea eliminar: "))
        self.pedido.eliminarPedido(idPedido)
        print("="*20)
        print("PEDIDIO ELIMINADO")
        print("="*20)
        input("ENTER PARA CONTINUAR")
        
