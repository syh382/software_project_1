# 04
class Course :
    name = ""
    code = 0
    professor = ""
    student = []
    def display_info(self):
        return self.name, self.code, self.professor, self.student
    def add_student(self, student):
        self.student.append(student)
    def list_student(self):
        return self.student
course1 = Course()
course1.name = "소프트웨어 프로젝트"
course1.code = 218
course1.professor = "박정수"
course1.student = ["임태영","송유현","김혜성"]
print(course1.display_info())
print(course1.list_student())





