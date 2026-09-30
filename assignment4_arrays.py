# Assignment 4: Lists (Arrays) in Python
# Built-in helpers like sum(), max(), min(), sort(), reverse(), index()
# are NOT used - the logic is written with loops so it can be explained.


# 1. Sum of Elements
def list_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


# Length without len()
def list_length(numbers):
    count = 0
    for _ in numbers:
        count += 1
    return count


# 2. Average of Elements
def list_average(numbers):
    size = list_length(numbers)
    if size == 0:
        return 0
    return list_sum(numbers) / size


# 3. Find Index of an Element (-1 means not found)
def find_index(numbers, target):
    i = 0
    for n in numbers:
        if n == target:
            return i
        i += 1
    return -1


# 4. Check Element Presence
def contains(numbers, target):
    for n in numbers:
        if n == target:
            return True
    return False


# 5. Remove an Element (first occurrence) - returns a new list
def remove_element(numbers, target):
    result = []
    removed = False
    for n in numbers:
        if n == target and not removed:
            removed = True          # skip only the first match
            continue
        result = result + [n]
    return result


# 6. Copy a List
def copy_list(numbers):
    copy = []
    for n in numbers:
        copy = copy + [n]
    return copy


# 7. Insert Element at Position
def insert_at(numbers, index, value):
    result = []
    i = 0
    for n in numbers:
        if i == index:
            result = result + [value]
        result = result + [n]
        i += 1
    if index >= i:                  # index at or past the end -> add at end
        result = result + [value]
    return result


# 8. Find Minimum and Maximum
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest


# 9. Reverse a List
def reverse_list(numbers):
    result = []
    i = list_length(numbers) - 1
    while i >= 0:
        result = result + [numbers[i]]
        i -= 1
    return result


# 10. Find Duplicate Elements
def find_duplicates(numbers):
    duplicates = []
    size = list_length(numbers)
    for i in range(size):
        for j in range(i + 1, size):
            if numbers[i] == numbers[j] and not contains(duplicates, numbers[i]):
                duplicates = duplicates + [numbers[i]]
    return duplicates


# 11. Count Even and Odd Numbers
def count_even_odd(numbers):
    even = 0
    odd = 0
    for n in numbers:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# 12. Common Elements Between Two Lists
def common_elements(list1, list2):
    common = []
    for a in list1:
        if contains(list2, a) and not contains(common, a):
            common = common + [a]
    return common


# 13. Remove Duplicates - returns a new list
def remove_duplicates(numbers):
    result = []
    for n in numbers:
        if not contains(result, n):
            result = result + [n]
    return result


# 14. Second Largest Element
def second_largest(numbers):
    first = None
    second = None
    for n in numbers:
        if first is None or n > first:
            second = first
            first = n
        elif n != first and (second is None or n > second):
            second = n
    return second


# 15. Difference Between Max and Min
def max_min_difference(numbers):
    smallest, largest = min_max(numbers)
    return largest - smallest


# 16. Check for Specific Elements 12 and 23
def has_12_and_23(numbers):
    return contains(numbers, 12) and contains(numbers, 23)


# 17. Unique Elements Only (values that appear exactly once)
def unique_only(numbers):
    result = []
    for n in numbers:
        count = 0
        for m in numbers:
            if m == n:
                count += 1
        if count == 1:
            result = result + [n]
    return result


# 18. Frequency Count
def frequency(numbers):
    counts = {}
    for n in numbers:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    return counts


# 19. Sorting Without sort()/sorted() - Bubble Sort
#     Compare neighbours and swap them if they are in the wrong order.
#     After each pass the largest remaining value "bubbles" to the end.
def bubble_sort(numbers):
    arr = copy_list(numbers)
    size = list_length(arr)
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 20. Merge Two Lists Without Duplicates
def merge_unique(list1, list2):
    result = []
    for n in list1:
        if not contains(result, n):
            result = result + [n]
    for n in list2:
        if not contains(result, n):
            result = result + [n]
    return result


# ---------------------------------------------------------------
# Driver code
# ---------------------------------------------------------------
data = [12, 45, 7, 23, 45, 9, 12, 30]
other = [7, 30, 50, 60, 12]
print("List      :", data)
print("Other list:", other)
print()

print("Q1.  Sum                 :", list_sum(data))
print("Q2.  Average             :", list_average(data))

idx = find_index(data, 23)
print("Q3.  Index of 23         :", idx if idx != -1 else "not found")
idx = find_index(data, 100)
print("     Index of 100        :", idx if idx != -1 else "100 not found in the list")

print("Q4.  Contains 9?         :", contains(data, 9))
print("Q5.  Remove 45           :", remove_element(data, 45))
print("Q6.  Copy                :", copy_list(data))
print("Q7.  Insert 99 at index 2:", insert_at(data, 2, 99))
low, high = min_max(data)
print("Q8.  Min / Max           :", low, "/", high)
print("Q9.  Reversed            :", reverse_list(data))
print("Q10. Duplicates          :", find_duplicates(data))
evens, odds = count_even_odd(data)
print("Q11. Even count / Odd    :", evens, "/", odds)
print("Q12. Common with other   :", common_elements(data, other))
print("Q13. Without duplicates  :", remove_duplicates(data))
print("Q14. Second largest      :", second_largest(data))
print("Q15. Max - Min           :", max_min_difference(data))
print("Q16. Has 12 and 23?      :", has_12_and_23(data))
print("Q17. Unique only         :", unique_only(data))
print("Q18. Frequency           :", frequency(data))
print("Q19. Sorted (bubble)     :", bubble_sort(data))
print("Q20. Merged, no dupes    :", merge_unique(data, other))
