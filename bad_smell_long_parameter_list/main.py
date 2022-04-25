# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move_up(self, value):
        self.y += value * self.speed

    def move_down(self, value):
        self.y -= value * self.speed

    def move_left(self, value):
        self.x -= value * self.speed

    def move_right(self, value):
        self.x += value * self.speed


class FlyUnit(Unit):

    def __init__(self, x, y, speed=1.2):
        super().__init__(x, y, speed)


class CrawlUnit(Unit):

    def __init__(self, x, y, speed=0.5):
        super().__init__(x, y, speed)


if __name__ == '__main__':
    bird = FlyUnit(0, 0)

    bird.move_left(5)
    bird.move_down(10)

    snake = CrawlUnit(0, 0)
    snake.move_left(3)
    snake.move_up(7)
