import unittest

from models.reserva import Reserva

class TestReserva(unittest.TestCase):

    def setUp(self):
        self.reserva = Reserva(0, 1111111111111, 22222222222)

    def testInitExceptISBN(self):
        with self.assertRaises(Exception):
            reserva1 = Reserva(0, 1, 22222222222)

    def testInitExceptCPF(self):
        with self.assertRaises(Exception):
            reserva1 = Reserva(0, 1111111111111, 2)

    def testGetUnidadeID(self):
        self.assertEqual(0, self.reserva.getUnidadeID())

    def testGetISBN(self):
        self.assertEqual(1111111111111, self.reserva.getISBN())

    def testGetCPF(self):
        self.assertEqual(22222222222, self.reserva.getCPF())

    def testGeDisponivel(self):
        self.assertFalse(self.reserva.getDisponivel())

    def testSetUnidadeID(self):
        self.reserva.setUnidadeID(1)
        self.assertEqual(1, self.reserva.getUnidadeID())

    def testSetISBN(self):
        self.reserva.setISBN(2222222222222)
        self.assertEqual(2222222222222, self.reserva.getISBN())

    def testNotSetISBN(self):
        self.reserva.setISBN(2)
        self.assertEqual(1111111111111, self.reserva.getISBN())

    def testSetCPF(self):
        self.reserva.setCPF(33333333333)
        self.assertEqual(33333333333, self.reserva.getCPF())

    def testNotSetCPF(self):
        self.reserva.setCPF(3)
        self.assertEqual(22222222222, self.reserva.getCPF())

    def testSeDisponivel(self):
        self.reserva.setDisponivel()
        self.assertTrue(self.reserva.getDisponivel())