class Materia:
    def __init__(self, id, nombre, departamento):
        self._id = id
        self._nombre = nombre
        self._departamento = departamento


    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Departamento: {self._departamento}"