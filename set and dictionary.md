# 🔹 What is a **Set** in Python?

* A **set** is an **unordered collection of unique elements**.
* **No duplicates allowed**.
* Elements are **not indexed** (no position numbers).
* Defined using **curly braces `{}`** or `set()` constructor.

---

## **Examples of Sets**

```python
# Using {}
s1 = {1, 2, 3, 4, 4}
print(s1)  # {1, 2, 3, 4} → duplicate removed

# Using set()
s2 = set([1, 2, 2, 3])
print(s2)  # {1, 2, 3}

# Empty set
s3 = set()
print(type(s3))  # <class 'set'>
```

✅ Key points:

* Sets **cannot have duplicates**
* Sets are **unordered**, so elements may not print in the same order
* Sets are **mutable** → you can add or remove elements

---

# 🔹 Set Operations

| Operation                | Example   | Description                                  |                                            |
| ------------------------ | --------- | -------------------------------------------- | ------------------------------------------ |
| **Union**                | \`s1      | s2\`                                         | Combine all unique elements from both sets |
| **Intersection**         | `s1 & s2` | Elements common to both sets                 |                                            |
| **Difference**           | `s1 - s2` | Elements in `s1` but not in `s2`             |                                            |
| **Symmetric Difference** | `s1 ^ s2` | Elements in either `s1` or `s2` but not both |                                            |
| **Membership**           | `x in s1` | Check if element exists in set               |                                            |

---

### **Examples of Set Operations**

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Union
print(s1 | s2)       # {1, 2, 3, 4, 5, 6}

# Intersection
print(s1 & s2)       # {3, 4}

# Difference
print(s1 - s2)       # {1, 2}
print(s2 - s1)       # {5, 6}

# Symmetric Difference
print(s1 ^ s2)       # {1, 2, 5, 6}

# Membership
print(3 in s1)       # True
print(7 in s1)       # False
```

---

# 🔹 Set Methods

| Method             | Description                            | Example             |
| ------------------ | -------------------------------------- | ------------------- |
| `add(elem)`        | Add an element                         | `s.add(10)`         |
| `update(iterable)` | Add multiple elements                  | `s.update([20,30])` |
| `remove(elem)`     | Remove element (error if not found)    | `s.remove(3)`       |
| `discard(elem)`    | Remove element (no error if not found) | `s.discard(3)`      |
| `pop()`            | Remove and return an arbitrary element | `x = s.pop()`       |
| `clear()`          | Remove all elements                    | `s.clear()`         |
| `copy()`           | Return a shallow copy                  | `s2 = s.copy()`     |

---

### **Examples of Set Methods**

```python
s = {1, 2, 3}

# Add
s.add(4)  
print(s)  # {1, 2, 3, 4}

# Update
s.update([5, 6])
print(s)  # {1, 2, 3, 4, 5, 6}

# Remove / Discard
s.remove(6)  
s.discard(10)  # No error even if 10 not in set

# Pop
x = s.pop()  # Removes and returns an element (random)
print(x, s)

# Copy
s2 = s.copy()
print(s2)

# Clear
s.clear()
print(s)  # set()
```

---

# 🔹 Key Points About Sets

* **Unordered** → cannot access by index: `s[0]` → ❌ Error
* **Unique** → duplicates are automatically removed
* **Mutable** → you can add/remove elements
* Good for **membership tests** and **set operations** like union/intersection/difference


## **1️⃣ Create a set from user input and print it**

```python
# Approach 1: Using set() and map
s = set(map(int, input("Enter numbers separated by space: ").split()))
print("Your set:", s)

# Approach 2: Using a for loop to add elements
nums = input("Enter numbers separated by space: ").split()
s2 = set()
for n in nums:
    s2.add(int(n))
print("Set using loop:", s2)
```

✅ This shows two ways to take user input and create a set.

---

## **2️⃣ Add and remove elements**

```python
s = {1, 2, 3}
print("Original set:", s)

# Add elements
s.add(4)
print("After add:", s)

# Add multiple elements
s.update([5, 6])
print("After update:", s)

# Remove element safely
s.discard(2)  # discard doesn't raise error if element not present
print("After discard:", s)

# Remove element (raises error if not found)
# s.remove(10)  # Uncomment to see error
```

✅ Demonstrates **add, update, discard, remove** methods.

---

## **3️⃣ Union, Intersection, Difference, Symmetric Difference**

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print("s1 | s2:", s1 | s2)  # Union
print("s1 & s2:", s1 & s2)  # Intersection
print("s1 - s2:", s1 - s2)  # Difference
print("s1 ^ s2:", s1 ^ s2)  # Symmetric Difference
```

✅ Classic **set operations** example.

---

## **4️⃣ Filter even numbers from user input**

```python
nums = set(map(int, input("Enter numbers: ").split()))

# Approach 1: Using comprehension
evens = {x for x in nums if x % 2 == 0}
print("Even numbers:", evens)

# Approach 2: Using filter() and lambda
evens2 = set(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter:", evens2)
```

✅ Shows **set comprehension** and **filter** with sets.

---

## **5️⃣ Find common elements between two sets**

```python
s1 = set(map(int, input("Enter first set: ").split()))
s2 = set(map(int, input("Enter second set: ").split()))

# Approach 1: Using & operator
common = s1 & s2
print("Common elements (&):", common)

# Approach 2: Using intersection() method
common2 = s1.intersection(s2)
print("Common elements (intersection):", common2)

# Approach 3: Using for loop
common3 = set()
for x in s1:
    if x in s2:
        common3.add(x)
print("Common elements (loop):", common3)
```

✅ Shows **operator, method, and loop** approaches to find common elements.

1. Creating sets
2. Adding/removing elements
3. Set operations (union, intersection, difference)
4. Filtering elements
5. Finding common elements


### 1. Find common elements in three sets

```python
a = {10, 20, 30, 40, 50, 60}
b = {20, 30, 50, 70, 80}
c = {30, 40, 50, 90}

common = a & b & c

print("Common elements:", common)
```

**Output:**

```text
Common elements: {50}
```

---

### 2. Find elements present in exactly one set

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
c = {7, 8, 9, 1}

result = a ^ b ^ c

print("Elements:", result)
```

**Output:**

```text
Elements: {2, 3, 6, 8, 9}
```

---

### 3. Find elements that occur in exactly two sets

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6}
c = {4, 5, 7, 8}

result = (a & b) | (b & c) | (a & c)
result -= a & b & c

print("Elements:", result)
```

**Output:**

```text
Elements: {3}
```

---

### 4. Find elements unique to each set

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {4, 5, 7, 8}

only_a = a - b - c
only_b = b - a - c
only_c = c - a - b

print("Only A:", only_a)
print("Only B:", only_b)
print("Only C:", only_c)
```

**Output:**

```text
Only A: {1, 2}
Only B: {6}
Only C: {7, 8}
```

---

### 5. Find missing numbers from a range

```python
numbers = {1, 2, 4, 6, 7, 10, 12}

start = 1
end = 12

complete = set(range(start, end + 1))

missing = complete - numbers

print("Missing numbers:", missing)
```

**Output:**

```text
Missing numbers: {3, 5, 8, 9, 11}
```

---

### 6. Find duplicate elements in a list using sets

```python
numbers = [10, 20, 30, 20, 40, 50, 30, 60, 10, 70]

seen = set()
duplicates = set()

for n in numbers:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print("Duplicates:", duplicates)
```

**Output:**

```text
Duplicates: {10, 20, 30}
```

---

### 7. Find elements occurring an odd number of times

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

unique = set(numbers)
result = set()

for n in unique:
    if numbers.count(n) % 2 != 0:
        result.add(n)

print("Odd frequency elements:", result)
```

**Output:**

```text
Odd frequency elements: {1, 3, 5}
```

---

### 8. Check whether two sets are disjoint

```python
a = {10, 20, 30, 40}
b = {50, 60, 70}

if a.isdisjoint(b):
    print("Sets are disjoint")
else:
    print("Sets are not disjoint")
```

**Output:**

```text
Sets are disjoint
```

---

### 9. Find common students between three classes

```python
python = {"A", "B", "C", "D", "E"}
java = {"B", "C", "D", "F"}
web = {"C", "D", "G", "H"}

common = python & java & web

print("Students in all three classes:", common)
```

**Output:**

```text
Students in all three classes: {'C', 'D'}
```

---

### 10. Find students who know Python but not Java

```python
python = {"A", "B", "C", "D", "E", "F"}
java = {"C", "D", "E"}
web = {"A", "E", "G"}

result = python - java

print("Python only:", result)
```

**Output:**

```text
Python only: {'A', 'B', 'F'}
```

---

### 11. Check subset and superset relationship

```python
employees = {"Java", "Python", "C", "SQL", "HTML", "CSS"}

required = {"Java", "Python", "SQL"}

if required.issubset(employees):
    print("All required skills are available")

if employees.issuperset(required):
    print("Employees set is a superset")
```

**Output:**

```text
All required skills are available
Employees set is a superset
```

---

### 12. Find common digits between two numbers

```python
n1 = 123456789
n2 = 567890

set1 = set(str(n1))
set2 = set(str(n2))

common = set1 & set2

print("Common digits:", common)
```

**Output:**

```text
Common digits: {'5', '6', '7', '8', '9'}
```

---

### 13. Find vowels present in a sentence

```python
sentence = "Python programming is powerful"

vowels = set("aeiou")

present = set(sentence.lower()) & vowels

print("Vowels present:", present)
```

**Output:**

```text
Vowels present: {'a', 'e', 'i', 'o'}
```

---

### 14. Find words appearing in both sentences

```python
sentence1 = "python java programming database"
sentence2 = "java python web development database"

words1 = set(sentence1.split())
words2 = set(sentence2.split())

common = words1 & words2

print("Common words:", common)
```

**Output:**

```text
Common words: {'python', 'java', 'database'}
```

---

### 15. Find numbers that satisfy multiple conditions using set comprehension

**Problem:** From 1 to 100, find numbers that are divisible by 3 or 5 but **not divisible by both**.

```python
numbers = set(range(1, 101))

divisible_by_3 = {n for n in numbers if n % 3 == 0}
divisible_by_5 = {n for n in numbers if n % 5 == 0}

result = divisible_by_3 ^ divisible_by_5

print("Numbers:", sorted(result))
```

**Output:**

```text
Numbers: [3, 5, 6, 9, 10, 12, 18, 20, 21, 24, 25, 27, 33, 35, 36, 39, 40, 42, 48, 50, 51, 54, 55, 57, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 95, 96, 99, 100]
```

### Important set concepts covered

| Concept                    | Problems            |   |
| -------------------------- | ------------------- | - |
| `&` Intersection           | 1, 3, 9, 12, 13, 14 |   |
| `                          | ` Union             | 3 |
| `-` Difference             | 4, 5, 10            |   |
| `^` Symmetric Difference   | 2, 15               |   |
| `issubset()`               | 11                  |   |
| `issuperset()`             | 11                  |   |
| `isdisjoint()`             | 8                   |   |
| Set comprehension          | 15                  |   |
| Duplicate detection        | 6, 7                |   |
| `set()` with strings/lists | 6, 12, 13, 14       |   |


# 🔹 What is a **Dictionary**?

* A **dictionary** is an **unordered collection of key-value pairs**.
* Each **key is unique**, and each key maps to a **value**.
* Defined using **curly braces `{}`** or the `dict()` constructor.

**Syntax:**

```python
my_dict = {"key1": value1, "key2": value2}
```

---

## **Examples**

```python
# Dictionary with strings as keys
student = {"name": "Priya", "age": 22, "city": "Hyderabad"}
print(student)

# Using numbers as keys
nums = {1: "one", 2: "two"}
print(nums)

# Empty dictionary
empty = {}
print(type(empty))  # <class 'dict'>
```

✅ Key points:

* Keys must be **immutable**: string, number, tuple (not list or dict)
* Values can be **any type**: int, string, list, tuple, another dict

---

# 🔹 Dictionary Operations

| Operation    | Description                    | Example                     |
| ------------ | ------------------------------ | --------------------------- |
| Access value | Get value by key               | `student["name"]` → "Priya" |
| Add/Update   | Add new key or update existing | `student["age"] = 23`       |
| Delete       | Remove a key-value pair        | `del student["city"]`       |
| Membership   | Check if key exists            | `"name" in student` → True  |

---

# 🔹 Dictionary Methods

| Method                       | Description                                                      | Example                            |
| ---------------------------- | ---------------------------------------------------------------- | ---------------------------------- |
| `get(key[, default])`        | Returns value for key, or default if key not found               | `student.get("name")`              |
| `keys()`                     | Returns all keys as a view                                       | `student.keys()`                   |
| `values()`                   | Returns all values as a view                                     | `student.values()`                 |
| `items()`                    | Returns key-value pairs as tuples                                | `student.items()`                  |
| `pop(key[, default])`        | Removes key and returns value                                    | `student.pop("age")`               |
| `popitem()`                  | Removes and returns last inserted key-value pair                 | `student.popitem()`                |
| `update(dict2)`              | Update dictionary with another dictionary                        | `student.update({"age": 23})`      |
| `clear()`                    | Removes all items                                                | `student.clear()`                  |
| `copy()`                     | Returns shallow copy                                             | `new_dict = student.copy()`        |
| `setdefault(key[, default])` | Returns value if key exists, else inserts key with default value | `student.setdefault("grade", "A")` |

---

# 🔹 Examples of Dictionary Methods

```python
student = {"name": "Priya", "age": 22, "city": "Hyderabad"}

# Access value
print(student["name"])      # Priya
print(student.get("city"))  # Hyderabad

# Keys, Values, Items
print(student.keys())   # dict_keys(['name', 'age', 'city'])
print(student.values()) # dict_values(['Priya', 22, 'Hyderabad'])
print(student.items())  # dict_items([('name', 'Priya'), ('age', 22), ('city', 'Hyderabad')])

# Add / Update
student["age"] = 23
student["grade"] = "A"
print(student)

# Delete
student.pop("grade")
print(student)
del student["city"]

# Copy
student2 = student.copy()
print(student2)

# Clear
student.clear()
print(student)
```

---

# 🔹 Key Points

* Dictionaries are **mutable** → you can change, add, or remove items
* **Keys must be unique**; duplicate keys are overwritten
* **Values can be anything** → int, string, list, tuple, dict, etc.
* Useful for **storing structured data** like JSON

---
Perfect Priya 🌸! Let’s do it step by step.
Here are **5 example programs on dictionaries**, each shown with **different approaches** (loops, comprehensions, methods).

---

# **1️⃣ Create a dictionary from user input**

👉 Input: `name Priya age 22 city Hyderabad`

```python
# Approach 1: Using split and loop
entries = input("Enter key-value pairs: ").split()
d = {}
for i in range(0, len(entries), 2):
    d[entries[i]] = entries[i+1]
print("Dictionary:", d)

# Approach 2: Using dict comprehension
entries = input("Enter key-value pairs: ").split()
d = {entries[i]: entries[i+1] for i in range(0, len(entries), 2)}
print("Dictionary:", d)
```

---

# **2️⃣ Count frequency of words**

👉 Input: `"apple banana apple mango banana apple"`
👉 Output: `{'apple': 3, 'banana': 2, 'mango': 1}`

```python
# Approach 1: Using loop
words = input("Enter words: ").split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# Approach 2: Using dict comprehension
freq2 = {w: words.count(w) for w in set(words)}
print(freq2)

# Approach 3: Using collections.Counter
from collections import Counter
print(Counter(words))
```

---

# **3️⃣ Swap keys and values in a dictionary**

👉 Input: `{'a': 1, 'b': 2, 'c': 3}`
👉 Output: `{1: 'a', 2: 'b', 3: 'c'}`

```python
d = {'a': 1, 'b': 2, 'c': 3}

# Approach 1: For loop
swapped = {}
for k, v in d.items():
    swapped[v] = k
print(swapped)

# Approach 2: Dict comprehension
swapped2 = {v: k for k, v in d.items()}
print(swapped2)
```

---

# **4️⃣ Merge two dictionaries**

👉 Input: `{'a': 1, 'b': 2}`, `{'b': 3, 'c': 4}`
👉 Output: `{'a': 1, 'b': 3, 'c': 4}`

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# Approach 1: Using update()
d1_copy = d1.copy()
d1_copy.update(d2)
print(d1_copy)

# Approach 2: Using dict unpacking (Python 3.5+)
merged = {**d1, **d2}
print(merged)

# Approach 3: Using dict comprehension
merged2 = {k: d2.get(k, d1.get(k)) for k in set(d1) | set(d2)}
print(merged2)
```

---

# **5️⃣ Filter dictionary by condition**

👉 Input: `{'a': 5, 'b': 12, 'c': 7}`
👉 Condition: keep only values > 10
👉 Output: `{'b': 12}`

```python
d = {'a': 5, 'b': 12, 'c': 7}

# Approach 1: For loop
filtered = {}
for k, v in d.items():
    if v > 10:
        filtered[k] = v
print(filtered)

# Approach 2: Dict comprehension
filtered2 = {k: v for k, v in d.items() if v > 10}
print(filtered2)
```

---

✨ These 5 examples cover:

1. Creating dictionaries
2. Counting frequencies
3. Swapping keys/values
4. Merging dictionaries
5. Filtering dictionaries

