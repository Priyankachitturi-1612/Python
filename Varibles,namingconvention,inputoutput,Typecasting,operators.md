
# Variables in Python

## 1. What is a Variable?

A **variable** is a name used to store a value in a program.

For example:

```python
name = "Pinky"
age = 23
marks = 85.5
```

Here:

* `name` → variable
* `"Pinky"` → value
* `age` → variable
* `23` → value
* `marks` → variable
* `85.5` → value

Think of a variable as a **container that holds a value**.

---

## 2. How to Create a Variable?

In Python, we simply use the **assignment operator `=`**.

### Syntax

```python
variable_name = value
```

Example:

```python
age = 23
```

Here, the value `23` is assigned to the variable `age`.

We can display it using `print()`:

```python
age = 23

print(age)
```

### Output

```text
23
```

---

# 3. Examples of Variables

### Integer

```python
age = 23
```

### Float

```python
price = 99.50
```

### String

```python
name = "Pinky"
```

### Boolean

```python
is_student = True
```

### Character

Python does not have a separate `char` data type.

A single character is also a **string**:

```python
grade = "A"
```

---

# 4. Multiple Variables

We can create multiple variables.

```python
name = "Pinky"
age = 23
city = "Rajahmundry"

print(name)
print(age)
print(city)
```

### Output

```text
Priyanka
23
Rajahmundry
```

---

# 5. Assign Multiple Values

Python allows us to assign values to multiple variables in one line.

```python
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
```

### Output

```text
10
20
30
```

Here:

```text
a = 10
b = 20
c = 30
```

---

# 6. Assign the Same Value to Multiple Variables

```python
a = b = c = 10

print(a)
print(b)
print(c)
```

### Output

```text
10
10
10
```

All three variables contain the value `10`.

---

# 7. Variable Values Can Be Changed

Python variables are **changeable**.

```python
age = 23

print(age)

age = 24

print(age)
```

### Output

```text
23
24
```

Initially:

```text
age → 23
```

Later:

```text
age → 24
```

---

# 8. Python is Dynamically Typed

In Python, we **don't need to specify the data type** while creating a variable.

For example:

```python
x = 10
```

Python understands that `x` is an integer.

We can later assign a different type:

```python
x = 10
print(x)

x = "Python"
print(x)
```

### Output

```text
10
Python
```

This is called **dynamic typing**.

---

# 9. Checking the Data Type

We can use the `type()` function.

```python
age = 23
name = "Priyanka"
marks = 85.5

print(type(age))
print(type(name))
print(type(marks))
```

### Output

```text
<class 'int'>
<class 'str'>
<class 'float'>
```

---

# 10. Variable Naming Rules

There are some important rules when naming variables in Python.

### Rule 1: Variable can contain letters

```python
name = "Priyanka"
```

---

### Rule 2: Variable can contain numbers

But **a variable cannot start with a number**.

 Correct:

```python
student1 = "Priyanka"
```

 Incorrect:

```python
1student = "Priyanka"
```

---

### Rule 3: Underscore `_` is allowed

```python
student_name = "Priyanka"
```

---

### Rule 4: No spaces are allowed

 Incorrect:

```python
student name = "Priyanka"
```

 Correct:

```python
student_name = "Priyanka"
```

---

### Rule 5: Python is case-sensitive

These are three different variables:

```python
name = "Priyanka"
Name = "Teddy"
NAME = "Anu"
```

Python treats:

```text
name
Name
NAME
```

as different names.

---

### Rule 6: Keywords cannot be used as variable names

Python has reserved keywords such as:

```text
if
else
for
while
class
def
return
True
False
```

So we cannot write:



```python
class = 10
```



```python
if = 20
```

---

# 11. Variable Naming Conventions

A **naming convention** is a recommended way of writing names so that the code is easy to read and understand.

## 1. Snake Case — Recommended in Python

Words are written in lowercase and separated using `_`.

```python
student_name = "Priyanka"
student_age = 23
total_marks = 450
```

This is the **most commonly recommended style for Python variables**.

---

## 2. Camel Case

The first word starts with lowercase and the next words start with uppercase.

```python
studentName = "Priyanka"
studentAge = 23
totalMarks = 450
```

This style is common in **Java**, but Python generally prefers snake_case.

---

## 3. Pascal Case

Every word starts with an uppercase letter.

```python
StudentName
StudentAge
TotalMarks
```

This is generally used for **class names** in Python rather than normal variables.

Example:

```python
class StudentDetails:
    pass
```

---

# 12. Good vs Bad Variable Names

| Bad / Less Clear | Good             |
| ---------------- | ---------------- |
| `x`              | `student_age`    |
| `a`              | `total_marks`    |
| `n`              | `student_name`   |
| `studentName`    | `student_name`   |
| `TotalMarks`     | `total_marks`    |
| `student name` ❌ | `student_name` ✅ |
| `1student` ❌     | `student1` ✅     |

Short names such as `i`, `j`, and `n` are still perfectly normal in small programs and loops.

Example:

```python
for i in range(5):
    print(i)
```

---

# 13. Meaningful Variable Names

Always try to use names that tell us **what the variable contains**.

Instead of:

```python
x = 50000
```

Prefer:

```python
salary = 50000
```

Instead of:

```python
x = 85
```

Prefer:

```python
marks = 85
```

Instead of:

```python
x = "Priyanka"
```

Prefer:

```python
student_name = "Priyanka"
```

This makes the program easier to understand.

---

# 14. Example Program Using Variables

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
```

### Input

```text
Enter your name: Priyanka
Enter your age: 23
Enter your marks: 85.5
```

### Output

```text
Name: Priyanka
Age: 23
Marks: 85.5
```

Here we have three variables:

```text
name  → "Priyanka"
age   → 23
marks → 85.5
```

---

## Quick Summary

**Variable:** A name used to store a value.

```python
age = 23
```

**Assignment operator:**

```python
=
```

**Check data type:**

```python
type(age)
```

**Python is dynamically typed:** No need to specify the data type while creating a variable.

**Recommended Python naming convention:**

```python
student_name
total_marks
employee_salary
```

**Remember the main naming rules:**

1. Can contain letters, numbers and `_`
2. Cannot start with a number
3. Cannot contain spaces
4. Cannot use Python keywords
5. Python is case-sensitive
6. Prefer **snake_case** for variable names.



# 1. Number Data Type

Python mainly has **3 numeric data types**:

* `int` → Whole numbers
* `float` → Decimal numbers
* `complex` → Numbers with real and imaginary parts

### Example 1: Integer

```python
age = 25
print(age)
```

**Output:**

```text
25
```

### Example 2: Negative Integer

```python
temperature = -10
print(temperature)
```

**Output:**

```text
-10
```

### Example 3: Float

```python
price = 99.50
print(price)
```

**Output:**

```text
99.5
```

### Example 4: Decimal Calculation

```python
length = 10.5
width = 5.2

area = length * width

print(area)
```

**Output:**

```text
54.6
```

### Example 5: Addition

```python
a = 10
b = 20

print(a + b)
```

**Output:**

```text
30
```

### Example 6: Division

```python
a = 20
b = 4

print(a / b)
```

**Output:**

```text
5.0
```

### Example 7: Modulus

```python
a = 17
b = 5

print(a % b)
```

**Output:**

```text
2
```

### Example 8: Power

```python
number = 5

print(number ** 2)
```

**Output:**

```text
25
```

### Example 9: Complex Number

```python
num = 3 + 4j

print(num)
```

**Output:**

```text
(3+4j)
```

### Example 10: Checking Numeric Type

```python
num = 100

print(type(num))
```

**Output:**

```text
<class 'int'>
```

---

# 2. String Data Type

A **string (`str`)** is a sequence of characters enclosed in:

* Single quotes `' '`
* Double quotes `" "`
* Triple quotes `''' '''` or `""" """`

Python does **not have a separate `char` data type**. A single character is also a string.

### Example 1: Simple String

```python
name = "Priyanka"

print(name)
```

**Output:**

```text
Priyanka
```

### Example 2: Single Character

```python
letter = "A"

print(letter)
```

**Output:**

```text
A
```

Here `"A"` is a **string**, not a separate character data type.

### Example 3: Sentence

```python
message = "Welcome to Python"

print(message)
```

**Output:**

```text
Welcome to Python
```

### Example 4: String Concatenation

```python
first_name = "Priyanka"
last_name = "Chitturi"

print(first_name + " " + last_name)
```

**Output:**

```text
Priyanka Chitturi
```

### Example 5: String Length

```python
name = "Python"

print(len(name))
```

**Output:**

```text
6
```

### Example 6: Uppercase

```python
name = "python"

print(name.upper())
```

**Output:**

```text
PYTHON
```

### Example 7: Lowercase

```python
name = "PYTHON"

print(name.lower())
```

**Output:**

```text
python
```

### Example 8: Accessing a Character

```python
word = "Python"

print(word[0])
```

**Output:**

```text
P
```

Indexing starts from **0**:

```text
P y t h o n
0 1 2 3 4 5
```

### Example 9: String Slicing

```python
word = "Python"

print(word[0:3])
```

**Output:**

```text
Pyt
```

### Example 10: String with User Input

```python
name = input("Enter your name: ")

print("Hello", name)
```

**Input:**

```text
Priyanka
```

**Output:**

```text
Hello Priyanka
```

---

# 3. Boolean Data Type

The Boolean data type has only **two values**:

```python
True
False
```

Important: **`True` and `False` must start with a capital letter.**

Boolean values are commonly obtained from **comparisons and conditions**.

### Example 1: True Value

```python
is_student = True

print(is_student)
```

**Output:**

```text
True
```

### Example 2: False Value

```python
is_completed = False

print(is_completed)
```

**Output:**

```text
False
```

### Example 3: Greater Than

```python
a = 10
b = 5

print(a > b)
```

**Output:**

```text
True
```

### Example 4: Less Than

```python
a = 10
b = 20

print(a < b)
```

**Output:**

```text
True
```

### Example 5: Equal To

```python
a = 10
b = 10

print(a == b)
```

**Output:**

```text
True
```

### Example 6: Not Equal

```python
a = 10
b = 20

print(a != b)
```

**Output:**

```text
True
```

### Example 7: Checking Even Number

```python
number = 10

print(number % 2 == 0)
```

**Output:**

```text
True
```

**Calculation:**

`10 % 2 = 0`

Therefore:

`0 == 0 → True`

### Example 8: Checking Age

```python
age = 20

print(age >= 18)
```

**Output:**

```text
True
```

### Example 9: Using `and`

```python
age = 25
has_id = True

print(age >= 18 and has_id)
```

**Output:**

```text
True
```

Both conditions are true.

### Example 10: Using `bool()`

```python
value = 10

print(bool(value))
```

**Output:**

```text
True
```

A non-zero number is considered **True**.

For example:

```python
print(bool(0))
print(bool(10))
print(bool(-5))
```

**Output:**

```text
False
True
True
```

---

## Quick Comparison

| Data Type | Meaning          | Examples          |
| --------- | ---------------- | ----------------- |
| `int`     | Whole number     | `10`, `-5`, `100` |
| `float`   | Decimal number   | `10.5`, `3.14`    |
| `complex` | Real + imaginary | `3+4j`            |
| `str`     | Text/characters  | `"Python"`, `"A"` |
| `bool`    | True/False       | `True`, `False`   |

### Easy way to remember

```text
Numbers  →  10, 20.5, 3+4j
String   →  "Python", "Hello", "A"
Boolean  →  True, False
```

**One important point:** `input()` always gives a **string**. So if you want a number from the user, you need type casting:

```python
age = int(input("Enter age: "))
```

Here the entered text is converted from `str` → `int`.



# Type Casting in Python

## 1. What is Type Casting?

**Type casting** means **converting a value from one data type to another data type**.

For example, converting:

```text
int → float
int → string
string → int
float → int
```

Python provides built-in functions for type casting.

### Common Type Casting Functions

| Function  | Converts value into |
| --------- | ------------------- |
| `int()`   | Integer             |
| `float()` | Float               |
| `str()`   | String              |
| `bool()`  | Boolean             |
| `list()`  | List                |
| `tuple()` | Tuple               |
| `set()`   | Set                 |

---

# 2. Integer to Float

We can convert an integer into a floating-point number using `float()`.

```python
num = 10

result = float(num)

print(result)
print(type(result))
```

### Output

```text
10.0
<class 'float'>
```

### Calculation

```text
10 → 10.0
```

---

# 3. Float to Integer

We can convert a float into an integer using `int()`.

```python
num = 10.75

result = int(num)

print(result)
```

### Output

```text
10
```

### Important

The decimal part is **removed**, not rounded.

```text
10.75 → 10
10.99 → 10
5.5   → 5
```

So:

```python
int(10.99)
```

gives:

```text
10
```

---

# 4. Integer to String

We can convert an integer into a string using `str()`.

```python
num = 100

result = str(num)

print(result)
print(type(result))
```

### Output

```text
100
<class 'str'>
```

Here:

```text
100 → "100"
```

The value looks the same when printed, but its data type is different.

---

# 5. String to Integer

We can convert a string containing a whole number into an integer.

```python
num = "100"

result = int(num)

print(result)
print(type(result))
```

### Output

```text
100
<class 'int'>
```

Here:

```text
"100" → 100
```

This is especially important when taking **numeric input** from the user.

---

# 6. String to Float

```python
num = "25.5"

result = float(num)

print(result)
print(type(result))
```

### Output

```text
25.5
<class 'float'>
```

Here:

```text
"25.5" → 25.5
```

---

# 7. Float to String

```python
num = 25.5

result = str(num)

print(result)
print(type(result))
```

### Output

```text
25.5
<class 'str'>
```

---

# 8. String to Boolean

We can use `bool()` to convert a value into Boolean.

```python
name = "Python"

result = bool(name)

print(result)
```

### Output

```text
True
```

A **non-empty string** gives `True`.

```python
bool("Hello")
```

Output:

```text
True
```

An **empty string** gives `False`.

```python
bool("")
```

Output:

```text
False
```

---

# 9. Integer to Boolean

```python
num = 10

result = bool(num)

print(result)
```

### Output

```text
True
```

### Rule

For numbers:

```text
0 → False
Any non-zero number → True
```

Examples:

```python
print(bool(0))
print(bool(1))
print(bool(100))
print(bool(-5))
```

### Output

```text
False
True
True
True
```

---

# 10. Boolean to Integer

```python
print(int(True))
print(int(False))
```

### Output

```text
1
0
```

In Python:

```text
True  → 1
False → 0
```

---

# 11. Why is Type Casting Important with `input()`?


```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

### Input

```text
Enter first number: 10
Enter second number: 20
```

### Output

```text
1020
```

Why?

Because `input()` returns **string values**.

So Python sees:

```text
"10" + "20"
```

which becomes:

```text
"1020"
```

---

## Correct Way

Convert the input into integers:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

### Input

```text
Enter first number: 10
Enter second number: 20
```

### Output

```text
30
```

Now Python performs:

```text
10 + 20 = 30
```

---

# 12. Type Casting with User Input

### Example 1: Age

```python
age = int(input("Enter your age: "))

print("Age:", age)
```

**Input:**

```text
Enter your age: 23
```

**Output:**

```text
Age: 23
```

---

### Example 2: Salary

```python
salary = float(input("Enter your salary: "))

print("Salary:", salary)
```

**Input:**

```text
Enter your salary: 25000.50
```

**Output:**

```text
Salary: 25000.5
```

---

### Example 3: Marks

```python
marks = float(input("Enter your marks: "))

print("Marks:", marks)
```

**Input:**

```text
Enter your marks: 85.5
```

**Output:**

```text
Marks: 85.5
```

---

# 13. Multiple Inputs with Type Casting

We can take multiple integer values in one line.

```python
a, b, c = map(int, input("Enter three numbers: ").split())

print("Sum =", a + b + c)
```

### Input

```text
Enter three numbers: 10 20 30
```

### Output

```text
Sum = 60
```

### How it works?

Input:

```text
10 20 30
```

`split()` separates them:

```text
"10"  "20"  "30"
```

`map(int, ...)` converts them:

```text
10  20  30
```

Then:

```text
10 + 20 + 30 = 60
```

---

# 14. Type Casting Between Collections

### String to List

```python
text = "Python"

result = list(text)

print(result)
```

### Output

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

### List to Tuple

```python
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
```

### Output

```text
(10, 20, 30)
```

---

### List to Set

```python
numbers = [10, 20, 20, 30]

result = set(numbers)

print(result)
```

### Output

```text
{10, 20, 30}
```

The duplicate `20` is removed because a **set does not allow duplicate values**.

---

# 15. Invalid Type Casting

Not every value can be converted into every type.

For example:

```python
num = "Python"

result = int(num)
```

This produces an error because `"Python"` cannot be converted into an integer.

Similarly:

```python
num = "10.5"

result = int(num)
```

This also gives an error because `"10.5"` is not an integer-formatted string.

Instead, use:

```python
num = "10.5"

result = float(num)

print(result)
```

### Output

```text
10.5
```

---

# Important Type Casting Examples

| Original | Conversion      | Result  |
| -------- | --------------- | ------- |
| `10`     | `float(10)`     | `10.0`  |
| `10.5`   | `int(10.5)`     | `10`    |
| `100`    | `str(100)`      | `"100"` |
| `"100"`  | `int("100")`    | `100`   |
| `"10.5"` | `float("10.5")` | `10.5`  |
| `10`     | `bool(10)`      | `True`  |
| `0`      | `bool(0)`       | `False` |
| `True`   | `int(True)`     | `1`     |
| `False`  | `int(False)`    | `0`     |



Remember this:

```python
input()
```

**always returns a string**.

Therefore, when you want numbers:

```python
age = int(input())
```

or

```python
marks = float(input())
```

### Simple flow

```text
User enters data
       ↓
    input()
       ↓
    String
       ↓
Type Casting
       ↓
Required Data Type
```

For example:

```python
age = int(input("Enter age: "))
```

means:

```text
User enters 23
      ↓
   "23"       ← input()
      ↓
    int()     ← type casting
      ↓
     23
```


# Python Input, Output Functions & f-String

## 1. Input Function – `input()`

The **`input()`** function is used to take data from the user during program execution.

### Syntax

```python
variable = input("Message")
```

### Example

```python
name = input("Enter your name: ")

print(name)
```

**Input:**

```text
Enter your name: Priyanka
```

**Output:**

```text
Priyanka
```

### Important Point

`input()` always returns the input as a **string**.

For numeric values, we use type casting:

```python
age = int(input("Enter your age: "))
```

```python
marks = float(input("Enter your marks: "))
```

---

# 2. Output Function – `print()`

The **`print()`** function is used to display information on the screen.

### Syntax

```python
print(value)
```

### Example

```python
print("Hello Python")
```

**Output:**

```text
Hello Python
```

---

## 3. Printing Multiple Values

We can pass multiple values to `print()` separated by commas.

```python
name = "Priyanka"
age = 23

print(name, age)
```

**Output:**

```text
Pinky 23
```

Another example:

```python
a = 10
b = 20

print("A =", a, "B =", b)
```

**Output:**

```text
A = 10 B = 20
```

---

# 4. `sep` in `print()`

`sep` specifies what should be placed **between multiple values**.

### Example

```python
a = 10
b = 20
c = 30

print(a, b, c, sep="-")
```

**Output:**

```text
10-20-30
```

Another example:

```python
print("2026", "09", "15", sep="/")
```

**Output:**

```text
2026/09/15
```

---

# 5. `end` in `print()`

Normally, `print()` moves to the next line after displaying the output.

We can change this using `end`.

### Normal

```python
print("Hello")
print("Python")
```

**Output:**

```text
Hello
Python
```

### Using `end`

```python
print("Hello", end=" ")
print("Python")
```

**Output:**

```text
Hello Python
```

Another example:

```python
print("Hello", end="-")
print("Python")
```

**Output:**

```text
Hello-Python
```

---

# 6. What is an f-string?

**f-string** means **formatted string**.

It is used to easily insert variables and expressions inside a string.

An f-string is created by putting **`f` before the string**.

### Syntax

```python
f"Text {variable}"
```

The variable or expression is placed inside **`{ }`**.

---

# 7. Basic f-string Example

```python
name = "Priyanka"
age = 23

print(f"My name is {name}")
print(f"My age is {age}")
```

### Output

```text
My name is Priyanka
My age is 23
```

Here:

```python
f"My name is {name}"
```

Python replaces:

```text
{name}
```

with the value of `name`.

So it becomes:

```text
My name is Priyanka
```

---

# 8. f-string with Multiple Variables

```python
name = "Priyanka"
age = 23
city = "Rajahmundry"

print(f"My name is {name}, I am {age} years old and I live in {city}.")
```

### Output

```text
My name is Priyanka, I am 23 years old and I live in Rajahmundry.
```

---

# 9. f-string with Expressions

We can also put calculations inside `{ }`.

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

### Output

```text
Sum = 30
```

Another example:

```python
a = 10
b = 5

print(f"Addition = {a + b}")
print(f"Subtraction = {a - b}")
print(f"Multiplication = {a * b}")
print(f"Division = {a / b}")
```

### Output

```text
Addition = 15
Subtraction = 5
Multiplication = 50
Division = 2.0
```

---

# 10. f-string with User Input

This is very commonly used.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and my age is {age}.")
```

### Input

```text
Enter your name: Priyanka
Enter your age: 23
```

### Output

```text
My name is Priyanka and my age is 23.
```

---

# 11. f-string for Calculations

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Sum = {a + b}")
print(f"Difference = {a - b}")
print(f"Product = {a * b}")
```

### Input

```text
Enter first number: 20
Enter second number: 10
```

### Output

```text
Sum = 30
Difference = 10
Product = 200
```

---

# 12. f-string with Decimal Values

Suppose we want to display only **2 decimal places**.

We can use:

```python
:.2f
```

Example:

```python
price = 99.5678

print(f"Price = {price:.2f}")
```

### Output

```text
Price = 99.57
```

Another example:

```python
percentage = 85.6789

print(f"Percentage = {percentage:.2f}%")
```

### Output

```text
Percentage = 85.68%
```

---

# 13. Difference Between Normal String and f-string

### Normal string

```python
name = "Priyanka"

print("My name is name")
```

### Output

```text
My name is name
```

Python treats `name` as normal text.

### f-string

```python
name = "Priyanka"

print(f"My name is {name}")
```

### Output

```text
My name is Priyanka
```

The **`{name}`** tells Python to use the value stored in the variable.

---

# 14. f-string vs String Concatenation

Without f-string:

```python
name = "Priyanka"
age = 23

print("My name is " + name + " and my age is " + str(age))
```

Notice that we need:

```python
str(age)
```

because `age` is an integer.

### Using f-string

```python
name = "Priyanka"
age = 23

print(f"My name is {name} and my age is {age}")
```

Much simpler.

### Output

```text
My name is Priyanka and my age is 23
```

---

# 15. Complete Example – Student Details

```python
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print("\n----- Student Details -----")
print(f"Name  : {name}")
print(f"Age   : {age}")
print(f"Marks : {marks:.2f}")
```

### Input

```text
Enter student name: Priyanka
Enter age: 23
Enter marks: 85.678
```

### Output

```text
----- Student Details -----
Name  : Priyanka
Age   : 23
Marks : 85.68
```

---

# Quick Revision

| Concept    | Purpose                         | Example                |
| ---------- | ------------------------------- | ---------------------- |
| `input()`  | Takes input                     | `name = input()`       |
| `print()`  | Displays output                 | `print(name)`          |
| `sep`      | Separates multiple values       | `print(a,b,sep="-")`   |
| `end`      | Controls ending of print        | `print("Hi", end=" ")` |
| `f-string` | Formats strings using variables | `f"Hello {name}"`      |
| `{}`       | Inserts variable/expression     | `f"{a+b}"`             |
| `:.2f`     | Displays 2 decimal places       | `f"{price:.2f}"`       |

###  Most important syntax

**Input:**

```python
name = input("Enter name: ")
```

**Integer input:**

```python
age = int(input("Enter age: "))
```

**Output:**

```python
print(name)
```

**f-string:**

```python
print(f"My name is {name}")
```

**f-string with calculation:**

```python
print(f"Sum = {a + b}")
```

**f-string with 2 decimal places:**

```python
print(f"Price = {price:.2f}")
```

# Operators in Python

An **operator** is a symbol or keyword used to perform an operation on values or variables.

For example:

```python
a = 10
b = 5

print(a + b)
```

Here, `+` is an **operator**.

Python operators are mainly divided into these types:

1. **Arithmetic Operators**
2. **Assignment Operators**
3. **Comparison (Relational) Operators**
4. **Logical Operators**
5. **Bitwise Operators**
6. **Membership Operators**
7. **Identity Operators**

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform **mathematical calculations**.

| Operator | Name           | Example   | Result |
| -------- | -------------- | --------- | -----: |
| `+`      | Addition       | `10 + 5`  |   `15` |
| `-`      | Subtraction    | `10 - 5`  |    `5` |
| `*`      | Multiplication | `10 * 5`  |   `50` |
| `/`      | Division       | `10 / 5`  |  `2.0` |
| `%`      | Modulus        | `10 % 3`  |    `1` |
| `//`     | Floor Division | `10 // 3` |    `3` |
| `**`     | Exponent       | `2 ** 3`  |    `8` |

### Example

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)
```

### Output

```text
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Modulus: 1
Floor Division: 3
Exponent: 1000
```

### Important: `/` vs `//`

```python
print(10 / 3)
print(10 // 3)
```

Output:

```text
3.3333333333333335
3
```

* `/` → normal division
* `//` → floor division

---

# 2. Assignment Operators

Assignment operators are used to **assign or update values in variables**.

The basic assignment operator is:

```python
=
```

Example:

```python
a = 10
```

Here, `10` is assigned to `a`.

### Compound Assignment Operators

| Operator | Example   | Equivalent to |
| -------- | --------- | ------------- |
| `=`      | `a = 10`  | `a = 10`      |
| `+=`     | `a += 5`  | `a = a + 5`   |
| `-=`     | `a -= 5`  | `a = a - 5`   |
| `*=`     | `a *= 5`  | `a = a * 5`   |
| `/=`     | `a /= 5`  | `a = a / 5`   |
| `%=`     | `a %= 5`  | `a = a % 5`   |
| `//=`    | `a //= 5` | `a = a // 5`  |
| `**=`    | `a **= 2` | `a = a ** 2`  |

### Example

```python
a = 10

a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)
```

### Output

```text
15
12
24
```

### Explanation

Initially:

```text
a = 10
```

After:

```python
a += 5
```

we get:

```text
a = 10 + 5 = 15
```

Then:

```python
a -= 3
```

```text
a = 15 - 3 = 12
```

Then:

```python
a *= 2
```

```text
a = 12 × 2 = 24
```

---

# 3. Comparison Operators

Comparison operators are used to **compare two values**.

The result is always:

```text
True
```

or

```text
False
```

| Operator | Meaning                  | Example    |
| -------- | ------------------------ | ---------- |
| `==`     | Equal to                 | `10 == 10` |
| `!=`     | Not equal to             | `10 != 5`  |
| `>`      | Greater than             | `10 > 5`   |
| `<`      | Less than                | `10 < 5`   |
| `>=`     | Greater than or equal to | `10 >= 10` |
| `<=`     | Less than or equal to    | `5 <= 10`  |

### Example

```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

### Output

```text
False
True
True
False
True
False
```

### Important: `=` vs `==`

This is very important.

```python
a = 10
```

`=` means **assignment**.

```python
a == 10
```

`==` means **comparison**.

---

# 4. Logical Operators

Logical operators are used to combine **multiple conditions**.

Python has three logical operators:

```text
and
or
not
```

---

## `and`

Returns `True` only when **both conditions are True**.

### Example

```python
age = 25

print(age >= 18 and age <= 60)
```

### Output

```text
True
```

Because:

```text
age >= 18 → True
age <= 60 → True

True and True → True
```

### Truth table

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

---

## `or`

Returns `True` if **at least one condition is True**.

```python
age = 15

print(age < 18 or age > 60)
```

### Output

```text
True
```

Because:

```text
age < 18 → True
age > 60 → False

True or False → True
```

### Truth table

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

## `not`

`not` reverses the result.

```python
a = 10

print(not(a > 5))
```

### Output

```text
False
```

Because:

```text
a > 5 → True
not True → False
```

### Truth table

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

---

# 5. Bitwise Operators

Bitwise operators work on numbers at the **binary/bit level**.

The main bitwise operators are:

| Operator | Name        |            |
| -------- | ----------- | ---------- |
| `&`      | Bitwise AND |            |
| `        | `           | Bitwise OR |
| `^`      | Bitwise XOR |            |
| `~`      | Bitwise NOT |            |
| `<<`     | Left Shift  |            |
| `>>`     | Right Shift |            |

These are more commonly used in **low-level programming, embedded systems, optimization, and DSA**.

---

## Bitwise AND `&`

```python
a = 5
b = 3

print(a & b)
```

Binary:

```text
5 = 101
3 = 011
---------
    001
```

### Output

```text
1
```

---

## Bitwise OR `|`

```python
a = 5
b = 3

print(a | b)
```

```text
5 = 101
3 = 011
---------
    111
```

`111` in decimal = `7`.

### Output

```text
7
```

---

## Bitwise XOR `^`

XOR gives `1` when the bits are **different**.

```python
a = 5
b = 3

print(a ^ b)
```

```text
5 = 101
3 = 011
---------
    110
```

`110` = `6`.

### Output

```text
6
```

---

## Bitwise NOT `~`

```python
a = 5

print(~a)
```

### Output

```text
-6
```

For Python integers, `~x` is equivalent to:

```text
-x - 1
```

So:

```text
~5 = -5 - 1 = -6
```

---

## Left Shift `<<`

```python
a = 5

print(a << 1)
```

### Output

```text
10
```

A left shift by 1 is equivalent to multiplying by 2 for this example:

```text
5 × 2 = 10
```

---

## Right Shift `>>`

```python
a = 10

print(a >> 1)
```

### Output

```text
5
```

A right shift by 1 is equivalent to floor-dividing by 2 for this positive integer:

```text
10 // 2 = 5
```

---

# 6. Membership Operators

Membership operators are used to check whether a value **exists inside a sequence or collection**.

There are two:

```text
in
not in
```

---

## `in`

```python
name = "Python"

print("P" in name)
```

### Output

```text
True
```

Because `"P"` exists in `"Python"`.

Another example:

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
```

### Output

```text
True
```

---

## `not in`

```python
numbers = [10, 20, 30, 40]

print(50 not in numbers)
```

### Output

```text
True
```

Because `50` does not exist in the list.

---

# 7. Identity Operators

Identity operators are:

```text
is
is not
```

They check whether two variables refer to the **same object**, rather than merely having equal values.

---

## `is`

```python
a = [1, 2, 3]
b = a

print(a is b)
```

### Output

```text
True
```

Here `b = a`, so both names refer to the same list object.

---

## `is not`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)
```

### Output

```text
True
```

Although the contents are the same, they are separate list objects.

### Important: `==` vs `is`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

### Output

```text
True
False
```

* `==` → checks whether **values are equal**
* `is` → checks whether they are the **same object**

---

# Complete Classification

| Type           | Operators                                       |                         |
| -------------- | ----------------------------------------------- | ----------------------- |
| **Arithmetic** | `+`, `-`, `*`, `/`, `%`, `//`, `**`             |                         |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `//=`, `**=` |                         |
| **Comparison** | `==`, `!=`, `>`, `<`, `>=`, `<=`                |                         |
| **Logical**    | `and`, `or`, `not`                              |                         |
| **Bitwise**    | `&`, `                                          | `, `^`, `~`, `<<`, `>>` |
| **Membership** | `in`, `not in`                                  |                         |
| **Identity**   | `is`, `is not`                                  |                         |

##  Easy way to remember

```text
Arithmetic   → Calculate
Assignment   → Assign/Update
Comparison   → Compare
Logical      → Combine conditions
Bitwise      → Work with bits
Membership   → Check whether a value exists
Identity     → Check whether objects are the same
```
## Operator Precedence in Python

**Operator precedence** tells us **which operator is evaluated first** when an expression contains multiple operators.

For example:

```python
result = 10 + 5 * 2
print(result)
```

Output:

```text
20
```

Why?

`*` has higher precedence than `+`.

So:

```text
10 + 5 * 2
10 + 10
20
```

### Python Operator Precedence — Highest to Lowest

| Priority | Operator                         | Meaning                                           |
| -------- | -------------------------------- | ------------------------------------------------- |
| 1        | `()`                             | Parentheses                                       |
| 2        | `**`                             | Exponent                                          |
| 3        | `+x`, `-x`, `~x`                 | Unary operators                                   |
| 4        | `*`, `/`, `//`, `%`              | Multiplication, Division, Floor Division, Modulus |
| 5        | `+`, `-`                         | Addition, Subtraction                             |
| 6        | `<<`, `>>`                       | Bitwise shifts                                    |
| 7        | `&`                              | Bitwise AND                                       |
| 8        | `^`                              | Bitwise XOR                                       |
| 9        | `\|`                             | Bitwise OR                                        |
| 10       | `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison                                        |
| 11       | `not`                            | Logical NOT                                       |
| 12       | `and`                            | Logical AND                                       |
| 13       | `or`                             | Logical OR                                        |

### Example 1: Arithmetic

```python
result = 10 + 20 * 3
print(result)
```

Calculation:

```text
20 * 3 = 60
10 + 60 = 70
```

Output:

```text
70
```

### Example 2: Parentheses

```python
result = (10 + 20) * 3
print(result)
```

Calculation:

```text
10 + 20 = 30
30 * 3 = 90
```

Output:

```text
90
```

### Example 3: Exponent

```python
result = 10 + 2 ** 3
print(result)
```

Calculation:

```text
2 ** 3 = 8
10 + 8 = 18
```

Output:

```text
18
```

### Example 4: Multiple Operators

```python
result = 20 + 10 * 2 - 5
print(result)
```

First `*`:

```text
10 * 2 = 20
```

Then:

```text
20 + 20 - 5
40 - 5
35
```

Output:

```text
35
```

### Example 5: Logical Operators

```python
result = True or False and False
print(result)
```

`and` has higher precedence than `or`.

So:

```text
False and False → False
True or False → True
```

Output:

```text
True
```

### Easy Rule to Remember

For basic Python programs, remember:

**`()` → `**` → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`**

Also, if operators have the **same precedence**, Python generally evaluates them **left to right**.

Example:

```python
result = 20 / 5 * 2
print(result)
```

```text
20 / 5 = 4
4 * 2 = 8
```

Output:

```text
8
```



## 1. Print Student Name

**Problem:** Store a student's name in a variable and print it.

```python
name = "Priyanka"

print(name)
```

**Output:**

```text
Priyanka
```

**Concepts:** Variable, String, `print()`

---

## 2. Store and Print Age

```python
age = 22

print(age)
```

**Output:**

```text
22
```

**Concepts:** Variable, Integer

---

## 3. Print Different Data Types

```python
name = "Priyanka"
age = 22
percentage = 85.5
is_student = True

print(name)
print(age)
print(percentage)
print(is_student)
```

**Output:**

```text
Priyanka
22
85.5
True
```

**Concepts:** String, Integer, Float, Boolean

---

## 4. Find the Type of a Variable

```python
number = 100

print(type(number))
```

**Output:**

```text
<class 'int'>
```

**Concept:** `type()`

---

# Input and Type Casting

## 5. Read Name from User

```python
name = input("Enter your name: ")

print("Hello", name)
```

**Input:**

```text
Priyanka
```

**Output:**

```text
Enter your name: Priyanka
Hello Priyanka
```

**Concepts:** `input()`, String, `print()`

---

## 6. Add Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum =", sum)
```

**Input:**

```text
10
20
```

**Output:**

```text
Enter first number: 10
Enter second number: 20
Sum = 30
```

**Concepts:** Input, type casting, arithmetic operator

---

## 7. Find the Difference

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

difference = a - b

print("Difference =", difference)
```

**Input:**

```text
50
20
```

**Output:**

```text
Difference = 30
```

---

## 8. Calculate Product

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

product = a * b

print("Product =", product)
```

**Input:**

```text
8
5
```

**Output:**

```text
Product = 40
```

---

## 9. Calculate Average

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

average = (a + b + c) / 3

print("Average =", average)
```

**Input:**

```text
10
20
30
```

**Calculation:**

```text
(10 + 20 + 30) / 3
= 60 / 3
= 20
```

**Output:**

```text
Average = 20.0
```

**Concepts:** Arithmetic, parentheses, division

---

# Arithmetic Operators

## 10. Find Quotient and Remainder

```python
a = int(input("Enter number: "))
b = int(input("Enter divisor: "))

print("Quotient =", a // b)
print("Remainder =", a % b)
```

**Input:**

```text
17
5
```

**Output:**

```text
Quotient = 3
Remainder = 2
```

**Concepts:** `//`, `%`

---

## 11. Find Square and Cube

```python
number = int(input("Enter a number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)
```

**Input:**

```text
5
```

**Output:**

```text
Square = 25
Cube = 125
```

**Concept:** Exponent `**`

---

## 12. Calculate Simple Interest

Formula:

```text
SI = (P × R × T) / 100
```

```python
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)
```

**Input:**

```text
10000
5
2
```

**Calculation:**

```text
SI = (10000 × 5 × 2) / 100
   = 1000
```

**Output:**

```text
Simple Interest = 1000.0
```

---

# f-Strings

## 13. Display Student Details Using f-string

```python
name = "Priyanka"
age = 22
course = "Python"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")
```

**Output:**

```text
Name: Priyanka
Age: 22
Course: Python
```

**Concept:** f-string

---

## 14. Calculate and Display Result Using f-string

```python
a = 10
b = 20

sum = a + b

print(f"{a} + {b} = {sum}")
```

**Output:**

```text
10 + 20 = 30
```

---

## 15. Calculate Rectangle Area Using f-string

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print(f"Area of rectangle = {area}")
```

**Input:**

```text
10
5
```

**Output:**

```text
Area of rectangle = 50.0
```

---

# Comparison and Boolean Operators

## 16. Check Whether Number is Greater

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a > b)
```

**Input:**

```text
20
10
```

**Output:**

```text
True
```

**Concept:** Comparison operator, Boolean

---

## 17. Check Whether Two Numbers are Equal

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a == b)
```

**Input:**

```text
10
10
```

**Output:**

```text
True
```

---

## 18. Check Even or Odd Using Boolean

```python
number = int(input("Enter a number: "))

print(number % 2 == 0)
```

**Input:**

```text
24
```

**Calculation:**

```text
24 % 2 = 0
0 == 0 → True
```

**Output:**

```text
True
```

---

## 19. Check Voting Eligibility

```python
age = int(input("Enter your age: "))

print(age >= 18)
```

**Input:**

```text
20
```

**Output:**

```text
True
```

---

## 20. Check Positive Number

```python
number = int(input("Enter a number: "))

print(number > 0)
```

**Input:**

```text
-5
```

**Output:**

```text
False
```

---

# Logical Operators

## 21. Check Age and ID

```python
age = 25
has_id = True

print(age >= 18 and has_id)
```

**Output:**

```text
True
```

Here:

```text
age >= 18 → True
has_id → True

True and True → True
```

---

## 22. Check Weekend

```python
day = "Sunday"

print(day == "Saturday" or day == "Sunday")
```

**Output:**

```text
True
```

---

## 23. Use `not` Operator

```python
is_raining = False

print(not is_raining)
```

**Output:**

```text
True
```

Because:

```text
not False → True
```

---

# Strings

## 24. Concatenate First Name and Last Name

```python
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = first_name + " " + last_name

print(f"Full Name: {full_name}")
```

**Input:**

```text
Priyanka
Chitturi
```

**Output:**

```text
Full Name: Priyanka Chitturi
```

**Concepts:** String, input, concatenation, f-string



## 27. Access First and Last Character

```python
word = input("Enter a word: ")

print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
```

**Input:**

```text
Python
```

**Output:**

```text
First character: P
Last character: n
```

**Concepts:** String indexing

---

# Type Casting

## 28. Convert String to Integer

```python
number = input("Enter a number: ")

print(type(number))

number = int(number)

print(type(number))
print(number + 10)
```

**Input:**

```text
25
```

**Output:**

```text
<class 'str'>
<class 'int'>
35
```

**Important concept:**

```text
input()
   ↓
"25"
   ↓ int()
25
```

---

# Operator Precedence

## 29. Solve Expression According to Precedence

```python
result = 10 + 5 * 2

print(result)
```

**Calculation:**

Multiplication is performed first:

```text
5 * 2 = 10

10 + 10 = 20
```

**Output:**

```text
20
```

---

## 30. Complex Expression with Parentheses

```python
a = 10
b = 5
c = 2

result = (a + b) * c ** 2

print(f"Result = {result}")
```

**Calculation:**

First parentheses:

```text
(10 + 5) = 15
```

Then exponent:

```text
2 ** 2 = 4
```

Then multiplication:

```text
15 * 4 = 60
```

**Output:**

```text
Result = 60
```


## 1. Swap Two Numbers

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")
```

**Input:**

```text
Enter a: 10
Enter b: 20
```

**Output:**

```text
a = 20
b = 10
```

**Operators/concept:** Assignment, multiple assignment

---

## 2. Find Average of Three Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

average = (a + b + c) / 3

print(f"Average = {average}")
```

**Input:**

```text
10
20
30
```

**Output:**

```text
Average = 20.0
```

**Operators:** `+`, `/`

---

## 3. Find the Last Digit of a Number

```python
number = int(input("Enter a number: "))

last_digit = number % 10

print(f"Last digit = {last_digit}")
```

**Input:**

```text
Enter a number: 4587
```

**Output:**

```text
Last digit = 7
```

**Operator:** `%`

---

## 4. Remove the Last Digit

```python
number = int(input("Enter a number: "))

result = number // 10

print(f"Result = {result}")
```

**Input:**

```text
Enter a number: 4587
```

**Output:**

```text
Result = 458
```

**Operator:** `//`

---

## 5. Check Whether a Number is Even

No `if` statement — only operators.

```python
number = int(input("Enter a number: "))

result = number % 2 == 0

print(result)
```

**Input:**

```text
Enter a number: 24
```

**Output:**

```text
True
```

Calculation:

```text
24 % 2 = 0
0 == 0 → True
```

**Operators:** `%`, `==`

---



## 7. Find Absolute Value Without `if`

Python's arithmetic trick:

```python
number = int(input("Enter a number: "))

absolute = (number ** 2) ** 0.5

print(f"Absolute value = {absolute}")
```

**Input:**

```text
Enter a number: -25
```

**Output:**

```text
Absolute value = 25.0
```

**Operators:** `**`

---

## 8. Calculate Total and Percentage

```python
m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

total = m1 + m2 + m3
percentage = total / 300 * 100

print(f"Total = {total}")
print(f"Percentage = {percentage}")
```

**Input:**

```text
80
75
90
```

**Output:**

```text
Total = 245
Percentage = 81.66666666666667
```

**Operators:** `+`, `/`, `*`

---

## 9. Check Whether Number is in a Range

Check whether a number is between **10 and 50** using comparison and logical operators.

```python
number = int(input("Enter a number: "))

result = number >= 10 and number <= 50

print(result)
```

**Input:**

```text
Enter a number: 25
```

**Output:**

```text
True
```

Calculation:

```text
25 >= 10 → True
25 <= 50 → True

True and True → True
```

**Operators:** `>=`, `<=`, `and`





