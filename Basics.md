# Python Basics – Input/Output, Variables, Data Types & Type Casting



## 1. **Input / Output Functions**

* **Output (`print()`)** → Displays text, numbers, variables.
* **Input (`input()`)** → Reads user input as a **string**.

* `input()` always returns a string, so conversion is needed for numbers:

  ```python
  
  age = int(input("Enter age: "))  # type casting applied
  
  ```
  * `print()` has parameters like `sep` (separator), `end` (ending character).

  ```
  
  print("Priya", "Rani", sep="-", end=" :)")
  
  # Output: Priya-Rani :)
  
  ```


 Example Programs on `sep` and `end`



##  **Using `sep` (Separator)**

`sep` defines what string should separate multiple values in a `print()` statement.
By default, it is a **space** `" "`.

```python
# Default separator (space)
print("Priya", "Rani", "Python")

# Using '-' as separator
print("Priya", "Rani", "Python", sep="-")

# Using ',' as separator
print("10", "20", "30", sep=",")

# Using custom text as separator
print("Apple", "Banana", "Cherry", sep=" <3 ")
```

✅ Output:

```
Priya Rani Python
Priya-Rani-Python
10,20,30
Apple <3 Banana <3 Cherry
```


##  **Using `end`**

`end` defines what should be printed **at the end** of the statement.
By default, it is a **newline** `\n`.

```python
# Default end (newline)
print("Hello")
print("Priya")

# Using space instead of newline
print("Hello", end=" ")
print("Priya")

# Using custom symbols
print("Python", end=" ~ ")
print("Rocks")
```

✅ Output:

```
Hello
Priya
Hello Priya
Python ~ Rocks
```


##  **Using Both `sep` and `end` Together**

```python
# Combine sep and end
print("2025", "08", "28", sep="-", end=" <-- Today's Date\n")
print("Done")
```

✅ Output:

```
2025-08-28 <-- Today's Date
Done
```


## 1. **Input and Print Functions Program**

```python
# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))   # input always gives string → typecasted to int

# Printing output
print("Hello", name, "you are", age, "years old")

# Using sep and end in print
print("Priya", "Rani", sep="-", end=" :) ")
print("Welcome to Python")
```

✅ Output (example):

```
Enter your name: Priya
Enter your age: 20
Hello Priya you are 20 years old
Priya-Rani :) Welcome to Python
```


## 2. **Variables in Python**

* Variables are **names to store data** in memory.
* No need to declare type (Python is **dynamically typed**).
* Think of it like a container/label that holds some value.
* Variable Naming Rules

✅ Allowed:

Letters (a-z, A-Z)

Digits (0-9) but not at start

Underscore _

❌ Not allowed:

Starting with digit (2name )

Special characters (@name, x-y )

Keywords (class, def, if, etc. )

 Examples:

name = "Priya"    # valid
_age = 20         # valid
roll_no_1 = 101   # valid
2marks = 50       # invalid


* **Dynamic typing:**

  ```python
  x = 10
  x = "Priya"   # same variable can hold different types
  ```
* **Multiple assignment:**

  ```python
  a, b, c = 1, 2, 3
  name = age = "Priya"   # same value assigned to multiple vars
  ```
* **Global vs Local variables:**

  ```python
  x = 10  # global

  def show():
      global x
      x = 20
  ```
  ##  **Variables Program**

```python
# Simple variable assignment
x = 10
y = "Python"
z = 3.14

print("x =", x)
print("y =", y)
print("z =", z)

# Multiple assignment
a, b, c = 1, 2, 3
print("a =", a, "b =", b, "c =", c)

# Same value to multiple variables
p = q = r = "Priya"
print(p, q, r)
```

## 3. **Data Types in Python**

* **Basic types:** `int`, `float`, `str`, `bool`.
* **Collections:** `list`, `tuple`, `set`, `dict`.
* Got it Priya 👍 You’re asking about **basic data types in Python** like `str`, `int`, `bool`, `float`. Let’s go step by step so you can use this in your GitHub notes.


#  Python Basic Data Types

Python provides several **built-in data types** to store different kinds of values. The most commonly used ones are:


## 1️⃣ **int (Integer)**

* Represents **whole numbers** (positive, negative, or zero).
* No decimal points.
* Example:

  ```python
  x = 10
  y = -25
  z = 0
  print(type(x))   # <class 'int'>
  ```


## 2️⃣ **float (Floating-point number)**

* Represents **numbers with decimals**.
* Can also represent scientific notation (`e` or `E`).
* Example:

  ```python
  a = 3.14
  b = -45.6
  c = 1.2e3   # 1.2 × 10³ = 1200.0
  print(type(a))   # <class 'float'>
  ```


## 3️⃣ **str (String)**

* Sequence of characters enclosed in **single quotes `'`**, **double quotes `"`**, or **triple quotes `'''` / `"""`**.
* Strings are **immutable** (can’t change directly after creation).
* Python stores some strings in a string pool (to save memory).
* If strings were mutable, changing one string would also change all other variables pointing to it.
* The string pool (also called interning) is a special memory area where Python stores unique immutable strings.
* If the same string value appears multiple times, Python reuses the same object from the pool instead of creating a new one.
* Memory Efficiency → Saves memory by avoiding duplicate copies of the same string.
* Speed → Comparing strings is faster if they are the same object.
  
  Example:

  ```python
  name = "Priya"
  msg = 'Hello, Python!'
  paragraph = """This is 
  a multiline string."""
  print(type(name))   # <class 'str'>
  ```


## 4️⃣ **bool (Boolean)**

* Represents **truth values**: `True` or `False`.
* Often used in conditions and comparisons.
* Example:

  ```python
  is_python_easy = True
  is_java_easy = False
  print(type(is_python_easy))   # <class 'bool'>
  ```


## 5️⃣ **NoneType**

* Special type that represents **no value / null**.
* Only value is `None`.
* Example:

  ```python
  data = None
  print(type(data))   # <class 'NoneType'>
  ```

# ✅ Quick Example Program

```python
x = 100               # int
pi = 3.14159          # float
name = "Priya"        # str
is_student = True     # bool
nothing = None        # NoneType

print(x, type(x))
print(pi, type(pi))
print(name, type(name))
print(is_student, type(is_student))
print(nothing, type(nothing))
```

👉 Output:

```
100 <class 'int'>
3.14159 <class 'float'>
Priya <class 'str'>
True <class 'bool'>
None <class 'NoneType'>
```


⚡ Advanced Note: Python is **dynamically typed**, so you don’t need to declare the type explicitly — it’s decided at runtime.


* **Mutable vs Immutable:**

  * Lists & dicts are mutable (can change).
  * Tuples & strings are immutable.
* **Type checking:**

  ```python
  x = 5.5
  print(type(x))   # <class 'float'>
  ```
* **None type:** Special type representing no value.

  ```python
  result = None
  ```
* **Complex numbers:**

  ```python
  z = 3 + 4j
  print(z.real, z.imag)   # 3.0 4.0
  ```
  ## 3. **Data Types Program**

```python
# Basic data types
num = 100          # int
pi = 3.1415        # float
name = "Priya"     # str
is_student = True  # bool

print(type(num))       # <class 'int'>
print(type(pi))        # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_student))# <class 'bool'>

# Collection data types
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_set = {7, 8, 9}
my_dict = {"name": "Priya", "age": 20}

print(type(my_list))   # <class 'list'>
print(type(my_tuple))  # <class 'tuple'>
print(type(my_set))    # <class 'set'>
print(type(my_dict))   # <class 'dict'>

# Complex number
z = 2 + 5j
print("Real part:", z.real)
print("Imaginary part:", z.imag)
```


## 4. **Type Casting (Type Conversion)**


* Conversion functions: `int()`, `float()`, `str()`, `bool()`.
* Needed when using `input()` or mixing types.

* **Implicit casting (Type Promotion):**
  Python automatically converts smaller to larger types in expressions.

  ```python
  x = 5     # int
  y = 2.5   # float
  print(x + y)  # 7.5 (int promoted to float)
  ```
* **Explicit casting:**

  ```python
  s = "123"
  n = int(s)   # string → int
  ```
* **Boolean casting:**

  ```python
  print(bool(""))    # False
  print(bool("Hi"))  # True
  print(bool(0))     # False
  print(bool(10))    # True
  ```
 ## 4. **Type Casting**

```python
# Explicit type casting
x = "100"
y = int(x)       # string → int
z = float(x)     # string → float

print("x:", x, type(x))
print("y:", y, type(y))
print("z:", z, type(z))

# Boolean type casting
print(bool(""))      # False (empty string)
print(bool("Hi"))    # True (non-empty string)
print(bool(0))       # False
print(bool(10))      # True

# Implicit type casting (type promotion)
a = 10      # int
b = 2.5     # float
c = a + b   # int + float → float
print("c:", c, type(c))
```

✅ Output:

```
x: 100 <class 'str'>
y: 100 <class 'int'>
z: 100.0 <class 'float'>
False
True
False
True
c: 12.5 <class 'float'>
```


* `print()` → output | `input()` → input (string).
* Variables are dynamic; can be reassigned.
* Data Types: int, float, str, bool, list, tuple, set, dict, None, complex.
* Type Casting: implicit (auto), explicit (`int()`, `float()`, `str()`).

