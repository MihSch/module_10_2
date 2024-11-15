import threading
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        foes = 100
        count = 0
        while foes:
            foes -= self.power
            count += 1
            print(f'"{self.name} сражается {count}..., '
                  f'осталось {foes} воинов."')
            sleep(1)
        print(f'{self.name} одержал победу спустя {count} '
              f'дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()