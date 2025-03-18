from flask import Flask
from flask import render_template
from view_loading import view_loader


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    example_place = view_loader.load(name)
    return render_template('index.html', place=example_review)