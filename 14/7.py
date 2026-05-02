# 07
# 나의 신체사이즈를 입력하고 출력하기
class My:
    def status(self,height, weight,):
        self.height = height
        self.weight = weight
    def display_info(self):
        return self.height,self.weight
me =My()
me.status(179,59)
print(me.display_info())






