# Один из классов не делает совсем ничего,
# просто переадресует вызовы к другому классу.
# Удалите этот класс и перенаправьте вызовы напрямую.

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
