class Curso:
    def __init__(self, curso, grupo):
        self._curso = curso
        self._grupo = grupo

    def __str__(self):
        return f"Curso: {self._curso}, Nivel: {self._grupo}"

