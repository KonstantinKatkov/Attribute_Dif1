# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества
# созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию


class Buiding:


    def __init__(self, total):
        self.total = total
        self.total += 1
        print(f'Объект номер {self.total}')



count = 0
for i in range(40):
    b = Buiding(total=count)
    count = b.total
    print(b, type(b))
