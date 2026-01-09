class Book():
    def __init__(self, title, author, ISBN, pages):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' by {self.author}, ISBN: {self.ISBN}, {self.pages} pages"
    
class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [book.get_info() for book in self.books]
    
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book.get_info()
        return "Book not found."

# Example usage
if __name__ == "__main__":
    library = Library() 
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 180)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789", 281)
    library.add_book(book1)
    library.add_book(book2)
    print(library.list_books())
    print(library.find_book_by_title("The Great Gatsby"))
    print(library.find_book_by_title("The Catcher in the Rye"))