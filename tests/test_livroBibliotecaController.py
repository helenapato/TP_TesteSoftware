from models.livroBiblioteca import db_livroBiblioteca, LivroBiblioteca
from models.reserva import db_reserva, Reserva
import reservaController
import livroBibliotecaController
from app import app
import unittest


class TestLivroBibliotecaController(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db_livroBiblioteca.init_app(app)
            livroBibliotecaController.criarLivroBiblioteca(1, 1111111111111, 20)

    def tearDown(self):
        with app.app_context():
            livroBibliotecaController.deletarLivroBiblioteca(1, 1111111111111)   

    def testLivroInseridoBD(self):
        with app.app_context():
            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            self.assertEqual(livro.getUnidadeID(), 1)
            self.assertEqual(livro.getISBN(), 1111111111111)
            self.assertEqual(livro.getCopiasDisponiveis(), 20)
            self.assertEqual(livro.getCopiasEmprestadas(), 0)

    def testMudarParametrosLivro(self):
        with app.app_context():
            livroBibliotecaController.setNovosParametrosLivroBiblioteca(1, 1111111111111, 2, 2222222222222, 30, 40)
            livro = LivroBiblioteca.query.filter_by(unidadeID=2, ISBN=2222222222222).first()
            self.assertEqual(livro.getUnidadeID(), 2)
            self.assertEqual(livro.getISBN(), 2222222222222)
            self.assertEqual(livro.getCopiasDisponiveis(), 30)
            self.assertEqual(livro.getCopiasEmprestadas(), 40)
            livroBibliotecaController.setNovosParametrosLivroBiblioteca(2, 2222222222222, 1, 1111111111111)

    def testAdquirirLivro(self):
        with app.app_context():
            livroBibliotecaController.adquirirLivros(1, 1111111111111, 10)
            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 30)

    def testAdquirirLivroNovo(self):
        with app.app_context():
            livroBibliotecaController.adquirirLivros(1, 2222222222222, 10)
            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=2222222222222).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 10)
            livroBibliotecaController.deletarLivroBiblioteca(1, 2222222222222)

    def testDoarLivros(self):
        with app.app_context():
            livroBibliotecaController.doarLivros(1, 1111111111111, 10)
            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 10)

    def testDoarLivrosDemais(self):
        with app.app_context():
            retVal = livroBibliotecaController.doarLivros(1, 1111111111111, 21)
            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 20)
            self.assertEqual(retVal, 1)

    def testLivroFoiEmprestado(self):
        with app.app_context():
            livroBibliotecaController.livroFoiEmprestado(1, 1111111111111)
            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 19)
            self.assertEqual(livro.getCopiasEmprestadas(), 1)

    def testLivroInexistenteFoiEmprestado(self):
        with app.app_context():
            retVal = livroBibliotecaController.livroFoiEmprestado(1, 2222222222222)
            self.assertEqual(retVal, 2)

    def testLivroIndisponivelFoiEmprestado(self):
        with app.app_context():
            livroBibliotecaController.setNovosParametrosLivroBiblioteca(1, 1111111111111, novoCopiasDisponiveis=0)
            retVal = livroBibliotecaController.livroFoiEmprestado(1, 1111111111111)
            self.assertEqual(retVal, 1)

    def testLivroFoiDevolvido(self):
        with app.app_context():
            db_reserva.init_app(app)
            reservaController.criarReserva(1, 1111111111111, 22222222222)

            livroBibliotecaController.setNovosParametrosLivroBiblioteca(1, 1111111111111, novoCopiasEmprestadas=1)
            livroBibliotecaController.livroFoiDevolvido(1, 1111111111111)

            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 21)
            self.assertEqual(livro.getCopiasEmprestadas(), 0)

            reserva = Reserva.query.filter_by(unidadeID=1, ISBN=1111111111111, CPF=22222222222).first()
            self.assertTrue(reserva.getDisponivel())
            reservaController.deletarReserva(1, 1111111111111, 22222222222)

    def testLivroIndisponivelFoiDevolvido(self):
        with app.app_context():
            retVal = livroBibliotecaController.livroFoiDevolvido(1, 1111111111111)
            self.assertEqual(1, retVal)
            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 20)
            self.assertEqual(livro.getCopiasEmprestadas(), 0)
