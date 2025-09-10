## 🔹 What is Time Complexity?

* **Time complexity** tells us **how fast an algorithm runs** as the **input size grows**.
* It’s measured in terms of **number of operations relative to input size** (usually `n`).
* Python itself doesn’t calculate it automatically — it’s a **theoretical concept**, but important for writing efficient code.


## 🔹 Big O Notation

We usually use **Big O notation** to describe time complexity:

| Complexity | Meaning                             | Example                                  |
| ---------- | ----------------------------------- | ---------------------------------------- |
| O(1)       | Constant time – doesn’t grow with n | Accessing a list element `lst[5]`        |
| O(n)       | Linear time – grows with n          | Looping through a list `for x in lst`    |
| O(n^2)     | Quadratic – grows with square of n  | Nested loops (2 loops inside each other) |
| O(log n)   | Logarithmic – halves each step      | Binary search                            |
| O(n log n) | Linearithmic                        | Efficient sorting (`sorted()` in Python) |


## 🔹 Python Examples

### 1️⃣ Constant Time: O(1)

```python
lst = [1, 2, 3, 4, 5]
print(lst[2])  # Accessing element → O(1)
```

### 2️⃣ Linear Time: O(n)

```python
lst = [1, 2, 3, 4, 5]
for x in lst:
    print(x)  # Looping through all elements → O(n)
```

### 3️⃣ Quadratic Time: O(n^2)

```python
lst = [1, 2, 3]
for i in lst:
    for j in lst:
        print(i, j)  # Nested loops → O(n^2)
```

### 4️⃣ Logarithmic Time: O(log n)

* Example: **Binary search**

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

* Each step **halves the array** → O(log n)

Ah, Priya! Let me explain **O(n log n)** clearly — it’s very common in **sorting algorithms** and some divide-and-conquer algorithms. 😄



## 🔹 What is O(n log n)?

* It’s called **linearithmic time complexity**.
* The **log n** part comes from **halving the problem repeatedly** (like in binary search or merge sort).
* The **n** part comes from **processing all elements at each step**.

**So basically:**

> “Do something to all n elements at each level of log n steps.”



## 🔹 Example: Merge Sort (O(n log n))

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
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [5, 2, 4, 1, 3]
print(merge_sort(arr))
```

**Explanation of O(n log n):**

1. **log n levels** → each recursion splits the array in half (`arr[:mid]` and `arr[mid:]`).
2. **n work at each level** → merging all elements takes linear time.
3. **Total = n × log n** → O(n log n)



## 🔹 Real-Life Example in Python

* **`sorted()`** function in Python uses **Timsort** → average case O(n log n).

```python
nums = [5, 2, 4, 1, 3]
sorted_nums = sorted(nums)  # internally O(n log n)
print(sorted_nums)
```


### 🔹 Why Time Complexity Matters

1. Helps us **predict performance** for large inputs.
2. Lets us **choose efficient algorithms**.
3. Avoids writing code that is **too slow** for big datasets.


Here’s a simple table for **5 common complexities**:

| Complexity | Best Case                  | Average Case  | Worst Case  | Example in Python            |
| ---------- | -------------------------- | ------------- | ----------- | ---------------------------- |
| O(1)       | Constant                   | Constant      | Constant    | Access list element `lst[0]` |
| O(log n)   | 1 step                     | log n steps   | log n steps | Binary search on sorted list |
| O(n)       | 1 step (found first)       | n/2 steps ≈ n | n steps     | Linear search in list        |
| O(n log n) | n log n                    | n log n       | n log n     | Merge sort, Timsort          |
| O(n²)      | 1 step (minimal iteration) | n²/2 ≈ n²     | n² steps    | Nested loops, bubble sort    |


### 🔹 Explanation:

1. **O(1)** – Constant: Always the same time, doesn’t depend on input size.
2. **O(log n)** – Logarithmic: Each step halves the problem size (binary search).
3. **O(n)** – Linear: Time grows proportionally to number of elements (linear search).
4. **O(n log n)** – Linearithmic: Sorting algorithms like Merge Sort, Timsort.
5. **O(n²)** – Quadratic: Nested loops, comparing every pair of elements (Bubble sort).


