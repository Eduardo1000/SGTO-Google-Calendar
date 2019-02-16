from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from routes.home import *

# TODO Falta implementar o flask admin
if __name__ == '__main__':
    # Create all Database tables
    from database.disciplina import Disciplina
    db.create_all()

    # Instantiate Route Methods
    app.run(debug=True)