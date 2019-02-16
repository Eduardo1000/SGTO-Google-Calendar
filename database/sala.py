from run_module import db

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    capacidade = db.Column(db.Integer, nullable=True)

    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
    
    def __repr__(self):
        return '<Sala %r>' % self.id