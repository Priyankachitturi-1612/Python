# 🔹 1. What is an Array in Python?

An array is a collection of elements stored under one variable name.
In other languages (like C/Java), arrays are type restricted (all elements must be the same type).
In Python, we usually use lists to represent arrays.
Python lists can store mixed data types, but when we treat them as arrays, we usually keep same type of elements for clarity.
An **array** is a collection of elements stored in a single variable.
In Python, we use **lists** to represent arrays.

👉 Example (1D Array):

```python
arr = [10, 20, 30, 40, 50]   # 1D array
print(arr[0])   # Access first element → 10
print(arr[2])   # Access third element → 30
```

👉 Example (2D Array):

```python
arr2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]   # 2D array

print(arr2d[0][1])   # 2 (row 0, col 1)
print(arr2d[2][2])   # 9 (row 2, col 2)
```

---

# 🔹 2. Array Operations (using lists)

| Operation    | Example             | Output               |
| ------------ | ------------------- | -------------------- |
| **Access**   | `arr[1]`            | Get element at index |
| **Update**   | `arr[1] = 99`       | Change value         |
| **Traverse** | `for x in arr:`     | Visit each element   |
| **Insert**   | `arr.insert(2, 15)` | Insert at index      |
| **Append**   | `arr.append(60)`    | Add at end           |
| **Delete**   | `arr.remove(30)`    | Remove by value      |
| **Pop**      | `arr.pop(2)`        | Remove by index      |
| **Length**   | `len(arr)`          | Count elements       |
| **Slicing**  | `arr[1:4]`          | Sub-array            |

---

# 🔹 3. Array Methods (List Methods)

| Method         | Example                            | Result |
| -------------- | ---------------------------------- | ------ |
| `append(x)`    | `[1,2].append(3)` → `[1,2,3]`      |        |
| `insert(i, x)` | `[1,2].insert(1, 99)` → `[1,99,2]` |        |
| `remove(x)`    | `[1,2,3].remove(2)` → `[1,3]`      |        |
| `pop(i)`       | `[1,2,3].pop(1)` → `[1,3]`         |        |
| `index(x)`     | `[1,2,3].index(2)` → `1`           |        |
| `count(x)`     | `[1,2,2,3].count(2)` → `2`         |        |
| `sort()`       | `[3,1,2].sort()` → `[1,2,3]`       |        |
| `reverse()`    | `[1,2,3].reverse()` → `[3,2,1]`    |        |
| `copy()`       | `arr.copy()` → clone               |        |
| `clear()`      | `arr.clear()` → `[]`               |        |

---

# 🔹 4. Example Programs

### ✅ 1D Array Programs

**1. Traverse and print elements**

```python
arr = [10, 20, 30, 40, 50]

print("Elements in array:")
for i in arr:
    print(i, end=" ")
```

**2. Find sum of elements**

```python
arr = [10, 20, 30, 40]
print("Sum:", sum(arr))   # 100
```

**3. Find max and min**

```python
arr = [10, 50, 30, 20, 40]
print("Max:", max(arr))   # 50
print("Min:", min(arr))   # 10
```

**4. Search element**

```python
arr = [10, 20, 30, 40, 50]
x = 30
if x in arr:
    print(x, "found at index", arr.index(x))
else:
    print(x, "not found")
```

---

### ✅ 2D Array Programs

**1. Traverse a 2D Array**

```python
arr2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D Array Elements:")
for row in arr2d:
    for val in row:
        print(val, end=" ")
    print()
```

**2. Sum of all elements in 2D Array**

```python
arr2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0
for row in arr2d:
    total += sum(row)

print("Sum:", total)   # 45
```

**3. Transpose of a 2D Array**

```python
arr2d = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [[arr2d[j][i] for j in range(len(arr2d))] for i in range(len(arr2d[0]))]

print("Transpose:", transpose)   # [[1, 4], [2, 5], [3, 6]]
```


✅ **Summary for Students:**

* In Python, **lists act as arrays**.
* You can do all array operations (insert, delete, update, traverse) with list methods.
* Lists can represent **1D and 2D arrays** easily.

---
Perfect Priya 👌 — let’s go **step by step** and cover **multiple approaches** for the three problems you asked:

---

# **1️⃣ Count Frequency of Elements in a 1D Array (List)**

### **Approach 1: Using Dictionary + Loop**

```python
arr = [10, 20, 10, 30, 20, 10]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency:", freq)
```

### **Approach 2: Using `dict.get()`**

```python
arr = [10, 20, 10, 30, 20, 10]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

print("Frequency:", freq)
```


### **Approach 4: Using `set()` + `count()`**

```python
arr = [10, 20, 10, 30, 20, 10]
unique = set(arr)
freq = {x: arr.count(x) for x in unique}

print("Frequency:", freq)
```

### **Approach 5: Using Loop + List of Tuples**

```python
arr = [10, 20, 10, 30, 20, 10]
freq_list = []
for x in set(arr):
    freq_list.append((x, arr.count(x)))

print("Frequency as tuples:", freq_list)
```

---

# **2️⃣ Find Second Largest Element in a 1D Array (List)**

### **Approach 1: Sort + Pick Second Last**

```python
arr = [10, 20, 50, 40, 30]
unique = list(set(arr))  # remove duplicates
unique.sort()
print("Second largest:", unique[-2])
```

### **Approach 2: Two Pass Without Sort**

```python
arr = [10, 20, 50, 40, 30]
unique = list(set(arr))
largest = max(unique)
unique.remove(largest)
second_largest = max(unique)
print("Second largest:", second_largest)
```



### **Approach 5: Sort Descending + Pick Index 1**

```python
arr = [10, 20, 50, 40, 30]
unique = list(set(arr))
unique.sort(reverse=True)
print("Second largest:", unique[1])
```

---

# **3️⃣ Move All Zeros to End in a 1D Array (List)**

### **Approach 1: Using List Comprehension**

```python
arr = [0, 10, 0, 20, 30, 0, 40]
non_zero = [x for x in arr if x != 0]
zeros = [0] * arr.count(0)
result = non_zero + zeros
print("After moving zeros:", result)
```

### **Approach 2: Using Loop**

```python
arr = [0, 10, 0, 20, 30, 0, 40]
result = []
count_zeros = 0

for x in arr:
    if x != 0:
        result.append(x)
    else:
        count_zeros += 1

result.extend([0]*count_zeros)
print("After moving zeros:", result)
```


### **Approach 4: Using `filter()`**

```python
arr = [0, 10, 0, 20, 30, 0, 40]
non_zero = list(filter(lambda x: x != 0, arr))
zeros = [0] * (len(arr) - len(non_zero))
result = non_zero + zeros
print("After moving zeros:", result)
```

### **Approach 5: Using `remove()` in Loop**

```python
arr = [0, 10, 0, 20, 30, 0, 40]
count = arr.count(0)
for _ in range(count):
    arr.remove(0)
arr.extend([0]*count)
print("After moving zeros:", arr)
```

---

✅ Priya, now you have **5 different approaches** for **each of the 3 problems**:

1. Count frequency
2. Find second largest
3. Move zeros to end

---

If you want, I can **combine all these 15 programs into a single ready-to-use lesson sheet** for students with explanations and expected output — so you can give it directly in class.

Do you want me to do that?

Do you want me to also prepare a **PDF-style notes format** with these explanations + programs so you can directly share it with your students?
Removing duplicate elements from array
## 🔹 Approach 1: Using `dict.fromkeys()` (short & clean ✅)

```python
arr = [10, 20, 30, 20, 40, 10, 50]
unique = list(dict.fromkeys(arr))
print("Unique:", unique)
```

👉 Output:

```
[10, 20, 30, 40, 50]
```

---

## 🔹 Approach 2: Using a Loop (manual check)

```python
arr = [10, 20, 30, 20, 40, 10, 50]
unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Unique:", unique)
```

👉 Output:

```
[10, 20, 30, 40, 50]
```

---

## 🔹 Approach 3: Using List Comprehension

```python
arr = [10, 20, 30, 20, 40, 10, 50]
unique = []
[unique.append(x) for x in arr if x not in unique]

print("Unique:", unique)
```

👉 Output:

```
[10, 20, 30, 40, 50]
```

---

## 🔹 Approach 4: Using `set()` + Loop (to preserve order)

```python
arr = [10, 20, 30, 20, 40, 10, 50]
seen = set()
unique = []

for num in arr:
    if num not in seen:
        seen.add(num)
        unique.append(num)

print("Unique:", unique)
```

👉 Output:

```
[10, 20, 30, 40, 50]
```
⚡ This is **efficient** because checking `in set` is faster than `in list`.

✅ **Summary:**

* Easiest → `dict.fromkeys()`
* Beginner-friendly → loop method
* Efficient → set + loop

