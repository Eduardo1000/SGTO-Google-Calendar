from run_module import db

class Vinculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)

    professor = db.relationship('Professor', backref='vinculo', lazy=True)

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return '<Vinculo %r>' % self.id