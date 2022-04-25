# Где-то тут закрался класс который никто не использует. 
# Есть мнение, что он зря тратит чернила монитора. Удалите его

class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def attack(self):
        pass

    def defense(self):
        pass


class Field:
    def set_unit(self, unit: Unit):
        pass


class Main:
    def __init__(self):
        self.field = Field()
        self.field.set_unit(Unit())


if __name__ == "__main__":
    main = Main()
