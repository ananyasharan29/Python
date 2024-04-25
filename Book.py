class Book:
    book = 5
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

b = Book('my name', 'Ananya', 3)
print(b)
