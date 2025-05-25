import unittest
from Proyecto.lib.Gestion_alumnos import GestionAlumnos
from Proyecto.lib.Gestion_preservar_datos import Gestion_preservar_datos
from Proyecto.lib.Gestionar_listado import Gestionar_listado
from Proyecto.lib.Gestionar_prestamos import Gestionar_prestamos
from Proyecto.lib.BBDD import BBDD

class TestGestionAlumnos(unittest.TestCase):
    def setUp(self):
        self.obj = GestionAlumnos()

    def test_validar_dni_valido(self):
        self.assertTrue(self.obj.validar_dni("12345678Z"))

    def test_validar_dni_invalido(self):
        self.assertIsInstance(self.obj.validar_dni("12345678A"), ValueError)

    def test_validar_dni_minusculas_y_espacios(self):
        self.assertTrue(self.obj.validar_dni(" 12345678z "))

    def test_validar_tramo_valido(self):
        self.assertTrue(self.obj.validar_tramo("1"))

    def test_validar_tramo_invalido(self):
        self.assertIsInstance(self.obj.validar_tramo("4"), ValueError)

    def test_validar_tramo_entero(self):
        self.assertIsInstance(self.obj.validar_tramo(1), ValueError)

    def test_bilingue_valido(self):
        self.assertTrue(self.obj.bilingue("0"))

    def test_bilingue_invalido(self):
        self.assertIsInstance(self.obj.bilingue("2"), ValueError)

    def test_bilingue_vacio(self):
        self.assertIsInstance(self.obj.bilingue(""), ValueError)

class TestGestionPreservarDatos(unittest.TestCase):
    def setUp(self):
        self.obj = Gestion_preservar_datos()

    def test_limpiar_comillas_cadena(self):
        self.assertEqual(self.obj.limpiar_comillas('"Hola"'), 'Hola')

    def test_limpiar_comillas_no_cadena(self):
        self.assertEqual(self.obj.limpiar_comillas(123), 123)

    def test_limpiar_comillas_multiples(self):
        self.assertEqual(self.obj.limpiar_comillas('"Hola" "Mundo"'), 'Hola Mundo')

    def test_limpiar_comillas_sin_comillas(self):
        self.assertEqual(self.obj.limpiar_comillas("Hola"), "Hola")

class TestGestionarListado(unittest.TestCase):
    def setUp(self):
        self.obj = Gestionar_listado()

    def test_instanciacion(self):
        self.assertIsInstance(self.obj, Gestionar_listado)

class TestGestionarPrestamos(unittest.TestCase):
    def setUp(self):
        self.obj = Gestionar_prestamos()

    def test_instanciacion(self):
        self.assertIsInstance(self.obj, Gestionar_prestamos)

    def test_tiene_metodo_generar_contrato(self):
        self.assertTrue(hasattr(self.obj, 'generar_contrato'))

class TestBBDD(unittest.TestCase):
    def setUp(self):
        self.obj = BBDD()

    def test_validar_isbn_valido(self):
        self.assertTrue(self.obj.validar_isbn("9780306406157"))

    def test_validar_isbn_invalido(self):
        self.assertIsInstance(self.obj.validar_isbn("9780306406158"), ValueError)

    def test_validar_isbn_letras(self):
        self.assertFalse(self.obj.validar_isbn("ABC1234567890"))

    def test_validar_isbn_corto(self):
        self.assertFalse(self.obj.validar_isbn("1234567"))

    def test_validar_isbn_con_espacios(self):
        self.assertFalse(self.obj.validar_isbn("978 0306406157"))

if __name__ == '__main__':
    unittest.main()