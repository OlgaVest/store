from .utils.data_validation import validate_book_data
from .utils.formatting import format_book_data

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_data):
        if validate_book_data(book_data):
            self.books.append(book_data)
            print(f"Книга добавлена: {book_data['title']}")
        else:
            print("Некорректные данные книги. Добавление отклонено.")

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"Книга '{title}' удалена.")
                return
        print(f"Книга '{title}' не найдена.")

    def find_books(self, **kwargs):
        results = []
        for book in self.books:
            if all(book.get(k) == v for k, v in kwargs.items()):
                results.append(book)
        return results

    def view_all_books(self):
        return self.books
