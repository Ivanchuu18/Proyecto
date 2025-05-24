import mysql
from Proyecto.lib.BBDD import BBDD
class Gestionar_listado:
    def listado_libros(self):
        """
        Muestra un listado de libros en la base de datos.
        """
        libros = {}
        contador = 1
        conexion = BBDD().conexion()
        # Verificar si la conexión fue exitosa
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            # Realizar la consulta SQL para obtener todos los libros
            query = "SELECT * FROM libros"
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Mostrar los resultados
            print(f"Se encontraron {len(resultados)} resultados:")
            print("-" * 50)
            for fila in resultados:
                print(contador, fila)
                libros[contador] = fila
                contador += 1
            print("-" * 50)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            BBDD().cerrar(conexion)
            return libros

    def listado_materias(self):
        """
        Muestra un listado de materias en la base de datos.
        """
        materias = {}
        contador = 1
        conexion = BBDD().conexion()
        # Verificar si la conexión fue exitosa
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            # Realizar la consulta SQL para obtener todas las materias
            query = "SELECT * FROM materias"
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Mostrar los resultados
            print(f"Se encontraron {len(resultados)} resultados:")
            print("-" * 50)
            for fila in resultados:
                print(contador, fila)
                materias[contador] = fila
                contador += 1
            print("-" * 50)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            BBDD().cerrar(conexion)
            return materias

    def listado_alumnos(self):
        """
        Muestra un listado de alumnos en la base de datos.
        """
        alumnos = {}
        contador = 1
        conexion = BBDD().conexion()
        # Verificar si la conexión fue exitosa
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            # Realizar la consulta SQL para obtener todos los alumnos
            query = "SELECT * FROM alumnos"
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Mostrar los resultados
            print(f"Se encontraron {len(resultados)} resultados:")
            print("-" * 50)
            for fila in resultados:
                print(contador, fila)
                alumnos[contador] = fila
                contador += 1
            print("-" * 50)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            BBDD().cerrar(conexion)
            return alumnos

    def listado_cursos(self):
        """
        Muestra un listado de cursos en la base de datos.
        """
        cursos = {}
        contador = 1
        conexion = BBDD().conexion()
        # Verificar si la conexión fue exitosa
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            # Realizar la consulta SQL para obtener todos los cursos
            query = "SELECT * FROM cursos"
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Mostrar los resultados
            print(f"Se encontraron {len(resultados)} resultados:")
            print("-" * 50)
            for fila in resultados:
                print(contador, fila)
                cursos[contador] = fila
                contador += 1
            print("-" * 50)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            BBDD().cerrar(conexion)
            return cursos

    def listado_prestamos(self):
        """
        Muestra un listado de prestamos en la base de datos.
        """
        prestamos = {}
        contador = 1
        conexion = BBDD().conexion()
        # Verificar si la conexión fue exitosa
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            # Realizar la consulta SQL para obtener todos los prestamos
            query = "SELECT * FROM prestamos"
            cursor.execute(query)
            resultados = cursor.fetchall()
            if len(resultados) != 0:
                # Mostrar los resultados
                print(f"Se encontraron {len(resultados)} resultados:")
                print("-" * 50)
                for fila in resultados:
                    print(contador, fila)
                    prestamos[contador] = fila
                    contador += 1
                print("-" * 50)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            BBDD().cerrar(conexion)
            return prestamos

        return cadena

    def listar_todos(self):
        self.listado_alumnos()
        self.listado_libros()
        self.listado_materias()
        self.listado_cursos()
        if self.listado_prestamos() == {}:
            print("No hay prestamos en la base de datos.")
        else:
            self.listado_prestamos()