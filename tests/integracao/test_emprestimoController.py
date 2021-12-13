from models.emprestimo import db_emprestimo, Emprestimo
import emprestimoController
from app import app
import unittest
from datetime import datetime

class TestEmprestimoController(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db_emprestimo.init_app(app)
            emprestimoController.criarEmprestimo(1111111111111, 22222222222, 3, datetime.now())
            
    def tearDown(self):
        with app.app_context():
            emprestimoController.deletarEmprestimo(1111111111111, 22222222222, 3)
           
    def testEmprestimoInseridoBD(self):
        with app.app_context():
            emprestimo = Emprestimo.query.filter_by(unidadeID=3, ISBN=1111111111111, CPF=22222222222).first()
            self.assertEqual(emprestimo.getISBN(), 1111111111111)
            self.assertEqual(emprestimo.getCPF(), 22222222222)
            self.assertEqual(emprestimo.getUnidadeID(), 3)

    def testSetDataDevolucaoReal(self):
        with app.app_context():
            emprestimo = Emprestimo.query.filter_by(unidadeID=3, ISBN=1111111111111, CPF=22222222222).first()
            self.assertIsNone(emprestimo.getDataDevolucaoReal())
            emprestimoController.setDataDevolucaoReal(1111111111111, 22222222222, 3, datetime.now().date())
            emprestimo2 = Emprestimo.query.filter_by(unidadeID=3, ISBN=1111111111111, CPF=22222222222).first()
            self.assertEqual(emprestimo2.getDataDevolucaoReal(), datetime.now().date())