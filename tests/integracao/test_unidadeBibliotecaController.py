from models.unidadeBiblioteca import db_unidadeBiblioteca, UnidadeBiblioteca
from models.livroBiblioteca import db_livroBiblioteca, LivroBiblioteca
import livroBibliotecaController
import unidadeBibliotecaController
from app import app
import unittest


class TestUnidadeBibliotecaController(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db_unidadeBiblioteca.init_app(app)
            unidadeBibliotecaController.criarUnidadeBiblioteca(1, 'Rua A, 1')

    def tearDown(self):
        with app.app_context():
            unidadeBibliotecaController.deletarUnidadeBiblioteca(1)   

    def testBibliotecaInseridaBD(self):
        with app.app_context():
            biblioteca = UnidadeBiblioteca.query.filter_by(unidadeID=1).first()
            self.assertEqual(biblioteca.getUnidadeID(), 1)
            self.assertEqual(biblioteca.getEndereco(), 'Rua A, 1')

    def testMudarParametrosBiblioteca(self):
        with app.app_context():
            unidadeBibliotecaController.setNovosParametrosBiblioteca(1, 2, 'Rua B, 2')
            biblioteca = UnidadeBiblioteca.query.filter_by(unidadeID=2).first()
            self.assertEqual(biblioteca.getUnidadeID(), 2)
            self.assertEqual(biblioteca.getEndereco(), 'Rua B, 2')
            unidadeBibliotecaController.setNovosParametrosBiblioteca(2, 1)

    def testTransferirLivroUnidade(self):
        with app.app_context():
            unidadeBibliotecaController.criarUnidadeBiblioteca(2, 'Rua B, 2')
            db_livroBiblioteca.init_app(app)
            livroBibliotecaController.criarLivroBiblioteca(1, 1111111111111, 20)

            unidadeBibliotecaController.transferirLivroUnidade(1, 2, 1111111111111, 10)
            livro1 = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            livro2 = LivroBiblioteca.query.filter_by(unidadeID=2, ISBN=1111111111111).first()
            self.assertEqual(livro1.getCopiasDisponiveis(), 10)
            self.assertEqual(livro2.getCopiasDisponiveis(), 10)

            unidadeBibliotecaController.deletarUnidadeBiblioteca(2)
            livroBibliotecaController.deletarLivroBiblioteca(1, 1111111111111)
            livroBibliotecaController.deletarLivroBiblioteca(2, 1111111111111)   

    def testComprarLivrosUnidade(self):
        with app.app_context():
            db_livroBiblioteca.init_app(app)

            unidadeBibliotecaController.comprarLivrosUnidade(1, 1111111111111, 20)

            livro = LivroBiblioteca.query.filter_by(unidadeID=1, ISBN=1111111111111).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 20)

            livroBibliotecaController.deletarLivroBiblioteca(1, 1111111111111) 