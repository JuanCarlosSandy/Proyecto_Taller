from os import system
from Comida import *
from conexion import *
from Menu import *
from administrador import *
from loginUsuario import *
from pedido import *
from RegistroPedido import *


class Restaurante:
    def __init__(self, admin) -> None:
        self.verfood = RegistroComida()
        self.verPedido = Orden()
        self.food = Menu()
        self.admin = admin
        self.users = Users()
        self.usuarios = Login()
        self.pedido = Pedidos()

    def verificarLoginAdmin(self):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if len(usuario) == 0 or len(contraseña) == 0:
            print("==Campo vacio==")
            input("ENTER PARA CONTINUAR")
        elif (usuario == self.admin.getUsuario() and contraseña == self.admin.getContraseña()):
            verificado = True
            return verificado
        else:
            print("="*4,"DATOS INCORRECTOS","="*4)
            input("ENTER PARA CONTINUAR")

    def menuLogin(opcion):
        system("cls")
        print("="*6,"MENU INICIO","="*6)
        print("[1].. Iniciar Sesion como Admin \n[2].. Iniciar Sesion como Usuario \n[3].. Registrarse \n[0].. Salir")
        opcion = int(input(">> "))
        return opcion

    def menuAdminPLato(opcion):
        system("cls")
        print("="*6,"MENU PLATOS","="*6)
        print('[1].. Aniadir Plato \n[2].. Ver plato \n[3].. Editar Plato \n[4].. Eliminar Plato \n[0].. Volver')
        opcion = int(input(">> "))
        return opcion

    def menuCliente(opcion):
        system("cls")
        print("="*6,"MENU PEDIDOS","="*6)
        print('[1].. Ver Menu \n[2].. Realizar Pedido \n[3].. Ver Pedidos \n[4].. Editar Pedido \n[5].. Eliminar Pedido \n[0].. Volver')
        opcion = int(input(">> "))
        return opcion

    def abrirRestauran(self):
        estado = True
        while estado == True:
            opcLogin = self.menuLogin()
            if opcLogin == 1:
                if self.verificarLoginAdmin() == True:
                    opc = self.menuAdminPLato()
                    while opc != 0:
                        if opc == 1:
                            self.food.resigistroComida()
                            self.food.enviarDatosComida()
                            opc = self.menuAdminPLato()
                        elif opc == 2:
                            self.verfood.mostrarMenu()
                            opc = self.menuAdminPLato()
                        elif opc == 3:
                            self.food.actualizarComida()
                            opc = self.menuAdminPLato()
                        elif opc == 4:
                            self.food.eliminarComida()
                            opc = self.menuAdminPLato()
                else:
                    print("No encontro Usuario")

            elif opcLogin == 2:
                #if self.users.verificarLoginUser() == True:
                opcionUser = self.menuCliente()
                while opcionUser != 0:
                    if opcionUser == 1:
                        self.verfood.mostrarMenu()
                        opcionUser = self.menuCliente()
                    elif opcionUser == 2:
                        self.verfood.mostrarMenu()
                        print("="*40)
                        self.pedido.registrarPedido()
                        self.pedido.enviarDatosPedido()
                        opcionUser = self.menuCliente()
                    elif opcionUser == 3:
                        self.verPedido.mostrarPedido()
                        opcionUser = self.menuCliente()
                    elif opcionUser == 4:
                        self.pedido.actualizarPedido()
                        opcionUser = self.menuCliente()
                    elif opcionUser == 5:
                        self.pedido.eliminarPedido()
                        opcionUser = self.menuCliente()
                #else:
                    #print("No se encontro Usuario")
            elif opcLogin == 3:
                self.users.resgistroUsuario()
                self.users.enviarDatosUsuario()

            elif opcLogin == 0:
                estado = False
            

admin = Admin()
restaurant = Restaurante(admin)
restaurant.abrirRestauran()