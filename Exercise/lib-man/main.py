class library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"Number of books:{self.noBooks} ")

l1 = library()
l1.addBook("Book 1")
l1.addBook("Book 2")
l1.showInfo()   

    