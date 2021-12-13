import unittest

from models.unidadeBiblioteca import UnidadeBiblioteca

class TestUnidadeBiblioteca(unittest.TestCase):

    def setUp(self):
        self.unidadeBiblioteca = UnidadeBiblioteca(123, 'Rua A, 1')

    def testGetUnidadeID(self):
        self.assertEqual(123, self.unidadeBiblioteca.getUnidadeID())

    def testGetEndereco(self):
        self.assertEqual('Rua A, 1', self.unidadeBiblioteca.getEndereco())

    def testSetUnidadeID(self):
        self.unidadeBiblioteca.setUnidadeID(321)
        self.assertEqual(321, self.unidadeBiblioteca.getUnidadeID())

    def testSetEndereco(self):
        self.unidadeBiblioteca.setEndereco('Rua B, 2')
        self.assertEqual('Rua B, 2', self.unidadeBiblioteca.getEndereco())
    
    