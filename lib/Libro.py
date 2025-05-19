class Libro:
    def __init__(self, isbn, autor, titulo, numero_ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.numero_ejemplares = numero_ejemplares


    def __str__(self):
        return f"ISBN: {self.isbn}, Titulo: {self.titulo}, Autor: {self.autor}, Numero de ejemplares: {self.numero_ejemplares}"

