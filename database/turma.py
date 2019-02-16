from run_module import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, db.ForeignKey('disciplina.id'))
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id'))
    codigo = db.Column(db.String(10), nullable=True)
    numero = db.Column(db.Integer, nullable=True)

    def __init__(self, id_disciplina, id_departamento, numero, codigo=''):
        self.id_disciplina = id_disciplina
        self.id_departamento = id_departamento
        self.numero = numero
        self.codigo = codigo

    def __repr__(self):
        return '<Turma %r>' % self.id