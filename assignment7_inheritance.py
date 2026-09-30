# Assignment 7: Inheritance & Polymorphism in Python
# Hierarchy:  A  ->  B  ->  C   (C inherits from B, B inherits from A)


class A:
    value = "A's class value"

    def __init__(self):
        print("  A constructor called")
        self.name = "Instance of A"          # same variable name in A, B, C

    def a_method1(self):
        print("A: a_method1")

    def a_method2(self):
        print("A: a_method2")

    def show(self):                          # common method
        print("A: show()")


class B(A):
    value = "B's class value"

    def __init__(self):
        super().__init__()                   # run A's constructor first
        print("  B constructor called")
        self.name = "Instance of B"

    def b_method1(self):
        print("B: b_method1")

    def b_method2(self):
        print("B: b_method2")

    def show(self):                          # overrides A.show
        super().show()                       # Q5: call parent version
        print("B: show() (overridden)")


class C(B):
    value = "C's class value"

    def __init__(self):
        super().__init__()                   # run B's (and so A's) constructor
        print("  C constructor called")
        self.name = "Instance of C"

    def c_method1(self):
        print("C: c_method1")

    def c_method2(self):
        print("C: c_method2")

    def show(self):                          # overrides B.show
        super().show()
        print("C: show() (overridden)")


# ---------------------------------------------------------------
# Q3 + Q7. Create objects (watch the constructor order) and call methods
# ---------------------------------------------------------------
print("Creating object of A:")
obj_a = A()
print("Creating object of B:")
obj_b = B()
print("Creating object of C (order: A -> B -> C):")
obj_c = C()
print()

print("Q3. Calling methods")
obj_a.a_method1()
obj_a.a_method2()
obj_a.show()
print("---")
obj_b.b_method1()
obj_b.b_method2()
obj_b.a_method1()                  # inherited from A
obj_b.show()
print("---")
obj_c.c_method1()
obj_c.c_method2()
obj_c.b_method1()                  # inherited from B
obj_c.a_method2()                  # inherited from A
obj_c.show()
print()


# ---------------------------------------------------------------
# Q4. Runtime polymorphism
#     The variable is "treated as" an A, but Python calls the method
#     of the ACTUAL object at runtime.
# ---------------------------------------------------------------
print("Q4. Runtime polymorphism")
ref: A = obj_b
print("ref = B object -> ref.show():")
ref.show()
ref = obj_c
print("ref = C object -> ref.show():")
ref.show()
print()


# ---------------------------------------------------------------
# Q6. Variables with the same name
#     The child's value hides (shadows) the parent's value.
# ---------------------------------------------------------------
print("Q6. Instance / class variables with same name")
print("obj_a.name  ->", obj_a.name, "| obj_a.value ->", obj_a.value)
print("obj_b.name  ->", obj_b.name, "| obj_b.value ->", obj_b.value)
print("obj_c.name  ->", obj_c.name, "| obj_c.value ->", obj_c.value)
ref: A = obj_c
print("A-reference to C object -> name:", ref.name, "| value:", ref.value)
print("Unlike Java, Python looks up variables on the real object too, so we get C's values.")
print()


# ---------------------------------------------------------------
# Q8. Real-world example: Vehicle -> Car -> ElectricCar
# ---------------------------------------------------------------
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(self.brand, "- Vehicle engine starting...")


class Car(Vehicle):
    def start_engine(self):
        print(self.brand, "- Car: turn key, petrol engine starts")


class ElectricCar(Car):
    def start_engine(self):
        print(self.brand, "- ElectricCar: press button, motor starts silently")


print("Q8. Vehicle -> Car -> ElectricCar")
for v in [Vehicle("Generic"), Car("Maruti"), ElectricCar("Tata Nexon EV")]:
    v.start_engine()               # same call, different behaviour = polymorphism
