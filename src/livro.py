import re

TAM_MAX_STR = 50

class Livro:
    
    def __init__(self, ISBN, titulo, autor):
        self.checaValidadeParametrosLivro(ISBN, titulo, autor)

        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor

    def checaValidadeParametrosLivro(self, ISBN, titulo, autor):
        if(not self.checaValidadeISBN(ISBN)):
            raise Exception('ISBN inválido: deve ter exatamente 13 dígitos de 0 a 9')
        
        if(not self.checaValidadeTitulo(titulo)):
            raise Exception('Título inválido: deve ter tamanho nmáximo ' + str(TAM_MAX_STR) + ' e conter apenas letras, dígitos e espaços')
        
        if(not self.checaValidadeAutor(autor)):
            raise Exception('Autor inválido: deve ter tamanho máximo ' + str(TAM_MAX_STR)) + ' e conter apenas letras e espaços'
    
    def checaValidadeISBN(self, ISBN):
        # ISBN deve conter apenas dígitos de 0 a 9
        if(not str(ISBN).isdecimal()):
            return False
        # ISBN deve conter 13 dígitos
        if(len(str(ISBN)) != 13):
            return False
        return True
    
    def checaValidadeTitulo(self, titulo):
        # Titulo pode conter letras, números e espaços
        caracteresInvalidos = re.sub('[0-9\sa-zA-z]', '', titulo)
        if(len(str(caracteresInvalidos)) != 0):
            return False
        # Titulo deve respeitar o tamanho máximo de caracteres numa string
        if(len(str(titulo)) > TAM_MAX_STR):
            return False
        return True
    
    def checaValidadeAutor(self, autor):
        # Autor deve conter apenas letras e espaços
        if(not autor.replace(' ', '').isalpha()):
            return False
        # Autor deve respeitar o tamanho máximo de caracteres numa string
        if(len(str(autor)) > TAM_MAX_STR):
            return False
        return True

    def getISBN(self):
        return self.ISBN
    
    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
        return self.autor
    
    def setTitulo(self, tituloNovo):
        self.titulo = tituloNovo
    
    def setAutor(self, autorNovo):
        self.autor = autorNovo
