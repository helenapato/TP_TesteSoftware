import unittest

from src.livroBiblioteca import LivroBiblioteca

class TestLivroBiblioteca(unittest.TestCase):

    def testGetISBN(self):
        livro = LivroBiblioteca(1, 20)
        self.assertEqual(1, livro.getISBN())

    def testGetCopiasDisponiveis(self):
        livro = LivroBiblioteca(1, 20)
        self.assertEqual(20, livro.getCopiasDisponiveis())

    def testGetCopiasEmprestadas(self):
        livro = LivroBiblioteca(1, 20, 5)
        self.assertEqual(5, livro.getCopiasEmprestadas())

    def testGetListaReservas(self):
        livro = LivroBiblioteca(1, 20, 5, ['12345678900'])
        self.assertEqual(['12345678900'], livro.getListaReservas())

    def testGetCopiasTotal(self):
        livro = LivroBiblioteca(1, 20, 5)
        self.assertEqual(25, livro.getCopiasTotal())

    def testSetCopiasDisponiveis(self):
        livro = LivroBiblioteca(1, 20)
        livro.setCopiasDisponiveis(50)
        self.assertEqual(50, livro.getCopiasDisponiveis())

    def testSetCopiasEmprestadas(self):
        livro = LivroBiblioteca(1, 20, 5)
        livro.setCopiasEmprestadas(30)
        self.assertEqual(30, livro.getCopiasEmprestadas())

    def testSetListaReservas(self):
        livro = LivroBiblioteca(1, 20, 5, ['12345678900'])
        livro.setListaReservas(['09876543210'])
        self.assertEqual(['09876543210'], livro.getListaReservas())

    def testAdquirirLivros(self):
        livro = LivroBiblioteca(1, 20)
        livro.adquirirLivros(5)
        self.assertEqual(25, livro.getCopiasDisponiveis())

    def testDoarLivrosDemais(self):
        livro = LivroBiblioteca(1, 20, 5)
        with self.assertRaises(Exception):
            livro.doarLivros(26)

    def testDoarLivrosIndisponiveis(self):
        livro = LivroBiblioteca(1, 20, 5)
        with self.assertRaises(Exception):
            livro.doarLivros(25)

    def testDoarLivrosCerto(self):
        livro = LivroBiblioteca(1, 20, 5)
        livro.doarLivros(10)
        self.assertEqual(10, livro.getCopiasDisponiveis())

    def testLivroFoiEmprestado(self):
        livro = LivroBiblioteca(1, 20)
        livro.livroFoiEmprestado()
        self.assertEqual(19, livro.getCopiasDisponiveis())
        self.assertEqual(1, livro.getCopiasEmprestadas())

    def testLivroFoiDevolvido(self):
        livro = LivroBiblioteca(1, 20, 5)
        livro.livroFoiDevolvido()
        self.assertEqual(21, livro.getCopiasDisponiveis())
        self.assertEqual(4, livro.getCopiasEmprestadas())

    def testLivroEstaDisponivel(self):
        livro = LivroBiblioteca(1, 20, 5)
        self.assertTrue(livro.livroEstaDisponivel())

    def testLivroEstaIndisponivel(self):
        livro = LivroBiblioteca(1, 0, 5)
        self.assertFalse(livro.livroEstaDisponivel())

    def testExisteUsuarioReserva(self):
        livro = LivroBiblioteca(1, 20, listaReservas=['12345678900'])
        self.assertTrue(livro.existeUsuarioReserva())

    def testNaoExisteUsuarioReserva(self):
        livro = LivroBiblioteca(1, 20)
        self.assertFalse(livro.existeUsuarioReserva())

    def testReservaUsuario(self):
        livro = LivroBiblioteca(1, 20)
        livro.reservaUsuario('12345678900')
        self.assertEqual(['12345678900'], livro.getListaReservas())

    def testReservaUsuarioDuas(self):
        # TODO
        # Por algum motivo, neste teste apenas, se não especificar a lista vazia, 
        # ele já inicializa com um elemento na lista de reservas
        livro = LivroBiblioteca(1, 20, 0, [])
        livro.reservaUsuario('12345678900')
        with self.assertRaises(Exception):
            livro.reservaUsuario('12345678900')

    def testRemoveUsuarioReserva(self):
        livro = LivroBiblioteca(1, 20, listaReservas=['12345678900'])
        self.assertEqual('12345678900', livro.removeUsuarioReserva())

    def testRemoveUsuarioInexistenteReserva(self):
        livro = LivroBiblioteca(1, 20)
        with self.assertRaises(Exception):
            livro.removeUsuarioReserva('12345678900')