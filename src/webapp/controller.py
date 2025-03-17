from flask import Flask
from flask import render_template
from view_loading import view_loader


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    example_review = view_loader.load(name)
    return render_template('index.html', review=example_review)