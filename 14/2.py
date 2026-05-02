# 02
class Vehicle:
    type = ""
    speed = 0
    company = ""
    name = ""

    def display_info(self):
        return self.type, self.company, self.name, self.speed

    def set_speed(self, speed):
        self.speed = speed
    def get_speed(self):
        return self.speed
exam1 = Vehicle()
exam1.type = "electric"
exam1.speed = 50
exam1.company = "tesla"
exam1.name = "model y"
print(exam1.display_info())
print(exam1.get_speed())
