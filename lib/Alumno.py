from enum_tramos import Tramos
import mysql
from BBDD import BBDD
class Alumno:
    def __init__(self, nombre, apellidos, dni, tramo , bilingue: int):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.tramo= tramo if tramo in Tramos else Tramos.NADA
        self.bilingue = bilingue
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, DNI: {self.dni}, Tramo: {self.tramo}, Bilingue: {self.bilingue}"

    def filtrar_alumnos(self):
        """
        Filtra la lista de alumnos según el criterio de búsqueda.
        """
        conexion = BBDD().conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            # Solicitar al usuario el criterio de búsqueda
            criterio = input("Introduzca el criterio de búsqueda (nombre, apellidos, dni): ")
            valor = input("Introduzca el valor a buscar: ")

            # Realizar la consulta SQL con el filtro
            query = f"SELECT * FROM alumnos WHERE {criterio} LIKE %s"
            cursor.execute(query, ('%' + valor + '%',))
            resultados = cursor.fetchall()

            # Mostrar los resultados
            for fila in resultados:
                print(fila)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            BBDD().cerrar(conexion)

