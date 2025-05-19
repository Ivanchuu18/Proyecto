from Proyecto.Doc.config import DATABASE, USER, PASSWORD, HOST
import mysql.connector
from mysql.connector import errorcode
from Proyecto.ui.Menu_cargar_datos import Menu_cargar_datos
+
6import re

class BBDD:

    def conexion(self):
        """
        Esta función establece una conexión a la base de datos SQLite.
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
        tablas = ["alumnos"
                  "alumnoscrusos"
                  "cursos"
                  "libros"
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

    def cargar_datos(self):
        Menu_cargar_datos().mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == 1:
            self.cargar_alumnos()
        if opcion == 2:
            self.cargar_libros()

        if opcion == 3:
           self.cargar_materias()

        if opcion == 4:
            self.cargar_cursos()

    def cargar_alumnos(self):
        """
        Esta función carga los datos de los alumnos en la base de datos.
        """

        conexion = self.conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            validar = False
            while not validar:
                nie = input("Introduzca el DNI del alumno: ")
                aux = self.validar_dni(nie)
                if aux == True:
                    validar = True
                else:
                    print("El DNI no es valido")

            nombre = input("Introduzca el nombre del alumno: ")
            apellidos = input("Introduzca los apellidos del alumno: ")
            while validar:
                tramo = input("Introduzca el tramo del alumno: (0 nada, I tramo 1, II tramo 2): ")
                aux = self.validar_tramo(int(tramo))
                if aux == True:
                    validar = False
                else:
                    print("El tramo no es valido")
            while not validar:
                bilingue = input("Introduzca si el alumno es bilingue: (0 si, 1 no): ")
                aux = self.bilingue(int(bilingue))
                if aux == True:
                    validar = True
                else:
                    print("El valor no es valido")
            cursor.execute("INSERT INTO alumnos (dni, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)",
                               (nie, nombre, apellidos, tramo, bilingue))
            conexion.commit()
        except mysql.connector.Error as err:
            print(err)

        finally:
            cursor.close()
            self.cerrar(conexion)

    def cargar_libros(self):
        """
        Esta función carga los datos de los libros en la base de datos.
        """

        conexion = self.conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            validar = False
            while not validar:
                isbn = input("Introduzca el ISBN del libro: ")
                aux = self.validar_isbn(isbn)
            titulo = input("Introduzca el titulo del libro: ")
            autor = input("Introduzca el autor del libro: ")
            editorial = input("Introduzca la editorial del libro: ")
            id_materia = input("Introduzca el id de la materia del libro: ")
            id_curso = input("Introduzca el id del curso del libro: ")
            cursor.execute(
                "INSERT INTO libros (isbn, titulo, autor, editorial, id_materia, id_curso) VALUES (%s, %s, %s, %s, %s, %s)",
                (isbn, titulo, autor, editorial, id_materia, id_curso))
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
            id_ = input("Introduzca el id de la materia: ")
            nombre = input("Introduzca el nombre de la materia: ")
            departemento = input("Introduzca el departamento de la materia: ")
            cursor.execute("INSERT INTO materias (id, curso, departamento) VALUES (%s, %s, %s)",
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
                validar = False
                while not validar:
                    curso = input("Introduzca el curso: ")
                    aux = self.validar_curso(curso)
                    if aux == True:
                        validar = True
                    else:
                        print("El curso no es valido")
                while validar:
                    nivel = input("Introduzca el nivel: ")
                    aux = self.validar_nivel(nivel)
                    if aux == True:
                        validar = False
                    else:
                        print("El nivel no es valido")
                cursor.execute("INSERT INTO cursos (curso, nivel) VALUES (%s, %s)",
                               (curso, nivel))
                conexion.commit()
            except mysql.connector.Error as err:
                print(err)

            finally:
                cursor.close()
                self.cerrar(conexion)

    def validar_curso(self, curso):
        # Verificar si el curso es uno de los valores permitidos
        cursos_permitidos = ["1", "2", "3", "4"]
        if curso in cursos_permitidos:
            return True
        else:
            raise ValueError("Curso no válido. Debe ser uno de los siguientes: 1, 2, 3, 4.")

    def validar_nivel(self, grupo):
        # Verificar si el nivel es uno de los valores permitidos
        niveles_permitidos = ["A", "B", "C", "D"]
        if grupo in niveles_permitidos:
            return True
        else:
            raise ValueError("Nivel no válido. Debe ser uno de los siguientes: A, B, C, D.")

    def validar_dni(self, dni: str) -> ValueError | bool:
        # Convertir a mayúsculas y eliminar espacios
        dni_alumno = dni.upper().strip()

        # Expresión regular para verificar el formato: 8 dígitos seguidos de una letra
        if not re.fullmatch(r'\d{8}[A-Z]', dni_alumno):
            return ValueError("Formato de DNI no válido. Debe tener 8 dígitos seguidos de una letra.")

        # Secuencia de letras para calcular la letra del DNI
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        numero = int(dni_alumno[:8])
        letra_calculada = letras[numero % 23]

        # Comparar la letra calculada con la letra proporcionada
        if dni_alumno[-1] == letra_calculada:
            return True
        else:
            return ValueError("La letra del DNI no es correcta. Debe ser: " + letra_calculada)

    def validar_tramo(self, tramo: int) -> bool:
        # Verificar si el tramo está entre 0 y 2
        return 0 <= tramo <= 2

    def bilingue(self, bilingue) -> bool | ValueError:
        # Verificar si el alumno es bilingüe
        if bilingue == 0 or bilingue == 1:
            return True
        else:
            return ValueError("Los valores permitidos son: 0 (si) o 1 (no)")

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








