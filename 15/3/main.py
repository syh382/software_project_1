# 03
class Employee:
    def __init__(self, name, number, department, pay):
        self.name = name
        self.number = number
        self.department = department
        self.pay = pay
    def info(self):
        return self.name, self.number, self.department, self.pay
    def set_department(self,department):
        self.department = department
    def get_department(self):
        return self.department
a = Employee("송유현",202611382,"인사부", 500)

print(a.info())
a.set_department("마케팅부")
print(a.get_department())

