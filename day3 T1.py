# Parent class 1
class Author:
    def __init__(self, author_name):
        self.author_name = author_name

    def display_author(self):
        print("Author:", self.author_name)


# Parent class 2
class Publisher:
    def __init__(self, publisher_name):
        self.publisher_name = publisher_name

    def display_publisher(self):
        print("Publisher:", self.publisher_name)


# Child class inheriting from multiple parents
class Book(Author, Publisher):
    def __init__(self, title, author_name, publisher_name):
        self.title = title
        Author.__init__(self, author_name)
        Publisher.__init__(self, publisher_name)

    def display_book_details(self):
        print("Book Title:", self.title)
        self.display_author()
        self.display_publisher()


# Create object
book = Book(
    title="Object Oriented Programming",
    author_name="James Gosling",
    publisher_name="Tech Books"
)

# Display details
book.display_book_details()
