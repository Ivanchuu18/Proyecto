from Proyecto.ui.Menu import Menu
from Proyecto.lib.Gestion_preservar_datos import Gestion_preservar_datos

class Menu_exportar(Menu):
    def mostrar_menu(self):
        print("._Bienvenido al menu de exportar datos_.")
        print("._Que desea hacer_.")
        print("1. Exportar en csv")
        print("2. Exportar en json")

    def tratar_opcion(self):
        while True:
            print("\n" * 50)
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                Gestion_preservar_datos().exportar_csv()
            elif opcion == "2":
                Gestion_preservar_datos().exportar_json()
            elif opcion == "0":
                from Proyecto.ui.Menu_Principal import Menu_principal
                print("\n" * 50)
                Menu_principal().tratar_opcion()
                break
            else:
                print("Opción no válida. Intente nuevamente.")