import unittest
from flask import current_app
from models.livro import db, Livro
from app import app

class Teste_livroBD(unittest.TestCase):
    def setUp(self):
        livro = Livro(1111111111111, 'titulo teste', 'autor teste')
        with app.app_context():
            db.init_app(app)
            db.session.add(livro)
            db.session.commit()
           
        
    def testa_busca_livroBD(self):
        with app.app_context():
            new_livro = Livro.query.filter_by(ISBN=1111111111111).first()
            self.assertEqual(new_livro.getISBN(), 1111111111111)
            self.assertEqual(new_livro.getTitulo(), 'titulo teste')
            self.assertEqual(new_livro.getAutor(), 'autor teste')


    def tearDown(self):
        with app.app_context():
            new_livro = Livro.query.filter_by(ISBN=1111111111111).first()
            db.session.delete(new_livro)
            db.session.commit()
    