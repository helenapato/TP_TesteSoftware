import unittest
from models.livro import db_livro, Livro
import livroController
from app import app

class TestLivroController(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db_livro.init_app(app)
            livroController.criarLivro(1111111111111, 'livro', 'autor')
            
    def tearDown(self):
        with app.app_context():
            livroController.deletarLivro(1111111111111)
           
    def testLivroInseridoBD(self):
        with app.app_context():
            livro = Livro.query.filter_by(ISBN=1111111111111).first()
            self.assertEqual(livro.getISBN(), 1111111111111)
            self.assertEqual(livro.getTitulo(), 'livro')
            self.assertEqual(livro.getAutor(), 'autor')

    def testMudarParametrosLivro(self):
        with app.app_context():
            livroController.setNovosParametrosLivro(1111111111111, 2222222222222, 'livro2', 'autorV')
            livro = Livro.query.filter_by(ISBN=2222222222222).first()
            self.assertEqual(livro.getISBN(), 2222222222222)
            self.assertEqual(livro.getTitulo(), 'livro2')
            self.assertEqual(livro.getAutor(), 'autorV')
            livroController.setNovosParametrosLivro(2222222222222, 1111111111111)
