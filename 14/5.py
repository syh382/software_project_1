# 05
class Book:
    title = ""
    author = ""
    year = ""
    ISBN = ""
    def display_info(self):
        return self.title + " " + self.author + " " + self.ISBN + " " + self.condition
    def set_status(self,condition):
        self.condition = condition
    def get_status(self):
        return self.condition
book1 = Book()
book1.set_status("True")
book1.title = "My first book"
book1.author = "송유현"
book1.year = 2026
book1.ISBN = "978-3-540-8915-6"
print(book1.display_info())
print(book1.get_status())









