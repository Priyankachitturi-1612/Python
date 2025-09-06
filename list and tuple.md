# ✅ **What is a List in Python?**

* A **list** is a **collection of items** (numbers, strings, objects, etc.).
* It is **ordered**, **mutable** (can change), and allows **duplicates**.

Example:
```python
nums = [10, 20, 30, 40]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.5, True]
```
📌 Properties:

* **Ordered** → items keep their order
* **Mutable** → can add, remove, or change values
* **Indexed** → first element is at index `0`
* **Duplicates allowed** → `[1,1,2,2]` is valid


# ✅ **Important List Functions / Methods**

Here’s a handy **list of commonly used ones** with examples:

### **1. append() → Add single item**

```python
nums = [1, 2, 3]
nums.append(4)
print(nums)   # [1, 2, 3, 4]
```

---

### **2. extend() → Add multiple items**

```python
nums = [1, 2, 3]
nums.extend([4, 5])
print(nums)   # [1, 2, 3, 4, 5]
```


### **3. insert() → Insert at position**

```python
nums = [1, 2, 4]
nums.insert(2, 3)   # insert 3 at index 2
print(nums)   # [1, 2, 3, 4]
```

---

### **4. remove() → Remove first occurrence**

```python
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)   # [1, 3, 2]
```

---

### **5. pop() → Remove by index (default last)**

```python
nums = [10, 20, 30]
nums.pop()
print(nums)   # [10, 20]
nums.pop(0)
print(nums)   # [20]
```

---

### **6. index() → Find index of value**

```python
nums = [10, 20, 30]
print(nums.index(20))  # 1
```

---

### **7. count() → Count occurrences**

```python
nums = [1, 2, 2, 3, 2]
print(nums.count(2))   # 3
```

---

### **8. sort() → Sort list**

```python
nums = [5, 2, 8, 1]
nums.sort()
print(nums)   # [1, 2, 5, 8]
```

---

### **9. reverse() → Reverse in place**

```python
nums = [1, 2, 3]
nums.reverse()
print(nums)   # [3, 2, 1]
```

---

### **10. copy() → Shallow copy**

```python
nums = [1, 2, 3]
copy_nums = nums.copy()
print(copy_nums)   # [1, 2, 3]
```

---

### **11. clear() → Remove all items**

```python
nums = [1, 2, 3]
nums.clear()
print(nums)   # []
```

---

# ✅ **Built-in Functions that Work on Lists**

Apart from methods, some **Python built-in functions** also work on lists:

* `len(nums)` → length of list
* `max(nums)` → largest element
* `min(nums)` → smallest element
* `sum(nums)` → sum of elements
* `sorted(nums)` → returns new sorted list
* `list(range(5))` → create list `[0,1,2,3,4]`

---

✨ Quick Example Using Many Functions Together:

```python
nums = [10, 5, 8, 5, 20]

print(len(nums))      # 5
print(max(nums))      # 20
print(min(nums))      # 5
print(sum(nums))      # 48
print(nums.count(5))  # 2
nums.sort()
print(nums)           # [5, 5, 8, 10, 20]
```


# ✅ **1. Create a list and print it**

```python
# Approach 1: Using split()
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("List:", nums)

# Approach 2: Using loop (fixed size)
n = int(input("How many numbers? "))
nums = []
for i in range(n):
    nums.append(int(input("Enter number: ")))
print("List:", nums)
```



# ✅ **2. Sum of all elements**

```python
nums = list(map(int, input("Enter numbers: ").split()))

# Approach 1: Built-in
print("Sum:", sum(nums))

# Approach 2: For loop
total = 0
for x in nums:
    total += x
print("Sum:", total)

# Approach 3: While loop
i, total = 0, 0
while i < len(nums):
    total += nums[i]
    i += 1
print("Sum:", total)
```


# ✅ **3. Largest and smallest element**

```python
nums = list(map(int, input("Enter numbers: ").split()))

# Approach 1: Built-in
print("Largest:", max(nums))
print("Smallest:", min(nums))

# Approach 2: Sort
nums.sort()
print("Smallest:", nums[0], "Largest:", nums[-1])

# Approach 3: Loop
largest, smallest = nums[0], nums[0]
for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest:", largest, "Smallest:", smallest)
```
Definition & basic syntax

A list comprehension builds a new list from an iterable using a compact single-line syntax

[ expression for item in iterable if condition]
expression → what goes into the new list (can be an expression or a function call).

for item in iterable → iterates source items.

if condition → (optional) filters items.

# ✅ **4. Count even and odd**

```python
nums = list(map(int, input("Enter numbers: ").split()))

# Approach 1: For loop
even = odd = 0
for x in nums:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# Approach 2: List comprehension
even = len([x for x in nums if x % 2 == 0])
odd = len(nums) - even
print("Even:", even, "Odd:", odd)

# Approach 3: filter()
even = len(list(filter(lambda x: x % 2 == 0, nums)))
odd = len(nums) - even
print("Even:", even, "Odd:", odd)
```


# ✅ **5. Reverse a list**

```python
nums = list(map(int, input("Enter numbers: ").split()))

# Approach 1: Slicing
print("Reversed:", nums[::-1])

# Approach 2: reversed()
print("Reversed:", list(reversed(nums)))

# Approach 3: Loop
rev = []
for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])
print("Reversed:", rev)

# Approach 4: Swapping
i, j = 0, len(nums)-1
while i < j:
    nums[i], nums[j] = nums[j], nums[i]
    i += 1
    j -= 1
print("Reversed in-place:", nums)
```



# ✅ **8. Sort ascending & descending**

```python
nums = list(map(int, input("Enter numbers: ").split()))

# Approach 1: sort()
nums.sort()
print("Ascending:", nums)
nums.sort(reverse=True)
print("Descending:", nums)

# Approach 2: sorted()
print("Ascending:", sorted(nums))
print("Descending:", sorted(nums, reverse=True))
```



# ✅ **9. Take input and print list**

```python
# Approach 1: One line
nums = list(map(int, input("Enter numbers: ").split()))
print("List:", nums)

# Approach 2: Loop
n = int(input("How many numbers? "))
nums = []
for i in range(n):
    nums.append(int(input("Enter number: ")))
print("List:", nums)
```
Great question Priya 🌸 — let’s go deep into **tuples** step by step.

---

# 🔹 What is a Tuple?

* A **tuple** is an **ordered, immutable** collection of items in Python.
* Looks like a list, but **cannot be changed** after creation.
* Defined with **round brackets `()`** instead of square brackets `[]`.

Example:

```python
my_tuple = (10, 20, 30, 40)
print(my_tuple)        # (10, 20, 30, 40)
print(type(my_tuple))  # <class 'tuple'>
```


# 🔹 Tuple Creation

```python
t1 = (1, 2, 3)        # Normal tuple
t2 = ()               # Empty tuple
t3 = (10,)            # Single element (must have comma!)
t4 = tuple([4, 5, 6]) # Using tuple() constructor
```

---

# 🔹 Tuple Operations

✅ Similar to lists but **no modification** allowed.

```python
t = (10, 20, 30, 40, 50)

# Indexing
print(t[0])   # 10
print(t[-1])  # 50

# Slicing
print(t[1:4])  # (20, 30, 40)

# Concatenation
t2 = (60, 70)
print(t + t2)  # (10, 20, 30, 40, 50, 60, 70)

# Repetition
print(t * 2)   # (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# Membership
print(20 in t)    # True
print(100 not in t) # True

# Iteration
for i in t:
    print(i, end=" ")  # 10 20 30 40 50
```

---

# 🔹 Tuple Methods

Tuples have very **few methods** because they are immutable.

1. **`count(value)`** → Returns how many times value appears

   ```python
   t = (1, 2, 2, 3, 2, 4)
   print(t.count(2))  # 3
   ```

2. **`index(value)`** → Returns first index of value

   ```python
   t = (10, 20, 30, 40)
   print(t.index(30))  # 2
   ```

---

# 🔹 Functions usable on Tuples

(Same as with lists, but without modification)

```python
t = (5, 10, 15, 20)

print(len(t))   # 4
print(max(t))   # 20
print(min(t))   # 5
print(sum(t))   # 50
print(sorted(t)) # [5, 10, 15, 20]  (returns list)
```

---

# 🔹 Nested Tuples

```python
t = (1, (2, 3), (4, 5, 6))
print(t[1][1])  # 3
```

---

# 🔹 Tuple Packing & Unpacking

```python
# Packing
person = ("Priya", 22, "Hyderabad")

# Unpacking
name, age, city = person
print(name)  # Priya
print(age)   # 22
print(city)  # Hyderabad
```

---

✅ **In short:**

* Tuples are like lists but **immutable**.
* Used when data should not change.
* Support indexing, slicing, iteration, but only **two methods** (`count`, `index`).

Perfect Priya 🌸 — let’s go **step by step** on tuple **packing and unpacking**, because it’s very common in Python.

---

# 🔹 1) Tuple Packing

**Packing** means **putting multiple values into a single variable (tuple)**.

Example:

```python
# Packing
person = ("Priya", 22, "Hyderabad")
print(person)           # ('Priya', 22, 'Hyderabad')
print(type(person))     # <class 'tuple'>
```

* Here, `"Priya"`, `22`, `"Hyderabad"` are **packed into the tuple `person`**.
* Packing can also be done **without parentheses**, Python will automatically pack into a tuple:

```python
person = "Priya", 22, "Hyderabad"
print(person)   # ('Priya', 22, 'Hyderabad')
```

---

# 🔹 2) Tuple Unpacking

**Unpacking** means **extracting values from a tuple into separate variables**.

Example:

```python
person = ("Priya", 22, "Hyderabad")

# Unpacking
name, age, city = person

print(name)  # Priya
print(age)   # 22
print(city)  # Hyderabad
```

✅ Key points:

* Number of variables on left **must match** the number of items in the tuple.
* Each variable receives the value from the tuple **in order**.


# 🔹 3) Using unpacking with user input

```python
person = (input("Enter name: "), int(input("Enter age: ")), input("Enter city: "))

name, age, city = person

print("Name:", name)
print("Age:", age)
print("City:", city)
```


# 🔹 4) Swapping values using unpacking

Python allows **swapping without temp variable**:

```python
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

* `a, b = b, a` is **tuple packing & unpacking in one line**.


# 🔹 5) Extended unpacking (Python 3+)

If you don’t want all values individually, you can use `*`:

```python
nums = (1, 2, 3, 4, 5)
a, *middle, b = nums
print(a)      # 1
print(middle) # [2, 3, 4]
print(b)      # 5
```


Here’s the code you shared:

```python
t = tuple(map(int, input().split()))
if len(t) > 1:
    t = (t[-1],) + t[1:-1] + (t[0],)
print(t)
```

## **Problem 1: Sum of all numeric elements**

Input: `1 2 3 4 5` → Output: `15`

**Approaches:**

**1️⃣ Using `sum()`**

```python
t = tuple(map(int, input("Enter numbers: ").split()))
print("Sum:", sum(t))
```

**2️⃣ Using for loop**

```python
t = tuple(map(int, input("Enter numbers: ").split()))
total = 0
for x in t:
    total += x
print("Sum:", total)
```

## **Problem 2: Count odd and even numbers**

Input: `1 2 3 4 5` → Output: `Even:2 Odd:3`

** For loop**

```python
t = tuple(map(int, input().split()))
even = odd = 0
for x in t:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)
```

**`filter()` + `len()`**

```python
t = tuple(map(int, input().split()))
even = len(list(filter(lambda x: x % 2 == 0, t)))
odd = len(t) - even
print("Even:", even, "Odd:", odd)
```

## **Problem : Reverse a tuple**

Input: `1 2 3 4` → Output: `(4,3,2,1)`

** Slicing**

```python
t = tuple(map(int, input().split()))
print("Reversed:", t[::-1])
```

** Using `reversed()`**

```python
t = tuple(map(int, input().split()))
print("Reversed:", tuple(reversed(t)))
```

## **Problem : Separate positive and negative numbers**

Input: `1 -2 3 -4` → Output: `(1,3) (-2,-4)`

**1️ Comprehension**

```python
t = tuple(map(int, input().split()))
pos = tuple(x for x in t if x>0)
neg = tuple(x for x in t if x<0)
print("Positive:", pos, "Negative:", neg)
```

**2 Using filter**

```python
t = tuple(map(int, input().split()))
pos = tuple(filter(lambda x: x>0, t))
neg = tuple(filter(lambda x: x<0, t))
print(pos, neg)
```

## **Problem : Swap first and last elements**

Input: `1 2 3 4` → Output: `(4,2,3,1)`

**1️⃣ Slicing + concatenation**

```python
t = tuple(map(int, input().split()))
if len(t)>1:
    t = (t[-1],) + t[1:-1] + (t[0],)
print(t)
```

## **Problem : Find common elements between two tuples**

Input: `(1 2 3)` and `(2 3 4)` → Output: `(2,3)`

**1️⃣ Comprehension**

```python
t1 = tuple(map(int, input("Tuple 1: ").split()))
t2 = tuple(map(int, input("Tuple 2: ").split()))
common = tuple(x for x in t1 if x in t2)
print(common)
```

