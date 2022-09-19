from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self,data):
        self.book_id = data['book_id']
        self.author_id = data['author_id']

    @classmethod
    def insertarBook(cls, formulario):
        query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s , %(author_id)s)"
        result = connectToMySQL('libros').query_db(query, formulario)
        return result

