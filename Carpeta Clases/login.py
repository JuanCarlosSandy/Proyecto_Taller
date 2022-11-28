import os
from Cliente import *
from getpass import getpass

class Login():
    def __init__(self):
        self.listaCliente=[]

    def Menu(self):
        os.system('cls')
        print("\tINICIO DE SESION")
        print("[1] Registrarse")
        print("[2] Iniciar sesion ")
        print("[3] Usuarios registrados")
        print("[0] Salir ")

    def Abrir(self):
        opcion = 1
        while opcion != 0:
            self.Menu()
            opcion = int(input("Ingrese opcion: "))
            if opcion == 1:
                self.registrarse()

            elif opcion == 2:
                self.iniciarSesion()
            elif opcion==3:
                self.mostrar()

            elif opcion == 0:
                print("termino el sistema")
        
    def registrarse(self):
        cliente=Cliente()
        cliente.setNombre(input("Nombre: "))
        cliente.setEdad(int(input("Edad: ")))
        cliente.setGenero(input("Genero: "))
        cliente.setCodigo(int(input("Codigo:")))
        cliente.setTelefono(int(input("Telefono:")))
        cliente.setCorreo(input("Correo:"))
        self.listaCliente.append(cliente)
    

    def iniciarSesion(self):
        print("INICIO DE SESION")
        nombre=input("Ingrese su nombre:")
        codigo = int(input("Ingrese su codigo:"))
        for i in self.listaCliente:
            if codigo == i.getCodigo() and nombre==i.getNombre():
                print(i)
                input()
                print("INGRESASTE AL SISTEMA")
            else:
                input()
                print("ERROR DE DATOS")

    def mostrar(self):
        print(">"*60)
        print("\t\tClientes registrados")
        print(">"*60)
        for i in self.listaCliente:
            print("\t",i)
        print(">"*60)
        input()
login=Login()
login.Abrir()
