class Student:
    count_student = 0

    def __init__(self, name, height=160):
        self.height = height
        self.name = name
        Student.count_student += 1
        print("I'm a Student!")

    def grow(self, grow=1):
        if self.height + grow < 220:
            self.height += grow

    def info(self):
        print(f"Name   : {self.name}")
        print(f"Height : {self.height}")

    def __str__(self):
        return f"Student(name={self.name}, height={self.height})"


print(Student.count_student)

student1 = Student("Seryas")
student1.grow(15)

print(student1)

print(Student.count_student)

student2 = Student("Genry", 170)
print(student2)
print(Student.count_student)
