from run_module import db

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    numero = db.Column(db.Integer, nullable=True)
    sigla = db.Column(db.String(10), nullable=True)

    turma = db.relationship('Turma', backref='disciplina', lazy=True)

    def __init__(self, nome, numero, sigla):
        self.nome = nome
        self.numero = numero
        self.sigla = sigla

    def __repr__(self):
        return '<Disciplina %r>' % self.id


        

