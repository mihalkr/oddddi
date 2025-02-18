import random

class cats:
    def __init__(self, name):
        self.name = name
        self.progress = 10
        self.gladness = 50
        self.alive = True

    def eat(self):
        self.progress += 1
        self.gladness -= 1
        print("Я поїв, я ситий")

    def chill(self):
        self.progress -= 1
        self.gladness += 1
        print("Я сьогодні гарно відпочив")

    def sleep(self):
        self.gladness += 0.5
        print("Я спав")

    def is_alive(self):
        if self.gladness < 0:
            print("Кіт помер від голоду")
            self.alive = False
        elif self.progress < 0:
            print("Кіт заснув на дуже довгий час")
            self.alive = False
        elif self.progress > 50:
            print("Я сьогодні став дорослив котом!")
            self.alive = False

    def info(self):
        print(f"Задоволення: {self.gladness}")
        print(f"Прогрес: {self.progress}")

    def live(self, day):
        print(f"\nДень № {day + 1}")
        print(f"Привіт, я {self.name}. І я сьогодні...")
        rnd = random.randint(1, 3)
        if rnd == 1:
            self.eat()
        elif rnd == 2:
            self.sleep()
        elif rnd == 3:
            self.chill()
        self.info()
        self.is_alive()


cats = cats("Murchik")
for day in range(365):
    if not cats.alive:
        break
    cats.live(day)