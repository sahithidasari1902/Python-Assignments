# Assignment 8: Encapsulation & Data Control in Python
# Encapsulation = keeping data inside a class and controlling how it is
# read and changed (through methods / properties with validation).


# ---------------------------------------------------------------
# 1 + 2. Student with getter/setter methods and validation
# ---------------------------------------------------------------
class Student:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Error: age must be greater than 0 (got", str(age) + ")")

    def get_age(self):
        return self.__age


print("Q1 & Q2. Getters / Setters with validation")
s = Student()
s.set_name("Sahithi")
s.set_age(21)
print("Name:", s.get_name(), "| Age:", s.get_age())
s.set_age(-5)                                   # rejected
print("Age is still:", s.get_age())
print()


# ---------------------------------------------------------------
# 3. Same class using @property and @setter
# ---------------------------------------------------------------
class StudentP:
    def __init__(self, name, age):
        self.name = name
        self.age = age                          # goes through the setter below

    @property
    def age(self):                              # getter: s.age
        return self._age

    @age.setter
    def age(self, value):                       # setter: s.age = value
        if value > 0:
            self._age = value
        else:
            print("Error: age must be greater than 0 (got", str(value) + ")")
            self._age = getattr(self, "_age", 0)


print("Q3. @property / @setter")
sp = StudentP("Ravi", 22)
print(sp.name, sp.age)
sp.age = 0                                      # rejected by setter
sp.age = 23
print("Updated age:", sp.age)
print()


# ---------------------------------------------------------------
# 4. Read-only property
# ---------------------------------------------------------------
class Employee:
    def __init__(self, emp_id, name):
        self._id = emp_id
        self.name = name

    @property
    def id(self):                               # only a getter, no setter
        return self._id


print("Q4. Read-only property")
e = Employee(101, "Anu")
print("Employee id:", e.id)
try:
    e.id = 999
except AttributeError as err:
    print("Cannot change id ->", err)
print()


# ---------------------------------------------------------------
# 5. Bank Account System
# ---------------------------------------------------------------
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance                # private: only changed by methods

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.__balance += amount
        print("Deposited", amount, "-> balance", self.__balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance! Tried", amount, "but balance is", self.__balance)
        else:
            self.__balance -= amount
            print("Withdrew", amount, "-> balance", self.__balance)

    @property
    def balance(self):
        return self.__balance


print("Q5. Bank Account")
acc = BankAccount("Sahithi", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(5000)                              # blocked: balance can't go negative
print("Final balance:", acc.balance)
print()


# ---------------------------------------------------------------
# 6. Internal variables (single underscore)
#    '_' is only a convention meaning "internal, please don't touch".
#    Python does not block access.
# ---------------------------------------------------------------
class Config:
    def __init__(self):
        self.version = "1.0"
        self._secret_key = "abc123"             # internal use


print("Q6. Internal variables")
cfg = Config()
print("Public version :", cfg.version)
print("Internal key   :", cfg._secret_key, "(accessible, but should not be used outside)")
print()


# ---------------------------------------------------------------
# 7. Computed property
# ---------------------------------------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):                             # calculated every time it is read
        return self.length * self.width


print("Q7. Computed property")
r = Rectangle(5, 4)
print("Area:", r.area)
r.length = 10
print("After length = 10, area:", r.area)
print()


# ---------------------------------------------------------------
# 8. Password validation system
# ---------------------------------------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.__password = None

    def set_password(self, password):
        # rule 1: at least 8 characters
        length = 0
        for _ in password:
            length += 1
        if length < 8:
            print("'" + password + "' rejected: must be at least 8 characters")
            return False
        # rule 2: must contain a number
        has_digit = False
        for ch in password:
            if "0" <= ch <= "9":
                has_digit = True
                break
        if not has_digit:
            print("'" + password + "' rejected: must contain a number")
            return False
        self.__password = password
        print("Password set successfully")
        return True


print("Q8. Password validation")
u = User("sahithi")
u.set_password("abc")
u.set_password("abcdefgh")
u.set_password("python2026")
