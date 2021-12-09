import unittest

from models.livroBiblioteca import LivroBiblioteca

class TestLivroBiblioteca(unittest.TestCase):

    def setUp(self):
        self.livroBiblioteca = LivroBiblioteca(1, 1111111111111, 20)

    def testInitExceptISBN(self):
        with self.assertRaises(Exception):
            livro1 = LivroBiblioteca(1, 1, 20)

    def testGetUnidadeID(self):
        self.assertEqual(1, self.livroBiblioteca.getUnidadeID())

    def testGetISBN(self):
        self.assertEqual(1111111111111, self.livroBiblioteca.getISBN())

    def testGetCopiasDisponiveis(self):
        self.assertEqual(20, self.livroBiblioteca.getCopiasDisponiveis())

    def testGetCopiasEmprestadas(self):
        self.assertEqual(0, self.livroBiblioteca.getCopiasEmprestadas())

    def testGetCopiasTotal(self):
        self.assertEqual(20, self.livroBiblioteca.getCopiasTotal())

    def testSetUnidadeID(self):
        self.livroBiblioteca.setUnidadeID(2)
        self.assertEqual(2, self.livroBiblioteca.getUnidadeID())

    def testSetISBN(self):
        self.livroBiblioteca.setISBN(2222222222222)
        self.assertEqual(2222222222222, self.livroBiblioteca.getISBN())

    def testNotSetISBN(self):
        self.livroBiblioteca.setISBN(2)
        self.assertEqual(1111111111111, self.livroBiblioteca.getISBN())

    def testSetCopiasDisponiveis(self):
        self.livroBiblioteca.setCopiasDisponiveis(50)
        self.assertEqual(50, self.livroBiblioteca.getCopiasDisponiveis())

    def testSetCopiasEmprestadas(self):
        self.livroBiblioteca.setCopiasEmprestadas(30)
        self.assertEqual(30, self.livroBiblioteca.getCopiasEmprestadas())

    def testAdquirirLivros(self):
        self.livroBiblioteca.adquirirLivros(5)
        self.assertEqual(25, self.livroBiblioteca.getCopiasDisponiveis())

    def testDoarLivros(self):
        self.assertTrue(self.livroBiblioteca.doarLivros(20))
        self.assertEqual(0, self.livroBiblioteca.getCopiasDisponiveis())

    def testDoarLivrosDemais(self):
        self.assertFalse(self.livroBiblioteca.doarLivros(21))
        self.assertEqual(20, self.livroBiblioteca.getCopiasDisponiveis())

    def testLivroFoiEmprestado(self):
        self.livroBiblioteca.livroFoiEmprestado()
        self.assertEqual(19, self.livroBiblioteca.getCopiasDisponiveis())
        self.assertEqual(1, self.livroBiblioteca.getCopiasEmprestadas())

    def testLivroNaoFoiEmprestado(self):
        self.livroBiblioteca.setCopiasDisponiveis(0)
        self.assertFalse(self.livroBiblioteca.livroFoiEmprestado())
        self.assertEqual(0, self.livroBiblioteca.getCopiasDisponiveis())

    def testLivroNaoFoiDevolvido(self):
        self.assertFalse(self.livroBiblioteca.livroFoiDevolvido())
        self.assertEqual(0, self.livroBiblioteca.getCopiasEmprestadas())

    def testLivroFoiDevolvido(self):
        self.livroBiblioteca.setCopiasEmprestadas(1)
        self.assertTrue(self.livroBiblioteca.livroFoiDevolvido())
        self.assertEqual(21, self.livroBiblioteca.getCopiasDisponiveis())
