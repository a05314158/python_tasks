import json
def add_book(library, title, author, year):
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    save_library(library)
def delete_book(library, title):
    library = [book for book in library if book["title"] != title]
    save_library(library)
def edit_book(library, old_title, new_title, new_author, new_year):
    for book in library:
        if book["title"] == old_title:
            book["title"] = new_title
            book["author"] = new_author
            book["year"] = new_year
            save_library(library)
            break
def show_books(library):
    for book in library:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
def save_library(library):
    with open('library.json', 'w') as file:
        json.dump(library, file, indent=2)
def load_library():
    try:
        with open('library.json', 'r') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
def main():
    library = load_library()
    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Редактировать книгу")
        print("4. Показать книги")
        print("5. Выход")
        choice = input("Выберите действие (1-5): ")
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год выпуска книги: ")
            add_book(library, title, author, year)
        elif choice == '2':
            title = input("Введите название книги, которую нужно удалить: ")
            delete_book(library, title)
        elif choice == '3':
            old_title = input("Введите название книги, которую нужно отредактировать: ")
            new_title = input("Введите новое название книги: ")
            new_author = input("Введите нового автора книги: ")
            new_year = input("Введите новый год выпуска книги: ")
            edit_book(library, old_title, new_title, new_author, new_year)
        elif choice == '4':
            show_books(library)
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите от 1 до 5.")
if __name__ == "__main__":
    main()
