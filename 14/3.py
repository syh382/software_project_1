# 03
class Student :
    name = ""
    number = 0
    major = ""
    grade = 0
    def display_info(self):
        return self.name, self.number, self.major, self.grade
    def set_grade(self, grade):
        self.grade = grade
    def get_grade(self):
        return self.grade
student1 = Student()
student1.name = "송유현"
student1.number = 202611382
student1.major = "computer science"
student1.grade = 4.5
print(student1.display_info())
print(student1.get_grade())


