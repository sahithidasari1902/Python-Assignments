# Assignment 1: Python Basics & Variables
# Run this file in your IDE (PyCharm / VS Code) and read the output with the code.


# ---------------------------------------------------------------
# 1. Print Your Name
# ---------------------------------------------------------------
print("Q1. Print Your Name")
print("My name is Sahithi")
print()


# ---------------------------------------------------------------
# 2. Comments in Python
# ---------------------------------------------------------------
print("Q2. Comments")

# This is a single-line comment. Python ignores everything after '#'.

"""
This is a multi-line comment (a triple-quoted string).
Python reads it as a string that is never used,
so it has no effect on the program.
"""

print("Comments explain the code to humans. Python ignores them when running.")
print()


# ---------------------------------------------------------------
# 3. Working with Basic Data Types
# ---------------------------------------------------------------
print("Q3. Basic Data Types")

age = 21                # int   -> whole number
height = 5.6            # float -> number with a decimal point
is_student = True       # bool  -> only True or False
name = "Sahithi"        # str   -> text
grade = "A"             # Python has no 'char' type; a 1-letter string is used

print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(name, type(name))
print(grade, type(grade))
print()


# ---------------------------------------------------------------
# 4. Local vs Global Variables
# ---------------------------------------------------------------
print("Q4. Local vs Global")

count = 10              # global variable: created outside any function


def show_scope():
    count = 99          # local variable: same name, but exists only inside this function
    print("Local count inside function :", count)
    print("Global count (via globals()) :", globals()["count"])


def change_global():
    global count        # tells Python: use the global 'count', don't create a new local one
    count = 50
    print("Changed global count inside function to", count)


show_scope()
print("Global count after show_scope   :", count)   # still 10, local didn't affect it
change_global()
print("Global count after change_global:", count)   # now 50
print()


# ---------------------------------------------------------------
# 5. Type Checking & Dynamic Typing
# ---------------------------------------------------------------
print("Q5. Dynamic Typing")

# In Python a variable is just a label; the same label can point to any type.
x = 100
print(x, type(x))
x = 3.14
print(x, type(x))
x = "hello"
print(x, type(x))
x = False
print(x, type(x))
print()


# ---------------------------------------------------------------
# 6. User Input Practice
# ---------------------------------------------------------------
print("Q6. User Input")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))   # input() always returns text, so convert to int

print("Hello", user_name + "!", "You are", user_age, "years old.")
print("Next year you will be", user_age + 1)
