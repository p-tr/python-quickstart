from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
# Les petites solutions de Lub1, ou comment cheese
def hello(name="World"):
    return render_template('hello.html.j2', name=name)

@app.route('/users/<int:id>')
def show_user(id):
    return f"<p>User {id}</p>"

@app.route('/sitemap')
def sitemap():
    urls={
        'index' : url_for('index'),
        'hello' : url_for('hello'),
        'hello(Pierre)' : url_for('hello', name='Pierre')
    }
    return render_template('sitemap.html.j2', urls=urls)

@app.errorhandler(404)
def not_found(error):
    code = error.get_response().status.split(' ')[0]
    return render_template('error.html.j2', code=code), code
