import unittest

from src.unidadeBiblioteca import UnidadeBiblioteca

class TestUnidadeBiblioteca(unittest.TestCase):

    def setUp(self):
        livros = {1 : [3, 4],
                  2 : [0, 5],
                  3 : [6, 0]}
        self.unidadeBiblioteca = UnidadeBiblioteca('123', 'Rua A, 1', livros)


    def testGetUnidadeID(self):
        self.assertEqual('123', self.unidadeBiblioteca.getUnidadeID())

    def testGetEndereco(self):
        self.assertEqual('Rua A, 1', self.unidadeBiblioteca.getEndereco())
    
    def testGetLivros(self):
        livros = {1 : [3, 4],
                  2 : [0, 5],
                  3 : [6, 0]}        
        self.assertEqual(livros, self.unidadeBiblioteca.getLivros())

    def testGetCopiasDisponiveisLivroExiste(self):
        self.assertEqual(3, self.unidadeBiblioteca.getCopiasDisponiveisLivro(1))
        self.assertEqual(0, self.unidadeBiblioteca.getCopiasDisponiveisLivro(2))

    def testGetCopiasDisponiveisLivroNaoExiste(self):
        self.assertEqual(0, self.unidadeBiblioteca.getCopiasDisponiveisLivro(4))

    def testGetCopiasAlugadasLivroExiste(self):
        self.assertEqual(5, self.unidadeBiblioteca.getCopiasAlugadasLivro(2))
        self.assertEqual(0, self.unidadeBiblioteca.getCopiasAlugadasLivro(3))

    def testGetCopiasAlugadasLivroNaoExiste(self):
        self.assertEqual(-1, self.unidadeBiblioteca.getCopiasAlugadasLivro(4))

    def testSetLivros(self):
        livros = {4 : [2, 7]}
        self.unidadeBiblioteca.setLivros(livros)
        self.assertEqual(livros, self.unidadeBiblioteca.getLivros())


    def testLivroExisteUnidade(self):
        self.assertTrue(self.unidadeBiblioteca.livroExisteUnidade(1))
        
    def testLivroNaoExisteUnidade(self):
        self.assertFalse(self.unidadeBiblioteca.livroExisteUnidade(4))

    def testAdquirirLivroNovo(self):
        self.unidadeBiblioteca.adquirirLivro(4, 20)
        self.assertEqual(20, self.unidadeBiblioteca.getCopiasDisponiveisLivro(4))
        self.assertEqual(0, self.unidadeBiblioteca.getCopiasAlugadasLivro(4))

    def testAdquirirLivroExistente(self):
        self.unidadeBiblioteca.adquirirLivro(1, 20)
        self.assertEqual(23, self.unidadeBiblioteca.getCopiasDisponiveisLivro(1))
        self.assertEqual(4, self.unidadeBiblioteca.getCopiasAlugadasLivro(1))    

    def testAtualizaContagemLivroAlugado(self):
        self.unidadeBiblioteca.atualizaContagemLivroAlugado(1)
        self.assertEqual(2, self.unidadeBiblioteca.getCopiasDisponiveisLivro(1))
        self.assertEqual(5, self.unidadeBiblioteca.getCopiasAlugadasLivro(1))

    def testAtualizaContagemLivroDevolvido(self):
        self.unidadeBiblioteca.atualizaContagemLivroDevolvido(1)
        self.assertEqual(4, self.unidadeBiblioteca.getCopiasDisponiveisLivro(1))
        self.assertEqual(3, self.unidadeBiblioteca.getCopiasAlugadasLivro(1))

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
