from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

book_repo.delete_all()
author_repo.delete_all()

author_1 = Author("Aldous Huxley")
author_repo.save(author_1)
book_1 = Book("Brave New World", author_1)
book_repo.save(book_1)
