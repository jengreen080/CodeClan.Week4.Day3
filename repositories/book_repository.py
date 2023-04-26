from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repo


def save(book):
    sql = "INSERT INTO books (title, author) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select(row["id"])
        book = Book(row["title"], author, row["id"])
        books.append(book)
    return books

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)