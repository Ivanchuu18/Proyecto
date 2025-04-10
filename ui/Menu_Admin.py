import Menu as Menu
from abc import abstractmethod
class Menu_admin(Menu):
    def mostrar_menu(self):
        print("._Bienvenido al menu de administrador_.")
        print("._Que desea manipular_.")
        print("1. BBDD")
        print("2. Alumnos")
        print("3. Contratos")
        print("4. Salir")
        
        