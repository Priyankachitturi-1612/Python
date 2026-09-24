Absolutely. Below are **20 Python list problems** focused only on:

* List creation
* Indexing
* Traversal
* Updating
* Searching
* Aggregation
* **Without using shortcuts** such as `sum()`, `max()`, `min()`, `count()`, `index()`, `sort()`, etc.

I’ve included **code + sample input/output** for each, suitable for beginner students.

---

# 1. Create a list and print all elements

```python
n = int(input())

numbers = []

for i in range(n):
    value = int(input())
    numbers.append(value)

print(numbers)
```

**Input:**

```text
5
10
20
30
40
50
```

**Output:**

```text
[10, 20, 30, 40, 50]
```

---

# 2. Print each element using traversal

```python
numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):
    print(numbers[i])
```

**Output:**

```text
10
20
30
40
50
```

---

# 3. Print elements using their indexes

```python
numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])
```

**Output:**

```text
Index: 0 Value: 10
Index: 1 Value: 20
Index: 2 Value: 30
Index: 3 Value: 40
```

---

# 4. Print the first and last element

```python
numbers = [10, 20, 30, 40, 50]

print("First:", numbers[0])
print("Last:", numbers[len(numbers) - 1])
```

**Output:**

```text
First: 10
Last: 50
```

---

# 5. Print elements at even indexes

```python
numbers = [10, 20, 30, 40, 50, 60]

for i in range(0, len(numbers), 2):
    print(numbers[i])
```

**Output:**

```text
10
30
50
```

---

# 6. Print elements at odd indexes

```python
numbers = [10, 20, 30, 40, 50, 60]

for i in range(1, len(numbers), 2):
    print(numbers[i])
```

**Output:**

```text
20
40
60
```

---

# 7. Update all negative numbers to zero

```python
numbers = [10, -5, 20, -8, 15, -2]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(numbers)
```

**Output:**

```text
[10, 0, 20, 0, 15, 0]
```

---

# 8. Update all even numbers by multiplying them by 2

```python
numbers = [10, 15, 20, 25, 30]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = numbers[i] * 2

print(numbers)
```

**Output:**

```text
[20, 15, 40, 25, 60]
```

---

# 9. Search for an element

Do not use `in`.

```python
numbers = [10, 20, 30, 40, 50]

target = int(input())

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
```

**Input:**

```text
30
```

**Output:**

```text
Element found
```

---

# 10. Find the position of an element

Do not use `index()`.

```python
numbers = [10, 20, 30, 40, 50]

target = int(input())

position = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        position = i
        break

print("Position:", position)
```

**Input:**

```text
40
```

**Output:**

```text
Position: 3
```

If the element doesn't exist:

**Input:**

```text
100
```

**Output:**

```text
Position: -1
```

---

# 11. Count occurrences of an element

Do not use `count()`.

```python
numbers = [10, 20, 10, 30, 10, 40]

target = int(input())

count = 0

for i in range(len(numbers)):
    if numbers[i] == target:
        count += 1

print("Occurrences:", count)
```

**Input:**

```text
10
```

**Output:**

```text
Occurrences: 3
```

---

# 12. Find the sum of all elements

Do not use `sum()`.

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for i in range(len(numbers)):
    total = total + numbers[i]

print("Sum:", total)
```

**Output:**

```text
Sum: 150
```

---

# 13. Find the average of elements

Do not use `sum()`.

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for i in range(len(numbers)):
    total += numbers[i]

average = total / len(numbers)

print("Average:", average)
```

**Output:**

```text
Average: 30.0
```

---

# 14. Find the largest element

Do not use `max()`.

```python
numbers = [25, 10, 45, 30, 15]

largest = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]

print("Largest:", largest)
```

**Output:**

```text
Largest: 45
```

---

# 15. Find the smallest element

Do not use `min()`.

```python
numbers = [25, 10, 45, 30, 15]

smallest = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]

print("Smallest:", smallest)
```

**Output:**

```text
Smallest: 10
```

---

# 16. Count positive, negative and zero values

```python
numbers = [10, -5, 0, 20, -8, 0, 15]

positive = 0
negative = 0
zero = 0

for i in range(len(numbers)):
    if numbers[i] > 0:
        positive += 1
    elif numbers[i] < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
```

**Output:**

```text
Positive: 3
Negative: 2
Zero: 2
```

---

# 17. Find the sum of even and odd numbers separately

```python
numbers = [10, 15, 20, 25, 30, 35]

even_sum = 0
odd_sum = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_sum += numbers[i]
    else:
        odd_sum += numbers[i]

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)
```

**Output:**

```text
Even sum: 60
Odd sum: 75
```

---

# 18. Find the second largest element

Do not use `sort()`.

```python
numbers = [10, 50, 30, 40, 20]

largest = numbers[0]
second = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > largest:
        second = largest
        largest = numbers[i]
    elif numbers[i] > second and numbers[i] != largest:
        second = numbers[i]

print("Largest:", largest)
print("Second largest:", second)
```

**Output:**

```text
Largest: 50
Second largest: 40
```

---

# 19. Reverse a list using indexing

Do not use `reverse()` or slicing.

```python
numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
```

**Output:**

```text
50
40
30
20
10
```

---

# 20. Find the number of elements greater than the average

This combines **aggregation + traversal + comparison**.

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for i in range(len(numbers)):
    total += numbers[i]

average = total / len(numbers)

count = 0

for i in range(len(numbers)):
    if numbers[i] > average:
        count += 1

print("Average:", average)
print("Elements greater than average:", count)
```

**Output:**

```text
Average: 30.0
Elements greater than average: 2
```

### Concepts covered

| Problem | Main concept               |
| ------- | -------------------------- |
| 1       | List creation              |
| 2       | Traversal                  |
| 3       | Indexing                   |
| 4       | Positive/negative indexing |
| 5       | Index traversal            |
| 6       | Index traversal            |
| 7       | Updating                   |
| 8       | Updating                   |
| 9       | Searching                  |
| 10      | Searching + index          |
| 11      | Counting                   |
| 12      | Aggregation                |
| 13      | Average                    |
| 14      | Largest                    |
| 15      | Smallest                   |
| 16      | Counting categories        |
| 17      | Conditional aggregation    |
| 18      | Largest/second largest     |
| 19      | Reverse traversal          |
| 20      | Aggregation + traversal    |

These are a good progression before moving to **list methods, list comprehensions, nested lists, and more difficult list problems**.
