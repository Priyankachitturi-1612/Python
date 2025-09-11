
## 🔎 1️⃣ Linear Search (Simple Search)

📌 **Concept:**

* Check each element one by one until you find the target.
* Works on **unsorted or sorted lists**.
* **Time Complexity:** O(n)

### ✅ Code Example:

```
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index where found
    return -1  # Not found


# Example usage
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr, target)
if result != -1:
    print(f"Linear Search: Found {target} at index {result}")
else:
    print(f"Linear Search: {target} not found")
```

## 🔎 2️⃣ Binary Search (Efficient Search)

📌 **Concept:**

* Works only on **sorted lists**.
* Divide the list into halves, repeatedly check the middle element.
* **Time Complexity:** O(log n)

### ✅ Iterative Binary Search Code:

```
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found


# Example usage
arr = [10, 20, 30, 40, 50]  # Must be sorted!
target = 30

result = binary_search(arr, target)
if result != -1:
    print(f"Binary Search: Found {target} at index {result}")
else:
    print(f"Binary Search: {target} not found")
```

---

## 🔑 Key Differences

| Feature            | Linear Search                   | Binary Search                                 |
| ------------------ | ------------------------------- | --------------------------------------------- |
| Works on           | Any list (sorted/unsorted)      | **Sorted list only**                          |
| Time Complexity    | O(n)                            | O(log n)                                      |
| Approach           | Sequential (check each element) | Divide & Conquer (cut list in half each time) |
| Speed (large data) | Slow                            | Fast                                          |

---

## ✅ Sample Output (If `target=30`)

```
Linear Search: Found 30 at index 2
Binary Search: Found 30 at index 2
```

Absolutely, Priya! 😊 I’ll give you **all 4 problems together**, each with its **Python code** and the **expected output** so you can see exactly what happens when you run them.

---

## **1️⃣ Linear Search – Find an Element in a List**

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [5, 8, 12, 20, 25]
target = 12

index = linear_search(arr, target)
print(f"Linear Search: Found at index {index}" if index != -1 else "Not found")
```

**Output:**

```
Linear Search: Found at index 2
```

---

## **2️⃣ Linear Search – Find the First Even Number**

```python
def first_even_index(arr):
    for i, val in enumerate(arr):
        if val % 2 == 0:
            return i
    return -1

arr = [7, 3, 9, 10, 14]

index = first_even_index(arr)
if index != -1:
    print(f"First even number {arr[index]} found at index {index}")
else:
    print("No even number found")
```

**Output:**

```
First even number 10 found at index 3
```

---

## **3️⃣ Binary Search – Search in a Sorted List**

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 4, 6, 8, 10, 15]
target = 8

index = binary_search(arr, target)
print(f"Binary Search: Found at index {index}" if index != -1 else "Not found")
```

**Output:**

```
Binary Search: Found at index 3
```

---

## **4️⃣ Binary Search – Find Smallest Number Greater Than Target**

```python
def smallest_greater(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

arr = [2, 5, 8, 12, 16]
target = 7

index = smallest_greater(arr, target)
if index != -1:
    print(f"Smallest number greater than {target} is {arr[index]} at index {index}")
else:
    print("No number greater than target found")
```

**Output:**

```
Smallest number greater than 7 is 8 at index 2
```

---

✅ **Summary**

* Linear search works on **any list**, sequentially.
* Binary search works only on **sorted lists**, efficiently.
* These codes are simple, easy to understand, and ready to run in VS Code.
