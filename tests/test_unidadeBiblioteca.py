import unittest

from src.unidadeBiblioteca import UnidadeBiblioteca
from src.livroBiblioteca import LivroBiblioteca

class TestUnidadeBiblioteca(unittest.TestCase):

    def setUp(self):
        livro1 = LivroBiblioteca(1, 3, 4)
        livro2 = LivroBiblioteca(2, 0, 5, ['12345678900'])
        livro3 = LivroBiblioteca(3, 6, 0)
        livros = {1 : livro1,
                  2 : livro2,
                  3 : livro3}
        self.unidadeBiblioteca = UnidadeBiblioteca('123', 'Rua A, 1', livros)


    def testGetUnidadeID(self):
        self.assertEqual('123', self.unidadeBiblioteca.getUnidadeID())

    def testGetEndereco(self):
        self.assertEqual('Rua A, 1', self.unidadeBiblioteca.getEndereco())
    
    def testGetLivros(self):    
        self.assertEqual(self.unidadeBiblioteca.livros, self.unidadeBiblioteca.getLivros())

    def testGetCopiasDisponiveisLivroExiste(self):
        self.assertEqual(3, self.unidadeBiblioteca.getCopiasDisponiveisLivro(1))
        self.assertEqual(0, self.unidadeBiblioteca.getCopiasDisponiveisLivro(2))

    def testGetCopiasDisponiveisLivroNaoExiste(self):
        self.assertEqual(0, self.unidadeBiblioteca.getCopiasDisponiveisLivro(4))

    def testGetCopiasEmprestadasLivroExiste(self):
        self.assertEqual(5, self.unidadeBiblioteca.getCopiasEmprestadasLivro(2))
        self.assertEqual(0, self.unidadeBiblioteca.getCopiasEmprestadasLivro(3))

    def testGetCopiasEmprestadasLivroNaoExiste(self):
        self.assertEqual(-1, self.unidadeBiblioteca.getCopiasEmprestadasLivro(4))

    def testSetLivros(self):
        livros = {4 : LivroBiblioteca(4, 2, 7)}
        self.unidadeBiblioteca.setLivros(livros)
        self.assertEqual(livros, self.unidadeBiblioteca.getLivros())


    def testLivroExisteUnidade(self):
        self.assertTrue(self.unidadeBiblioteca.livroExisteUnidade(1))
        
    def testLivroNaoExisteUnidade(self):
        self.assertFalse(self.unidadeBiblioteca.livroExisteUnidade(4))

    def testAdquirirLivroNovo(self):
        self.unidadeBiblioteca.adquirirLivro(4, 20)
        self.assertEqual(20, self.unidadeBiblioteca.getCopiasDisponiveisLivro(4))
        self.assertEqual(0, self.unidadeBiblioteca.getCopiasEmprestadasLivro(4))

    def testAdquirirLivroExistente(self):
        self.unidadeBiblioteca.adquirirLivro(1, 20)
        self.assertEqual(23, self.unidadeBiblioteca.getCopiasDisponiveisLivro(1))
        self.assertEqual(4, self.unidadeBiblioteca.getCopiasEmprestadasLivro(1))    

    def testLivroFoiEmprestado(self):
        self.unidadeBiblioteca.livroFoiEmprestado(1)
        self.assertEqual(2, self.unidadeBiblioteca.getCopiasDisponiveisLivro(1))
        self.assertEqual(5, self.unidadeBiblioteca.getCopiasEmprestadasLivro(1))

    def testLivroFoiDevolvido(self):
        self.unidadeBiblioteca.livroFoiDevolvido(1)
        self.assertEqual(4, self.unidadeBiblioteca.getCopiasDisponiveisLivro(1))
        self.assertEqual(3, self.unidadeBiblioteca.getCopiasEmprestadasLivro(1))

    def testChecaLivroDisponivelNaoExiste(self):
        self.assertFalse(self.unidadeBiblioteca.checaLivroDisponivel(4))

    def testChecaLivroEstaDisponivel(self):
        self.assertTrue(self.unidadeBiblioteca.checaLivroDisponivel(1))

    def testChecaLivroNaoDisponivel(self):
        self.assertFalse(self.unidadeBiblioteca.checaLivroDisponivel(2))

    def testListaLivrosDisponiveis(self):
        self.assertEqual([1, 3], self.unidadeBiblioteca.listaLivrosDisponiveis())

    def testListaLivrosDisponiveisVazio(self):
        self.unidadeBiblioteca.setLivros({})
        self.assertEqual([], self.unidadeBiblioteca.listaLivrosDisponiveis())
<<<<<<< HEAD


    def testTransferirLivroNaoExisteUnidade(self):
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {})
        with self.assertRaises(Exception):
            self.unidadeBiblioteca.transferirLivroUnidade(4, unidade, 20)

    def testTransferirLivrosDemaisUnidade(self):
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {})
        with self.assertRaises(Exception):
            self.unidadeBiblioteca.transferirLivroUnidade(1, unidade, 8)

    def testTransferirLivrosIndisponiveisUnidade(self):
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {})
        with self.assertRaises(Exception):
            self.unidadeBiblioteca.transferirLivroUnidade(1, unidade, 5)

    def testTransferirLivrosDisponiveisUnidade(self):
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {})
        self.unidadeBiblioteca.transferirLivroUnidade(1, unidade, 2)
        self.assertEqual(2, unidade.getCopiasDisponiveisLivro(1))
=======
>>>>>>> 0431a7c6e928653174ff45f9d013d2d1f74c3ad0
