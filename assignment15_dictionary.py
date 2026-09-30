# Assignment 15: Dictionaries in Python
# A dictionary stores key -> value pairs. Keys must be unique.


# 1. Create a dictionary: Student ID -> Name
print("Q1. Create dictionary")
students = {101: "Sahithi", 102: "Ravi", 103: "Anu", 104: "Kiran", 105: "Meena"}
print(students)
print()

# 1.1 Add new entries
print("Q1.1 Add entries")
students[106] = "Arjun"
students[107] = "Divya"
print(students)
print()

# 1.2 Update an existing value
print("Q1.2 Update")
students[102] = "Ravi Kumar"
print("Updated 102 ->", students[102])
print()

# 1.3 Access values
print("Q1.3 Access")
print("Student 103:", students[103])
print("All names:", end=" ")
for sid in students:
    print(students[sid], end=", ")
print("\n")

# 1.4 Iterate through keys and values
print("Q1.4 Keys and values")
for sid, name in students.items():
    print(" ", sid, "->", name)
print()

# 1.5 Only keys
print("Q1.5 Keys only")
for sid in students.keys():
    print(sid, end=" ")
print("\n")

# 1.6 Only values
print("Q1.6 Values only")
for name in students.values():
    print(name, end=" | ")
print("\n")

# 1.7 Nested dictionary
print("Q1.7 Nested dictionary")
details = {
    101: {"name": "Sahithi", "age": 21},
    102: {"name": "Ravi", "age": 22},
    103: {"name": "Anu", "age": 20},
}
print(details)
print()

# 1.8 Access nested values
print("Q1.8 Nested access")
print("Name of 101:", details[101]["name"])
print("Age of 101 :", details[101]["age"])
print()

# 1.9 Delete elements
print("Q1.9 Delete")
del students[104]
print("After del 104       :", students)
last = students.popitem()          # removes the most recently added pair
print("popitem() removed   :", last)
removed = students.pop(105)        # removes by key and returns the value
print("pop(105) removed    :", removed)
print("Now                 :", students)
print()

# 2. Check if a key exists
print("Q2. Key exists?")
for sid in [101, 999]:
    if sid in students:
        print(sid, "exists ->", students[sid])
    else:
        print(sid, "does not exist")
print()

# 3. Count entries (manual count, then len() to confirm)
print("Q3. Count")
count = 0
for _ in students:
    count += 1
print("Total students:", count, "(len() also gives", str(len(students)) + ")")
print()

# 4. Merge two dictionaries
print("Q4. Merge")
batch_a = {201: "Lakshmi", 202: "Suresh"}
batch_b = {203: "Pooja", 204: "Naveen"}
merged = {}
for k, v in batch_a.items():
    merged[k] = v
for k, v in batch_b.items():
    merged[k] = v
print(merged)
print()

# 5. Dictionary comprehension: number -> square
print("Q5. Dictionary comprehension")
squares = {n: n * n for n in range(1, 6)}
print(squares)
print()

# 6. Reverse dictionary: name -> ID
print("Q6. Reverse dictionary")
reversed_dict = {}
for sid, name in students.items():
    reversed_dict[name] = sid
print(reversed_dict)
