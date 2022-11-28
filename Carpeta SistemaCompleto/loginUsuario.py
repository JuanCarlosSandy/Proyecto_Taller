from Usuario import *
from conexion import *

class Users:
    def __init__(self) -> None:
        self.listaUsuario = []
        self.usuarios = Login()

    def resgistroUsuario(self):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        user = Usuario(usuario, contraseña)
        self.listaUsuario.append(user)

    def enviarDatosUsuario(self):
        for i in self.listaUsuario:
            usuario = i.getUsuario()
            contraseña = i.getContraseña()
            self.usuarios.crearUsuario(usuario, contraseña)
        self.listaUsuario.clear()

#esto terminalo liz
    '''def verificarLoginUser(self):
        posi = False
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if len(usuario) == 0 or len(contraseña) == 0:
            print("==Campo vacio==")
        elif posi == False:
            self.usuarios.verificarUsuario(usuario, contraseña)
            posi = True
            if posi == True:
                verificacion = True
                return verificacion'''


