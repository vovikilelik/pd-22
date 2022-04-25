# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
# Для решения этой задачи не используйте наследование

class Deflection:

    def defense(self):
        pass


class Movable:

    def move(self):
        pass


class Warrior(Deflection, Movable):

    def attack(self):
        pass


class Healer(Deflection, Movable):

    def heal(self):
        pass


class Tree(Deflection):

    def on_fire(self):
        pass


class Trap:

    def trap_attack(self):
        print("It's a trap!")


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()