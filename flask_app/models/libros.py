from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Libro:
    def __init__(self, data):
        self.id = data['id']
        self.tittle = data['tittle']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.autores = []

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO books (tittle, num_of_pages) VALUES (%(tittle)s, %(pages)s)"
        results = connectToMySQL("libros").query_db(query, formulario)
        return results

    @classmethod
    def show(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL("libros").query_db(query)

        libros = []

        for x in results:
            libros.append(cls(x))
        return libros

    @classmethod
    def join_tables(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites on favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s"
        results = connectToMySQL("libros").query_db(query, data)
        book = cls(results[0])

        for lista in results:
            n = {
                'id': lista['authors.id'],
                'name': lista['name'],
                'created_at': lista['authors.created_at'],
                'updated_at': lista['authors.updated_at']
            }   

            instancia_autores = author.Autor(n)
            book.autores.append(instancia_autores)

        return book
