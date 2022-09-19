from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import libros

class Autor:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.libros = []

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO authors (name) VALUES (%(name)s)"
        results = connectToMySQL("libros").query_db(query, formulario)
        return results

    @classmethod
    def show(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL("libros").query_db(query)

        autores = []

        for x in results:
            autores.append(cls(x))
        return autores

    

    @classmethod
    def join_tables(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites on favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s"
        results = connectToMySQL("libros").query_db(query, data)
        autor = cls(results[0])

        for lista in results:
            n = {
                'id': lista["books.id"],
                'tittle': lista["tittle"],
                'num_of_pages': lista["num_of_pages"],
                'created_at': lista["books.created_at"],
                'updated_at': lista["books.updated_at"]
            }   

            instancia_libros = libros.Libro(n)
            autor.libros.append(instancia_libros)

        return autor



    



