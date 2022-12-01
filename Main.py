from os import system
from CarpetaClases.Comida import *
from CarpetaBD.conexion import *
from CarpetaClases.Menu import *
from CarpetaClases.administrador import *
from CarpetaClases.loginUsuario import *
from CarpetaClases.pedido import *
from CarpetaClases.RegistroPedido import *


class Restaurante:
    def __init__(self, admin,) -> None:
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
        print("""╔═════════════════════════════════════════════════════════════════╗ 
║ ＢＩＥＮＶＥＮＩＤＯ ＡＬ ＲＥＳＴＡＵＲＡＮＴＥ ＢＵＢＬＥ...♥ ║ 
╚═════════════════════════════════════════════════════════════════╝""")
        print(" "*16,"━━━━【ᴍᴇɴᴜ ɪɴɪᴄɪᴏ】━━━━")
        #【___━━━━ᴹᴱᴺᵁ ᴵᴺᴵᶜᴵᴼ━━━___】
        print(" "*10,"╔══════════════════════════════════╗")
        print(" "*11," [1].. Iniciar Sesion como Admin \n\t     [2].. Iniciar Sesion como Usuario \n\t     [3].. Registrarse como usuario\n\t     [0].. Salir«╝")
        print(" "*10,"╚══════════════════════════════════╝")
        opcion = int(input(">> "))
        return opcion

    def menuAdminPLato(opcion):
        system("cls")
        print(" "*11,"  ━━━━【ᴍᴇɴᴜ ᴘʟᴀᴛᴏs】━━━━")
        print(" "*10,"╔══════════════════════════╗")
        print(" "*11," [1].. Añadir Plato \n\t     [2].. Ver plato \n\t     [3].. Editar Plato \n\t     [4].. Eliminar Plato")
        print(" "*10,"╚══════════════════════════╝")
        print(" "*5,"     【ᴍᴇɴᴜ ᴜsᴜᴀʀɪᴏs ʀᴇɢɪsᴛʀᴀᴅᴏs】")
        print(" "*10,"╔══════════════════════════╗")
        print(" "*11," [5].. Ver usuarios ")
        print(" "*11," [6].. Eliminar usuarios \n\t     [0].. Volver")
        print(" "*10,"╚══════════════════════════╝")

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
            try:
                opcLogin = self.menuLogin()
                if opcLogin == 1:
                    if self.verificarLoginAdmin() == True:
                        try:
                            opc = self.menuAdminPLato()
                            while opc != 0:
                                    if opc == 1:
                                        self.verfood.mostrarMenu()
                                        self.food.resigistroComida()
                                        self.food.enviarDatosComida()
                                        opc = self.menuAdminPLato()
                                    elif opc == 2:
                                        self.verfood.mostrarMenu()
                                        opc = self.menuAdminPLato()
                                    elif opc == 3:
                                        self.verfood.mostrarMenu()
                                        self.food.actualizarComida()
                                        opc = self.menuAdminPLato()
                                    elif opc == 4:
                                        self.verfood.mostrarMenu()
                                        self.food.eliminarComida()
                                        opc = self.menuAdminPLato()
                                    elif opc == 5:
                                        self.usuarios.mostrarUsuario()
                                        opc= self.menuAdminPLato()
                                    elif opc == 6:
                                        self.usuarios.mostrarUsuario()
                                        self.usuarios.eliminarUsuario()
                                        opc = self.menuAdminPLato()
                                    elif opc==0:
                                        self.menuLogin()
                        except:
                            print("INVALIDO")
                            input()
                    print("No encontro Usuario")

                elif opcLogin == 2:
                    if self.usuarios.verificarUsuario()==True:
                        try:
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
                                    tiempoEspera=input("==ENTER=")
                                    opcionUser = self.menuCliente()
                                    input("[ENTER]")
                                elif opcionUser == 4:
                                    self.pedido.actualizarPedido()
                                    opcionUser = self.menuCliente()
                                elif opcionUser == 5:
                                    self.pedido.eliminarPedido()
                                    opcionUser = self.menuCliente()
                        except:
                            print("== OPCION INVALIDA ==")
                            input()
                    else:
                        print("No se encontro Usuario")
                elif opcLogin == 3:
                    self.users.resgistroUsuario()
                    self.users.enviarDatosUsuario()
                elif opcLogin == 0:
                    estado = False
            except:
                print("Opcion INVALIDA")
                input("=== ENTER PA CONTINUAR ===")
            

admin = Admin()
restaurant = Restaurante(admin)
restaurant.abrirRestauran()