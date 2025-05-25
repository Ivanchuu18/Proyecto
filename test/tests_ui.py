import unittest
from unittest.mock import patch, MagicMock
from Proyecto.ui.Menu_gestion_listado import Menu_gestion_listado
from Proyecto.ui.Menu_preservar_datos import Menu_exportar
from Proyecto.ui.Menu_Principal import Menu_principal
from Proyecto.ui.Menu_gestion_alumnos import Menu_gestion_alumnos

class TestMenuGestionListado(unittest.TestCase):
    def setUp(self):
        self.menu = Menu_gestion_listado()

    def test_instanciacion(self):
        self.assertIsInstance(self.menu, Menu_gestion_listado)

class TestMenuExportarDatos(unittest.TestCase):
    def setUp(self):
        self.menu = Menu_exportar()

    def test_instanciacion(self):
        self.assertIsInstance(self.menu, Menu_exportar)

class TestMenuPrincipal(unittest.TestCase):
    def setUp(self):
        self.menu = Menu_principal()

    def test_instanciacion(self):
        self.assertIsInstance(self.menu, Menu_principal)

class TestMenuGestionAlumnos(unittest.TestCase):
    def setUp(self):
        self.menu = Menu_gestion_alumnos()

    def test_instanciacion(self):
        self.assertIsInstance(self.menu, Menu_gestion_alumnos)

if __name__ == '__main__':
    unittest.main()
