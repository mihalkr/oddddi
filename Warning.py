class Human:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"{passenger.name} сів у авто")

    def info(self):
        print(f"Авто, модель - {self.model}")
        if self.passengers != []:
            print("Зараз в автівці їдуть:")
            for passanger in self.passengers:
                print(passanger.name)

class Shop:
    def __init__(self, money=1500):
        self.money = money
        self.items = {"Перекус": 950,"Відпочинок":600}

    def shopping(self, buyer, item):
        if buyer in car.passengers:
            if item in self.items:
                if self.money >= self.items[item]:
                    self.money -= self.items[item]
                    print(f"{buyer.name} купив {item} за {self.items[item]} грн")
                    print(f"Залишок грошей {self.money} грн")
                else:
                    print(f"Недостатньо грошей для {item}!")
            else:
                print(f"{item} закінчився")

car = Car("Tesla Molel M")
car.info()
human1 = Human("Петроша")
human2 = Human("Ванька")
car.add_passenger(human1)
car.add_passenger(human2)
car.info()
shop = Shop()
shop.shopping(human1, "Перекус")
shop.shopping(human2, "Відпочинок")