# Assignment 9: Abstract Classes in Python
# An abstract class is a "template". It cannot be used to create objects
# directly; child classes must implement its abstract methods.
from abc import ABC, abstractmethod
import math


# ---------------------------------------------------------------
# 1 + 6. Abstract class with abstract and normal methods
# ---------------------------------------------------------------
class Animal(ABC):
    @abstractmethod
    def sound(self):            # no implementation here
        pass

    @abstractmethod
    def move(self):             # Q6: second abstract method
        pass

    def breathe(self):          # normal (non-abstract) method
        print("All animals breathe oxygen")


# ---------------------------------------------------------------
# 2. Child class implementing ALL abstract methods
# ---------------------------------------------------------------
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")

    def move(self):
        print("Dog runs on four legs")


print("Q3. Non-abstract method via child object")
d = Dog()
d.breathe()                     # inherited from Animal
print()

print("Q4. Implemented abstract methods")
d.sound()
d.move()
print()


# ---------------------------------------------------------------
# 5. Try to create an object of the abstract class
# ---------------------------------------------------------------
print("Q5. Instantiating the abstract class")
try:
    a = Animal()
except TypeError as err:
    print("TypeError:", err)
    print("Why: Animal has abstract methods with no body, so Python refuses to create it.")
print()


# ---------------------------------------------------------------
# 7. Real-world example: Shape
# ---------------------------------------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def display(self):
        print(self.__class__.__name__, "area =", round(self.area(), 2))


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


print("Q7. Shape example")
for shape in [Circle(3), Rectangle(4, 5)]:
    shape.display()
print()


# ---------------------------------------------------------------
# 8. Partial implementation - child does NOT implement every method
# ---------------------------------------------------------------
class Fish(Animal):
    def sound(self):
        print("Fish makes no sound")
    # move() is missing!


print("Q8. Partial implementation")
try:
    f = Fish()
except TypeError as err:
    print("TypeError:", err)
    print("Why: Fish is still abstract because move() is not implemented.")
