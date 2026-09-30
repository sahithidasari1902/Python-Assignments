# Assignment 12: Constructors in Python
# Python has only ONE __init__ per class. Default values let one
# constructor behave like Java's default / 1-arg / 2-arg constructors.


# ---------------------------------------------------------------
# 1. Default and parameterized constructors
# ---------------------------------------------------------------
class Person:
    def __init__(self, name=None, age=None):
        if name is None and age is None:
            print("Default constructor called")
            self.name = "Unknown"
            self.age = 0
        elif age is None:
            print("One-argument constructor called")
            self.name = name
            self.age = 0
        else:
            print("Two-argument constructor called")
            self.name = name
            self.age = age


print("Q1. Constructors")
p1 = Person()
p2 = Person("Sahithi")
p3 = Person("Ravi", 25)
for p in [p1, p2, p3]:
    print("  ->", p.name, p.age)
print()


# ---------------------------------------------------------------
# 2. Calling the parent constructor with super()
# ---------------------------------------------------------------
class Parent:
    def __init__(self, family_name):
        print("Parent constructor called")
        self.family_name = family_name


class Child(Parent):
    def __init__(self, family_name, first_name):
        super().__init__(family_name)           # parent sets family_name
        print("Child constructor called")
        self.first_name = first_name            # extra variable


print("Q2. super() in constructors")
c = Child("Dasari", "Sahithi")
print("  ->", c.first_name, c.family_name)
print()


# ---------------------------------------------------------------
# 3. Public, protected and private attributes
# ---------------------------------------------------------------
class Account:
    def __init__(self):
        self.owner = "Sahithi"          # public
        self._branch = "Hyderabad"      # protected (convention only)
        self.__pin = 1234               # private (name mangling)


print("Q3. Access levels")
a = Account()
print("Public    a.owner   ->", a.owner)
print("Protected a._branch ->", a._branch, "(works, but by convention shouldn't be used)")
try:
    print(a.__pin)
except AttributeError:
    print("Private   a.__pin   -> AttributeError (hidden from outside)")
print("Name-mangled a._Account__pin ->", a._Account__pin, "(Python renamed it internally)")
print()


# ---------------------------------------------------------------
# 4. Constructor initialises attributes - print all of them
# ---------------------------------------------------------------
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price


print("Q4. Attributes set by the constructor")
lap = Laptop("Dell", "16GB", 55000)
print("lap.brand:", lap.brand, "| lap.ram:", lap.ram, "| lap.price:", lap.price)
print("All attributes (__dict__):", lap.__dict__)
print()


# ---------------------------------------------------------------
# 5. __str__() for readable output
# ---------------------------------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "Book: '" + self.title + "' by " + self.author


print("Q5. __str__()")
print(Book("Python Basics", "JALA Academy"))    # print() uses __str__
print()


# ---------------------------------------------------------------
# 6. Constructor with *args (any number of values)
# ---------------------------------------------------------------
class Marks:
    def __init__(self, *args):
        self.marks = args                       # args is a tuple
        total = 0
        for m in args:
            total += m
        self.total = total


print("Q6. *args constructor")
m = Marks(78, 85, 92, 64)
print("Marks:", m.marks, "| Total:", m.total)
print()


# ---------------------------------------------------------------
# 7. Real-world example: Employee
# ---------------------------------------------------------------
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def __str__(self):
        return "ID " + str(self.emp_id) + " | " + self.name + " | Salary: " + str(self.salary)


print("Q7. Employee details")
employees = [
    Employee("Sahithi", 101, 45000),
    Employee("Ravi", 102, 52000),
    Employee("Anu", 103, 48000),
]
for e in employees:
    print(e)
