from datetime import date
import unittest

from src.unidadeBiblioteca import UnidadeBiblioteca
from src.livroBiblioteca import LivroBiblioteca
from src.emprestimo import Emprestimo
from src.usuario import Usuario

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

    def testReservarLivroUnidadeSucesso(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {1 : LivroBiblioteca(1, 0, 4)})
        try:
            usuario.reservarLivroUnidade(1, unidade)
        except:
            self.fail('Usuário reservando livro correramente gerou exceção')

    def testReservarLivroUnidadeException(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {1 : LivroBiblioteca(1, 0, 4)})
        usuario.reservarLivroUnidade(1, unidade)
        with self.assertRaises(Exception):
            usuario.reservarLivroUnidade(1, unidade)

    def testEmprestarLivroUnidadeSucesso(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {1 : LivroBiblioteca(1, 5, 4)})
        usuario.emprestarLivroUnidade(1, unidade)
        self.assertEqual(1, len(usuario.listaEmprestimos))

    def testEmprestarLivroUnidadeFalha(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {1 : LivroBiblioteca(1, 0, 4)})
        usuario.emprestarLivroUnidade(1, unidade)
        self.assertEqual(0, len(usuario.listaEmprestimos))
        self.assertEqual('01234567890', unidade.livros[1].removeUsuarioReserva())

    def testDevolverLivroUnidade(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {1 : LivroBiblioteca(1, 5, 4)})
        usuario.devolverLivroUnidade(1, unidade)
        self.assertEqual(6, unidade.getCopiasDisponiveisLivro(1))

    def testVerLivrosDisponiveisUnidade(self):
        livro1 = LivroBiblioteca(1, 3, 4)
        livro2 = LivroBiblioteca(2, 0, 5, ['12345678900'])
        livro3 = LivroBiblioteca(3, 6, 0)
        livros = {1 : livro1,
                  2 : livro2,
                  3 : livro3}
        unidade = UnidadeBiblioteca('123', 'Rua A, 1', livros)
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        listaLivros = usuario.verLivrosDisponiveisUnidade(unidade)
        self.assertEqual([1,3], listaLivros)

    def testConsultarDisponibilidadeLivroUnidade(self):
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com')
        unidade = UnidadeBiblioteca('456', 'Rua B, 2', {1 : LivroBiblioteca(1, 5, 4)})
        self.assertTrue(usuario.consultarDisponibilidadeLivroUnidade(1, unidade))
        self.assertFalse(usuario.consultarDisponibilidadeLivroUnidade(2, unidade))

    def testVerMeusLivrosAlugados(self):
        emprestimo1 = Emprestimo(1, '01234567890', 3, date.today())
        emprestimo2 = Emprestimo(2, '01234567890', 3, date.today())
        emprestimos = { 1 : emprestimo1, 
                        2 : emprestimo2 }
        usuario = Usuario('01234567890', 'joao', 'joao@exemplo.com', emprestimos)
        self.assertEqual([1, 2], usuario.verMeusLivrosAlugados())

