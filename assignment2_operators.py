# Assignment 2: Operators in Python


# ---------------------------------------------------------------
# 1. Basic Arithmetic Operations
# ---------------------------------------------------------------
def arithmetic_operations(a, b):
    print("Addition       :", a, "+", b, "=", a + b)
    print("Subtraction    :", a, "-", b, "=", a - b)
    print("Multiplication :", a, "*", b, "=", a * b)
    if b != 0:
        print("Division       :", a, "/", b, "=", a / b)   # '/' always gives a float
    else:
        print("Division       : cannot divide by zero")


# ---------------------------------------------------------------
# 2. Simulating Increment and Decrement
# ---------------------------------------------------------------
def increment_decrement(n):
    # Python has no ++ or --, so we use += 1 and -= 1
    print("Before increment:", n)
    n += 1                      # same as n = n + 1
    print("After  increment:", n)
    print("Before decrement:", n)
    n -= 1                      # same as n = n - 1
    print("After  decrement:", n)


# ---------------------------------------------------------------
# 3. Check if Two Numbers are Equal
# ---------------------------------------------------------------
def check_equal(a, b):
    if a == b:
        print(a, "and", b, "are equal")
    else:
        print(a, "and", b, "are NOT equal")


# ---------------------------------------------------------------
# 4. Relational Operators Demonstration
# ---------------------------------------------------------------
def relational_operators(a, b):
    print(a, "< ", b, ":", a < b)
    print(a, "<=", b, ":", a <= b)
    print(a, "> ", b, ":", a > b)
    print(a, ">=", b, ":", a >= b)


# ---------------------------------------------------------------
# 5. Find Smaller and Larger Numbers
# ---------------------------------------------------------------
def smaller_and_larger(a, b):
    # No min()/max(): we decide using a comparison operator
    if a < b:
        smaller, larger = a, b
    else:
        smaller, larger = b, a
    print("Smaller number:", smaller)
    print("Larger  number:", larger)


# ---------------------------------------------------------------
# 6. Combine Conditions - largest of three
# ---------------------------------------------------------------
def largest_of_three(a, b, c):
    # 'and' combines two conditions: both must be True
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print("Largest among", a, b, c, "is", largest)


# ---------------------------------------------------------------
# 7. Operator-Based Calculator
# ---------------------------------------------------------------
def calculator(a, op, b):
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Error: division by zero is not allowed")
            return
        result = a / b
    else:
        print("Invalid operator:", op)
        return
    print(a, op, b, "=", result)


# ---------------------------------------------------------------
# Driver code
# ---------------------------------------------------------------
print("Q1. Arithmetic Operations")
x = float(input("Enter first number : "))
y = float(input("Enter second number: "))
arithmetic_operations(x, y)
print()

print("Q2. Increment and Decrement")
increment_decrement(int(input("Enter a number: ")))
print()

print("Q3. Equality Check")
check_equal(x, y)
print()

print("Q4. Relational Operators")
relational_operators(x, y)
print()

print("Q5. Smaller and Larger")
smaller_and_larger(x, y)
print()

print("Q6. Largest of Three")
p = float(input("Enter number 1: "))
q = float(input("Enter number 2: "))
r = float(input("Enter number 3: "))
largest_of_three(p, q, r)
print()

print("Q7. Calculator")
n1 = float(input("Enter first number : "))
operator = input("Enter operator (+, -, *, /): ").strip()
n2 = float(input("Enter second number: "))
calculator(n1, operator, n2)
