class Worker:
    def __init__(self, name, salary, hours):
        self.name = name
        self.salary = salary
        self.hours = hours

    def get_info(self):
        return f"{self.name}, зарплата: {self.salary} грн, години: {self.hours} год"

class Workor(Worker):
    def __init__(self, name):
        super().__init__(name, 30000, 7)

class Werkor(Worker):
    def __init__(self, name):
        super().__init__(name, 18000, 8)

class Werker(Worker):
    def __init__(self, name):
        super().__init__(name, 22000, 9)

class Workir(Worker):
    def __init__(self, name):
        super().__init__(name, 20000, 10)

workers = [
    Workor("Олег"),
    Werkor("Марія"),
    Werker("Іван"),
    Workir("Петро")
]

for worker in workers:
    print(worker.get_info())