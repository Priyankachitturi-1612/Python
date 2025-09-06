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


