from models.unidadeBiblioteca import db_unidadeBiblioteca
from models.livroBiblioteca import db_livroBiblioteca, LivroBiblioteca
from models.emprestimo import db_emprestimo, Emprestimo
from models.reserva import db_reserva, Reserva

import emprestimoController
import livroBibliotecaController
import unidadeBibliotecaController
import usuarioController
import reservaController

from models.usuario import db_usuario, Usuario
from app import app
import unittest


class TestUsuarioController(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db_usuario.init_app(app)
            usuarioController.criarUsuario(11111111111, 'joao', 'joao@exemplo.com')

    def tearDown(self):
        with app.app_context():
            usuarioController.deletarUsuario(11111111111)   

    def testUsuarioInseridoBD(self):
        with app.app_context():
            usuario = Usuario.query.filter_by(CPF=11111111111).first()
            self.assertEqual(usuario.getCPF(), 11111111111)
            self.assertEqual(usuario.getNome(), 'joao')
            self.assertEqual(usuario.getEmail(), 'joao@exemplo.com')

    def testMudarParametrosUsuario(self):
        with app.app_context():
            usuarioController.setNovosParametrosUsuario(11111111111, 22222222222, 'joao silva', 'joao_silva@exemplo.com')
            usuario = Usuario.query.filter_by(CPF=22222222222).first()
            self.assertEqual(usuario.getCPF(), 22222222222)
            self.assertEqual(usuario.getNome(), 'joao silva')
            self.assertEqual(usuario.getEmail(), 'joao_silva@exemplo.com')            
            usuarioController.setNovosParametrosUsuario(22222222222, 11111111111)

    def testEmprestarLivroUnidade(self):
        with app.app_context():
            db_unidadeBiblioteca.init_app(app)
            unidadeBibliotecaController.criarUnidadeBiblioteca(2, 'Rua A, 1')
            db_livroBiblioteca.init_app(app)
            livroBibliotecaController.criarLivroBiblioteca(2, 3333333333333, 20)
            db_emprestimo.init_app(app)

            usuarioController.emprestarLivroUnidadeBiblioteca(11111111111, 2, 3333333333333)

            emprestimo = Emprestimo.query.filter_by(CPF=11111111111, unidadeID=2, ISBN=3333333333333).first()
            self.assertEqual(emprestimo.getISBN(), 3333333333333)
            self.assertEqual(emprestimo.getCPF(), 11111111111)
            self.assertEqual(emprestimo.getUnidadeID(), 2)

            livro = LivroBiblioteca.query.filter_by(unidadeID=2, ISBN=3333333333333).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 19)

            unidadeBibliotecaController.deletarUnidadeBiblioteca(2)
            livroBibliotecaController.deletarLivroBiblioteca(2, 3333333333333)   
            emprestimoController.deletarEmprestimo(3333333333333, 11111111111, 2)

    def testDevolverLivroUnidade(self):
        with app.app_context():
            db_unidadeBiblioteca.init_app(app)
            unidadeBibliotecaController.criarUnidadeBiblioteca(2, 'Rua A, 1')
            db_livroBiblioteca.init_app(app)
            livroBibliotecaController.criarLivroBiblioteca(2, 3333333333333, 20)
            db_emprestimo.init_app(app)

            usuarioController.emprestarLivroUnidadeBiblioteca(11111111111, 2, 3333333333333)
            usuarioController.devolverLivroUnidadeBiblioteca(11111111111, 2, 3333333333333)

            emprestimo = Emprestimo.query.filter_by(CPF=11111111111, unidadeID=2, ISBN=3333333333333).first()
            self.assertIsNone(emprestimo)
            
            livro = LivroBiblioteca.query.filter_by(unidadeID=2, ISBN=3333333333333).first()
            self.assertEqual(livro.getCopiasDisponiveis(), 20)

            unidadeBibliotecaController.deletarUnidadeBiblioteca(2)
            livroBibliotecaController.deletarLivroBiblioteca(2, 3333333333333)

    def testReservarLivroUnidade(self):
        with app.app_context():
            db_unidadeBiblioteca.init_app(app)
            unidadeBibliotecaController.criarUnidadeBiblioteca(2, 'Rua A, 1')
            db_livroBiblioteca.init_app(app)
            livroBibliotecaController.criarLivroBiblioteca(2, 3333333333333, 0, 20)
            db_reserva.init_app(app)

            usuarioController.reservarLivroUnidadeBiblioteca(11111111111, 2, 3333333333333)

            reserva = Reserva.query.filter_by(CPF=11111111111, unidadeID=2, ISBN=3333333333333).first()
            self.assertEqual(reserva.getUnidadeID(), 2)
            self.assertEqual(reserva.getISBN(), 3333333333333)
            self.assertEqual(reserva.getCPF(), 11111111111)

            unidadeBibliotecaController.deletarUnidadeBiblioteca(2)
            livroBibliotecaController.deletarLivroBiblioteca(2, 3333333333333)   
            reservaController.deletarReserva(2, 3333333333333, 11111111111)         