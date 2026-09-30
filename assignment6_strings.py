# Assignment 6: Strings in Python
import re


# 1. Creating strings in different ways
print("Q1. Creating Strings")
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = '''Triple single quotes
can span lines'''
s4 = """Triple double quotes
also span lines"""
print(s1)
print(s2)
print(s3)
print(s4)
print()

# 2. Concatenation
print("Q2. Concatenation")
first = "Bright IT"
second = "Career"
print(first + " " + second)
print()

# 3. Length (built-in len)
print("Q3. Length")
text = "Python Programming"
print("Length of '" + text + "' is", len(text))
print()

# 4. Substring using slicing  [start : end]  (end is not included)
print("Q4. Substring (slicing)")
print("text[0:6]  ->", text[0:6])      # Python
print("text[7:]   ->", text[7:])       # Programming
print("text[-4:]  ->", text[-4:])      # last 4 characters
print()

# 5. Search: find() returns -1 when not found, index() raises ValueError
print("Q5. Search")
print("find('Pro')  ->", text.find("Pro"))
print("find('Java') ->", text.find("Java"), "(-1 means not found)")
print("index('Pro') ->", text.index("Pro"))
try:
    print(text.index("Java"))
except ValueError:
    print("index('Java') -> ValueError: substring not found (handled)")
print()

# 6. Compare strings
print("Q6. Compare")
a = "hello"
b = "Hello"
print("'hello' == 'Hello' ->", a == b)     # case-sensitive
print("'hello' != 'Hello' ->", a != b)
print()

# 7. startswith() and endswith()
print("Q7. startswith / endswith")
file_name = "report_2026.pdf"
print("Starts with 'report'?", file_name.startswith("report"))
print("Ends with '.pdf'?    ", file_name.endswith(".pdf"))
print()

# 8. Lexicographical comparison (dictionary order, by character codes)
print("Q8. Lexicographical Comparison")
w1 = "apple"
w2 = "banana"
if w1 < w2:
    print("'" + w1 + "' comes before '" + w2 + "'")
elif w1 > w2:
    print("'" + w1 + "' comes after '" + w2 + "'")
else:
    print("Both strings are equal")
print()

# 9. strip() removes spaces at the start and end
print("Q9. strip()")
messy = "   Python   "
print("Before: [" + messy + "]")
print("After : [" + messy.strip() + "]")
print()

# 10. replace()
print("Q10. replace()")
sentence = "I like Java"
print(sentence, "->", sentence.replace("Java", "Python"))
print()

# 11. split()
print("Q11. split()")
csv_line = "red,green,blue"
print(csv_line, "->", csv_line.split(","))
print()

# 12. Integer to string
print("Q12. int -> str")
number = 2026
converted = str(number)
print(number, type(number))
print(converted, type(converted))
print()

# 13. Upper and lower case
print("Q13. upper / lower")
name = "Sahithi"
print(name.upper())
print(name.lower())
print()

# 14. Pattern matching with the re module
print("Q14. Pattern matching (re)")
email_pattern = r"^[\w.]+@[\w]+\.[a-z]{2,}$"
for email in ["sahithi@gmail.com", "wrong-email@", "abc.xyz@company.in"]:
    if re.match(email_pattern, email):
        print(email, "-> valid email")
    else:
        print(email, "-> invalid email")
for value in ["12345", "12a45"]:
    if re.fullmatch(r"\d+", value):
        print(value, "-> contains only digits")
    else:
        print(value, "-> not only digits")
print()

# 15. Count vowels and consonants (manual loop)
print("Q15. Vowels and Consonants")
word = "Bright IT Career"
vowels = 0
consonants = 0
for ch in word:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
        consonants += 1          # letters that are not vowels
print("Text:", word)
print("Vowels:", vowels, "| Consonants:", consonants)
print()

# 16. Reverse a string using slicing  [::-1] steps backwards
print("Q16. Reverse")
print(word, "->", word[::-1])
