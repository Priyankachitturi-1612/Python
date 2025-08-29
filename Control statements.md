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

Perfect Priya 🌸 You want me to **go deeper into each use case** of conditional statements. Let’s expand every point clearly with explanation + code example + real-life analogy.

---

# 🔹 **Uses of Conditional Statements in Python**

---

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

---

## **5. Data Processing (Filtering / Categorization)**

When working with large datasets, conditions help to **filter or classify data**.

**Code:**

```python
numbers = [10, -5, 20, -8, 0]

positive = []
negative = []

for n in numbers:
    if n >= 0:
        positive.append(n)
    else:
        negative.append(n)

print("Positive numbers:", positive)
print("Negative numbers:", negative)
```

**Real-life analogy:** Banks categorize customers:

* If balance > 1,00,000 → Premium customer
* Else → Normal customer

---

## **6. Security Checks (Authentication & Authorization)**

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


#### **(e) Short-hand if (Single-line if)**

```python
x = 5
if x > 0: print("Positive number")
```


#### **(f) Short-hand if-else (Ternary Operator)**

```python
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
```


#### **(g) Using Logical Operators with if**

```python
age = 20
citizen = True
if age >= 18 and citizen:
    print("Eligible to vote")
```


#### **(h) Using Membership / Identity Operators**

```python
name = "Priya"
if "i" in name:
    print("Contains i")
```

```python
x = None
if x is None:
    print("x is None type")
```


### **5. Real Life Example**

Login system:

```python
username = "Priya"
password = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("Login successful!")
else:
    print("Login failed!")
```


Conditional statements are the **decision-making backbone** of any program. They can be used in **simple, nested, or shorthand forms** and combined with operators (`and`, `or`, `not`, `in`, `is`) for powerful logic.



# 🔹 **Uses of Loops in Python**


## **1. Repetition of Tasks (Automation)**

Loops let us repeat a task **multiple times** without rewriting code.
Instead of writing the same line 100 times, we use a loop.

**Code:**

```python
for i in range(5):
    print("Hello Priya")
```

**Output:**

```
Hello Priya (5 times)
```

**Real-life analogy:** Washing machine rotates clothes multiple times in cycles — no need to manually turn them each time.


## **2. Iterating Over Collections (Lists, Tuples, Strings, Dicts)**

We can use loops to **go through each element** in a data structure.

**Code:**

```python
names = ["Priya", "Rani", "Raju"]
for name in names:
    print(name)
```

**Output:**

```
Priya
Rani
Raju
```

**Real-life analogy:** Teacher calls attendance roll one by one from the list.

---

## **3. Searching for an Item**

Loops can be used to **find something** inside a collection.

**Code:**

```python
nums = [2, 4, 6, 8, 10]
target = 6

found = False
for n in nums:
    if n == target:
        found = True
        break

print("Found:", found)
```

**Real-life analogy:** Searching for your name in an exam results list.


## **4. Summation / Aggregation**

Loops help in **calculating totals** or other aggregate values.

**Code:**

```python
numbers = [10, 20, 30, 40]
total = 0

for n in numbers:
    total += n

print("Sum =", total)
```

**Output:** `Sum = 100`

**Real-life analogy:** Shopkeeper calculates bill by adding each item price.


## **5. Generating Sequences / Patterns**

Loops are used to generate **tables, series, or patterns**.

**Code (Multiplication Table):**

```python
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

**Output:**

```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

**Real-life analogy:** School bell rings every period — a repetitive pattern.


## **6. Validations (Until Correct Input)**

`while` loops are useful for repeating **until a valid condition** is met.

**Code:**

```python
password = ""
while password != "1234":
    password = input("Enter password: ")

print("Correct password! Access granted.")
```

**Real-life analogy:** ATM asks for PIN again if entered wrong.

## **7. Infinite Processes (Real-time Systems)**

Some loops are meant to run **continuously** (with exit conditions inside).

**Code:**

```python
while True:
    command = input("Enter command (stop to exit): ")
    if command == "stop":
        break
```

**Real-life analogy:** Lift keeps running until it is switched off.

---

## **8. Simulations (Games, Experiments)**

Games and simulations rely on loops to **keep updating the state**.

**Code:**

```python
lives = 3
while lives > 0:
    print("Life remaining:", lives)
    lives -= 1
```

**Real-life analogy:** Video game loop — keeps running until player dies.


## **9. Nested Loops (Grids / Multi-Dimensional Data)**

When working with **2D data (like matrices, tables, chess boards)**, nested loops are used.

**Code:**

```python
for i in range(3):
    for j in range(3):
        print("(", i, ",", j, ")")
```

**Output:**

```
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

**Real-life analogy:** Reading rows and columns in a spreadsheet.

## **10. Breaking Large Problems into Small Iterations**

Loops help in **step-by-step solutions** for big problems.

**Example: Factorial using loop**

```python
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is", fact)
```

**Output:** `Factorial of 5 is 120`

**Real-life analogy:** Counting votes in an election one ballot at a time.


✅ **Summary of Loop Uses:**

1. Automating repetitive tasks
2. Iterating over collections
3. Searching items
4. Calculating totals
5. Generating tables/patterns
6. Validations until correct input
7. Infinite real-time processes
8. Simulations & games
9. Nested loops for grids
10. Step-by-step problem solving
