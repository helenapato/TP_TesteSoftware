TAM_MAX_NOME = 50

class Usuario:

    def __init__(self, CPF, nome, email):
        # CPF só pode conter dígitos de 0 a 9
        if(not CPF.isdecimal()):
            raise Exception('CPF contém símbolos inválidos')
        # Tamanho do CPF deve ser de exatamente 11 dígitos
        if(len(str(CPF)) != 11):
            raise Exception('Tamanho do CPF inválido, não tem 11 dígitos')

        # Nome só pode conter letras e espaços
        if(not nome.replace(' ', '').isalpha()):
            raise Exception('Nome contém símbolos inválidos')
        # Tamanho do nome deve ser menor ou igual a TAM_MAX_NOME
        if(len(str(nome)) > TAM_MAX_NOME):
            raise Exception('Tamanho do nome inválido, deve ter até', TAM_MAX_NOME, 'caracteres')

        # Email deve conter @
        if(not '@' in email):
            raise Exception('Email inválido')

        self.CPF = CPF
        self.nome = nome
        self.email = email

    def getCPF(self):
        return self.CPF

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def setNome(self, nomeNovo):
        # Nome só pode conter letras e espaços
        if(not nomeNovo.replace(' ', '').isalpha()):
            return
        # Tamanho do nome deve ser menor ou igual a TAM_MAX_NOME
        if(len(str(nomeNovo)) > TAM_MAX_NOME):
            return
        self.nome = nomeNovo

    def setEmail(self, emailNovo):
        # Email deve conter @
        if(not '@' in emailNovo):
            return
        self.email = emailNovo


    def alugarLivroUnidade(self, ISBN, unidadeID):
        #TODO
        print('TODO')

    def devolverLivroUnidade(self, ISBN, unidadeID):
        #TODO
        print('TODO')

    def reservarLivroUnidade(self, ISBN, unidadeID):
        #TODO
        print('TODO')

    def verLivrosDisponiveisUnidade(self, unidadeID):
        #TODO
        print('TODO')

    def consultarDisponibilidadeLivroUnidade(self, ISBN, unidadeID):
        #TODO
        print('TODO')

    def verMeusLivrosAlugados(self):
        #TODO
        print('TODO')