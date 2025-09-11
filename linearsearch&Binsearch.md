
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

---

Would you like me to also show you a **recursive version of Binary Search** (a bit more advanced, useful for interviews)?
