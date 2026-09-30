# Assignment 11: File Handling in Python
# The program creates its own sample files next to this .py file.
import os
from datetime import datetime

folder = os.path.dirname(os.path.abspath(__file__))
sample = os.path.join(folder, "sample.txt")
user_file = os.path.join(folder, "user_notes.txt")
copy_file = os.path.join(folder, "sample_copy.txt")
log_file = os.path.join(folder, "log.txt")

# Create a sample file to work with
with open(sample, "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("File handling lets us read and write data.\n")
    f.write("JALA Academy assignments.\n")


# ---------------------------------------------------------------
# 1. Read a text file ('r' = read mode)
# ---------------------------------------------------------------
print("Q1. Read a file")
with open(sample, "r") as f:        # 'with' closes the file automatically
    print(f.read())


# ---------------------------------------------------------------
# 2. Write user input to a file ('w' overwrites, 'a' appends)
# ---------------------------------------------------------------
print("Q2. Write to a file")
text = input("Type a line to save: ")
with open(user_file, "w") as f:
    f.write(text + "\n")
more = input("Type another line to append: ")
with open(user_file, "a") as f:
    f.write(more + "\n")
with open(user_file, "r") as f:
    print("user_notes.txt now contains:")
    print(f.read())


# ---------------------------------------------------------------
# 3. read() vs readline() vs readlines()
# ---------------------------------------------------------------
print("Q3. read / readline / readlines")
with open(sample, "r") as f:
    print("read()      ->", repr(f.read()))            # whole file as one string
with open(sample, "r") as f:
    print("readline()  ->", repr(f.readline()))        # only the first line
with open(sample, "r") as f:
    print("readlines() ->", f.readlines())             # list of all lines
print()


# ---------------------------------------------------------------
# 4 + 5. seek() - move the cursor and read from there
# ---------------------------------------------------------------
print("Q4. seek() to a position")
with open(sample, "r") as f:
    f.seek(10)                      # jump to character position 10
    print("From position 10:", repr(f.readline()))

print("Q5. Read fixed characters from an index")
index = 25
count = 13
with open(sample, "r") as f:
    f.seek(index)
    print("Read", count, "chars from index", index, "->", repr(f.read(count)))
    print("Cursor is now at position", f.tell())
print()


# ---------------------------------------------------------------
# 6. Check file permissions
# ---------------------------------------------------------------
print("Q6. File permissions")
print("Readable? ", os.access(sample, os.R_OK))
print("Writable? ", os.access(sample, os.W_OK))
print("Exists?   ", os.access(sample, os.F_OK))
print()


# ---------------------------------------------------------------
# 7. Count lines, words and characters (manual counting)
# ---------------------------------------------------------------
print("Q7. Count lines, words, characters")
lines = 0
words = 0
chars = 0
with open(sample, "r") as f:
    for line in f:
        lines += 1
        in_word = False
        for ch in line:
            chars += 1
            if ch == " " or ch == "\n" or ch == "\t":
                in_word = False
            elif not in_word:
                words += 1          # a new word starts here
                in_word = True
print("Lines:", lines, "| Words:", words, "| Characters:", chars)
print()


# ---------------------------------------------------------------
# 8. Copy file content
# ---------------------------------------------------------------
print("Q8. Copy file")
with open(sample, "r") as src, open(copy_file, "w") as dst:
    for line in src:
        dst.write(line)
print("Copied sample.txt -> sample_copy.txt")
print()


# ---------------------------------------------------------------
# 9. Append with timestamp
# ---------------------------------------------------------------
print("Q9. Append with timestamp")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(log_file, "a") as f:
    f.write(now + " - Program ran successfully\n")
with open(log_file, "r") as f:
    print(f.read())
