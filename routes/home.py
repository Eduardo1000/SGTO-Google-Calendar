from run_module import app
from flask import render_template

@app.route('/')       # Home Route and Method
def home():
    return render_template('404.html')