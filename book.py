class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.formet(selftitle, self.author)


class Bookcase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def create bookcase(cls, book_list):
        for title, author in book_list:
            books.append(Book(title, author))
        retrun cls(books)


# Dream Vaacation activity
class DreamVacation:
    def __init__(self, location, activities):
        self.location = location
        self.activities = activities

    # insert your code here
    @classmethod
    def rome(cls):
        location = 'Rome'
        activities = ['visit the Colosseum', 'Eat gelato']
        return cls(location, activities)


# Rectangle activity
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width*self.length

    @property
    def perimeter(self):
        return (self.length*2)+(self.width*2)
