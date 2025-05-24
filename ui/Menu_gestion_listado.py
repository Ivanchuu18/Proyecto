from Proyecto.ui.Menu import Menu
from Proyecto.lib.Gestionar_listado import Gestionar_listado

class Menu_gestion_listado(Menu):
    def mostrar_menu(self):
        print("._Bienvenido al menu de gestion de listado_.")
        print("._Que desea hacer_.")
        print("1. Listar libros")
        print("2. Listar alumnos")
        print("3. Listar materias")
        print("4. Listar cursos")
        print("5. Listar prestamos")
        print("6. Listar todos")
        print("0. Volver")

    def tratar_opcion(self):
        while True:
            print("\n" * 50)
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                Gestionar_listado().listado_libros()
            elif opcion == "2":
                Gestionar_listado().listado_alumnos()
            elif opcion == "3":
                Gestionar_listado().listado_materias()
            elif opcion == "4":
                Gestionar_listado().listado_cursos()
            elif opcion == "5":
                Gestionar_listado().listado_prestamos()
            elif opcion == "6":
                Gestionar_listado().listar_todos()
            elif opcion == "0":
                from Proyecto.ui.Menu_Principal import Menu_principal
                print("\n" * 50)
                Menu_principal().tratar_opcion()
                break
