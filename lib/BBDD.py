from config import DATABASE, USER, PASSWORD, HOST
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from dateutil.relativedelta import relativedelta

class BBDD:

    def conexion(self):
        """
        Esta función establece una conexión a la base de datos MySQL
        """
        try:
            cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Acceso denegado")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de datos no encontrada")
            else:
                print(err)

    def cerrar(self, cnx):
        """
        Esta función cierra la conexión a la base de datos SQLite.
        """
        cnx.close()

    def eliminar_BBDD(self):
        """
        Esta función elimina la base de datos SQLite.
        """
        tablas = ["alumnos",
                  "prestamos",
                  "cursos",
                  "libros",
                  "materias"]
        conexion = self.conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            for tabla in tablas:
                cursor.execute(f"DELETE FROM {tabla}")
            conexion.commit()
            print("Eliminada la base de datos")
        except mysql.connector.Error as err:
            print(err)

        finally:
            cursor.close()
            self.cerrar(conexion)

    def cargar_datos_inicial(self):
        self.cargar_alumnos_inicial()
        self.cargar_materias()
        self.cargar_cursos()
        self.cargar_libros()




    def cargar_alumnos_inicial(self):
        """
        Esta función carga los datos de los alumnos en la base de datos.
        """

        conexion = self.conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            from Proyecto.lib.Gestion_alumnos import GestionAlumnos
            with open("Proyecto/lib/Csv/Carga_inicial/ci_alumnos.csv", "r", encoding="utf-8") as f:
                contenido = f.readlines()
                # Empieza desde línea 2 para el conteo humano
                for i, linea in enumerate(contenido[1:], start=2):
                    columnas = linea.strip().split(";")
                    # Línea vacía
                    if not linea:
                        continue
                    # Saltamos líneas con datos incompletos
                    if len(columnas) < 5:
                        print(f"Línea {i} incompleta")
                        continue
                    nie = columnas[0].strip('"')
                    nombre = columnas[1].strip('"')
                    apellidos = columnas[2].strip('"')
                    tramo = columnas[3]
                    bilingue = columnas[4]
                    # Validar el DNI si esta o no en la base de datos
                    if not self.validar_idalumno(nie):
                        print(f"El DNI {nie} ya existe en la base de datos.")
                        continue
                    # Validar DNI si no esta en la Base de datos
                    if not GestionAlumnos().validar_dni(nie):
                        print(f"El DNI {nie} no es válido.")
                        continue
                    # Validar el tramo
                    if not GestionAlumnos().validar_tramo(int(tramo)):
                        print(f"El tramo {tramo} no es válido.")
                        continue
                    # Validar el bilingue
                    if not GestionAlumnos().bilingue(int(bilingue)):
                        print(f"El valor de bilingue {bilingue} no es válido.")
                        continue
                    else:
                        cursor.execute("INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)",
                               (nie, nombre, apellidos, tramo, bilingue))
            conexion.commit()
        except mysql.connector.Error as err:
            print(err)

        finally:
            cursor.close()
            self.cerrar(conexion)

    def cargar_libros   (self):
        """
        Esta función carga los datos de los libros en la base de datos.
        """

        conexion = self.conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            with open("Proyecto/lib/Csv/Carga_inicial/ci_libros.csv", "r", encoding="utf-8") as f:
                contenido = f.readlines()
                # Empieza desde línea 2 para el conteo humano
                for i, linea in enumerate(contenido[1:], start=2):
                    columnas = linea.strip().split(";")
                    # Línea vacía
                    if not linea:
                        continue
                    # Saltamos líneas con datos incompletos
                    if len(columnas) < 6:
                        print(f"Línea {i} incompleta")
                        continue
                    isbn = columnas[0].replace('"', '')
                    titulo = columnas[1]
                    autor = columnas[2]
                    numero_ejemplares = int(columnas[3].replace('"', ''))
                    id_materia = int(columnas[4].replace('"', ''))
                    id_curso = columnas[5]

                    # Validar el ISBN
                    if not self.validar_isbn(isbn):
                        print(f"El ISBN {isbn} no es válido.")
                        continue
                    # Validar el ISBN si no esta en la base de datos
                    if not self.validar_isbn_basededatos(isbn):
                        print(f"El ISBN {isbn} ya existe en la base de datos.")
                        continue
                    # Validar el ID de materia
                    if self.validar_idmateria(id_materia):
                        print(f"El ID de materia {id_materia} no esta en la base de datos.")
                        continue
                    # Validar el ID de curso
                    if not self.validar_idcurso(id_curso):
                        print(f"El ID de curso {id_curso} no esta en la base de datos.")
                        continue
                    # Insertar los datos en la base de datos
                    else:
                        cursor.execute(
                            "INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) VALUES (%s, %s, %s, %s, %s, %s)",
                            (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso))
            conexion.commit()
        except mysql.connector.Error as err:
            print(err)

        finally:
            cursor.close()
            self.cerrar(conexion)

    def cargar_materias(self):
        """
        Esta función carga los datos de las materias en la base de datos.
        """

        conexion = self.conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            with open("Proyecto/lib/Csv/Carga_inicial/ci_materia.csv", "r", encoding="utf-8") as f:
                contenido = f.readlines()
                # Empieza desde línea 2 para el conteo humano
                for i, linea in enumerate(contenido[1:], start=2):
                    columnas = linea.strip().split(";")
                    # Línea vacía
                    if not linea:
                        continue
                    # Saltamos líneas con datos incompletos
                    if len(columnas) < 3:
                        print(f"Línea {i} incompleta")
                        continue
                    id_ = int(columnas[0])
                    nombre = columnas[1]
                    departemento = columnas[2]
                    # Validar si el ID de materia ya esta en la base de datos
                    if not self.validar_idmateria(id_):
                        print(f"El ID de materia {id_} ya existe en la base de datos.")
                        continue

                    else:
                        cursor.execute("INSERT INTO materias (id, nombre, departamento) VALUES (%s, %s, %s)",
                           (id_, nombre, departemento))
            conexion.commit()
        except mysql.connector.Error as err:
            print(err)

        finally:
            cursor.close()
            self.cerrar(conexion)

    def cargar_cursos(self):
        conexion = self.conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            with open("Proyecto/lib/Csv/Carga_inicial/ci_cursos.csv", "r", encoding="utf-8") as f:
                contenido = f.readlines()
                # Empieza desde línea 2 para el conteo humano
                for i, linea in enumerate(contenido[1:], start=2):
                    columnas = linea.strip().split(";")
                    # Línea vacía
                    if not linea:
                        continue
                    # Saltamos líneas con datos incompletos
                    if len(columnas) < 2:
                        print(f"Línea {i} incompleta")
                        continue
                    curso = columnas[0]
                    nivel = columnas[1]
                    # Validar si el curso ya existe en la base de datos
                    if self.validar_curso(curso):
                        print(f"El curso {curso} ya existe en la base de datos.")
                        continue
                    else:
                        cursor.execute("INSERT INTO cursos (curso, nivel) VALUES (%s, %s)",
                            (curso, nivel))
                conexion.commit()
        except mysql.connector.Error as err:
            print(err)

        finally:
            cursor.close()
            self.cerrar(conexion)

    def validar_curso(self, curso):
        # Verificar si el curso esta en la base de datos
        conexion = self.conexion()
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM cursos WHERE curso = %s", (curso,))
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                return False
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            self.cerrar(conexion)
        return True


    def validar_isbn(self, isbn):
        # Verificar si el ISBN tiene 13 dígitos
        if len(isbn) != 13:
            return False

        # Verificar si el ISBN contiene solo dígitos
        if not isbn.isdigit():
            return False

        # Calcular el dígito de control
        suma = 0
        for i in range(12):
            if i % 2 == 0:
                suma += int(isbn[i])
            else:
                suma += int(isbn[i]) * 3

        digito_control = (10 - (suma % 10)) % 10

        # Comparar el dígito de control calculado con el proporcionado
        if digito_control == int(isbn[-1]):
            return True
        else:
            return ValueError("El ISBN no es válido. El dígito de control no coincide.")


    def validar_idmateria(self, id_materia):
        # Verificar si el ID de materia es un número entero
        if not isinstance(id_materia, int):
            return False

        # Verificar si el ID de materia está en la base de datos
        conexion = self.conexion()
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM materias WHERE id = %s", (id_materia,))
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                return True
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            self.cerrar(conexion)

        return False

    def validar_idcurso(self, id_curso):

        conexion = self.conexion()
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM cursos WHERE curso = %s", (id_curso,))
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                return False
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            self.cerrar(conexion)
        return True
    def validar_idalumno(self, id_alumno) :

        # Verificar si el NIE de alumno está en la base de datos
        conexion = self.conexion()
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM alumnos WHERE NIE = %s", (id_alumno,))
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                return True
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            self.cerrar(conexion)
        return False
    def validar_isbn_basededatos(self, isbn) :

        # Verificar si el isbn del libro está en la base de datos
        conexion = self.conexion()
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM libros WHERE isbn = %s", (isbn,))
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                return True
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            self.cerrar(conexion)
        return False