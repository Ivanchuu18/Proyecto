import csv
import json
import os
import mysql
from Proyecto.lib.BBDD import BBDD


class Gestion_preservar_datos:
    def exportar_csv(self):
        """
        Exporta los datos de una tabla a un archivo CSV.
        """
        tablas = ["alumnos",
                  "prestamos",
                  "cursos",
                  "libros",
                  "materias"]
        while True:
            opcion = input("Cual tabla quieres exportar? (alumnos, prestamos, cursos, libros, materias o todos): ")
            if opcion in tablas:
                try:
                    conn = BBDD().conexion()
                    cursor = conn.cursor()
                    ruta = f"Csv/Backup/cs_{opcion}.csv"
                    escribir_cabecera = True
                    # Comprobar si el archivo tiene contenido
                    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
                        escribir_cabecera = False
                    with open(ruta, "a", newline="", encoding="utf-8") as f:
                        cursor.execute(f"SELECT * FROM {opcion}")
                        resultados = cursor.fetchall()
                        resultados_limpios = self.limpiar_comillas(resultados)
                        writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)
                        if escribir_cabecera:
                            writer.writerow([i[0] for i in cursor.description])
                        writer.writerows(resultados_limpios)
                    cursor.close()
                    conn.close()
                except mysql.connector.Error as e:
                    print(f"Error conectando a la base de datos: {e}")
                    return
                break
            elif opcion == "todos":
                try:
                    conn = BBDD().conexion()
                    cursor = conn.cursor()
                    for tabla in tablas:
                        ruta = f"Csv/Backup/cs_{tabla}.csv"
                        escribir_cabecera = True
                        # Comprobar si el archivo tiene contenido
                        if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
                            escribir_cabecera = False
                        with open(ruta, "a", newline="", encoding="utf-8") as f:
                            cursor.execute(f"SELECT * FROM {tabla}")
                            resultados = cursor.fetchall()
                            resultados_limpios = self.limpiar_comillas(resultados)
                            writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)
                            if escribir_cabecera:
                                writer.writerow([i[0] for i in cursor.description])
                            writer.writerows(resultados_limpios)
                    cursor.close()
                    conn.close()
                except mysql.connector.Error as e:
                    print(f"Error conectando a la base de datos: {e}")
                    return
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        input("Exportando...")

    def exportar_json(self):
        """
        Exporta los datos de una tabla o todas las tablas a archivos JSON.
        """
        tablas = ["alumnos", "prestamos", "cursos", "libros", "materias"]

        while True:
            opcion = input(
                "¿Qué tabla quieres exportar a JSON? (alumnos, prestamos, cursos, libros, materias o todos): ")
            if opcion in tablas:
                try:
                    conn = BBDD().conexion()
                    # Devuelve cada fila como un diccionario
                    cursor = conn.cursor(dictionary=True)
                    ruta = f"Json/js_{opcion}.json"
                    cursor.execute(f"SELECT * FROM {opcion}")
                    resultados = cursor.fetchall()
                    # Crear carpeta si no existe
                    os.makedirs(os.path.dirname(ruta), exist_ok=True)
                    # Abrir en modo append y mantener lista existente si ya existe
                    datos_totales = []
                    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
                        with open(ruta, "r", encoding="utf-8") as f:
                            datos_totales = json.load(f)
                    datos_totales.extend(resultados)
                    with open(ruta, "w", encoding="utf-8") as f:
                        json.dump(datos_totales, f, ensure_ascii=False, indent=4)

                    cursor.close()
                    conn.close()
                except mysql.connector.Error as e:
                    print(f"Error conectando a la base de datos: {e}")
                    return
                break
            elif opcion == "todos":
                try:
                    conn = BBDD().conexion()
                    cursor = conn.cursor(dictionary=True)
                    for tabla in tablas:
                        ruta = f"Json/js_{tabla}.json"
                        cursor.execute(f"SELECT * FROM {tabla}")
                        resultados = cursor.fetchall()
                        os.makedirs(os.path.dirname(ruta), exist_ok=True)
                        datos_totales = []
                        if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
                            with open(ruta, "r", encoding="utf-8") as f:
                                datos_totales = json.load(f)
                        datos_totales.extend(resultados)
                        with open(ruta, "w", encoding="utf-8") as f:
                            json.dump(datos_totales, f, ensure_ascii=False, indent=4)
                    cursor.close()
                    conn.close()
                except mysql.connector.Error as e:
                    print(f"Error conectando a la base de datos: {e}")
                    return
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        input("Exportando...")

    def limpiar_comillas(self, cadena):
        if isinstance(cadena, str):
            return cadena.replace('"', '')