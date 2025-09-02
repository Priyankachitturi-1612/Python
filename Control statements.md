
#  Python Operators

## 🔹 1. Arithmetic Operators

Arithmetic operators are used to perform **basic math operations**.

### 1. `+` (Addition)

* Adds two values.

```python
print(10 + 5)   # 15
```

### 2. `-` (Subtraction)

* Subtracts the right-hand value from the left-hand value.

```python
print(10 - 5)   # 5
```

### 3. `*` (Multiplication)

* Multiplies two numbers.

```python
print(10 * 5)   # 50
```

### 4. `/` (Division)

* Divides left-hand value by right-hand value.
* Always gives a **float result**, even if divisible.

```python
print(10 / 2)   # 5.0
```

### 5. `//` (Floor Division)

* Division but discards the decimal part (gives integer).

```python
print(10 // 3)   # 3
```

### 6. `%` (Modulus)

* Returns the **remainder** of division.

```python
print(10 % 3)   # 1
```

### 7. `**` (Exponentiation / Power)

* Raises a number to the power of another.

```python
print(2 ** 3)   # 8   (2 × 2 × 2)
```


## 🔹 2. Relational (Comparison) Operators

Used to **compare two values**. The result is always **True or False**.

### 1. `==` (Equal to)

* Checks if values are equal.

```python
print(5 == 5)   # True
print(5 == 3)   # False
```

### 2. `!=` (Not equal to)

* Checks if values are not equal.

```python
print(5 != 3)   # True
```

### 3. `>` (Greater than)

```python
print(10 > 5)   # True
```

### 4. `<` (Less than)

```python
print(2 < 5)    # True
```

### 5. `>=` (Greater than or equal to)

```python
print(5 >= 5)   # True
```

### 6. `<=` (Less than or equal to)

```python
print(3 <= 5)   # True
```

## 🔹 3. Logical Operators

Used to combine multiple conditions.

### 1. `and`

* Returns `True` if **both conditions** are True.

```python
x = 10
print(x > 5 and x < 20)   # True
```

### 2. `or`

* Returns `True` if **any one condition** is True.

```python
x = 10
print(x < 5 or x > 5)     # True
```

### 3. `not`

* Reverses the condition.

```python
x = 10
print(not(x > 5))         # False
```

## 🔹 4. Assignment Operators

Used to **assign values** and perform operations at the same time.

### 1. `=` (Simple assignment)

```python
x = 5
print(x)    # 5
```

### 2. `+=` (Add and assign)

```python
x = 5
x += 3   # same as x = x + 3
print(x)   # 8
```

### 3. `-=` (Subtract and assign)

```python
x = 5
x -= 2   # x = x - 2
print(x)   # 3
```

### 4. `*=` (Multiply and assign)

```python
x = 5
x *= 2   # x = x * 2
print(x)   # 10
```

### 5. `/=` (Divide and assign)

```python
x = 10
x /= 2   # x = x / 2
print(x)   # 5.0
```

### 6. `//=` (Floor divide and assign)

```python
x = 10
x //= 3
print(x)   # 3
```

### 7. `%=` (Modulo and assign)

```python
x = 10
x %= 3
print(x)   # 1
```

### 8. `**=` (Power and assign)

```python
x = 2
x **= 3   # x = x ** 3
print(x)   # 8
```

## 🔹 5. Bitwise Operators

Work at the **bit level** (binary digits).

### 1. `&` (AND)

* 1 & 1 = 1, else 0

```python
print(5 & 3)   # 1   (binary: 101 & 011 = 001)
```

### 2. `|` (OR)

* 1 | 0 = 1

```python
print(5 | 3)   # 7   (101 | 011 = 111)
```

### 3. `^` (XOR – Exclusive OR)

* 1 ^ 1 = 0, but different bits = 1

```python
print(5 ^ 3)   # 6   (101 ^ 011 = 110)
```

### 4. `~` (NOT – bitwise complement)

* Flips all bits (gives negative numbers in Python).

```python
print(~5)   # -6
```

### 5. `<<` (Left Shift)

* Shifts bits to the left (multiplies by 2 each shift).

```python
print(5 << 1)   # 10
```

### 6. `>>` (Right Shift)

* Shifts bits to the right (divides by 2 each shift).

```python
print(5 >> 1)   # 2
```


## 🔹 6. Membership Operators

Used with sequences like lists, tuples, strings.

### 1. `in`

* Returns `True` if value exists in sequence.

```python
print("a" in "apple")   # True
```

### 2. `not in`

* Returns `True` if value does not exist.

```python
print("z" not in "apple")   # True
```


## 🔹 7. Identity Operators

Used to check if two variables point to the **same object in memory**.

### 1. `is`

* Returns True if objects are identical (same memory).

```python
x = [1,2,3]
y = x
print(x is y)   # True
```

### 2. `is not`

* Returns True if objects are not identical.

```python
x = [1,2,3]
y = [1,2,3]
print(x is not y)   # True   (different objects, same values)
```

⚡ Difference between `is` and `==`:

* `is` → checks memory location
* `==` → checks values

#  Conditional Statements in Python

### 1. What are Conditional Statements?

* Conditional statements allow us to **make decisions** in code.
* They let the program choose **different paths of execution** depending on whether a condition is `True` or `False`.

###  Syntax of Conditional Statements

```python
if condition:
    # block executes if condition is True
elif another_condition:
    # block executes if first was False and this is True
else:
    # executes if none of the above are True

 Example:

“If it rains, take an umbrella; otherwise, go without it.”

In Python:

```python
raining = True
if raining:
    print("Take an umbrella")
else:
    print("Go without umbrella")
```

### Why are they useful? (Uses)

* **Decision making** (different output depending on conditions).
* **Validations** (check inputs, password, age, etc.).
* **Flow control** (skip, allow, or restrict actions).
* **Game logic** (if score > 100 → level up).
* **Data processing** (filtering, categorization).

###  Syntax of Conditional Statements

```python
if condition:
    # block executes if condition is True
elif another_condition:
    # block executes if first was False and this is True
else:
    # executes if none of the above are True
```


## ✅ Basic Programs Using Conditional Statements

### 1. **Check if a number is positive or negative**

```python
num = -7
if num > 0:
    print("Positive")
else:
    print("Negative")
```


### 2. **Check if a number is even or odd**

```python
num = 12
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```


### 3. **Find the largest of two numbers**

```python
a, b = 15, 25
if a > b:
    print("a is larger")
else:
    print("b is larger")
```


### 4. **Find the largest of three numbers**

```python
a, b, c = 10, 25, 15
if a >= b and a >= c:
    print("a is largest")
elif b >= a and b >= c:
    print("b is largest")
else:
    print("c is largest")
```


### 5. **Check if a year is a leap year**

```python
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```


### 6. **Check eligibility to vote**

```python
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```


### 7. **Grade based on marks**

```python
marks = 72
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

### 8. **Check if character is vowel or consonant**

```python
ch = 'e'
if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```


### 9. **Simple calculator (using if-elif)**

```python
a, b, op = 10, 5, '+'

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid Operator")
```

### 10. **Check if a number is divisible by both 3 and 5**

```python
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not Divisible by both")
```


# 🔹 **Uses of Conditional Statements in Python**



## **1. Decision Making**

Conditional statements are mainly used for **taking decisions** in a program.
👉 Example: “If you have enough money, you can buy the product, else you cannot.”

**Code:**

```python
money = 500
price = 300

if money >= price:
    print("You can buy it!")
else:
    print("Not enough money.")
```

**Real-life analogy:** ATM machines check if you have sufficient balance before allowing withdrawal.

---

## **2. Validations**

They are used to **validate input data** (check correctness, range, or format).

**Code:**

```python
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 18:
    print("You are a minor")
else:
    print("You are an adult")
```

**Real-life analogy:** Websites validate if your email format is correct before allowing you to sign up.

---

## **3. Flow Control**

They **control which part of the code executes** and which part is skipped.
This avoids unnecessary execution.

**Code:**

```python
x = 10
if x > 0:
    print("Positive number")
else:
    print("Negative or Zero")
print("This will always execute")
```

💡 Here, depending on condition, one branch executes, then flow continues normally.

**Real-life analogy:** Traffic signals control flow — “If red → stop, If green → go.”

---

## **4. Game Logic**

Games depend heavily on conditions (score, lives, moves).
Without conditions, games cannot decide win/loss or next level.

**Code:**

```python
score = 120

if score >= 100:
    print("Level Up!")
else:
    print("Keep trying...")
```

**Real-life analogy:** In cricket, “If runs ≥ 300 → team likely to win, else tough situation.”




## **5. Security Checks (Authentication & Authorization)**

Many systems use conditions to **check identity or permissions.**

**Code:**

```python
username = "Priya"
password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Access Granted")
else:
    print("Access Denied")
```

**Real-life analogy:** Office entry gate – “If employee ID is valid, allow entry; else deny.”

---

## **7. Error Handling / Preventing Invalid Operations**

They prevent programs from crashing by checking before an operation.

**Code:**

```python
denominator = 0

if denominator != 0:
    print(10 / denominator)
else:
    print("Division by zero not allowed")
```

**Real-life analogy:** Car won’t start unless brake pedal is pressed (safety condition).

---

## **8. Dynamic Behavior (Different Outputs for Different Inputs)**

Programs respond differently based on user input.

**Code:**

```python
choice = input("Enter your choice (tea/coffee): ")

if choice == "tea":
    print("Here is your tea ☕")
elif choice == "coffee":
    print("Here is your coffee ☕")
else:
    print("Invalid choice")
```

**Real-life analogy:** Online shopping –
“If payment method = UPI → ask UPI ID, If card → ask card details.”

---

**Summary:**
Conditional statements are **indispensable** because they let programs:

1. **Decide actions**
2. **Validate inputs**
3. **Control execution flow**
4. **Implement game or application logic**
5. **Filter data**
6. **Enforce security**
7. **Avoid errors**
8. **Provide dynamic responses**


###  Different Ways We Can Use Conditionals

#### **(a) Simple if**

```python
x = 10
if x > 5:
    print("x is greater than 5")
```


#### **(b) if-else**

```python
age = 18
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```


#### **(c) if-elif-else (Multiple conditions)**

```python
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```


#### **(d) Nested if (if inside if)**

```python
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
```




# What is a loop?


# 1) `for` loop — iterate over iterables

## Concept

* Python’s `for` iterates **item by item** over an iterable.
* You don’t manually manage an index unless you need it.

## Syntax

```python
for item in iterable:
    # use item
```

## Core examples

### Iterate a list

```python
nums = [10, 20, 30]
for n in nums:
    print(n)
```

### Iterate a string

```python
for ch in "Priya":
    print(ch)
```

### Iterate with `range(start, stop, step)`

* `start` default = 0
* `stop` is **exclusive**
* `step` can be negative

```python
for i in range(1, 6):       # 1,2,3,4,5
    print(i)

for i in range(10, 0, -2):  # 10,8,6,4,2
    print(i)
```
Got it Priya 👍
I’ll keep this **only about `for` loops** (without using lists). Here are some **basic programs** you can practice:

---

## ✅ For Loop Example Programs

### 1. Print numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

### 2. Print even numbers from 1 to 20

```python
for i in range(2, 21, 2):
    print(i)
```

---

### 3. Print odd numbers from 1 to 20

```python
for i in range(1, 21, 2):
    print(i)
```

---

### 4. Print squares of numbers 1 to 5

```python
for i in range(1, 6):
    print(i, "squared is", i*i)
```

---

### 5. Multiplication table of a number

```python
num = 7
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
```

---

### 6. Sum of first 10 natural numbers

```python
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)
```

---

### 7. Factorial of a number

```python
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is", fact)
```

---

### 8. Fibonacci series (first 10 numbers)

```python
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a+b
```

---

### 9. Reverse counting (from 10 to 1)

```python
for i in range(10, 0, -1):
    print(i)
```

---

### 10. Print star pattern (triangle)

```python
rows = 5
for i in range(1, rows+1):
    print("*" * i)
```

# 2) `while` loop — repeat while condition is True

## Concept

* Use when you **don’t know** the exact number of iterations beforehand.
* Classic for reading input until a sentinel, polling, retry logic, etc.

## Syntax

```python
while condition:
    # body runs while condition is True
```

## Examples

### Basic counter

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```


### 1. Print multiples of 3 up to 30

```python
i = 3
while i <= 30:
    print(i)
    i += 3
```
### 2. Print squares of numbers 1 to 10

```python
i = 1
while i <= 10:
    print(i, "squared is", i*i)
    i += 1
```

### 3. Print cube of numbers 1 to 5

```python
i = 1
while i <= 5:
    print(i, "cube is", i**3)
    i += 1
```


### 4. Check if a number is palindrome

```python
n = 121
temp = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
```

### 5. Print ASCII values of A to Z

```python
ch = 'A'
while ch <= 'Z':
    print(ch, "=", ord(ch))
    ch = chr(ord(ch) + 1)
```


### 6. Print sum of digits of a number

```python
n = 1234
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)
```

### 7. Armstrong number check (e.g., 153 = 1³ + 5³ + 3³)

```python
n = 153
temp = n
total = 0
while n > 0:
    digit = n % 10
    total += digit**3
    n //= 10
if temp == total:
    print("Armstrong Number")
else:
    print("Not Armstrong")
```

### 8. Print alphabets from a to z

```python
ch = 'a'
while ch <= 'z':
    print(ch, end=" ")
    ch = chr(ord(ch) + 1)
```


### 9. Print table of 9 in reverse

```python
i = 10
while i >= 1:
    print("9 x", i, "=", 9*i)
    i -= 1
```

### 10. Number guessing game (simple)

```python
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess a number (1-10): "))
print("Correct! 🎉")
```


# 3) Loop control statements

### `break`

* Exit the **innermost** loop immediately.

```python
for n in range(10):
    if n == 3:
        break
    print(n)  # 0,1,2
```

### `continue`

* Skip the rest of this iteration, go to the next.

```python
for n in range(5):
    if n == 2:
        continue
    print(n)  # 0,1,3,4
```

### `pass`

* Do nothing (placeholder for future code).

```python
for _ in range(3):
    pass  # to be implemented later
```



## 🔹 What is a Matching Statement in Python?

The **matching statement** in Python is the **`match` statement** (introduced in Python 3.10).
It is Python’s version of **switch-case** (like in C, C++, Java).

👉 It allows you to compare a variable against multiple **patterns** or **values** and run the code that matches.


## 🔹 Speciality of `match` Statement

1. **Cleaner than if-elif-else**

   * Instead of writing many `if-elif` conditions, we can write one `match` with multiple `case` blocks.

2. **Supports Pattern Matching**

   * Not just equality, it can check **ranges, conditions, data structures (lists, tuples)**.

3. **Default Case with `_`**

   * The `_` acts as a wildcard → matches anything (like `else` in `if-else`).

4. **Readable and Structured**

   * Easy to understand when there are many options.


## 🔹 Syntax

```python
match variable:
    case value1:
        # code if variable == value1
    case value2:
        # code if variable == value2
    case _:
        # code if nothing matches (default)
```


## ✅ Example 1: Day of Week

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
```

Output:

```
Wednesday
```

---

## ✅ Example 2: Grade System with Conditions

```python
marks = 82

match marks:
    case m if m >= 90:
        print("Grade A")
    case m if m >= 75:
        print("Grade B")
    case m if m >= 50:
        print("Grade C")
    case _:
        print("Fail")
```

Output:

```
Grade B
```

---

## ✅ Example 3: Calculator

```python
a, b, op = 10, 5, '*'

match op:
    case '+':
        print("Sum:", a + b)
    case '-':
        print("Difference:", a - b)
    case '*':
        print("Product:", a * b)
    case '/':
        print("Division:", a / b)
    case _:
        print("Invalid Operator")
```

Output:

```
Product: 50
```

✨ **In short:**

* `match` is Python’s **modern replacement for long if-elif chains**.
* Speciality → handles **multiple cases + pattern matching + default option `_`** in a clean way.
