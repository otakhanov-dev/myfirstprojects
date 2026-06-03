class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Ism: {self.name}, Yosh: {self.age}")

s1 = Student("Asqarali", 24)
s1.info()

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height

r = Rectangle(6,8)
print("area: ", r.area())

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
    def show(self):
        return self.balance

acc = BankAccount(1000)
acc.deposit(500)
print(f"Qolgan mablag: {acc.show()}")

class car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def info(self):
        return f"{self.brand} - {self.year}"

c = car("Kia", 2023)
print(c.info())

class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b

calc = Calculator()

print(calc.add(5,8))
print(calc.multiply(5,3))