from datetime import date
from src.emprestimo import Emprestimo
from src.unidadeBiblioteca import UnidadeBiblioteca

TAM_MAX_NOME = 50

class Usuario:

    def __init__(self, CPF, nome, email, listaEmprestimos=None):

        self.checaValidadeParametrosUsuario(CPF, nome, email)

        self.CPF = CPF
        self.nome = nome
        self.email = email
        # Dicionario cuja chave é o ISBN do livro e os valores são objetos Emprestimo
        if(listaEmprestimos is None):
            self.listaEmprestimos = {}
        else:
            self.listaEmprestimos = listaEmprestimos

    def checaValidadeParametrosUsuario(self, CPF, nome, email):
        if(not self.checaValidadeCPF(CPF)):
            raise Exception('CPF inválido: deve ter exatamente 11 dígitos de 0 a 9')

        if(not self.checaValidadeNome(nome)):
            raise Exception('Nome inválido: deve ter tamanho máximo '+ str(TAM_MAX_NOME) +' e conter apenas letras e espaços')

        if(not self.checaValidadeEmail(email)):
            raise Exception('Email inválido: deve conter @')

    def checaValidadeCPF(self, CPF):
        # CPF só pode conter dígitos de 0 a 9
        if(not CPF.isdecimal()):
            return False
        # Tamanho do CPF deve ser de exatamente 11 dígitos
        if(len(str(CPF)) != 11):
            return False
        return True

    def checaValidadeNome(self, nome):
        # Nome só pode conter letras e espaços
        if(not nome.replace(' ', '').isalpha()):
            return False
        # Tamanho do nome deve ser menor ou igual a TAM_MAX_NOME
        if(len(str(nome)) > TAM_MAX_NOME):
            return False
        return True

    def checaValidadeEmail(self, email):
        # Email deve conter @
        if(not '@' in email):
            return False
        return True

    def getCPF(self):
        return self.CPF

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getListaEmprestimos(self):
        return self.listaEmprestimos    

    def setNome(self, nomeNovo):
        if(self.checaValidadeNome(nomeNovo)):
            self.nome = nomeNovo

    def setEmail(self, emailNovo):
        if(self.checaValidadeEmail(emailNovo)):
            self.email = emailNovo

    def setListaEmprestimos(self, emprestimosNovo):
        self.listaEmprestimos = emprestimosNovo
            
               
    def emprestarLivroUnidade(self, ISBN, unidade):
        if(self.consultarDisponibilidadeLivroUnidade(ISBN, unidade)):
            self.listaEmprestimos[ISBN] = Emprestimo(ISBN, self.CPF, unidade.getUnidadeID(), date.today())
        else:
            self.reservarLivroUnidade(ISBN, unidade)

    def devolverLivroUnidade(self, ISBN, unidade):
        unidade.usuarioDevolveLivro(ISBN)

    def reservarLivroUnidade(self, ISBN, unidade):
        unidade.usuarioReservaLivro(ISBN, self.CPF)

    def verLivrosDisponiveisUnidade(self, unidade):
        return unidade.listaLivrosDisponiveis()

    def consultarDisponibilidadeLivroUnidade(self, ISBN, unidade):
        return unidade.checaLivroDisponivel(ISBN)

    def verMeusLivrosAlugados(self):
        return list(self.listaEmprestimos.keys())
