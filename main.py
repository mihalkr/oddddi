class Pet:
    print("Привіт!")
    pt = 0

    def __init__(self, nm, sp, age):
        self.nm = nm
        self.sp = sp
        self.age = age
        Pet.pt += 1
        print("Нова тварина!")

    def ld(self, years=1):
        self.age += years
        print(f"{self.nm} став старшим на {years} років!")

    def nf(self):
        print(f"Ім'я: {self.nm}\nВид: {self.sp}\nВік: {self.age}")

    def __str__(self):
        return f"Ім'я: {self.nm}\nВид: {self.sp}\nВік: {self.age}"

print(Pet.pt)

pet1 = Pet("Барсик", "Кот", 3)
pet1.ld(2)
print(pet1)

print(Pet.pt)

pet2 = Pet("Шарик", "Собака", 5)
print(pet2)
print(Pet.pt)

print(len(pet2.nm))