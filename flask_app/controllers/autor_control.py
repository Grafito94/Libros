from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.author import Autor
from flask_app.models.libros import Libro
from flask_app.models.favorites import Favorite


@app.route('/')
def index():
    return redirect('/newAutor')

@app.route('/newAutor')
def newAutor():
    autores = Autor.show()
    return render_template("index.html", autores = autores)

@app.route('/authors', methods = ['POST'])
def authors():
    Autor.save(request.form)
    return redirect('/newAutor')

@app.route('/showbooks')
def books():
    todos_libros = Libro.show()
    return render_template("books.html", todos_libros = todos_libros)

@app.route('/books', methods = ['POST'])
def libros():
    Libro.save(request.form)
    return redirect('/showbooks')


@app.route('/autores/<int:id>')
def viewL(id):
    data = {'id':id}
    autoresN = Autor.join_tables(data)
    return render_template("autores.html", autoresN = autoresN)

@app.route('/visualizar/<int:id>')
def visualizar(id):
    data = {'id':id}
    librosN = Libro.join_tables(data)
    autores = Autor.show()
    return render_template("libros.html", librosN = librosN, autores = autores, data = data)

@app.route('/libros')
def viewLibros():
    return render_template("libros.html")

@app.route('/agregar/autor', methods = ['POST'])
def agregarA():
    Favorite.insertarBook(request.form)
    return redirect('/showbooks')


