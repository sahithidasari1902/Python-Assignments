# Assignment 3: Loops & Control Flow in Python


# ---------------------------------------------------------------
# 1. Print a message 10 times using a for loop
# ---------------------------------------------------------------
print("Q1. Print message 10 times")
for i in range(10):
    print(i + 1, "Bright IT Career")
print()


# ---------------------------------------------------------------
# 2. Print numbers 1 to 20 using a while loop
# ---------------------------------------------------------------
print("Q2. Numbers 1 to 20 (while loop)")
num = 1
while num <= 20:
    print(num, end=" ")
    num += 1
print("\n")


# ---------------------------------------------------------------
# 3. Equal and Not Equal Check
# ---------------------------------------------------------------
print("Q3. Equal / Not Equal")
a = int(input("Enter first number : "))
b = int(input("Enter second number: "))
if a == b:
    print(a, "==", b, "-> the numbers are equal")
if a != b:
    print(a, "!=", b, "-> the numbers are not equal")
print()


# ---------------------------------------------------------------
# 4. Odd and Even Numbers from 1 to 50
# ---------------------------------------------------------------
print("Q4. Even and Odd numbers from 1 to 50")
print("Even:", end=" ")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()
print("Odd :", end=" ")
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")


# ---------------------------------------------------------------
# 5. Largest Among Three Numbers
# ---------------------------------------------------------------
print("Q5. Largest among three")
x, y, z = 45, 78, 23
largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z
print("Largest among", x, y, z, "is", largest)
print()


# ---------------------------------------------------------------
# 6. Even numbers between 10 and 20 using a while loop
# ---------------------------------------------------------------
print("Q6. Even numbers between 10 and 20")
n = 10
while n <= 20:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1
print("\n")


# ---------------------------------------------------------------
# 7. Armstrong Number
#    A number equal to the sum of its digits, each raised to the
#    power of the number of digits. Example: 153 = 1^3 + 5^3 + 3^3
# ---------------------------------------------------------------
def count_digits(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        number = number // 10       # remove last digit
        count += 1
    return count


def is_armstrong(number):
    digits = count_digits(number)
    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10           # take last digit
        power = 1
        for _ in range(digits):     # digit ** digits, done by hand
            power *= digit
        total += power
        temp //= 10
    return total == number


print("Q7. Armstrong Number")
for value in [153, 370, 123]:
    if is_armstrong(value):
        print(value, "is an Armstrong number")
    else:
        print(value, "is NOT an Armstrong number")
print()


# ---------------------------------------------------------------
# 8. Prime Number Check
#    A prime is divisible only by 1 and itself.
#    We only need to test divisors up to the square root.
# ---------------------------------------------------------------
def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


print("Q8. Prime Check")
for value in [2, 17, 21, 1]:
    print(value, "is prime" if is_prime(value) else "is NOT prime")
print()


# ---------------------------------------------------------------
# 9. Palindrome Number Check (reads the same backwards: 121)
# ---------------------------------------------------------------
def is_palindrome(number):
    original = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    return original == reverse


print("Q9. Palindrome Check")
for value in [121, 1331, 123]:
    print(value, "is a palindrome" if is_palindrome(value) else "is NOT a palindrome")
print()


# ---------------------------------------------------------------
# 10. Even or Odd using conditions
# ---------------------------------------------------------------
print("Q10. Even or Odd")
value = int(input("Enter a number: "))
if value % 2 == 0:
    print(value, "is Even")
else:
    print(value, "is Odd")
print()


# ---------------------------------------------------------------
# 11. Gender Identification
# ---------------------------------------------------------------
print("Q11. Gender Identification")
gender = input("Enter gender (M/F): ").strip()
if gender == "M" or gender == "m":
    print("Male")
elif gender == "F" or gender == "f":
    print("Female")
else:
    print("Invalid Input")
print()


# ---------------------------------------------------------------
# 12. Multiplication Table
# ---------------------------------------------------------------
print("Q12. Multiplication Table")
table = int(input("Enter a number for its table: "))
for i in range(1, 11):
    print(table, "x", i, "=", table * i)
print()


# ---------------------------------------------------------------
# 13. Count Digits in a Number (using a loop)
# ---------------------------------------------------------------
print("Q13. Count Digits")
value = int(input("Enter a number: "))
if value < 0:
    value = -value              # ignore the minus sign
print("Number of digits:", count_digits(value))
