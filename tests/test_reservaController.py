from models.reserva import db_reserva, Reserva
import reservaController
from app import app
import unittest


class TestReservaController(unittest.TestCase):
    def setUp(self):
        reserva = Reserva(1, 1111111111111, 22222222222)
        with app.app_context():
            db_reserva.init_app(app)
            db_reserva.session.add(reserva)
            db_reserva.session.commit()
           
    def testReservaInseridaBD(self):
        with app.app_context():
            newReserva = Reserva.query.filter_by(unidadeID=1, ISBN=1111111111111, CPF=22222222222).first()
            self.assertEqual(newReserva.getUnidadeID(), 1)
            self.assertEqual(newReserva.getISBN(), 1111111111111)
            self.assertEqual(newReserva.getCPF(), 22222222222)

    def testMudarDisponibilidade(self):
        with app.app_context():
            newReserva = Reserva.query.filter_by(unidadeID=1, ISBN=1111111111111, CPF=22222222222).first()
            self.assertFalse(newReserva.getDisponivel())
            reservaController.mudarDisponibilidade(1, 1111111111111)
            newReserva2 = Reserva.query.filter_by(unidadeID=1, ISBN=1111111111111, CPF=22222222222).first()
            self.assertTrue(newReserva2.getDisponivel())

    def testMudarParametrosReserva(self):
        with app.app_context():
            reservaController.setNovosParametrosReserva(1, 1111111111111, 22222222222, 3, 4444444444444, 55555555555)
            newReserva = Reserva.query.filter_by(unidadeID=3, ISBN=4444444444444, CPF=55555555555).first()
            self.assertEqual(newReserva.getUnidadeID(), 3)
            self.assertEqual(newReserva.getISBN(), 4444444444444)
            self.assertEqual(newReserva.getCPF(), 55555555555)
            reservaController.setNovosParametrosReserva(3, 4444444444444, 55555555555, 1, 1111111111111, 22222222222)

    def tearDown(self):
        with app.app_context():
            newReserva = Reserva.query.filter_by(unidadeID=1, ISBN=1111111111111, CPF=22222222222).first()
            db_reserva.session.delete(newReserva)
            db_reserva.session.commit()
    