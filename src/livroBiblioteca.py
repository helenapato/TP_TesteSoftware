class LivroBiblioteca:

    def __init__(self, ISBN, copiasDisponiveis, copiasEmprestadas=0, listaReservas=[]):
        self.ISBN = ISBN
        self.copiasDisponiveis = copiasDisponiveis
        self.copiasEmprestadas = copiasEmprestadas
        self.listaReservas = listaReservas

    def getISBN(self):
        return self.ISBN

    def getCopiasDisponiveis(self):
        return self.copiasDisponiveis

    def getCopiasEmprestadas(self):
        return self.copiasEmprestadas

    def getListaReservas(self):
        return self.listaReservas

    def getCopiasTotal(self):
        return self.copiasDisponiveis + self.copiasEmprestadas

    def setCopiasDisponiveis(self, copiasNovo):
        self.copiasDisponiveis = copiasNovo

    def setCopiasEmprestadas(self, copiasNovo):
        self.copiasEmprestadas = copiasNovo

    def setListaReservas(self, reservasNovo):
        self.listaReservas = reservasNovo

    def adquirirLivros(self, quantidade):
        self.copiasDisponiveis += quantidade

    def doarLivros(self, quantidade):
        if(quantidade > self.getCopiasTotal()):
            raise Exception('Não é possível doar mais livros do que o total')
        if(quantidade > self.copiasDisponiveis):
            raise Exception('Não há cópias disponíveis o suficiente, aguarde devolução')
        self.copiasDisponiveis -= quantidade

    def livroFoiEmprestado(self):
        self.copiasDisponiveis -= 1
        self.copiasEmprestadas += 1

    def livroFoiDevolvido(self):
        self.copiasDisponiveis += 1
        self.copiasEmprestadas -= 1

    def livroEstaDisponivel(self):
        if(self.copiasDisponiveis > 0):
            return True
        return False

    def existeUsuarioReserva(self):
        if(self.listaReservas):
            return True
        return False

    def reservaUsuario(self, CPF):
        if(self.existeUsuarioReserva()):
            if(CPF in self.listaReservas):
                raise Exception('Um usuário só pode reservar um mesmo livro uma vez')
        self.listaReservas.append(CPF)

    def removeUsuarioReserva(self):
        if(self.existeUsuarioReserva()):
            return self.listaReservas.pop(0)
        raise Exception('Nenhum usuário reservou este livro')

    
