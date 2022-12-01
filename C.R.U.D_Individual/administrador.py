from Usuario import *

class Admin(Usuario):
    def __init__(self, usuario='juan', contraseña='123abc') -> None:
        super().__init__(usuario, contraseña)