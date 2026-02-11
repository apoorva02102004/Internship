class Book:
    
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # User-friendly representation
    def __str__(self):
        return f"'{self.title}' by {self.author} costs ₹{self.price}"

    # Developer-friendly representation
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"


# Creating 2 objects
book1 = Book("Python Basics", "John Doe", 499)
book2 = Book("OOP Concepts", "Jane Smith", 599)

# Using print() → Calls __str__()
print(book1)
print(book2)

print("----------------------")

# Printing inside a list → Calls __repr__()
book_list = [book1, book2]
print(book_list)
