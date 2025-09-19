
## 🧠 1. What is Dynamic Programming?

**Dynamic Programming (DP)** is a technique used to solve problems by breaking them into **overlapping subproblems** and **reusing their solutions** instead of recomputing them.

> 📌 **Key Idea:** *"Remember what you already solved, so you don’t solve it again."*

---

### ✅ When to use DP

You use DP when:

1. The problem can be broken into **smaller subproblems**.
2. Those subproblems **repeat** (overlap).
3. You want an **optimal solution** (min, max, count, etc.).

---

### 🔑 Real-Life Analogy

Think of preparing tea ☕:

* If you boil water once and reuse it for multiple cups, you save time.
* DP is like storing intermediate work and reusing it later.

---

---

## 🧾 2. Memoization (Top-Down Approach)

**Memoization** = *"Remember what you computed during recursion."*

* You write a **recursive solution**.
* Store results in a cache (`dp` list/dict).
* Before recomputing, check the cache — if present, return directly.

---

### 🟢 Example: Fibonacci with Memoization

```
def fib_memo(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:          # if already computed
        return dp[n]
    dp[n] = fib_memo(n-1, dp) + fib_memo(n-2, dp)  # store result
    return dp[n]

n = 6
dp = [-1] * (n+1)       # create cache
print(f"Fibonacci({n}) =", fib_memo(n, dp))
```

🔍 **Working:**

* First time, `fib(3)` is computed.
* Next time if `fib(3)` is needed again, we **just read dp\[3]** — no extra recursion.

✅ **Time Complexity:** `O(n)`
✅ **Space Complexity:** `O(n)` (dp array + recursion stack)

---

---

## 📋 3. Tabulation (Bottom-Up Approach)

**Tabulation** = *"Build the solution iteratively from smaller problems."*

* You start from the **smallest subproblem**.
* Use a table (`dp` list) to store solutions.
* Build up to the final answer step by step.

---

### 🟢 Example: Fibonacci with Tabulation

```
def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print("Fibonacci(6) =", fib_tab(6))
```

🔍 **Working:**

* Start with `dp[0]=0, dp[1]=1`
* Compute `dp[2] = dp[1] + dp[0]`, then `dp[3]`, and so on, until `dp[n]`.

✅ **Time Complexity:** `O(n)`
✅ **Space Complexity:** `O(n)` (can be optimized to `O(1)` if we just keep last two values)


### 🧾 **Fibonacci using Normal Recursion (Python)**

```
    if n <= 1:
        return n  # Base case
    return fib(n - 1) + fib(n - 2)  # Recursive case

# Test
n = 5
print(f"Fibonacci of {n} is:", fib(n))
```

---

### 🔎 **Step-by-Step Execution (n = 5)**

Here’s how the calls happen:

```
fib(5)
 ├── fib(4)
 │    ├── fib(3)
 │    │    ├── fib(2)
 │    │    │    ├── fib(1) → 1
 │    │    │    └── fib(0) → 0
 │    │    └── fib(1) → 1
 │    └── fib(2)
 │         ├── fib(1) → 1
 │         └── fib(0) → 0
 └── fib(3)
      ├── fib(2)
      │    ├── fib(1) → 1
      │    └── fib(0) → 0
      └── fib(1) → 1
```

---

### 📊 Observations

* **Repeated Work:** Notice `fib(3)` and `fib(2)` are computed **multiple times**.
* This is why **normal recursion is slow** (exponential time complexity `O(2^n)`).
* This is exactly where **memoization** comes in — to store results and avoid recomputing them.

---

Would you like me to show you a **side-by-side comparison** of:

* **Normal recursion**
* **Memoization**
* **Tabulation**

for Fibonacci (with number of function calls), so you can see how DP makes it faster?


## 🆚 Memoization vs Tabulation

| Feature          | Memoization (Top-Down)                        | Tabulation (Bottom-Up)       |
| ---------------- | --------------------------------------------- | ---------------------------- |
| Approach         | Recursive + cache                             | Iterative (loop)             |
| Start Point      | Solve big problem first                       | Solve smallest problem first |
| Cache Access     | Before recursion (check)                      | Always build table           |
| Space            | `O(n)` + recursion stack                      | `O(n)` only                  |
| Easier to Write  | ✅ (if you know recursion)                     | Slightly more code           |
| Faster (usually) | ❌ Slightly slower (due to recursion overhead) | ✅ Faster, no recursion       |

---

### 🎯 Key Takeaways

* **Memoization** → Great for quickly converting a recursive solution into DP.
* **Tabulation** → More efficient (no recursion overhead), often preferred in interviews for large constraints.
* **Both do the same work**, just in different directions.

  

##  **Python Code **

``
def knapSack(W, wt, val, n):
    # Create a DP table initialized with 0
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                take = val[i - 1] + dp[i - 1][w - wt[i - 1]]
                skip = dp[i - 1][w]
                dp[i][w] = max(take, skip)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Example usage

n = int(input("Enter number of items: "))
val = list(map(int, input("Enter values: ").split()))
wt = list(map(int, input("Enter weights: ").split()))
W = int(input("Enter capacity of knapsack: "))

result = knapSack(W, wt, val, n)
print("Maximum value in Knapsack =", result)
```

---

## 🧠 **Step-by-Step Explanation**

### 🔹 Function Definition

```python
def knapSack(W, wt, val, n):
```

* `W` → Maximum weight the knapsack can carry.
* `wt` → List of weights of `n` items.
* `val` → List of values of `n` items.
* `n` → Total number of items.

This function will return the **maximum total value** that can be carried without exceeding `W`.

---

### 🔹 Create DP Table

```python
dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
```

* Creates a **2D DP table** of size `(n+1) x (W+1)`.
* Each cell `dp[i][w]` = max value possible using **first `i` items** with capacity `w`.
* We initialize with **0** (base case: if no items or capacity is 0 → value = 0).

Example for `n=3, W=5`:

```
Initial DP Table:
i/w  0  1  2  3  4  5
0    0  0  0  0  0  0
1    0  0  0  0  0  0
2    0  0  0  0  0  0
3    0  0  0  0  0  0
```

---

### 🔹 Filling DP Table (Bottom-Up)

```python
for i in range(1, n + 1):
    for w in range(1, W + 1):
```

* Loop over each item `i` (1 to n)
* Loop over each capacity `w` (1 to W)

We decide whether to **take item `i-1` or skip it**.

---

### 🔹 Decision Step

```python
if wt[i - 1] <= w:
    take = val[i - 1] + dp[i - 1][w - wt[i - 1]]
    skip = dp[i - 1][w]
    dp[i][w] = max(take, skip)
```

* **Condition:** `wt[i-1] <= w`
  Means this item **can fit** in current capacity `w`.

* `take` → Value if we **take the item**:

  * Add its value `val[i-1]`
  * Plus best solution for remaining capacity `w - wt[i-1]` using previous items.

* `skip` → Value if we **skip the item**:

  * Just use `dp[i-1][w]` (solution without this item).

* `dp[i][w] = max(take, skip)`
  Pick whichever gives maximum value.

---

### 🔹 If Item Doesn't Fit

```python
else:
    dp[i][w] = dp[i - 1][w]
```

* If current item weight > available capacity → we **cannot take it**,
  so we just copy value from row above.

---

### 🔹 Final Answer

```python
return dp[n][W]
```

* This is the last cell → maximum value using all `n` items with full capacity `W`.

---

### 🔹 Main Program

```python
n = int(input("Enter number of items: "))
val = list(map(int, input("Enter values: ").split()))
wt = list(map(int, input("Enter weights: ").split()))
W = int(input("Enter capacity of knapsack: "))
```

* Take user input for number of items, values, weights, and knapsack capacity.

```python
result = knapSack(W, wt, val, n)
print("Maximum value in Knapsack =", result)
```

* Call the function and print result.

---

## 🔑 **Key Idea**

* This approach **builds solutions step by step** → small capacities → larger capacities.
* Hence called **Bottom-Up DP**.
* `dp[i][w]` stores the best answer for first `i` items and capacity `w`.

---

### ✅ Example Walkthrough

Input:

```
n=3
val=[60, 100, 120]
wt=[10, 20, 30]
W=50
```

Filling `dp` step by step gives final answer:

```
Maximum value in Knapsack = 220
```

(by taking items 2 and 3).



## 🧠 Why We Use `i - 1` in 0/1 Knapsack

We are using a **2D DP table** `dp[i][w]` where:

* `i` = number of items we are considering (from 0 to n)
* `w` = current capacity we are checking (from 0 to W)

But our `wt[]` and `val[]` arrays are **0-indexed** (in Python/Java):

* `wt[0]` = weight of **1st item**
* `wt[1]` = weight of **2nd item**
* …

So, when we are at `i` (say i = 1 → first item), we actually need to look at `wt[i-1]` (because arrays start at 0).

---

### 🖊 Formula:

```python
if wt[i - 1] <= w:  # Can we take this item?
    take = val[i - 1] + dp[i - 1][w - wt[i - 1]]  # Take it
    skip = dp[i - 1][w]  # Or skip it
    dp[i][w] = max(take, skip)
```

---

### 🔎 Explanation of Each Term

1. **`wt[i-1] <= w`**

   * Check if weight of current item (`i-1`) fits in available capacity `w`.

2. **`take = val[i-1] + dp[i-1][w - wt[i-1]]`**

   * If we take this item, we add its value (`val[i-1]`)
   * Plus the best solution we can achieve using previous items (`i-1`) with reduced capacity (`w - wt[i-1]`).

3. **`skip = dp[i-1][w]`**

   * If we skip this item, we just take the best value for previous items (`i-1`) at same capacity `w`.

4. **`dp[i][w] = max(take, skip)`**

   * Choose whichever gives maximum value.

---

## 📌 Small Example to Understand `i-1`

Suppose:

```
n = 2
val = [50, 60]   # values of items
wt  = [1, 2]     # weights of items
W   = 3          # capacity
```

### DP Table Setup:

`dp` is of size `(n+1) x (W+1)` → `3 x 4`

| i/w | 0 | 1 | 2 | 3 |
| --- | - | - | - | - |
| 0   | 0 | 0 | 0 | 0 |
| 1   |   |   |   |   |
| 2   |   |   |   |   |

---

### Filling Step-by-Step:

#### i = 1 (Considering first item → wt\[0] = 1, val\[0] = 50)

* **w = 1** → wt\[0] = 1 ≤ w → can take
  `take = 50 + dp[0][0] = 50`
  `skip = dp[0][1] = 0`
  `dp[1][1] = max(50, 0) = 50`

* **w = 2** → still can take
  `take = 50 + dp[0][1] = 50`
  `skip = dp[0][2] = 0`
  `dp[1][2] = 50`

* **w = 3** → still can take
  `take = 50 + dp[0][2] = 50`
  `skip = dp[0][3] = 0`
  `dp[1][3] = 50`

Now table looks like:

| i/w | 0 | 1  | 2  | 3  |
| --- | - | -- | -- | -- |
| 0   | 0 | 0  | 0  | 0  |
| 1   | 0 | 50 | 50 | 50 |
| 2   |   |    |    |    |

---

#### i = 2 (Considering second item → wt\[1] = 2, val\[1] = 60)

* **w = 1** → wt\[1] = 2 > w → cannot take
  So `dp[2][1] = dp[1][1] = 50`

* **w = 2** → can take
  `take = 60 + dp[1][0] = 60 + 0 = 60`
  `skip = dp[1][2] = 50`
  `dp[2][2] = max(60, 50) = 60`

* **w = 3** → can take
  `take = 60 + dp[1][1] = 60 + 50 = 110`
  `skip = dp[1][3] = 50`
  `dp[2][3] = max(110, 50) = 110`

Final DP Table:

| i/w | 0 | 1  | 2  | 3   |
| --- | - | -- | -- | --- |
| 0   | 0 | 0  | 0  | 0   |
| 1   | 0 | 50 | 50 | 50  |
| 2   | 0 | 50 | 60 | 110 |

✅ Final answer = `dp[2][3] = 110` (Take both items)

---

### 🎯 Key Insight

* `i-1` is used because **our dp table starts from 1 but array indexes start from 0**.
* `dp[i][w]` = best value using **first `i` items** → the current item is `i-1` (0-based index).
* Without `i-1`, we would access wrong weight/value and break logic.



