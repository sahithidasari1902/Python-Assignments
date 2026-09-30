# Assignment 10: Packages & Modules in Python
#
# Project structure:
#   assignment10_packages/
#   |-- main.py
#   |-- mypackage/
#       |-- __init__.py
#       |-- class_one.py
#       |-- class_two.py
#
# Run this file (main.py) from PyCharm.

# Q3. Different ways of importing
import mypackage.class_one                       # full module import
from mypackage.class_two import ClassTwo         # import one class directly
import mypackage.class_one as c1                 # Q6. alias import
from mypackage import ClassOne                   # works because of __init__.py

print("Q4/Q5. Using the classes")
print("--- Object via full module path ---")
obj1 = mypackage.class_one.ClassOne("Sahithi")
print(obj1.greet())

print("--- Object via 'from ... import' ---")
obj2 = ClassTwo(10, 20)
print("Sum of", obj2.a, "and", obj2.b, "=", obj2.add())

print("--- Object via alias c1 ---")
obj3 = c1.ClassOne("JALA Academy")
print(obj3.greet())

print("--- Object via package-level import (__init__.py) ---")
obj4 = ClassOne("Package import")
print(obj4.greet())

print()
print("Q7. Relative import inside the package")
print(obj2.use_class_one())
