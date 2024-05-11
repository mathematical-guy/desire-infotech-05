
class Book:
    publication = "McGraw Hills"
    # cover = "Yellow"
    # title = "ABCD"
    # pages = 300
    # author =  "XYZ"

    # Functions with double underscores __function_name__ are called 
    # - double underscore methods
    # - dunder methods
    # - magic methods (because they are called automatically)

    def __init__(self, cover, title, pages: int, author):
        self.cover = cover
        self.title = title
        self.pages = pages
        self.author = author
        print(self)
    
    def __str__(self) -> str:
        return str(self.pages)

book1 = Book(
    cover="Green", 
    title="8086 Microprocessor", 
    pages=1000, author="Mohd Rashid"
)
print(book1)

# book2 = Book(
#     cover="White",
#     title="Networking with C",
#     pages="300",
#     author="Ajay"
# )
# print(book2)


# book3 = Book(
#     cover="Dark Green",
#     title="Secrets of Mahabharata",
#     pages=500,
#     author="ABCD",
# )


# print(book3)
# print(book1, book1.author, book1.pages, book1.publication)
# print(book2, book2.author, book2.pages, book2.publication)
# print(book3, book3.author, book3.pages, book3.publication)


def myfunc():
    pass

list.append

myfunc