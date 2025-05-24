from datetime import date

import mysql
from dateutil.relativedelta import relativedelta

from Proyecto.lib.BBDD import BBDD
from Proyecto.lib.Gestionar_listado import Gestionar_listado


class Gestionar_prestamos:
    def generar_contrato(self, alumnos_filtrados:dict, libros:dict, cursos:dict, contador:int = 1):
        """
        Genera un contrato para un alumno en la base de datos.
        """
        alumnos = alumnos_filtrados
        conexion = BBDD().conexion()
        # Verificar si la conexión fue exitosa
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            if contador > 1:
                print(f"Se encontraron {len(alumnos)} resultados:")
                print("-" * 50)
                for i in alumnos:
                    print(i, alumnos[i])
                print("-" * 50)

            while True:
                # Solicitar al usuario el número del alumno a elegir
                opcion = int(input("Seleccione el número del alumno a elegir: "))
                if opcion in alumnos_filtrados:
                    alumno = alumnos_filtrados[opcion]
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

            while True:
                # Solicitar al usuario el número del libro a elegir
                opcion = int(input("Seleccione el número del libro a elegir: "))
                if opcion in libros:
                    if libros[opcion][3] == 0:
                        print("No hay ejemplares disponibles")
                        continue
                    libro = libros[opcion]
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            while True:
                # Solicitar al usuario el número del curso a elegir
                opcion = int(input("Seleccione el número del curso a elegir: "))
                if opcion in cursos:
                    curso = cursos[opcion]
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            fecha_entrega = date.today()
            fecha_devolucion = fecha_entrega + relativedelta(years=1)
            respuesta = input("Desea firmar el contrato? (s/n): ")
            if respuesta.lower() == "s":
                # Realizar el Insert en la tabla alumnoscrusoslibros
                query = f"INSERT INTO prestamos (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (alumno[0],curso[0], str(libro[0]), fecha_entrega, fecha_devolucion, "P"))
                conexion.commit()
                query_restar_numero_ejemplares = f"UPDATE libros SET numero_ejemplares = numero_ejemplares - 1 WHERE isbn = %s "
                cursor.execute(query_restar_numero_ejemplares, (libro[0],))
                conexion.commit()
            else:
                respuesta_2 = input("Quieres volver a generar un contrato? (s/n): ")
                if respuesta_2.lower() == "s":
                    self.generar_contrato(alumnos, Gestionar_listado().listado_libros(), Gestionar_listado().listado_cursos(), contador + 1)
                else:
                    print("Saliendo...")
        except mysql.connector.Error as err:
            print(err)
        except ValueError:
            print("Opción no válida. Debe ser un número.")
        finally:
            cursor.close()
            BBDD().cerrar(conexion)
            print("Contrato generado con éxito")