from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repo

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select_all(row["id"])
        book = Book(row["title"], author, row["id"])
        books.append(book)
    return books