from flask import Flask, render_template
from models.livro import db
from models.reserva import db_reserva
from models.usuario import db_usuario
from models.emprestimo import db_emprestimo
from models.livroBiblioteca import db_livroBiblioteca
from models.unidadeBiblioteca import db_unidadeBiblioteca


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
    db_reserva.create_all()
    db_usuario.create_all()
    db_emprestimo.create_all()
    db_livroBiblioteca.create_all()
    db_unidadeBiblioteca.create_all()

@app.route('/')
def home():
    return render_template('home.html')


import livroController
import usuarioController
import reservaController
import emprestimoController
import livroBibliotecaController
import unidadeBibliotecaController
