# 06
class Library :
    books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        return self.books
    def fine_book(self, name):
        return name in self.books
library = Library()
library.books = ["해리포터 마법사의 돌","해리포터 비밀의방"]
library.add_book("해리포터 아즈카반의 죄수")
print(library.list_books())
print(library.fine_book("해리포터 마법사의 돌"))






