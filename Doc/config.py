import mysql.connector
from mysql.connector import errorcode

USUARIO = "admin"
CONTRASENA = "admin"

USER ="root"
PASSWORD = ""
HOST = "localhost"
DATABASE = ("proyec"
            "to_1daw")

def conexion():
    """
    Esta función establece una conexión a la base de datos SQLite.
    """
    import sqlite3
    try:
        cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=database)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Base de datos no encontrada")
        else:
            print(err)

def cerrar(cnx):
    """
    Esta función cierra la conexión a la base de datos SQLite.
    """
    cnx.close()



