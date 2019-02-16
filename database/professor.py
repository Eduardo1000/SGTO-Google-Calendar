from run_module import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    siape = db.Column(db.Integer, nullable=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    telefone = db.Column(db.String(15), nullable=True)
    ramal = db.Column(db.String(15), nullable=True)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id'))
    id_vinculo = db.Column(db.Integer, db.ForeignKey('vinculo.id'))

    def __init__(self, siape, nome, email, telefone, ramal, id_departamento, id_vinculo):
        self.siape = siape
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.ramal = ramal
        self.id_departamento = id_departamento
        self.id_vinculo = id_vinculo

    def __repr__(self):
        return '<Professor %r>' % self.id