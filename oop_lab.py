class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa
student1 = Student('Настя', 17, 4.5)

print("Имя студента:", student1.get_name())
print("Возраст студента:", student1.get_age())
print("Средний балл студента:", student1.get_gpa())

student1.set_name("Кирилл")
student1.set_gpa(4.55)

print("Измененное имя студента:", student1.get_name())
print("Измененный средний балл студента:", student1.get_gpa())



#2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(10, 15)

area = rectangle1.get_area()
perimeter = rectangle1.get_perimeter()

print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")





#3
class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def display_info(self):
        print(f"Марка: {self.make}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Пробег: {self.mileage} км")

car1 = Car("Ford", "Focus", 2019, 40000)

car1.display_info()

car1.set_make("Toyota")
car1.set_mileage(60000)

car1.display_info()



#4
class BankAccount:
    def __init__(self, client_name, initial_balance=0):
        self.client_name = client_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесена сумма {amount} руб. выполнен. Новый баланс: {self.balance} руб.")
        else:
            print("Вы выбрали не ту операцию")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Снятие на сумму {amount} руб. выполнено. Новый баланс: {self.balance} руб.")
        elif amount > self.balance:
            print("Недостаточно средств на счете.")


    def get_balance(self):
        print(f"Баланс {self.client_name}: {self.balance} руб.")


account1 = BankAccount("Сергей Сергеевич", 3000)

account1.deposit(11111)
account1.withdraw(222)

account1.get_balance()


#5


import math
class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        s = (self.x + self.y + self.z) / 2
        return math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))

    def triangle_type(self):
        def is_equilateral():
            return self.x == self.y == self.z

        def is_isosceles():
            return self.x == self.y or self.y == self.z or self.z == self.x

        def is_scalene():
            return not is_equilateral() and not is_isosceles()

        if is_equilateral():
            return "Равносторонний треугольник"
        elif is_isosceles():
            return "Равнобедренный треугольник"
        elif is_scalene():
            return "Разносторонний треугольник"
        else:
            return "Неопределенный треугольник"

triangle1 = Triangle(1, 1, 1)
triangle2 = Triangle(1, 2, 2)
triangle3 = Triangle(1, 2, 3)

print(triangle1.triangle_type())
print(triangle2.triangle_type())
print(triangle3.triangle_type())

print("Площадь треугольника ", triangle3.area())

