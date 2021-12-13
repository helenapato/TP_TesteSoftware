from models.reserva import db_reserva, Reserva
import reservaController
from app import app
import unittest


class TestReservaController(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db_reserva.init_app(app)
            reservaController.criarReserva(1, 1111111111111, 22222222222)
            
    def tearDown(self):
        with app.app_context():
            reservaController.deletarReserva(1, 1111111111111, 22222222222)
           
    def testReservaInseridaBD(self):
        with app.app_context():
            reserva = Reserva.query.filter_by(unidadeID=1, ISBN=1111111111111, CPF=22222222222).first()
            self.assertEqual(reserva.getUnidadeID(), 1)
            self.assertEqual(reserva.getISBN(), 1111111111111)
            self.assertEqual(reserva.getCPF(), 22222222222)

    def testMudarDisponibilidade(self):
        with app.app_context():
            reserva = Reserva.query.filter_by(unidadeID=1, ISBN=1111111111111, CPF=22222222222).first()
            self.assertFalse(reserva.getDisponivel())
            reservaController.mudarDisponibilidade(1, 1111111111111)
            reserva2 = Reserva.query.filter_by(unidadeID=1, ISBN=1111111111111, CPF=22222222222).first()
            self.assertTrue(reserva2.getDisponivel())

    def testMudarParametrosReserva(self):
        with app.app_context():
            reservaController.setNovosParametrosReserva(1, 1111111111111, 22222222222, 3, 4444444444444, 55555555555)
            reserva = Reserva.query.filter_by(unidadeID=3, ISBN=4444444444444, CPF=55555555555).first()
            self.assertEqual(reserva.getUnidadeID(), 3)
            self.assertEqual(reserva.getISBN(), 4444444444444)
            self.assertEqual(reserva.getCPF(), 55555555555)
            reservaController.setNovosParametrosReserva(3, 4444444444444, 55555555555, 1, 1111111111111, 22222222222)
