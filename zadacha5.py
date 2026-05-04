class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
    
        print("Название:", self.title, ", Автор:", self.author)


b = Book("Герой нашего времени", "Лермонтов")
b.info()
