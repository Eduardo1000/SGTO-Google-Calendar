from run_module import db

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    sigla = db.Column(db.String(10), nullable=True)
    numero = db.Column(db.String(15), nullable=True)
    responsavel = db.Column(db.String(120), nullable=True)
    email_responsavel = db.Column(db.String(120), nullable=True)

    def __init__(self, nome, sigla, numero, responsavel, email_responsavel):
        self.nome = nome
        self.sigla = sigla
        self.numero = numero
        self.responsavel = responsavel
        self.email_responsavel = email_responsavel

    def __repr__(self):
        return '<Curso %r>' % self.id
