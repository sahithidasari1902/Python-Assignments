# Assignment 14: Exception Handling in Python
import logging
import os

logging.basicConfig(level=logging.ERROR, format="LOG %(levelname)s: %(message)s")


# ---------------------------------------------------------------
# 1. Generate an exception without handling it
#    Uncommenting the last line crashes the program with:
#    ZeroDivisionError: division by zero
# ---------------------------------------------------------------
def divide_unsafe(a, b):
    return a / b

print("Q1. Unhandled exception")
print("divide_unsafe(10, 0) would crash with ZeroDivisionError (line kept commented out)")
# divide_unsafe(10, 0)
print()


# ---------------------------------------------------------------
# 2. Handle it with try / except
# ---------------------------------------------------------------
print("Q2. Handled exception")
try:
    divide_unsafe(10, 0)
except ZeroDivisionError:
    print("Cannot divide by zero - handled gracefully")
print()


# ---------------------------------------------------------------
# 3. Multiple except blocks
# ---------------------------------------------------------------
print("Q3. Multiple except blocks")
try:
    x = int(input("Enter numerator  : "))
    y = int(input("Enter denominator: "))
    print("Result:", x / y)
except ZeroDivisionError:
    print("Error: denominator cannot be zero")
except ValueError:
    print("Error: please enter whole numbers only")
print()


# ---------------------------------------------------------------
# 4. Raise an exception manually
# ---------------------------------------------------------------
def check_age(age):
    if age < 18:
        raise ValueError("Age " + str(age) + " is below 18 - not eligible")
    print("Age", age, "is eligible")

print("Q4. raise")
for age in [25, 15]:
    try:
        check_age(age)
    except ValueError as err:
        print("Caught:", err)
print()


# ---------------------------------------------------------------
# 5. Function that always raises
# ---------------------------------------------------------------
def always_fails():
    raise RuntimeError("This function always fails")

print("Q5. Function that always raises")
print("Calling it without try/except would stop the program (kept commented out)")
# always_fails()
try:
    always_fails()
except RuntimeError as err:
    print("Handled:", err)
print()


# ---------------------------------------------------------------
# 6. Custom exception
# ---------------------------------------------------------------
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            "Cannot withdraw " + str(amount) + ", balance is only " + str(balance))
    return balance - amount

print("Q6. Custom exception")
try:
    print("New balance:", withdraw(1000, 400))
    print("New balance:", withdraw(1000, 5000))
except InsufficientBalanceError as err:
    print("InsufficientBalanceError:", err)
print()


# ---------------------------------------------------------------
# 7. finally - always runs, so the file is always closed
# ---------------------------------------------------------------
print("Q7. finally")
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo.txt")
with open(path, "w") as tmp:
    tmp.write("Hello from demo file\n")
f = None
try:
    f = open(path, "r")
    print("Read:", f.read().strip())
except OSError as err:
    print("Error:", err)
finally:
    if f is not None:
        f.close()
    print("finally block ran - file closed:", f.closed)
print()


# ---------------------------------------------------------------
# 8. FileNotFoundError
# ---------------------------------------------------------------
print("Q8. FileNotFoundError")
try:
    open("this_file_does_not_exist.txt", "r")
except FileNotFoundError:
    print("File not found - please check the file name")
print()


# ---------------------------------------------------------------
# 9. TypeError
# ---------------------------------------------------------------
print("Q9. TypeError")
try:
    result = "Age: " + 21           # cannot add str and int
except TypeError as err:
    print("TypeError:", err)
print()


# ---------------------------------------------------------------
# 10. AttributeError
# ---------------------------------------------------------------
print("Q10. AttributeError")
class Student:
    def __init__(self):
        self.name = "Sahithi"

try:
    print(Student().marks)          # 'marks' does not exist
except AttributeError as err:
    print("AttributeError:", err)
print()


# ---------------------------------------------------------------
# 11. IndexError
# ---------------------------------------------------------------
print("Q11. IndexError")
items = [10, 20, 30]
try:
    print(items[5])
except IndexError as err:
    print("IndexError:", err)
print()


# ---------------------------------------------------------------
# 12. else - runs only when no exception happened
# ---------------------------------------------------------------
print("Q12. else block")
for divisor in [5, 0]:
    try:
        answer = 100 / divisor
    except ZeroDivisionError:
        print("100 /", divisor, "-> error, else block skipped")
    else:
        print("100 /", divisor, "=", answer, "-> no error, else block ran")
print()


# ---------------------------------------------------------------
# 13. Logging errors instead of printing
# ---------------------------------------------------------------
print("Q13. Logging")
try:
    int("abc")
except ValueError as err:
    logging.error("Conversion failed: %s", err)
print()


# ---------------------------------------------------------------
# 14. Keep asking until valid input is entered
# ---------------------------------------------------------------
print("Q14. Input validation loop")
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if marks < 0 or marks > 100:
            raise ValueError("marks must be between 0 and 100")
        break                       # valid -> leave the loop
    except ValueError as err:
        print("Invalid input:", err, "- try again")
print("Accepted marks:", marks)
