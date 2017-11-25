class Hello:
    def __init__(self,Book,Author,Pages):
        self.Book = Book
        self.Author = Author
        self.pages = Pages

    def __str__(self):
        return '{0},{1},{2}'.format(self.Book, self.Author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Object is destroyed")


book = Hello("Python","Mano",347)
print(book)
print(str(book))
print(len(book))
