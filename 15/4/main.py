# 04
class GameCharacter  :
    def __init__(self, name, charclass, level, hp):
        self.name = name
        self.charclass = charclass
        self.level = level
        self.hp = hp
    def info(self):
        return self.name, self.charclass,self.level, self.hp
    def level_up(self):
        self.level += 1
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("죽었습니다")
player = GameCharacter("정글차이", "전사", 1, 680)
print(player.info())
player.level_up()
player.take_damage(150)
print(player.info())





