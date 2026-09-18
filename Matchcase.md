## Python `match-case`

`match-case` is Python's **pattern matching** statement. It is similar to `switch-case` in languages like Java, but Python's `match` can do more than simply compare one value.

It was introduced in **Python 3.10**.

### Basic syntax

```python
match variable:
    case value1:
        # statements
    case value2:
        # statements
    case _:
        # default case
```

* `match` → checks the value/expression.
* `case` → defines a possible pattern.
* `_` → default case, similar to `default` in switch.
* Only the **first matching case** is executed.

### Simple example

```python
day = int(input())

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

**Input**

```text
2
```

**Output**

```text
Tuesday
```

### `match-case` vs `if-elif`

For simple value checking:

```python
if choice == 1:
    print("Add")
elif choice == 2:
    print("Subtract")
else:
    print("Invalid")
```

can be written as:

```python
match choice:
    case 1:
        print("Add")
    case 2:
        print("Subtract")
    case _:
        print("Invalid")
```





## 1. Calculator using operators

**Problem:** Take two numbers and an operator and perform the operation.

```python
a = float(input())
b = float(input())
operator = input()

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero")
    case "%":
        if b != 0:
            print(a % b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")
```

**Input**

```text
20
5
*
```

**Output**

```text
100.0
```

---

## 2. Month and number of days

**Problem:** Given a month number, print the number of days.

```python
month = int(input())

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        print("28 or 29 days")
    case _:
        print("Invalid month")
```

**Input**

```text
4
```

**Output**

```text
30 days
```

Here:

```python
case 1 | 3 | 5 | 7 | 8 | 10 | 12:
```

means **1 OR 3 OR 5 OR...**

---

# 3. ATM menu

```python
choice = int(input())
balance = 10000

match choice:
    case 1:
        print(f"Balance = {balance}")
    case 2:
        amount = float(input())

        if amount <= balance:
            balance -= amount
            print(f"Withdrawn = {amount:.2f}")
            print(f"Balance = {balance:.2f}")
        else:
            print("Insufficient balance")

    case 3:
        amount = float(input())
        balance += amount
        print(f"Balance = {balance:.2f}")

    case 4:
        print("Thank you")

    case _:
        print("Invalid choice")
```

**Input**

```text
2
3000
```

**Output**

```text
Withdrawn = 3000.00
Balance = 7000.00
```

---

# 4. Grade calculator

```python
grade = input().upper()

match grade:
    case "A+" | "A":
        print("Excellent")
    case "B+" | "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")
```

**Input**

```text
B+
```

**Output**

```text
Very Good
```

---

# 5. Traffic signal

```python
signal = input().lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")
```

**Input**

```text
yellow
```

**Output**

```text
Get Ready
```

---

# 6. Login system using tuple pattern

Take username and password.

```python
username = input()
password = input()

match (username, password):
    case ("admin", "1234"):
        print("Admin Login Successful")
    case ("student", "stud123"):
        print("Student Login Successful")
    case ("teacher", "teach123"):
        print("Teacher Login Successful")
    case _:
        print("Invalid Username or Password")
```

**Input**

```text
student
stud123
```

**Output**

```text
Student Login Successful
```

Here we match **two values together**:

```python
match (username, password):
```

---

# 7. Coordinate identification

Given `(x, y)`, identify whether the point is origin, x-axis, y-axis, or a quadrant.

```python
x = int(input())
y = int(input())

match (x, y):
    case (0, 0):
        print("Origin")

    case (0, y):
        print("Y-axis")

    case (x, 0):
        print("X-axis")

    case (x, y) if x > 0 and y > 0:
        print("First Quadrant")

    case (x, y) if x < 0 and y > 0:
        print("Second Quadrant")

    case (x, y) if x < 0 and y < 0:
        print("Third Quadrant")

    case (x, y) if x > 0 and y < 0:
        print("Fourth Quadrant")
```

**Input**

```text
-5
7
```

**Output**

```text
Second Quadrant
```

The important concept here is the **guard**:

```python
case (x, y) if x < 0 and y > 0:
```

---

# 8. HTTP status code

```python
code = int(input())

match code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("Bad Request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")
```

**Input**

```text
404
```

**Output**

```text
Not Found
```

---

# 9. Rock Paper Scissors

```python
p1 = input().lower()
p2 = input().lower()

match (p1, p2):

    case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
        print("Player 1 Wins")

    case ("scissors", "rock") | ("paper", "scissors") | ("rock", "paper"):
        print("Player 2 Wins")

    case (x, y) if x == y:
        print("Draw")

    case _:
        print("Invalid Input")
```

**Input**

```text
rock
scissors
```

**Output**

```text
Player 1 Wins
```

---

# 10. Day type using weekday number

```python
day = int(input())

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")

    case 6 | 7:
        print("Weekend")

    case _:
        print("Invalid Day")
```

**Input**

```text
6
```

**Output**

```text
Weekend
```

---

# 11. Food ordering system

```python
choice = int(input())

match choice:
    case 1:
        item = "Pizza"
        price = 250

    case 2:
        item = "Burger"
        price = 150

    case 3:
        item = "Biryani"
        price = 220

    case 4:
        item = "Fried Rice"
        price = 180

    case _:
        item = None

if item is not None:
    quantity = int(input())
    total = price * quantity

    print(f"Item = {item}")
    print(f"Total = {total}")
else:
    print("Invalid Choice")
```

**Input**

```text
3
2
```

**Output**

```text
Item = Biryani
Total = 440
```

---

# 12. Employee department and role

Here we match **nested patterns**.

```python
department = input().lower()
role = input().lower()

match (department, role):

    case ("it", "developer"):
        print("IT Developer")

    case ("it", "tester"):
        print("IT Tester")

    case ("hr", "manager"):
        print("HR Manager")

    case ("finance", "analyst"):
        print("Finance Analyst")

    case ("sales", "executive"):
        print("Sales Executive")

    case _:
        print("Role Not Found")
```

**Input**

```text
it
developer
```

**Output**

```text
IT Developer
```

---

# 13. Number classification using guard

```python
number = int(input())

match number:
    case 0:
        print("Zero")

    case n if n > 0 and n % 2 == 0:
        print("Positive Even")

    case n if n > 0 and n % 2 != 0:
        print("Positive Odd")

    case n if n < 0 and n % 2 == 0:
        print("Negative Even")

    case n if n < 0 and n % 2 != 0:
        print("Negative Odd")
```

**Input**

```text
-8
```

**Output**

```text
Negative Even
```

---

# 14. Student result using tuple + guard

```python
marks = int(input())
attendance = int(input())

match (marks, attendance):

    case (m, a) if m >= 90 and a >= 75:
        print("A Grade")

    case (m, a) if m >= 75 and a >= 75:
        print("B Grade")

    case (m, a) if m >= 60 and a >= 75:
        print("C Grade")

    case (m, a) if m >= 40 and a >= 75:
        print("Pass")

    case _:
        print("Fail")
```

**Input**

```text
82
80
```

**Output**

```text
B Grade
```

---

# 15. ATM transaction using tuple

```python
transaction = input().lower()
amount = int(input())

match (transaction, amount):

    case ("withdraw", a) if a > 0 and a % 100 == 0:
        print(f"Withdrawal request: {a}")

    case ("deposit", a) if a > 0:
        print(f"Deposit request: {a}")

    case ("withdraw", _):
        print("Withdrawal amount must be positive and a multiple of 100")

    case ("deposit", _):
        print("Deposit amount must be positive")

    case _:
        print("Invalid transaction")
```

**Input**

```text
withdraw
2500
```

**Output**

```text
Withdrawal request: 2500
```

---

# 16. List pattern matching

Python `match-case` can match the **structure of a list**.

```python
numbers = list(map(int, input().split()))

match numbers:

    case []:
        print("Empty List")

    case [x]:
        print(f"One Element: {x}")

    case [x, y]:
        print(f"Two Elements: {x}, {y}")

    case [x, y, z]:
        print(f"Three Elements: {x}, {y}, {z}")

    case _:
        print("More than Three Elements")
```

**Input**

```text
10 20 30
```

**Output**

```text
Three Elements: 10, 20, 30
```

---

# 17. First element and remaining elements

This is more advanced list pattern matching.

```python
numbers = list(map(int, input().split()))

match numbers:

    case []:
        print("Empty List")

    case [first, *remaining]:
        print(f"First = {first}")
        print(f"Remaining = {remaining}")
```

**Input**

```text
10 20 30 40 50
```

**Output**

```text
First = 10
Remaining = [20, 30, 40, 50]
```

`*remaining` collects all remaining elements.

---

# 18. Dictionary pattern matching

```python
student = {
    "name": input(),
    "marks": int(input())
}

match student:

    case {"name": name, "marks": marks} if marks >= 90:
        print(f"{name} got A Grade")

    case {"name": name, "marks": marks} if marks >= 75:
        print(f"{name} got B Grade")

    case {"name": name, "marks": marks} if marks >= 60:
        print(f"{name} got C Grade")

    case {"name": name, "marks": marks}:
        print(f"{name} needs improvement")
```

**Input**

```text
Priyanka
86
```

**Output**

```text
Priyanka got B Grade
```

---

# 19. E-commerce order validation

This combines **tuple pattern + guard + multiple conditions**.

```python
quantity = int(input())
price = float(input())
payment = input().lower()
member = input().lower()

match (quantity, price, payment, member):

    case (q, p, "online", "yes") if q > 0 and p > 0:
        total = q * p * 0.90
        print(f"Total = {total:.2f}")

    case (q, p, "online", "no") if q > 0 and p > 0:
        total = q * p * 0.95
        print(f"Total = {total:.2f}")

    case (q, p, "cod", "yes") if q > 0 and p > 0:
        total = q * p * 0.95 + 50
        print(f"Total = {total:.2f}")

    case (q, p, "cod", "no") if q > 0 and p > 0:
        total = q * p + 50
        print(f"Total = {total:.2f}")

    case _:
        print("Invalid Order")
```

**Input**

```text
2
1000
online
yes
```

**Calculation**

```text
2 × 1000 = 2000
10% discount = 200
2000 - 200 = 1800
```

**Output**

```text
Total = 1800.00
```

---

# 20. Advanced: Command-based student system

This combines **tuple matching, multiple patterns, guards and list patterns**.

```python
command = input().lower()
data = input().split()

match (command, data):

    case ("add", [name, marks]) if 0 <= int(marks) <= 100:
        print(f"Student Added: {name}")
        print(f"Marks: {marks}")

    case ("result", [name, marks]) if int(marks) >= 90:
        print(f"{name} - A Grade")

    case ("result", [name, marks]) if int(marks) >= 75:
        print(f"{name} - B Grade")

    case ("result", [name, marks]) if int(marks) >= 60:
        print(f"{name} - C Grade")

    case ("result", [name, marks]) if int(marks) >= 40:
        print(f"{name} - Pass")

    case ("result", [name, marks]) if 0 <= int(marks) < 40:
        print(f"{name} - Fail")

    case ("delete", [name]):
        print(f"Student Deleted: {name}")

    case _:
        print("Invalid Command")
```

**Input**

```text
result
Priyanka 86
```

**Output**

```text
Priyanka - B Grade
```

---

## Important `match-case` concepts to remember

| Concept                 | Example                                |
| ----------------------- | -------------------------------------- |
| Simple matching         | `case 1:`                              |
| Multiple values         | `case 1 \| 2 \| 3:`                    |
| Default                 | `case _:`                              |
| Tuple matching          | `case ("admin", "1234"):`              |
| Guard condition         | `case n if n > 0:`                     |
| Multiple conditions     | `case n if n > 0 and n % 2 == 0:`      |
| List matching           | `case [x, y, z]:`                      |
| Empty list              | `case []:`                             |
| Remaining list elements | `case [first, *remaining]:`            |
| Dictionary matching     | `case {"name": name, "marks": marks}:` |

### One important point

`match-case` is **not just another name for `if-elif`**.

For example:

```python
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
```

is mainly **pattern/value matching**.

But:

```python
match number:
    case n if n > 10:
        print("Greater than 10")
```

uses a **guard** to add a condition.

So for your Python class, I would teach it in this order:

**Basic match → multiple patterns `|` → default `_` → tuple matching → guards `if` → list patterns → dictionary patterns.**
