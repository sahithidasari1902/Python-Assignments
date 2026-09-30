# Assignment 13: Functions & Flexible Arguments in Python


# 1. Function with parameters
def add(a, b):
    return a + b


# 2. Default parameter
def greet(name, message="Hello"):
    print(message + ", " + name + "!")


# 3. Keyword arguments
def show_person(name, age, city):
    print("Name:", name, "| Age:", age, "| City:", city)


# 4. *args - any number of positional values (arrives as a tuple)
def total(*args):
    result = 0
    for n in args:
        result += n
    return result


# 5. **kwargs - any number of key=value pairs (arrives as a dictionary)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print("  " + key + ": " + str(value))


# 6. Flexible function: number -> square, string -> uppercase
def flexible(value):
    if isinstance(value, (int, float)):
        print(value, "squared =", value * value)
    elif isinstance(value, str):
        print(value, "in uppercase =", value.upper())
    else:
        print("Unsupported type:", type(value))


# 7. Default + *args + **kwargs together
#    base price, optional extra item prices, optional discount/tax
def calculate_bill(base_price, *extra_items, discount=0, **charges):
    subtotal = base_price
    for item in extra_items:
        subtotal += item
    print("  Base + extras      :", subtotal)
    if discount > 0:
        subtotal -= subtotal * discount / 100
        print("  After", str(discount) + "% discount:", subtotal)
    for name, amount in charges.items():
        subtotal += amount
        print("  +", name, amount)
    print("  Final total        :", subtotal)
    return subtotal


# ---------------------------------------------------------------
# Driver code
# ---------------------------------------------------------------
print("Q1. add(10, 20) =", add(10, 20))
print()

print("Q2. Default parameter")
greet("Sahithi")
greet("Sahithi", "Good morning")
print()

print("Q3. Keyword arguments in different orders")
show_person(name="Sahithi", age=21, city="Hyderabad")
show_person(city="Vijayawada", name="Ravi", age=24)
show_person(age=22, city="Chennai", name="Anu")
print()

print("Q4. *args")
print("total(1, 2, 3)        =", total(1, 2, 3))
print("total(10, 20, 30, 40) =", total(10, 20, 30, 40))
print()

print("Q5. **kwargs")
print_details(name="Sahithi", course="Python", batch=2026)
print()

print("Q6. Flexible function")
flexible(7)
flexible("python")
print()

print("Q7. Advanced function (bill calculator)")
calculate_bill(1000, 200, 300, discount=10, delivery=50, tax=90)
print()

print("Q8. Lambda functions")
add_lambda = lambda a, b: a + b         # small one-line anonymous function
square = lambda x: x * x
print("add_lambda(5, 3) =", add_lambda(5, 3))
print("square(6)        =", square(6))
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Q9. map() - square every element")
print(numbers, "->", list(map(lambda x: x * x, numbers)))
print()

print("Q10. filter() - keep only even numbers")
print(numbers, "->", list(filter(lambda x: x % 2 == 0, numbers)))
