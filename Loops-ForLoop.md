# Loops in Python

A **loop** is used to execute a block of code **repeatedly**.

For example, instead of writing:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

we can use a loop:

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

So, the main purpose of a loop is:

> **Repeat a set of statements without writing the same code again and again.**

---

# Types of Loops in Python

Python mainly has **two types of loops**:

### 1. `for` loop

Used when we generally know **how many times** we want to iterate or when we want to iterate through a sequence.

```python
for i in range(5):
    print(i)
```

### 2. `while` loop

Used when repetition depends mainly on a **condition**.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Since you asked specifically for the **`for` loop**, let's focus completely on that.

---

# `for` Loop

### Syntax

```python
for variable in sequence:
    statement
```

Example:

```python
for i in range(1, 6):
    print(i)
```

Here:

* `i` → loop variable
* `range(1, 6)` → generates `1, 2, 3, 4, 5`
* `print(i)` → executes once for every value

### Important: `range()`

```python
range(start, stop, step)
```

The **stop value is excluded**.

Examples:

```python
range(5)
```

gives:

```text
0 1 2 3 4
```

```python
range(1, 6)
```

gives:

```text
1 2 3 4 5
```

```python
range(2, 11, 2)
```

gives:

```text
2 4 6 8 10
```

```python
range(10, 0, -1)
```

gives:

```text
10 9 8 7 6 5 4 3 2 1
```

---

# 20 `for` Loop Problems — Easy to Hard

---

## 1. Print numbers from 1 to 10

### Code

```python
for i in range(1, 11):
    print(i)
```

### Output

```text
1
2
3
4
5
6
7
8
9
10
```

---

# 2. Print even numbers from 1 to 20

```python
for i in range(2, 21, 2):
    print(i)
```

### Output

```text
2
4
6
8
10
12
14
16
18
20
```

Here:

```python
range(2, 21, 2)
```

means:

* Start = `2`
* Stop before = `21`
* Step = `2`

---

# 3. Print numbers from 10 to 1

```python
for i in range(10, 0, -1):
    print(i)
```

### Output

```text
10
9
8
7
6
5
4
3
2
1
```

---

# 4. Print multiplication table

### Problem

Take a number from the user and print its multiplication table.

```python
num = int(input())

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Input

```text
7
```

### Output

```text
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

---

# 5. Find the sum from 1 to N

### Problem

Take `N` from the user and calculate:

```text
1 + 2 + 3 + ... + N
```

```python
n = int(input())

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
```

### Input

```text
10
```

### Output

```text
Sum = 55
```

Calculation:

```text
1 + 2 + 3 + ... + 10 = 55
```

Here `total` is an **accumulator**.

---
Sure. Here are **20 `for` loop problems only on Counters and Accumulators**, at a similar difficulty level to the previous problems. I’ll avoid `while` loops and focus on **tracking values, counting, summing, and combining counters + accumulators**.

---

# A. Counter Problems

## 1. Count Even Numbers

Count how many even numbers are present among `n` numbers.

**Input**

```text
8
12
7
4
9
16
21
10
5
```

**Output**

```text
Even Count = 4
```

```python
n = int(input())
count = 0

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        count += 1

print("Even Count =", count)
```

---

## 2. Count Positive Numbers

**Input**

```text
7
10
-5
20
-3
0
15
-8
```

**Output**

```text
Positive Count = 3
```

```python
n = int(input())
count = 0

for i in range(n):
    num = int(input())

    if num > 0:
        count += 1

print("Positive Count =", count)
```

---

## 3. Count Numbers Greater Than 50

**Input**

```text
6
45
72
90
31
55
20
```

**Output**

```text
Count = 3
```

```python
n = int(input())
count = 0

for i in range(n):
    num = int(input())

    if num > 50:
        count += 1

print("Count =", count)
```

---

## 4. Count Numbers Divisible by 3 and 5

**Input**

```text
10
15
20
30
45
50
60
22
75
91
90
```

**Output**

```text
Count = 6
```

```python
n = int(input())
count = 0

for i in range(n):
    num = int(input())

    if num % 3 == 0 and num % 5 == 0:
        count += 1

print("Count =", count)
```

---

## 5. Count Numbers in a Range

Count numbers between **10 and 50 inclusive**.

**Input**

```text
7
5
12
25
60
40
8
50
```

**Output**

```text
Count = 4
```

```python
n = int(input())
count = 0

for i in range(n):
    num = int(input())

    if 10 <= num <= 50:
        count += 1

print("Count =", count)
```

---

## 6. Count Positive, Negative and Zero

**Input**

```text
8
10
-5
0
20
-3
7
0
-8
```

**Output**

```text
Positive = 3
Negative = 3
Zero = 2
```

```python
n = int(input())

positive = 0
negative = 0
zero = 0

for i in range(n):
    num = int(input())

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive =", positive)
print("Negative =", negative)
print("Zero =", zero)
```

---

# B. Accumulator Problems

## 7. Sum of N Numbers

**Input**

```text
5
10
20
30
40
50
```

**Output**

```text
Sum = 150
```

```python
n = int(input())
total = 0

for i in range(n):
    num = int(input())
    total += num

print("Sum =", total)
```

---

## 8. Sum of Even Numbers

Find the sum of all even numbers from 1 to 20.

**Output**

```text
Sum = 110
```

```python
total = 0

for i in range(1, 21):
    if i % 2 == 0:
        total += i

print("Sum =", total)
```

---

## 9. Sum of Odd Numbers

Find the sum of odd numbers from 1 to 15.

**Output**

```text
Sum = 64
```

```python
total = 0

for i in range(1, 16):
    if i % 2 != 0:
        total += i

print("Sum =", total)
```

---

## 10. Sum of Numbers Divisible by 5

Find the sum of numbers from 1 to 50 divisible by 5.

**Output**

```text
Sum = 275
```

```python
total = 0

for i in range(1, 51):
    if i % 5 == 0:
        total += i

print("Sum =", total)
```

---

## 11. Product of N Numbers

**Input**

```text
5
1
2
3
4
5
```

**Output**

```text
Product = 120
```

```python
n = int(input())
product = 1

for i in range(n):
    num = int(input())
    product *= num

print("Product =", product)
```

---

## 12. Sum of Squares

Find the sum of squares from 1 to 10.

**Output**

```text
Sum = 385
```

```python
total = 0

for i in range(1, 11):
    total += i ** 2

print("Sum =", total)
```

---

# C. Counter + Accumulator

## 13. Count Even Numbers and Find Their Sum

**Input**

```text
7
10
15
20
25
30
35
40
```

**Output**

```text
Even Count = 4
Even Sum = 100
```

```python
n = int(input())

count = 0
total = 0

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        count += 1
        total += num

print("Even Count =", count)
print("Even Sum =", total)
```

---

## 14. Count Positive Numbers and Find Their Sum

**Input**

```text
6
10
-5
20
-3
15
-8
```

**Output**

```text
Positive Count = 3
Positive Sum = 45
```

```python
n = int(input())

count = 0
total = 0

for i in range(n):
    num = int(input())

    if num > 0:
        count += 1
        total += num

print("Positive Count =", count)
print("Positive Sum =", total)
```

---

## 15. Count Numbers Greater Than 50 and Find Their Sum

**Input**

```text
7
45
70
90
25
80
40
60
```

**Output**

```text
Count = 4
Sum = 300
```

```python
n = int(input())

count = 0
total = 0

for i in range(n):
    num = int(input())

    if num > 50:
        count += 1
        total += num

print("Count =", count)
print("Sum =", total)
```

---

## 16. Count Multiples of 3 and Find Their Sum

**Input**

```text
8
3
5
6
10
12
15
20
18
```

**Output**

```text
Count = 5
Sum = 54
```

```python
n = int(input())

count = 0
total = 0

for i in range(n):
    num = int(input())

    if num % 3 == 0:
        count += 1
        total += num

print("Count =", count)
print("Sum =", total)
```

---

# D. Higher-Level Counter + Accumulator

## 17. Count Passed Students and Find Total Marks

Passing mark = 40.

**Input**

```text
6
75
35
80
45
25
65
```

**Output**

```text
Passed = 4
Total Marks = 325
```

```python
n = int(input())

passed = 0
total = 0

for i in range(n):
    marks = int(input())

    total += marks

    if marks >= 40:
        passed += 1

print("Passed =", passed)
print("Total Marks =", total)
```

---

## 18. Count Numbers in the Range 10–50 and Find Their Sum

**Input**

```text
8
5
15
25
60
40
8
50
30
```

**Output**

```text
Count = 5
Sum = 160
```

```python
n = int(input())

count = 0
total = 0

for i in range(n):
    num = int(input())

    if 10 <= num <= 50:
        count += 1
        total += num

print("Count =", count)
print("Sum =", total)
```

---

## 19. Count Even and Odd Numbers + Find Both Sums

**Input**

```text
6
10
15
20
25
30
35
```

**Output**

```text
Even Count = 3
Even Sum = 60
Odd Count = 3
Odd Sum = 75
```

```python
n = int(input())

even_count = 0
odd_count = 0

even_sum = 0
odd_sum = 0

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        even_count += 1
        even_sum += num
    else:
        odd_count += 1
        odd_sum += num

print("Even Count =", even_count)
print("Even Sum =", even_sum)
print("Odd Count =", odd_count)
print("Odd Sum =", odd_sum)
```

---

# 20. Count, Sum and Average of Positive Numbers

This combines **counter + accumulator + calculation**.

**Input**

```text
7
10
-5
20
15
-8
25
30
```

Positive numbers:

```text
10, 20, 15, 25, 30
```

Count = 5
Sum = 100
Average = 20

**Output**

```text
Positive Count = 5
Positive Sum = 100
Average = 20.00
```

```python
n = int(input())

count = 0
total = 0

for i in range(n):
    num = int(input())

    if num > 0:
        count += 1
        total += num

if count > 0:
    average = total / count
else:
    average = 0

print("Positive Count =", count)
print("Positive Sum =", total)
print(f"Average = {average:.2f}")
```

### The main pattern to teach students

```python
count = 0       # Counter
total = 0       # Accumulator

for i in range(n):
    num = int(input())

    if condition:
        count += 1
        total += num
```

**Counter → `count += 1`**
**Accumulator → `total += value`**

# 6. Find the sum of even numbers

```python
n = int(input())

total = 0

for i in range(2, n + 1, 2):
    total += i

print("Sum =", total)
```

### Input

```text
20
```

### Output

```text
Sum = 110
```

Because:

```text
2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20
= 110
```

---

# 7. Count even and odd numbers

### Problem

Take `N` numbers from the user and count how many are even and odd.

```python
n = int(input())

even_count = 0
odd_count = 0

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Count =", even_count)
print("Odd Count =", odd_count)
```

### Input

```text
6
10
15
22
7
8
13
```

### Output

```text
Even Count = 3
Odd Count = 3
```

---

# 8. Find the largest number

### Problem

Take `N` numbers and find the largest number without using `max()`.

```python
n = int(input())

largest = int(input())

for i in range(n - 1):
    num = int(input())

    if num > largest:
        largest = num

print("Largest =", largest)
```

### Input

```text
5
25
80
12
95
40
```

### Output

```text
Largest = 95
```

### Logic

```text
largest = 25

80 > 25 → largest = 80
12 > 80 → No
95 > 80 → largest = 95
40 > 95 → No
```

---

# 9. Find the smallest number

```python
n = int(input())

smallest = int(input())

for i in range(n - 1):
    num = int(input())

    if num < smallest:
        smallest = num

print("Smallest =", smallest)
```

### Input

```text
5
25
80
12
95
40
```

### Output

```text
Smallest = 12
```

---

# 10. Count numbers divisible by 3 and 5

### Problem

From `1` to `N`, count numbers divisible by both 3 and 5.

```python
n = int(input())

count = 0

for i in range(1, n + 1):

    if i % 3 == 0 and i % 5 == 0:
        count += 1

print("Count =", count)
```

### Input

```text
100
```

### Output

```text
Count = 6
```

The numbers are:

```text
15 30 45 60 75 90
```

---

# 11. Factorial of a number

### Problem

Calculate:

```text
5! = 5 × 4 × 3 × 2 × 1
```

### Code

```python
n = int(input())

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)
```

### Input

```text
5
```

### Output

```text
Factorial = 120
```

### Calculation

```text
1 × 2 × 3 × 4 × 5 = 120
```

---

# 12. Reverse a number

This is slightly harder because we need to extract digits.

```python
num = int(input())

reverse = 0

for i in range(len(str(num))):
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse =", reverse)
```

### Input

```text
12345
```

### Output

```text
Reverse = 54321
```

### Logic

```text
12345 → digit 5
1234  → digit 4
123   → digit 3
12    → digit 2
1     → digit 1
```

---

# 13. Sum of digits

### Problem

Find the sum of digits of a number.

```python
num = int(input())

total = 0

for i in range(len(str(num))):
    digit = num % 10
    total += digit
    num //= 10

print("Sum =", total)
```

### Input

```text
5832
```

### Output

```text
Sum = 18
```

Because:

```text
5 + 8 + 3 + 2 = 18
```

---

# 14. Check Prime Number

### Problem

Check whether a number is prime.

A prime number has exactly **two factors: 1 and itself**.

```python
n = int(input())

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")
```

### Input

```text
17
```

### Output

```text
Prime
```

Factors of 17:

```text
1, 17
```

So count = 2.

---

# 15. Print all prime numbers from 1 to N

Now we use a `for` loop **inside another `for` loop**.

This is called a **nested for loop**.

```python
n = int(input())

for num in range(2, n + 1):

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)
```

### Input

```text
20
```

### Output

```text
2
3
5
7
11
13
17
19
```

### Structure

```text
Outer loop → chooses number
       ↓
Inner loop → finds factors
       ↓
If exactly 2 factors → Prime
```

---

# 16. Fibonacci Series

### Problem

Print the first `N` Fibonacci numbers.

```python
n = int(input())

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b
```

### Input

```text
8
```

### Output

```text
0
1
1
2
3
5
8
13
```

The next number is calculated as:

```text
next = previous + current
```

---

# 17. Armstrong Number

### Problem

Check whether a 3-digit number is an Armstrong number.

For example:

```text
153 = 1³ + 5³ + 3³
   = 1 + 125 + 27
   = 153
```

### Code

```python
num = int(input())

original = num
total = 0

for i in range(len(str(num))):
    digit = num % 10
    total += digit ** 3
    num //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
```

### Input

```text
153
```

### Output

```text
Armstrong Number
```

---

# 18. Find Second Largest Number

### Problem

Find the second largest number without sorting.

```python
n = int(input())

largest = float("-inf")
second = float("-inf")

for i in range(n):

    num = int(input())

    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print("Second Largest =", second)
```

### Input

```text
6
20
50
10
80
40
60
```

### Output

```text
Second Largest = 60
```

### Important logic

When a new largest value is found:

```text
second = largest
largest = num
```

For example:

```text
largest = 50
second = 40

new number = 80

second = 50
largest = 80
```

---

# 19. Pattern Printing

### Problem

Print:

```text
*
**
***
****
*****
```

### Code

```python
n = int(input())

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print("*", end="")

    print()
```

### Input

```text
5
```

### Output

```text
*
**
***
****
*****
```

This is another example of a **nested `for` loop**.

Outer loop controls the **rows**.

Inner loop controls the **stars**.

---

# 20. Find the longest consecutive increasing sequence

### Problem

Given numbers, find the length of the longest sequence where every next number is greater than the previous number.

Example:

```text
1 2 3 2 4 5 6 1
```

Sequences:

```text
1 2 3       → length 3
2 4 5 6     → length 4
```

So answer = `4`.

### Code

```python
n = int(input())

previous = int(input())

current_count = 1
longest = 1

for i in range(n - 1):

    num = int(input())

    if num > previous:
        current_count += 1
    else:
        current_count = 1

    if current_count > longest:
        longest = current_count

    previous = num

print("Longest Length =", longest)
```

### Input

```text
8
1
2
3
2
4
5
6
1
```

### Output

```text
Longest Length = 4
```

---

# Important `for` Loop Concepts

### 1. Basic `for`

```python
for i in range(1, 6):
    print(i)
```

---

### 2. `for` with `if`

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

---

### 3. `for` with accumulator

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

---

### 4. `for` with counter

```python
count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count += 1

print(count)
```

---

### 5. Nested `for`

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

---


For a `for` loop, think:

```text
START
  ↓
Take next value
  ↓
Execute loop body
  ↓
Take next value
  ↓
Execute loop body
  ↓
No more values?
  ↓
STOP
```

For example:

```python
for i in range(1, 6):
    print(i)
```

traces as:

```text
i = 1 → print 1
i = 2 → print 2
i = 3 → print 3
i = 4 → print 4
i = 5 → print 5
range finished → STOP
```

