import unittest
from src.livro import Livro

class TestLivro(unittest.TestCase):

    def setUp(self):
        #TODO
        pass

    def tearDown(self):
        #TODO
        pass
    
    def testInitLivroValido(self):
        try:
            livro = Livro('1234567891011', 'titulo 1', 'autor')
        except:
            self.fail('Inicialização correta gerou exceção')
    
    def testInitISBN_CaractereInvalido(self):
        with self.assertRaises(Exception):
            livro = Livro('123456789101a', 'titulo', 'autor')
        with self.assertRaises(Exception):
            livro = Livro('123456789101#', 'titulo', 'autor')
    
    def testInitISBN_TamanhoInvalidoMenor(self):
        with self.assertRaises(Exception):
            livro = Livro('123456789101', 'titulo', 'autor')
    
    def testInitISBN_TamanhoInvalidoMaior(self):
        with self.assertRaises(Exception):
            livro = Livro('12345678910111', 'titulo', 'autor')
    
    def testInitTitulo_CaractereInvalido(self):
        with self.assertRaises(Exception):
            livro = Livro('1234567891011', 'titulo@', 'autor')
    
    def testInitTitulo_TamanhoInvalido(self):
        with self.assertRaises(Exception):
            livro = Livro('1234567891011', 'A vida de Pedro de Alcântara Francisco Antônio João', 'autor')
    
    def testInitAutor_CaractereInvalido(self):
        with self.assertRaises(Exception):
            livro = Livro('1234567891011', 'titulo', 'aut0r')
        with self.assertRaises(Exception):
            livro = Livro('1234567891011', 'titulo', '@utor')
    
    def testInitAutor_TamanhoInvalido(self):
        with self.assertRaises(Exception):
            livro = Livro('1234567891011', 'titulo', 'Pedro de Alcântara Francisco Antônio João Carlos II')
    
    def testGetISBN(self):
        livro = Livro('1234567891011', 'titulo 1', 'autor')
        self.assertEqual('1234567891011', livro.getISBN())
    
    def testGetTitulo(self):
        livro = Livro('1234567891011', 'titulo 1', 'autor')
        self.assertEqual('titulo 1', livro.getTitulo())
    
    def testGetAutor(self):
        livro = Livro('1234567891011', 'titulo 1', 'autor')
        self.assertEqual('autor', livro.getAutor())

    def testSetTitulo(self):
        livro = Livro('1234567891011', 'titulo 1', 'autor')
        livro.setTitulo('titulo')
        self.assertEqual('titulo', livro.getTitulo())

    def testSetAutor(self):
        livro = Livro('1234567891011', 'titulo 1', 'autor')
        livro.setAutor('autora')
        self.assertEqual('autora', livro.getAutor())
