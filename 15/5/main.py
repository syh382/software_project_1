# 05
class Post:
    def __init__(self, title, writer, content, view):
        self.title = title
        self.writer = writer
        self.content = content
        self.view = view
    def info(self):
        print(self.title, self.writer, self.view)
        print(self.content)
    def edit_content(self, content):
        self.content = content
    def increase_views(self):
        self.view += 1
first = Post("아무제목","송유현", "ㅈㄱㄴ",0)
first.info()
first.edit_content("점메추")
first.increase_views()
first.info()







