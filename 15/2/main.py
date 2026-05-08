# 02
class Car:
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed
    def upSpeed(self,num):
        if self.speed + num > 100:
            self.speed = 100
        else:
            self.speed += num
    def downSpeed(self,num):
        if self.speed - num < 0:
            self.speed = 0
        else:
            self.speed -= num
    def getSpeed(self):
        return self.speed
a = Car("red",0)
a.upSpeed(150)
print(a.getSpeed())
a.downSpeed(120)
print(a.getSpeed())



