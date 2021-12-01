import unittest
from src.emprestimo import Emprestimo
from datetime import date, timedelta

PERIODO_EMPRESTIMO = 15
VALOR_MULTA = 10

class TestEmprestimo(unittest.TestCase):

    def setUp(self):
        self.today = date.today()
        self.emprestimo = Emprestimo('1234567891011', '12345678900', '1', self.today)
    
    def tearDown(self):
        #TODO
        pass

    def testSetDataDevolucaoRealInvalida(self):
        dataDevolucao = self.today - timedelta(days=1)
        with self.assertRaises(Exception):
            self.emprestimo.setDataDevolucaoReal(dataDevolucao)

    def testGetDataAluguel(self):
        self.assertEqual(self.today, self.emprestimo.getDataAluguel())
    
    def testGetDataDevolucaoPrevista(self):
        self.assertEqual(self.today + timedelta(days = PERIODO_EMPRESTIMO), self.emprestimo.getDataDevolucaoPrevista())

    def testGetDataDevolucaoRealVazia(self):
        self.assertIsNone(self.emprestimo.getDataDevolucaoReal())
    
    def testGetDataDevolucaoPreenchida(self):
        dataDevolucao = self.today
        self.emprestimo.setDataDevolucaoReal(dataDevolucao)
        self.assertEqual(dataDevolucao, self.emprestimo.getDataDevolucaoReal())
    
    def testCalcularMultaSemMulta(self):
        futuro = self.today + timedelta(days = PERIODO_EMPRESTIMO)
        self.assertEqual(0, self.emprestimo.calcularMulta(futuro))
    
    def testCalcularMultaComMulta(self):
        futuro = self.today + timedelta(days = PERIODO_EMPRESTIMO + 3)
        self.assertEqual(3, self.emprestimo.calcularMulta(futuro))
