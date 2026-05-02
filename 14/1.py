# 01
class Car :
    color = ""
    speed = 0
    def setting(self, color, speed, passengers):
        self.color = color
        self.speed = speed
        self.passengers = passengers

    def accelerate(self, speed):
        self.speed += speed
    def decelerate(self, speed):
        self.speed -= speed
car1 = Car()
car1.setting("Gray", 80, 5)
print(car1.color, car1.speed)
car2 = Car()
car2.setting("Orange", 150, 5)
print(car2.color, car2.speed)
car3 = Car()
car3.setting("White", 50, 5)
print(car3.color, car3.speed)
car4 = Car()
car4.setting("Gray", 80, 5)
car4.accelerate(30)
print(car4.color, car4.speed, car4.passengers)
car5 = Car()
car5.setting("Black", 100, 5)
car5.decelerate(20)
print(car5.color, car5.speed, car5.passengers)

