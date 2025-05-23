from enum_tramos import Tramos
class Alumno:
    def __init__(self, nombre, apellidos, dni, tramo , bilingue: int):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.tramo= tramo if tramo in Tramos else Tramos.NADA
        self.bilingue = bilingue
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, DNI: {self.dni}, Tramo: {self.tramo}, Bilingue: {self.bilingue}"



