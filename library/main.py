from library_manager import Library, generate_report

def main():
    # Создаём библиотеку
    lib = Library()

    # Добавляем книги
    lib.add_book({
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian"
    })

    lib.add_book({
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy"
    })

    lib.add_book({
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "genre": "Classic"
    })

    # Выводим все книги
    print("📚 Все книги в библиотеке:")
    print(generate_report(lib))

    # Поиск по жанру
    print("\n🔍 Поиск книг жанра 'Fantasy':")
    fantasy_books = lib.find_books(genre="Fantasy")
    for book in fantasy_books:
        print(book)

    # Удаление книги
    lib.remove_book("1984")

    # Отчёт после удаления
    print("\n📚 Список книг после удаления '1984':")
    print(generate_report(lib))

if __name__ == "__main__":
    main()
