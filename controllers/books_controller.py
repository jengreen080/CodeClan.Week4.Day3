from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books/")
def books():
    books = book_repo.select_all()
    return render_template("books/index.html", books_to_display = books)