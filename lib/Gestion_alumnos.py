import re

import mysql
from Proyecto.lib.BBDD import BBDD


class GestionAlumnos:
    def anadir_alumnos(self):
        """
        Esta función carga los datos de los alumnos en la base de datos.
        """

        conexion = BBDD().conexion()
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
                    print(aux)

            nombre = input("Introduzca el nombre del alumno: ")
            apellidos = input("Introduzca los apellidos del alumno: ")
            while validar:
                tramo = input("Introduzca el tramo del alumno: (0 nada, I tramo 1, II tramo 2): ")

                aux = self.validar_tramo(tramo)
                if aux == True:
                        validar = False
                else:
                    print(aux)
            while not validar:
                bilingue = input("Introduzca si el alumno es bilingue: (0 si, 1 no): ")
                aux = self.bilingue(bilingue)
                if aux == True:
                    validar = True
                else:
                    print(aux)
            cursor.execute("INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)",
                               (nie, nombre, apellidos, tramo, bilingue))
            conexion.commit()
        except mysql.connector.Error as err:
            print(err)

        finally:
            cursor.close()
            BBDD().cerrar(conexion)

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

    def validar_tramo(self, tramo: int) -> ValueError | bool:
        # Verificar si el tramo está entre 0 y 2
        if tramo != "0" and tramo != "1" and tramo != "2":
            return ValueError("El tramo debe ser 0 (nada), 1 (I tramo) o 2 (II tramo).")
        else:
            return True

    def bilingue(self, bilingue) -> bool | ValueError:
        # Verificar si el alumno es bilingüe
        if bilingue == "0" or bilingue == "1":
            return True
        else:
            return ValueError("Los valores permitidos son: 0 (si) o 1 (no)")

    def filtrar_alumnos(self):
        """
        Filtra la lista de alumnos según el criterio de búsqueda.
        """
        alumnos_filtrados = {}
        contador = 1
        conexion = BBDD().conexion()
        filas = ["apellidos", "nombre", "nie"]
        # Verificar si la conexión fue exitosa
        if not conexion:
            return False
        cursor = conexion.cursor()
        try:
            # Solicitar al usuario el criterio de búsqueda
            while True:
                criterio = input("Introduzca el criterio de búsqueda (nombre, apellidos, nie): ").lower()
                if criterio in filas:
                    break
                else:
                    print("Criterio no válido. Debe ser uno de los siguientes: nombre, apellidos, nie.")
            valor = input("Introduzca el valor a buscar: ")

            # Realizar la consulta SQL con el filtro
            query = f"SELECT * FROM alumnos WHERE {criterio} LIKE %s"
            cursor.execute(query, ('%' + valor + '%',))
            resultados = cursor.fetchall()

            # Mostrar los resultados
            if not resultados:
                print("No se encontraron resultados.")
                opcion = input("Quieres volver a intentar? (s/n): ")
                if opcion.lower() == "s":
                    self.filtrar_alumnos()
                else:
                    print("Saliendo...")
            else:
                print(f"Se encontraron {len(resultados)} resultados:")
                print("-" * 50)
                for fila in resultados:
                    print(contador, fila)
                    alumnos_filtrados[contador] = fila
                    contador += 1
                print("-" * 50)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            BBDD().cerrar(conexion)
            return alumnos_filtrados

    def modificar_alumno(self, alumnos_filtrados):
        """
        Modifica los datos de un alumno en la base de datos.
        """
        opciones = ["nombre", "apellidos", "tramo", "bilingue"]
        conexion = BBDD().conexion()
        aux = False
        if not conexion:
            return
        cursor = conexion.cursor()
        try:
            # Solicitar al usuario el nuevo nombre y apellidos
            while not aux:
                alumno = input("Que alumno quieres modificar: ")
                if alumno not in str(alumnos_filtrados.keys()):
                    for i in alumnos_filtrados.keys():
                        print(i)
                    print("Solo pon un valor pon pantalla.")
                    for i in alumnos_filtrados:
                        print(i, alumnos_filtrados[i])
                else:
                    aux = True
            while aux:
                opcion = input("¿Qué dato quieres modificar? (nombre, apellidos, tramo, bilingue): ").lower()
                if opcion not in opciones:
                    print("Opción no válida. Debe ser uno de los siguientes: nombre, apellidos, tramo, bilingue.")
                else:
                    aux = False
                valor = input("Introduzca el nuevo valor: ")

            # Actualizar los datos del alumno en la base de datos
            query = (f"UPDATE alumnos SET {opcion} = LIKE %s",)
            cursor.execute(query, (valor,))

            conexion.commit()
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            BBDD().cerrar(conexion)
