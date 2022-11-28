class Usuario:
    def __init__(self, usuario, contraseña) -> None:

        self.usuario = usuario
        self.contraseña = contraseña

    def getUsuario(self):
        return self.usuario

    def getContraseña(self):
        return self.contraseña

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContraseña(self, contraseña):
        self.contraseña = contraseña