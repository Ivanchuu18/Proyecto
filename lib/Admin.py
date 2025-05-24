from config import CONTRASENA, USUARIO

class Admin:
    def __init__(self, usuario, contrasena):
        self._usuario = usuario
        self._contrasena = contrasena

    def login(self):
        if self._usuario == USUARIO and self._contrasena == CONTRASENA:
            return True
        else:
            return ValueError("Usuario o contraseña incorrectos.")