
# Python `while` Loop

A **while loop** repeatedly executes a block of code **as long as the condition is `True`**.

### Syntax

```python
while condition:
    statements
```

Example:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

**Output**

```text
1
2
3
4
5
```


### Three important parts

```python
i = 1              # Initialization

while i <= 5:      # Condition
    print(i)
    i += 1         # Update
```

If you forget the update:

```python
i = 1

while i <= 5:
    print(i)
```

the loop becomes an **infinite loop** because `i` always remains `1`.

---





# 1 Count Digits and Find Digit Sum

**Input**

```text
58392
```

**Output**

```text
Number of Digits = 5
Digit Sum = 27
```

```python
num = int(input())

count = 0
total = 0

while num > 0:
    digit = num % 10

    count += 1
    total += digit

    num = num // 10

print("Number of Digits =", count)
print("Digit Sum =", total)
```

Here:

* `count` → counter
* `total` → accumulator
* `num = num // 10` → moves toward termination

---

# 2. Find Largest Digit

**Input**

```text
58392
```

**Output**

```text
Largest Digit = 9
```

```python
num = int(input())

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest Digit =", largest)
```

---

# 3. Find Smallest Digit

**Input**

```text
58392
```

**Output**

```text
Smallest Digit = 2
```

```python
num = int(input())

smallest = 9

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Smallest Digit =", smallest)
```

---

# 4. Count Even and Odd Digits

**Input**

```text
583924
```

**Output**

```text
Even Digits = 3
Odd Digits = 3
```

```python
num = int(input())

even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    num = num // 10

print("Even Digits =", even_count)
print("Odd Digits =", odd_count)
```

---

# 5. Check Palindrome Number

**Input**

```text
1221
```

**Output**

```text
Palindrome
```

```python
num = int(input())

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---


# 6. Find GCD of Two Numbers

**Input**

```text
48
18
```

**Output**

```text
GCD = 6
```

```python
a = int(input())
b = int(input())

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD =", a)
```

This uses the **Euclidean algorithm**.

---

# 7. Find LCM of Two Numbers

**Input**

```text
12
18
```

**Output**

```text
LCM = 36
```

```python
a = int(input())
b = int(input())

x = a
y = b

while y != 0:
    remainder = x % y
    x = y
    y = remainder

gcd = x

lcm = (a * b) // gcd

print("LCM =", lcm)
```

---




# 8. Find Second Largest Digit

**Input**

```text
58392
```

**Output**

```text
Second Largest Digit = 8
```

```python
num = int(input())

largest = -1
second_largest = -1

while num > 0:
    digit = num % 10

    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit

    num = num // 10

print("Second Largest Digit =", second_largest)
```

---

# 9. Find Frequency of a Digit

Count how many times a given digit occurs.

**Input**

```text
12233442
2
```

**Output**

```text
Frequency = 3
```

```python
num = int(input())
target = int(input())

count = 0

while num > 0:
    digit = num % 10

    if digit == target:
        count += 1

    num = num // 10

print("Frequency =", count)
```



# 10. Decimal to Binary

Convert a decimal number into binary.

**Input**

```text
13
```

**Output**

```text
Binary = 1101
```

```python
num = int(input())

binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("Binary =", binary)
```

---


# 11. Fibonacci Series

Print the first `n` Fibonacci numbers.

**Input**

```text
8
```

**Output**

```text
0 1 1 2 3 5 8 13
```

```python
n = int(input())

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")

    c = a + b
    a = b
    b = c

    count += 1
```

Here `count` controls the termination.

---

# 12. Find Maximum Consecutive Increasing Sequence

**Input**

```text
8
2
4
6
3
5
7
9
1
```

**Output**

```text
Longest Length = 4
```

The longest increasing sequence is:

```text
3 5 7 9
```

```python
n = int(input())

previous = int(input())

current_count = 1
longest = 1

i = 1

while i < n:
    num = int(input())

    if num > previous:
        current_count += 1
    else:
        current_count = 1

    if current_count > longest:
        longest = current_count

    previous = num
    i += 1

print("Longest Length =", longest)
```

## 13 Find Difference Between Adjacent Digits

For 58392:

|5-8| = 3
|8-3| = 5
|3-9| = 6
|9-2| = 7

Find the maximum difference.

Input

58392

Output

Maximum Difference = 7
num = int(input())

previous = num % 10
num //= 10

maximum = 0

while num > 0:
    digit = num % 10

    difference = digit - previous

    if difference < 0:
        difference = -difference

    if difference > maximum:
        maximum = difference

    previous = digit
    num //= 10

print("Maximum Difference =", maximum)


##  14 Check Whether Digits Are in Increasing Order

Input

123456

Output

Increasing Order
num = int(input())

previous = num % 10
num //= 10

increasing = True

while num > 0:
    digit = num % 10

    if digit >= previous:
        increasing = False
        break

    previous = digit
    num //= 10

if increasing:
    print("Increasing Order")
else:
    print("Not Increasing")


 
 ## 15 Find average of even digits

Input: 5839267

n = int(input("Enter number: "))

temp = n
count = 0
total = 0

while temp > 0:
    digit = temp % 10

    if digit % 2 == 0:
        count += 1
        total += digit

    temp = temp // 10

if count > 0:
    average = total / count
else:
    average = 0

print("Sum =", total)
print("Count =", count)
print("Average =", average)

Output:

Enter number: 5839267
Sum = 20
Count = 3
Average = 6.666666666666667



## 16 Find the second smallest digit

Input: 5839267

n = int(input("Enter number: "))

temp = n
smallest = 10
second_smallest = 10

while temp > 0:
    digit = temp % 10

    if digit < smallest:
        second_smallest = smallest
        smallest = digit
    elif digit < second_smallest and digit != smallest:
        second_smallest = digit

    temp = temp // 10

print("Smallest Digit =", smallest)
print("Second Smallest Digit =", second_smallest)

Output:

Enter number: 5839267
Smallest Digit = 2
Second Smallest Digit = 3

## 17 Find the longest consecutive even sequence

Input:

8
2
4
6
3
8
10
12
14
n = int(input("Enter number of elements: "))

num = int(input("Enter number: "))

current_count = 0
longest = 0
i = 0

while i < n:
    if num % 2 == 0:
        current_count += 1

        if current_count > longest:
            longest = current_count
    else:
        current_count = 0

    i += 1

    if i < n:
        num = int(input("Enter number: "))

print("Longest Even Sequence =", longest)

Output:

Enter number of elements: 8
Enter number: 2
Enter number: 4
Enter number: 6
Enter number: 3
Enter number: 8
Enter number: 10
Enter number: 12
Enter number: 14
Longest Even Sequence = 4

## 18 Find the longest consecutive positive sequence

Input:

9
5
8
-2
4
7
9
-1
6
10
n = int(input("Enter number of elements: "))

num = int(input("Enter number: "))

current_count = 0
longest = 0
i = 0

while i < n:
    if num > 0:
        current_count += 1

        if current_count > longest:
            longest = current_count
    else:
        current_count = 0

    i += 1

    if i < n:
        num = int(input("Enter number: "))

print("Longest Positive Sequence =", longest)

Output:

Enter number of elements: 9
Enter number: 5
Enter number: 8
Enter number: -2
Enter number: 4
Enter number: 7
Enter number: 9
Enter number: -1
Enter number: 6
Enter number: 10
Longest Positive Sequence = 3


## 19 Find the number having the largest digit sum

Enter numbers one by one and find which number has the largest sum of its digits.

Input:

4
123
456
789
235
n = int(input("How many numbers: "))

i = 0
largest_sum = -1
largest_number = 0

while i < n:
    num = int(input("Enter number: "))

    temp = num
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp = temp // 10

    if digit_sum > largest_sum:
        largest_sum = digit_sum
        largest_number = num

    i += 1

print("Number =", largest_number)
print("Digit Sum =", largest_sum)

Output:

How many numbers: 4
Enter number: 123
Enter number: 456
Enter number: 789
Enter number: 235
Number = 789
Digit Sum = 24




# 20. Find Digital Root

Repeatedly add digits until only one digit remains.

**Input**

```text
9875
```

Calculation:

```text
9 + 8 + 7 + 5 = 29
2 + 9 = 11
1 + 1 = 2
```

**Output**

```text
Digital Root = 2
```

```python
num = int(input())

while num >= 10:

    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    num = total

print("Digital Root =", num)
```
