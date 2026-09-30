# Assignment 5: Class Variables (Static Variables) in Python
# A class variable is defined inside the class but outside any method.
# It is SHARED by all objects - like 'static' in Java.


class College:
    college_name = "JALA Academy"       # class variable (shared)


# ---------------------------------------------------------------
# 1. Access via class name
# ---------------------------------------------------------------
print("Q1. Access via class")
print("College.college_name ->", College.college_name)
print()


# ---------------------------------------------------------------
# 2. Access via object
# ---------------------------------------------------------------
print("Q2. Access via object")
c1 = College()
print("c1.college_name ->", c1.college_name)
print()


# ---------------------------------------------------------------
# 3. Modify class variable via instance
#    Assigning through an object does NOT change the class variable.
#    It creates a NEW instance variable on that object only.
# ---------------------------------------------------------------
print("Q3. Modify via instance")
c1.college_name = "Changed by c1"
print("c1.college_name      ->", c1.college_name)          # the object's own copy
print("College.college_name ->", College.college_name)     # class value unchanged
print()


# ---------------------------------------------------------------
# 4. Modify class variable via class name
#    This changes the value for every object that has not
#    created its own copy.
# ---------------------------------------------------------------
print("Q4. Modify via class")
College.college_name = "Bright IT Career"
c2 = College()
c3 = College()
print("College.college_name ->", College.college_name)
print("c2.college_name      ->", c2.college_name)
print("c3.college_name      ->", c3.college_name)
print("c1.college_name      ->", c1.college_name, "(c1 still has its own copy from Q3)")
print()


# ---------------------------------------------------------------
# 5. Class variable vs instance variable
# ---------------------------------------------------------------
class Car:
    wheels = 4                          # class variable: same for all cars

    def __init__(self, color):
        self.color = color              # instance variable: different per car


print("Q5. Class vs Instance variable")
car1 = Car("Red")
car2 = Car("Blue")
print("car1:", car1.wheels, "wheels,", car1.color)
print("car2:", car2.wheels, "wheels,", car2.color)

car1.color = "Black"                    # changes only car1
print("After car1.color = 'Black' -> car1:", car1.color, "| car2:", car2.color)

Car.wheels = 6                          # changes for all cars
print("After Car.wheels = 6       -> car1:", car1.wheels, "| car2:", car2.wheels)
print()


# ---------------------------------------------------------------
# 6. Shared Counter
# ---------------------------------------------------------------
class Student:
    count = 0                           # shared counter

    def __init__(self, name):
        self.name = name
        Student.count += 1              # use class name, so all objects share it


print("Q6. Shared Counter")
s1 = Student("Sahithi")
s2 = Student("Ravi")
s3 = Student("Anu")
print("Total students created:", Student.count)
print()


# ---------------------------------------------------------------
# 7. Configuration setting example
# ---------------------------------------------------------------
class Course:
    course_name = "Python Basics"       # acts like a global setting

    def show(self, who):
        print(who, "sees course:", Course.course_name)

    def change(self, new_name):
        Course.course_name = new_name   # change through the class -> affects everyone


print("Q7. Configuration setting")
learner1 = Course()
learner2 = Course()
learner1.show("learner1")
learner2.show("learner2")
learner1.change("Advanced Python")
print("learner1 changed the course name...")
learner1.show("learner1")
learner2.show("learner2")
