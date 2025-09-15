## 🔹 **What is Bubble Sort?**

Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.
After each pass, the largest element "bubbles up" to its correct position at the end.


###  **Explanation (Easy):**

1. Compare `arr[0]` with `arr[1]`.
   If `arr[0] > arr[1]`, swap them.
2. Move to `arr[1]` and `arr[2]`, compare and swap if needed.
3. Keep going until the last pair.
4. After first pass, the largest element is at the last position.
5. Repeat the process for remaining elements until the array is sorted.


### 🔑 **Key Points:**

* Works by swapping neighbors until sorted.
* **Time Complexity:**

  * Worst case: O(n²)
  * Best case: O(n) (if already sorted)
* **Space Complexity:** O(1) (no extra space needed)
* **Easy to understand but slow** for large data.
**Bubble Sort** is one of the simplest sorting algorithms.
It works like this:

* Compare **adjacent elements**.
* Swap them if they are in the wrong order.
* Repeat this process until the list is sorted.

🔑 **Key Idea:**
After the first pass, the **largest element “bubbles up” to the end**.
After the second pass, the second-largest element is at the second-last position, and so on.

## 🔹 **Simple Example Code**

Here’s the **easiest way** to write Bubble Sort in Python:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Number of passes
        for j in range(n - i - 1):  # Compare adjacent elements
            if arr[j] > arr[j + 1]:  # Swap if in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
numbers = [5, 2, 8, 1, 3]
print("Original List:", numbers)
print("Sorted List:", bubble_sort(numbers))
```

✅ **Output:**

```
Original List: [5, 2, 8, 1, 3]
Sorted List: [1, 2, 3, 5, 8]
```


## 🔹 **Explanation of Loops**

### ✅ **Outer Loop → `for i in range(n):`**

This loop decides **how many passes** we make through the list.
We need to do `n` passes because after every pass, the biggest element “bubbles” to the end.

For example, if `n = 5` (5 elements),

* **Pass 1** → biggest element is at last position
* **Pass 2** → 2nd biggest element is at 2nd last
* ... until all sorted

---

### ✅ **Inner Loop → `for j in range(n - i - 1):`**

This loop **compares adjacent elements** and swaps them if they are in wrong order.
Notice `n - i - 1`:

* After every pass, last `i` elements are already sorted, so we don't need to compare them again.
  This **reduces unnecessary comparisons** and makes sorting faster.

---

## 🔹 **Dry Run Example**

Take `numbers = [5, 2, 8, 1, 3]`

| Pass (i)       | Comparisons (j)                                                                                                                                    | Swaps Done | Result After Pass                 |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------------------------- |
| i=0 (1st pass) | Compare (5,2) → swap → \[2,5,8,1,3] <br> Compare (5,8) → no swap <br> Compare (8,1) → swap → \[2,5,1,8,3] <br> Compare (8,3) → swap → \[2,5,1,3,8] | 3 swaps    | Biggest element (8) moved to last |
| i=1 (2nd pass) | Compare (2,5) → no swap <br> Compare (5,1) → swap → \[2,1,5,3,8] <br> Compare (5,3) → swap → \[2,1,3,5,8]                                          | 2 swaps    | 2nd biggest (5) is now 2nd last   |
| i=2 (3rd pass) | Compare (2,1) → swap → \[1,2,3,5,8] <br> Compare (2,3) → no swap                                                                                   | 1 swap     | Now first 3 elements sorted       |
| i=3 (4th pass) | Compare (1,2) → no swap                                                                                                                            | 0 swaps    | Already sorted                    |

✅ **Final Sorted List:** `[1, 2, 3, 5, 8]`

---

### 🔑 **Takeaway**

* **Outer loop** → Number of passes needed (how many times we go through the list).
* **Inner loop** → Compare & swap adjacent elements for current pass.
* After each pass, **largest element moves to end**.

---

Would you like me to rewrite this code **without function and with print statements inside the loops** so you can see exactly what happens in each pass (live step-by-step)? That will make it super easy to follow.



## 🔹 **Practice Programs on Bubble Sort**

### ✅ 1. Sort in **Descending Order**

```python
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:  # Change condition for descending
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [5, 2, 8, 1, 3]
print("Descending Order:", bubble_sort_desc(numbers))
```

---

### ✅ 2. Sort a **List of Strings**

```python
def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Alphabetical order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

words = ["banana", "apple", "cherry", "mango"]
print("Sorted Words:", bubble_sort_strings(words))
```

---

### ✅ 3. Sort **Even and Odd Numbers Separately**

(Evens first, then odds, both in ascending order)

```
def bubble_sort_even_odd(arr):
    arr.sort()  # Simple sort first
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    return evens + odds

numbers = [5, 2, 8, 1, 3, 4]
print("Even then Odd:", bubble_sort_even_odd(numbers))
```


## 🔹 **What is Selection Sort?**

**Selection Sort** is a simple sorting algorithm that works like this:

1. Find the **smallest element** in the list.
2. Swap it with the **first element**.
3. Then find the **next smallest** and swap with the **second element**.
4. Repeat until the whole list is sorted.

💡 **Key Idea:** We keep "selecting" the smallest element and putting it at the correct position — that's why it’s called **Selection Sort**.
### 🔑 **Key Points:**

* Selects minimum and places it at correct position.
* **Time Complexity:** O(n²) (always compares even if sorted)
* **Space Complexity:** O(1)
* **Fewer swaps** than bubble sort but still slow for big data.

---

## 🔹 **Simple Example Code**

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):  # Move through each position
        min_index = i   # Assume current i is smallest
        for j in range(i+1, n):  # Find smallest in remaining list
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap smallest with element at i
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

numbers = [5, 2, 8, 1, 3]
print("Original List:", numbers)
print("Sorted List:", selection_sort(numbers))
```

✅ **Output:**

```
Original List: [5, 2, 8, 1, 3]
Sorted List: [1, 2, 3, 5, 8]
```

---

## 🔹 **Dry Run Example**

Take `[5, 2, 8, 1, 3]`

| Pass | i | min\_index found     | After Swap                    |
| ---- | - | -------------------- | ----------------------------- |
| 1    | 0 | 3 (value 1)          | `[1, 2, 8, 5, 3]`             |
| 2    | 1 | 1 (value 2)          | `[1, 2, 8, 5, 3]` (no change) |
| 3    | 2 | 4 (value 3)          | `[1, 2, 3, 5, 8]`             |
| 4    | 3 | 3 (value 5)          | `[1, 2, 3, 5, 8]`             |
| 5    | 4 | Already last element | `[1, 2, 3, 5, 8]` ✅           |

---

## 🔹 **Programs for Practice**

### ✅ 1. Selection Sort Without Function

```
arr = [5, 2, 8, 1, 3]
n = len(arr)

print("Original List:", arr)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted List:", arr)
```

---

### ✅ 2. Selection Sort in Descending Order

```
def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

numbers = [5, 2, 8, 1, 3]
print("Descending Order:", selection_sort_desc(numbers))
```

---

### ✅ 3. Selection Sort on Strings

```
words = ["banana", "apple", "cherry", "mango"]
n = len(words)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if words[j] < words[min_index]:  # Alphabetical order
            min_index = j
    words[i], words[min_index] = words[min_index], words[i]

print("Sorted Words:", words)
```


## 🔑 **When to Use Selection Sort**

* ✅ Easy to implement, good for **small lists**
* ❌ Not efficient for large datasets (O(n²) complexity)

---



## 🧩 **3. Merge Sort (Step-by-Step)**

Merge Sort is a **divide and conquer algorithm**.
It splits the array into two halves, sorts each half recursively, and then merges the two sorted halves.

### 🧠 **Explanation (Easy):**

1. Divide the array into two halves until single elements remain.
2. Merge two single elements into a sorted pair.
3. Merge sorted pairs into sorted groups.
4. Continue merging until the full array is combined in sorted order.

### 🔑 **Key Points:**

* **Divide and Conquer** approach.
* **Time Complexity:** O(n log n) (very efficient)
* **Space Complexity:** O(n) (uses extra space for merging)
* **Stable sorting algorithm** (keeps equal elements in order)
* **Good choice for large data**.


```
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
You want **custom key support** (like `key=len`) but still using **only one function** like your single-function merge sort.
Yes — we can absolutely do that! ✅

Here’s the modified version:

---

## ✅ **Merge Sort with Custom Key (Single Function)**

```python
def merge_sort(arr, key=lambda x: x):  # ✅ key argument (default: identity)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)

    # ✅ Merge step with custom key
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):  # <-- compare by key
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example: sort by length of words
words = ["cat", "elephant", "dog", "bear"]
print("Sorted by length:", merge_sort(words, key=len))
```

---

### ✅ **Output**

```
Sorted by length: ['cat', 'dog', 'bear', 'elephant']
```


## ⚡ 4. Quick Sort 

## 🔑 Why It Works

* Each step **puts the pivot in its correct position**.
* Then we **repeat the process** for left and right sides separately.
* Finally, we join everything together → sorted array.


## 🔑 Key Points (Super Simple)

* **Splitting happens in the `for` loop** (smaller to left, bigger to right)
* **Recursion stops when array size is 0 or 1**
* No merging like merge sort — we just stick parts together in order



Quick Sort is also a **divide and conquer algorithm**.
It chooses a **pivot** element, partitions the array into two sub-arrays (smaller than pivot and greater than pivot), and then recursively sorts the sub-arrays.


### 🧠 **Explanation (Easy):**

1. Choose a pivot (middle, first, last, or random element).
2. Put all elements smaller than pivot on left, larger on right.
3. Recursively sort left and right parts.
4. Combine to get fully sorted array.


### 🔑 **Key Points:**

* **Divide and Conquer** but faster in practice than merge sort (less memory).
* **Time Complexity:**

  * Average: O(n log n)
  * Worst case: O(n²) (if bad pivot chosen)
* **Space Complexity:** O(log n) (uses recursion stack)
* **Very efficient** for large data (most used in real life).


```
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [5, 3, 8, 4, 2]
print("Original array:", arr)
print("Sorted array:", quick_sort(arr))
```


Think of Quick Sort like this:
📦 **Pick a pivot** (a reference number)
📦 **Put all smaller numbers on the left**, bigger numbers on the right
📦 **Repeat the same for left side and right side** until everything is sorted.

-

## 🔹 2. Easiest Quick Sort Code

```python
def quick_sort(arr):
    if len(arr) <= 1:  # ✅ Base case: stop when array has 1 or 0 elements
        return arr

    pivot = arr[0]  # ✅ Pick first element as pivot (easy choice)
    left = []   # smaller elements go here
    right = []  # bigger elements go here

    for x in arr[1:]:  # ✅ Start from second element (skip pivot)
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    # ✅ Sort left & right recursively, then combine results
    return quick_sort(left) + [pivot] + quick_sort(right)
```

---

## 🔹 3. Step-by-Step Example

Let’s take `arr = [5, 2, 8, 1, 3]`

---

### **Step 1: First Call**

* **Pivot = 5**
* `left = [2, 1, 3]` (all smaller than 5)
* `right = [8]` (all bigger than 5)

Now sort left and right **separately**.

---

### **Step 2: Sort Left (\[2, 1, 3])**

* Pivot = 2
* left = \[1]
* right = \[3]
  Sorted left = `[1, 2, 3]`

---

### **Step 3: Sort Right (\[8])**

* Only one element → already sorted → `[8]`

---

### **Step 4: Combine**

`sorted_left + pivot + sorted_right`
`[1, 2, 3] + [5] + [8] = [1, 2, 3, 5, 8]`



---

# 📝 **Quick Summary Table**

| Algorithm          | Working Style          | Time (Avg) | Space    | Best For                            |
| ------------------ | ---------------------- | ---------- | -------- | ----------------------------------- |
| **Bubble Sort**    | Swap adjacent elements | O(n²)      | O(1)     | Very small arrays, learning purpose |
| **Selection Sort** | Select min and swap    | O(n²)      | O(1)     | Small arrays, fewer swaps needed    |
| **Merge Sort**     | Divide & merge         | O(n log n) | O(n)     | Large arrays, stable sort           |
| **Quick Sort**     | Partition around pivot | O(n log n) | O(log n) | Large arrays, in-place fast sort    |






# 📚 **Heap Sort **

## ✅ **Definition**

Heap Sort is a **comparison-based sorting algorithm** that uses a **binary heap data structure**.
It works by first building a **max heap** from the input data, then repeatedly extracting the largest element from the heap and placing it at the end of the array.

---

## 🧠 **Key Concepts**

* **Heap** → A complete binary tree that satisfies the **heap property**:

  * **Max-Heap**: Parent node is always **greater than or equal** to its children.
  * **Min-Heap**: Parent node is always **less than or equal** to its children.
* Heap is usually stored as an **array**:

  * For node at index `i`:

    * Left child → `2*i + 1`
    * Right child → `2*i + 2`
    * Parent → `(i-1) // 2`

---

## 🔄 **Algorithm Steps**

1. **Build Max Heap** from the array.
2. Swap the root (largest element) with the last element.
3. Reduce heap size by 1.
4. Call `heapify` on root to maintain max-heap property.
5. Repeat until entire array is sorted.


## ⏱ **Time Complexity**

| Step                | Complexity     |
| ------------------- | -------------- |
| Building max heap   | **O(n)**       |
| Heapify per element | **O(log n)**   |
| Total (n elements)  | **O(n log n)** |

✅ **Overall Complexity:** **O(n log n)** (for best, average, worst case)

---

## 💾 **Space Complexity**

* **O(1)** (in-place sorting, no extra array needed)


## 🟢 **Advantages**

* Guaranteed **O(n log n)** performance (no worst-case like Quick Sort).
* Works **in-place** (no extra memory).
* Good for large datasets where memory is limited.

---

## 🔴 **Disadvantages**

* **Not stable** (relative order of equal elements may change).
* Slightly slower than Quick Sort in practice due to overhead of heap operations.



## 🧠 **When to Use Heap Sort**

* When you need **O(n log n)** performance **guaranteed** (even in worst case).
* When you have **limited extra memory**.
* When **stability is not required**.



```
def heap_sort(arr):
    n = len(arr)   # Step 1: Get number of elements in array

    # Step 2: Define heapify function inside heap_sort
    # heapify() will maintain the max-heap property for a subtree
    def heapify(i, size):
        largest = i               # Assume root is largest
        left = 2 * i + 1          # Index of left child
        right = 2 * i + 2         # Index of right child

        # If left child exists and is greater than root -> update largest
        if left < size and arr[left] > arr[largest]:
            largest = left

        # If right child exists and is greater than current largest -> update largest
        if right < size and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and recursively heapify affected subtree
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(largest, size)  # Recursively fix the subtree

    # Step 3: Build max heap
    # Start from last non-leaf node and heapify each one
    for i in range(n // 2 - 1, -1, -1):
        heapify(i, n)

    # Step 4: Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move largest element (root) to end
        heapify(0, i)  # Heapify remaining part (reduce size by 1 each time)
```

---

## 🔎 **How It Works (Step by Step)**

Let’s take `arr = [12, 11, 13, 5, 6, 7]`

### **Step 1: Build Max Heap**

We start heapifying from last non-leaf node (`n // 2 - 1 = 2`) backwards.

✅ After building max heap → `arr = [13, 11, 12, 5, 6, 7]`
(Largest element 13 is now at root, index 0)

---

### **Step 2: Sorting**

Now we repeatedly swap root with last element and heapify reduced array:

| Iteration | Swap Root with End               | After Swap              | After Heapify (Max Heap)         |
| --------- | -------------------------------- | ----------------------- | -------------------------------- |
| 1         | Swap `13` (root) with `7` (last) | `[7, 11, 12, 5, 6, 13]` | `[12, 11, 7, 5, 6, 13]`          |
| 2         | Swap `12` with `6`               | `[6, 11, 7, 5, 12, 13]` | `[11, 6, 7, 5, 12, 13]`          |
| 3         | Swap `11` with `5`               | `[5, 6, 7, 11, 12, 13]` | `[7, 6, 5, 11, 12, 13]`          |
| 4         | Swap `7` with `5`                | `[5, 6, 7, 11, 12, 13]` | `[6, 5, 7, 11, 12, 13]`          |
| 5         | Swap `6` with `5`                | `[5, 6, 7, 11, 12, 13]` | `[5, 6, 7, 11, 12, 13]` ✅ Sorted |

---

### **Final Output**

```
Original array: [12, 11, 13, 5, 6, 7]
Sorted array:   [5, 6, 7, 11, 12, 13]
```

## **Step 0: Original Array as Binary Tree**

Array: `[12, 11, 13, 5, 6, 7]`
Tree representation (indices in parentheses):

```
        12(0)
       /     \
   11(1)     13(2)
   /   \     /
 5(3) 6(4) 7(5)
```



**Heap after building max heap:**

```
        13
       /  \
     11    12
    /  \   /
   5    6 7
```

Array now: `[13, 11, 12, 5, 6, 7]`

---

## **Step 2: Extract Max and Heapify**

### **Iteration 1: Swap root with last element (index 5)**

* Swap 13 ↔ 7
* Array: `[7, 11, 12, 5, 6, 13]`
* Heapify root (index 0):

```
        7
       / \
     11   12
    /  \
   5    6
```

* Largest child 12 → swap 7 and 12

```
        12
       /  \
     11    7
    /  \
   5    6
```

Array now: `[12, 11, 7, 5, 6, 13]`

* 13 is now at the **sorted position** (end of array)

---

### **Iteration 2: Swap root with index 4**

* Swap 12 ↔ 6
* Array: `[6, 11, 7, 5, 12, 13]`
* Heapify root (6):

```
        6
       / \
     11   7
    /
   5
```

* Largest child 11 → swap 6 and 11

```
        11
       /  \
      6    7
     /
    5
```

Array now: `[11, 6, 7, 5, 12, 13]`

* 12 and 13 are sorted at the end

---

### **Iteration 3: Swap root with index 3**

* Swap 11 ↔ 5
* Array: `[5, 6, 7, 11, 12, 13]`
* Heapify root (5):

```
        5
       / \
      6   7
```

* Largest child 7 → swap 5 and 7

```
        7
       / \
      6   5
```

Array now: `[7, 6, 5, 11, 12, 13]`

* 11,12,13 are sorted

---

### **Iteration 4: Swap root with index 2**

* Swap 7 ↔ 5
* Array: `[5, 6, 7, 11, 12, 13]`
* Heapify root (5):

```
        6
       /
      5
```

* Largest child 6 → swap 5 and 6

```
        6
       /
      5
```

Array now: `[6, 5, 7, 11, 12, 13]`

---

### **Iteration 5: Swap root with index 1**

* Swap 6 ↔ 5
* Array now fully sorted: `[5, 6, 7, 11, 12, 13]`

---

## ✅ **Final Sorted Array**

```
[5, 6, 7, 11, 12, 13]
```

---

### 🔑 **Key Takeaways from the Tree Diagram**

1. Heap Sort **builds max heap** first (largest at root).
2. Repeatedly **swap root with last element** → reduces heap size.
3. **Heapify the reduced heap** to maintain max heap.
4. Sorted elements accumulate at the **end of the array**.


## 🎯 Key Idea

* **heapify()** ensures each subtree follows **max heap property**.
* We **build max heap once**, then keep removing largest element (root) and placing it at the end.
* Each `heapify()` call takes `O(log n)` time, and we do it for `n` elements → **O(n log n)** overall.


