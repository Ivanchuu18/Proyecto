from Proyecto.lib.Gestion_alumnos import GestionAlumnos
from Proyecto.ui.Menu import Menu
class Menu_gestion_alumnos(Menu):
    def mostrar_menu(self):
        print("._Bienvenido al menu de gestion de alumnos_.")
        print("._Que desea hacer_.")
        print("1. Filtrar alumnos")
        print("2. Añadir alumno")
        print("3. Modificar datos de un alumno")
        print("0. Volver")


    def tratar_opcion(self):
        while True:
            print("\n" * 50)
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                GestionAlumnos().filtrar_alumnos()
            elif opcion == "2":
                GestionAlumnos().anadir_alumnos()
            elif opcion == "3":
                GestionAlumnos().modificar_alumno(GestionAlumnos().filtrar_alumnos())
            elif opcion == "0":
                from Proyecto.ui.Menu_Principal import Menu_principal
                print("\n" * 50)
                Menu_principal().tratar_opcion()
                break
            else:
                print("Opción no válida. Intente nuevamente.")
