TP_TesteSoftware
# Sistema de Bibliotecas

Membros do grupo
- Ana Flávia de Miranda Silva
- Filipe Barros Vitorino
- Helena Pato Magalhães

## Explicação do sistema

Sistema de unidades de uma rede de bibliotecas. Seu propósito é gerenciar os livros e empréstimos de cada unidade da biblioteca. As principais entidades são a unidade da biblioteca, o usuário da biblioteca, o livro e o empréstimo.

### Unidade da Bilioteca
Tem o propósito de gerenciar seus livros e os empréstimos feitos. Pode transferir livros para outras unidades e recebe-los de outras unidades. Controla a disponibilidade dos livros e os empréstimos feitos.

### Usuário
Usuário pode pegar livros emprestados e devolvê-los. Ele também pode consultar sua disponibilidade e fazer reservas.

### Livro
Uma entidade que existe para ser manipulada pelas demais. O livro é central ao sistema, mas não faz muita coisa sozinho.

### Empréstimo 
Registro do empréstimo de um livro feito pelo usuário em uma unidade. Pode calcular o valor da multa que um usuário deve.

## Explicação das tecnologias utilizadas

Para construir o sistema, utilizamos a linguagem de programação Python. Para os testes de unidade utilizamos o módulo unittest. O GitHub Actions foi usado para construir versões do sistema e executar os testes. A interface web foi criada usando o micro framework Flask.