
## 🫧 **1. Bubble Sort (Step-by-Step)**

```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"\nPass {i+1}:")
        for j in range(n - i - 1):
            print(f"Compare {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                print(f"Swap {arr[j]} and {arr[j+1]}")
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print("Current array:", arr)
    return arr

arr = [5, 3, 8, 4, 2]
print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))
```

✅ **Output (Easy to Follow):**

```
Original array: [5, 3, 8, 4, 2]

Pass 1:
Compare 5 and 3
Swap 5 and 3
Current array: [3, 5, 8, 4, 2]
Compare 5 and 8
Current array: [3, 5, 8, 4, 2]
Compare 8 and 4
Swap 8 and 4
Current array: [3, 5, 4, 8, 2]
Compare 8 and 2
Swap 8 and 2
Current array: [3, 5, 4, 2, 8]

... (continues for Pass 2, Pass 3 ...)
Sorted array: [2, 3, 4, 5, 8]
```

---

## 🏆 **2. Selection Sort (Step-by-Step)**

```
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(f"\nPass {i+1}:")
        for j in range(i+1, n):
            print(f"Compare {arr[j]} with current minimum {arr[min_index]}")
            if arr[j] < arr[min_index]:
                min_index = j
        print(f"Swap {arr[i]} with {arr[min_index]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("Current array:", arr)
    return arr

arr = [5, 3, 8, 4, 2]
print("Original array:", arr)
print("Sorted array:", selection_sort(arr))
```

---

## 🧩 **3. Merge Sort (Step-by-Step)**

Got it! ✅
You want a **clean and simple Merge Sort code** (just like the snippet you wrote), with no extra prints — just the sorting logic.

Here’s the **exact code** in that style:

---

### 🧩 **Merge Sort (Simple & Clean Code)**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge step
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
arr = [5, 3, 8, 4, 2]
print("Original array:", arr)
print("Sorted array:", merge_sort(arr))
```

---

### ✅ **Output**

```
Original array: [5, 3, 8, 4, 2]
Sorted array: [2, 3, 4, 5, 8]
```


## ⚡ **4. Quick Sort (Step-by-Step)**

```
def quick_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    print("  " * depth + f"Pivot chosen: {pivot}")
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("  " * depth + f"Left: {left}, Middle: {middle}, Right: {right}")
    return quick_sort(left, depth+1) + middle + quick_sort(right, depth+1)

arr = [5, 3, 8, 4, 2]
print("Original array:", arr)
print("Sorted array:", quick_sort(arr))
```

---

### ✅ **These Codes Are:**

* **Easy to Read** (Beginner-friendly)
* **Step-by-Step Explained** (Prints after every important step)
* **Understandable** (Shows how array changes at each pass)

Absolutely! 🙌
Let’s go through **Bubble Sort, Selection Sort, Merge Sort, and Quick Sort** one by one —
I’ll give you **clear matter + simple explanation + easy points to remember**.

---

# 🫧 **1. Bubble Sort**

### 📖 **Matter:**

Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.
After each pass, the largest element "bubbles up" to its correct position at the end.

---

### 🧠 **Explanation (Easy):**

1. Compare `arr[0]` with `arr[1]`.
   If `arr[0] > arr[1]`, swap them.
2. Move to `arr[1]` and `arr[2]`, compare and swap if needed.
3. Keep going until the last pair.
4. After first pass, the largest element is at the last position.
5. Repeat the process for remaining elements until the array is sorted.

---

### 🔑 **Key Points:**

* Works by swapping neighbors until sorted.
* **Time Complexity:**

  * Worst case: O(n²)
  * Best case: O(n) (if already sorted)
* **Space Complexity:** O(1) (no extra space needed)
* **Easy to understand but slow** for large data.

---

---

# 🏆 **2. Selection Sort**

### 📖 **Matter:**

Selection Sort works by finding the smallest element from the unsorted part of the array and putting it at the beginning. It keeps selecting the minimum and placing it in order until the entire array is sorted.

---

### 🧠 **Explanation (Easy):**

1. Find the smallest element in the entire array.
2. Swap it with the first element.
3. Now, find the smallest element in the remaining array.
4. Swap it with the second element.
5. Continue until the whole array is sorted.

---

### 🔑 **Key Points:**

* Selects minimum and places it at correct position.
* **Time Complexity:** O(n²) (always compares even if sorted)
* **Space Complexity:** O(1)
* **Fewer swaps** than bubble sort but still slow for big data.

---

---

# 🧩 **3. Merge Sort**

### 📖 **Matter:**

Merge Sort is a **divide and conquer algorithm**.
It splits the array into two halves, sorts each half recursively, and then merges the two sorted halves.

---

### 🧠 **Explanation (Easy):**

1. Divide the array into two halves until single elements remain.
2. Merge two single elements into a sorted pair.
3. Merge sorted pairs into sorted groups.
4. Continue merging until the full array is combined in sorted order.

---

### 🔑 **Key Points:**

* **Divide and Conquer** approach.
* **Time Complexity:** O(n log n) (very efficient)
* **Space Complexity:** O(n) (uses extra space for merging)
* **Stable sorting algorithm** (keeps equal elements in order)
* **Good choice for large data**.

---

---

# ⚡ **4. Quick Sort**

### 📖 **Matter:**

Quick Sort is also a **divide and conquer algorithm**.
It chooses a **pivot** element, partitions the array into two sub-arrays (smaller than pivot and greater than pivot), and then recursively sorts the sub-arrays.

---

### 🧠 **Explanation (Easy):**

1. Choose a pivot (middle, first, last, or random element).
2. Put all elements smaller than pivot on left, larger on right.
3. Recursively sort left and right parts.
4. Combine to get fully sorted array.

---

### 🔑 **Key Points:**

* **Divide and Conquer** but faster in practice than merge sort (less memory).
* **Time Complexity:**

  * Average: O(n log n)
  * Worst case: O(n²) (if bad pivot chosen)
* **Space Complexity:** O(log n) (uses recursion stack)
* **Very efficient** for large data (most used in real life).

---

# 📝 **Quick Summary Table**

| Algorithm          | Working Style          | Time (Avg) | Space    | Best For                            |
| ------------------ | ---------------------- | ---------- | -------- | ----------------------------------- |
| **Bubble Sort**    | Swap adjacent elements | O(n²)      | O(1)     | Very small arrays, learning purpose |
| **Selection Sort** | Select min and swap    | O(n²)      | O(1)     | Small arrays, fewer swaps needed    |
| **Merge Sort**     | Divide & merge         | O(n log n) | O(n)     | Large arrays, stable sort           |
| **Quick Sort**     | Partition around pivot | O(n log n) | O(log n) | Large arrays, in-place fast sort    |



## 📝 **1. Sort an Array in Ascending Order**

### **Code (Easiest Way – Using Built-in Function)**

```python
arr = [5, 1, 4, 2, 8]
arr.sort()  # sorts in ascending order
print("Sorted Array:", arr)
```

✅ **Output:**

```
Sorted Array: [1, 2, 4, 5, 8]
```

---

## 📝 **2. Sort an Array in Descending Order**

### **Code:**

```python
arr = [10, 7, 15, 3, 9]
arr.sort(reverse=True)  # sorts in descending order
print("Sorted Array (Descending):", arr)
```

✅ **Output:**

```
Sorted Array (Descending): [15, 10, 9, 7, 3]
```

---

## 📝 **3. Find K-th Smallest Element**

### **Code:**

```python
arr = [7, 2, 1, 10, 5]
arr.sort()
k = 3
print(f"{k}rd smallest element is:", arr[k-1])
```

✅ **Output:**

```
3rd smallest element is: 5
```

---

## 📝 **4. Sort Names Alphabetically**

### **Code:**

```python
names = ["Zara", "Amit", "Rahul", "Kiran"]
names.sort()  # sorts alphabetically
print("Sorted Names:", names)
```

✅ **Output:**

```
Sorted Names: ['Amit', 'Kiran', 'Rahul', 'Zara']
```

---

## 📝 **5. Sort Based on Absolute Values**

### **Code:**

```python
arr = [-3, 1, -7, 4, -2]
arr.sort(key=abs)  # sort by absolute value
print("Sorted by Absolute Values:", arr)
```

✅ **Output:**

```
Sorted by Absolute Values: [1, -2, -3, 4, -7]
```

---

## 📝 **6. Sort Only Even Numbers (Keep Odd in Place)**

### **Code (Easy Approach):**

```python
arr = [9, 4, 2, 7, 6, 5]

# Extract even numbers and sort them
evens = sorted([x for x in arr if x % 2 == 0])

# Place back sorted evens into original array
j = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = evens[j]
        j += 1

print("Array after sorting evens only:", arr)
```

✅ **Output:**

```
Array after sorting evens only: [9, 2, 4, 7, 6, 5]
```

---

## 📝 **7. Check If Array is Already Sorted**

### **Code:**

```python
arr = [1, 3, 5, 7, 9]
if arr == sorted(arr):
    print("Array is already sorted")
else:
    print("Array is not sorted")
```

✅ **Output:**

```
Array is already sorted
```

---

## 📝 **8. Sort Students by Marks**

### **Code:**

```python
students = [("A", 50), ("B", 90), ("C", 70)]
students.sort(key=lambda x: x[1])  # sort by marks (second value)
print("Sorted by Marks:", students)
```

✅ **Output:**

```
Sorted by Marks: [('A', 50), ('C', 70), ('B', 90)]
```

---

## 📝 **9. Sort and Remove Duplicates**

### **Code:**

```python
arr = [4, 2, 4, 3, 2, 1]
arr = sorted(set(arr))  # remove duplicates using set, then sort
print("Sorted without duplicates:", arr)
```

✅ **Output:**

```
Sorted without duplicates: [1, 2, 3, 4]
```

---

## 📝 **10. Sort in Wave Form**

### **Code (Easy Way):**

```python
arr = [10, 5, 6, 3, 2, 20]
arr.sort()  # sort first

# Swap adjacent pairs to make wave
for i in range(0, len(arr)-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]

print("Wave Form Array:", arr)
```

✅ **Output:**

```
Wave Form Array: [3, 2, 6, 5, 20, 10]
```

---

### 🧠 **Why These Are Easy Approaches**

* We used **Python’s built-in `sort()`** where possible (simplest way).
* For small variations (like even numbers only), we combined `sorted()` + list comprehension.
* No complicated manual sorting loops — so it's beginner-friendly.

