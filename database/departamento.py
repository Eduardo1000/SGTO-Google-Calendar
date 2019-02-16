from run_module import db

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    sigla = db.Column(db.String(10), nullable=True)
    codigo = db.Column(db.String(5), nullable=True)

    professor = db.relationship('Professor', backref='departamento', lazy=True)
    #turma = db.relationship('Turma', backref='departamento', lazy=True)

    def __init__(self, nome, sigla, codigo):
        self.nome = nome
        self.sigla = sigla
        self.codigo = codigo

    def __repr__(self):
        return '<Departamento %r>' % self.id