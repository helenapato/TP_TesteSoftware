import unittest

from models.usuario import Usuario

TAM_MAX_NOME = 50

class TestUsuario(unittest.TestCase):

    def testInitUsuarioValido(self):
        try:
            usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        except:
            self.fail('CEP correto inserido gerou exceção')

    def testInitCPF_CaractereInvalido(self):
        with self.assertRaises(Exception):
            usuario = Usuario('a1234567890', 'joao', 'joao@exemplo.com')
        with self.assertRaises(Exception):
            usuario = Usuario('#1234567890', 'joao', 'joao@exemplo.com')

    def testInitCPF_TamanhoInvalidoMenor(self):
        with self.assertRaises(Exception):
            usuario = Usuario('1234567890', 'joao', 'joao@exemplo.com')

    def testInitCPF_TamanhoInvalidoMaior(self):
        with self.assertRaises(Exception):
            usuario = Usuario('012345678901', 'joao', 'joao@exemplo.com')

    
    def testInitNome_CaractereInvalido(self):
        with self.assertRaises(Exception):
            usuario = Usuario('01234567890', 'joao1', 'joao@exemplo.com')
        with self.assertRaises(Exception):
            usuario = Usuario('01234567890', 'joao#', 'joao@exemplo.com')

    def testInitNome_LimiteTamanhoValido(self):
        try:
            usuario = Usuario('01234567890', 'Pedro de Alcântara Francisco Antônio João Carlos X', 'pedro@exemplo.com')
        except:
            self.fail('Nome com', TAM_MAX_NOME, 'caracteres gerou exceção')

    def testInitNome_LimiteTamanhoInvalido(self):
        with self.assertRaises(Exception):
            usuario = Usuario('01234567890', 'Pedro de Alcântara Francisco Antônio João Carlos Xa', 'pedro@exemplo.com')

    
    def testInitEmailInvalido(self):
        with self.assertRaises(Exception):
            usuario = Usuario('01234567890', 'joao', 'joaoexemplo.com')


    def testGetCPF(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        self.assertEqual('01234567890', usuario.getCPF())
        
    def testGetNome(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        self.assertEqual('joao', usuario.getNome())

    def testGetEmail(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        self.assertEqual('joao@exemplo.com', usuario.getEmail())


    def testSetNomeCorreto(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        usuario.setNome('joao lucas')
        self.assertEqual('joao lucas', usuario.getNome())

    def testSetNomeCaractereInvalido(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        usuario.setNome('joao#')
        self.assertEqual('joao', usuario.getNome())    
        usuario.setNome('joao1')
        self.assertEqual('joao', usuario.getNome())

    def testSetNomeLimiteTamanhoValido(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        usuario.setNome('Pedro de Alcântara Francisco Antônio João Carlos X')
        self.assertEqual('Pedro de Alcântara Francisco Antônio João Carlos X', usuario.getNome())

    def testSetNomeLimiteTamanhoInvalido(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        usuario.setNome('Pedro de Alcântara Francisco Antônio João Carlos Xa')
        self.assertEqual('joao', usuario.getNome())


    def testSetEmailValido(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        usuario.setEmail('joaolucas@exemplo.com')
        self.assertEqual('joaolucas@exemplo.com', usuario.getEmail())

    def testSetEmailInvalido(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        usuario.setEmail('joaoexemplo.com')
        self.assertEqual('joao@exemplo.com', usuario.getEmail())