from Proyecto.ui.Menu import Menu
from Proyecto.ui.Menu_gestion_alumnos import Menu_gestion_alumnos
from Proyecto.ui.Menu_gestion_listado import Menu_gestion_listado
from Proyecto.ui.Menu_preservar_datos import Menu_exportar
from Proyecto.lib.Gestionar_prestamos import Gestionar_prestamos
from Proyecto.lib.Gestion_alumnos import GestionAlumnos
from Proyecto.lib.Gestionar_listado import Gestionar_listado
class Menu_principal(Menu):
    def mostrar_menu(self):
        print("._Bienvenido al menu principal_.")
        print("._Que desea _.")
        print("1. Gestionar contratos")
        print("2. Gestionar alumnos")
        print("3. Gestionar listado")
        print("4. Exportar datos")
        print("0. Salir")

    def tratar_opcion(self):
        while True:
            print("\n" * 50)
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                Gestionar_prestamos().generar_contrato(GestionAlumnos().filtrar_alumnos(), Gestionar_listado().listado_libros(), Gestionar_listado().listado_cursos())
            elif opcion == "2":
                Menu_gestion_alumnos().tratar_opcion()
            elif opcion == "3":
                Menu_gestion_listado().tratar_opcion()
            elif opcion == "4":
                Menu_exportar().tratar_opcion()
            elif opcion == "0":
                print("\n" * 50)
                pregunta = input("¿Está seguro de que has guardado? (s/n): ")
                if pregunta.lower() == "s":
                    input("Pulsa enter para salir")
                    print("Saliendo del programa...")
                    break
                else:
                    print("Volviendo al menú para exportar...")
                    Menu_exportar().tratar_opcion()





