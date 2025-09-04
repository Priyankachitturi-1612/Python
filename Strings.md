
# 🔹 **String Operations in Python**

A **string** is a sequence of characters inside quotes.
Example:

```python
s = "Hello World"
```

Python provides many operations we can perform on strings:


# 🔹 String Operations in Python with Multiple Examples

---

## **1. Concatenation (`+`)**

Joining two or more strings.

```python
# Example 1
a = "Good"
b = "Morning"
print(a + " " + b)  
# Output: Good Morning

# Example 2
first = "Data"
second = "Science"
third = " with Python"
print(first + second + third)  
# Output: DataScience with Python

# Example 3
x = "123"
y = "456"
print(x + y)  
# Output: 123456 (not addition, but joining)
```

---

## **2. Repetition (`*`)**

Repeating strings multiple times.

```python
# Example 1
print("Hi " * 3)  
# Output: Hi Hi Hi 

# Example 2
print("Python-" * 5)  
# Output: Python-Python-Python-Python-Python-

# Example 3
stars = "*"
print(stars * 10)  
# Output: **********
```

---


## **5. Length (`len()`)**

Count total characters (including spaces).

```python
# Example 1
print(len("Hello"))   # 5

# Example 2
print(len("Python Programming"))   # 18

# Example 3
print(len("  Spaces  "))   # 9
```

---

## **6. Membership (`in`, `not in`)**

Check if substring exists.

```python
msg = "Python is powerful"

# Example 1
print("Python" in msg)      # True

# Example 2
print("Java" not in msg)    # True

# Example 3
print("power" in msg)       # True
```

## ** Indexing**

Access characters by position.

```python
text = "Python"

# Example 1
print(text[0])   # P

# Example 2
print(text[3])   # h

# Example 3 (negative index from end)
print(text[-2])  # o
```

---

## ** Slicing**

Extract parts of string.

```python
word = "Programming"

# Example 1
print(word[0:6])    # Progra

# Example 2
print(word[3:8])    # gram

# Example 3 (using negative indexes)
print(word[-5:])    # mming
```
```python
s = "Programming"
print(s[0:6])   # Progra
print(s[3:])    # gramming
print(s[:5])    # Progr
print(s[::2])   # Pormig (step by 2)
```

Okay Priya 👍 you want a clear explanation of **string functions and methods** in Python.
Let’s break it down:

---

# 🔹 Difference Between **Functions** and **Methods**

* **Functions** → Built-in functions in Python that work on strings (and sometimes on other data types too).
  👉 Example: `len()`, `max()`, `min()`, `sorted()`

* **Methods** → Functions that belong specifically to **string objects** (called using `string.method()`).
  👉 Example: `"hello".upper()`, `"python".isalpha()`

---

# ✅ **String Functions in Python**

Common functions that can be applied to strings:

```python
s = "Python"

print(len(s))       # 6   → length of string
print(max(s))       # y   → highest alphabetical character
print(min(s))       # P   → smallest alphabetical character
print(sorted(s))    # ['P', 'h', 'n', 'o', 't', 'y']
print(str(123))     # '123' → convert number to string
```

---

# ✅ **String Methods in Python**

These are **special operations** available only for strings.

---

## 1. **Case Conversion**

```python
s = "hello world"

print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.title())       # Hello World
print(s.capitalize())  # Hello world
print(s.swapcase())    # HELLO WORLD -> hello world
```

---

## 2. **Check methods**

```python
s1 = "Python"
s2 = "123"
s3 = "Python123"
s4 = "   "

print(s1.isalpha())   # True  (only letters)
print(s2.isdigit())   # True  (only digits)
print(s3.isalnum())   # True  (letters + digits)
print(s4.isspace())   # True  (only spaces)
print(s1.isupper())   # False
print(s1.islower())   # False
```

---

## 3. **Search**

```python
s = "I love Python"

print(s.find("love"))     # 2
print(s.rfind("o"))       # 12
print(s.startswith("I"))  # True
print(s.endswith("Python")) # True
```

---

## 4. **Modify**

```python
s = "   Python is fun   "

print(s.strip())    # "Python is fun"  (remove spaces both sides)
print(s.lstrip())   # "Python is fun   "
print(s.rstrip())   # "   Python is fun"
print(s.replace("Python", "Java"))  # "   Java is fun   "
```

---

## 5. **Split & Join**

```python
s = "apple,banana,grapes"

print(s.split(","))   # ['apple', 'banana', 'grapes']

words = ["I", "love", "Python"]
print(" ".join(words))   # I love Python


# 🔹 **`split()` Method**

👉 Breaks a string into a list of substrings, based on a **separator** (default = space).

---

## ✅ Examples of `split()`

### 1. Default split (by spaces)

```python
s = "I love Python programming"
print(s.split())
# Output: ['I', 'love', 'Python', 'programming']
```

---

### 2. Split by comma

```python
s = "apple,banana,grapes,orange"
print(s.split(","))
# Output: ['apple', 'banana', 'grapes', 'orange']
```

---

### 3. Split by hyphen

```python
s = "2025-09-04"
print(s.split("-"))
# Output: ['2025', '09', '04']
```

---

### 4. Split with limit (maxsplit)

```python
s = "Python is very easy"
print(s.split(" ", 2))
# Output: ['Python', 'is', 'very easy']
```

👉 Here, only 2 splits are done.

---

### 5. Split by newline

```python
s = "Line1\nLine2\nLine3"
print(s.splitlines())
# Output: ['Line1', 'Line2', 'Line3']
```



# 🔹 **`join()` Method**

👉 Joins elements of a list (or any iterable) into a single string using a **separator**.



## ✅ Examples of `join()`

### 1. Join with space

```python
words = ["I", "love", "Python"]
print(" ".join(words))
# Output: I love Python
```


### 2. Join with hyphen

```python
letters = ['P', 'Y', 'T', 'H', 'O', 'N']
print("-".join(letters))
# Output: P-Y-T-H-O-N
```


### 3. Join with comma

```python
fruits = ["apple", "banana", "grapes"]
print(",".join(fruits))
# Output: apple,banana,grapes
```


### 4. Join numbers (after converting to string)

```python
numbers = [1, 2, 3, 4]
print("-".join(map(str, numbers)))
# Output: 1-2-3-4
```


### 5. Join lines with newline

```python
lines = ["Hello", "How are you?", "Bye!"]
print("\n".join(lines))
# Output:
# Hello
# How are you?
# Bye!
```


# 🎯 **Quick Summary**

* **`split()`** → Breaks string → list
* **`join()`** → Joins list → string
Great question Priya 👍 Escape sequences are **special characters** in Python strings that begin with a **backslash `\`**.
They let you represent things that are **hard to type directly** (like newline, tab, quotes, etc.).

---

# 🔹 Common Escape Sequences in Python

| Escape Sequence | Meaning                                         | Example              | Output           |
| --------------- | ----------------------------------------------- | -------------------- | ---------------- |
| `\'`            | Single quote                                    | `'It\'s fine'`       | It's fine        |
| `\"`            | Double quote                                    | `"He said \"Hi\""`   | He said "Hi"     |
| `\\`            | Backslash                                       | `"C:\\Users\\Priya"` | C:\Users\Priya   |
| `\n`            | Newline (line break)                            | `"Hello\nWorld"`     | Hello <br> World |
| `\t`            | Tab (4-8 spaces)                                | `"Hello\tWorld"`     | Hello World      |
| `\b`            | Backspace (deletes previous char)               | `"Hello\bWorld"`     | HellWorld        |
| `\r`            | Carriage return (cursor moves to start of line) | `"Hello\rWorld"`     | World            |
| `\f`            | Form feed (page break, rarely used)             | `"Hello\fWorld"`     | Hello<br>World   |
| `\ooo`          | Octal value                                     | `"\110\145\154"`     | Hel              |
| `\xhh`          | Hex value                                       | `"\x48\x65\x6C"`     | Hel              |
| `\u####`        | Unicode character (16-bit)                      | `"\u2602"`           | ☂                |
| `\U########`    | Unicode character (32-bit)                      | `"\U0001F600"`       | 😀               |

---

# 🔹 Examples in Code


# Newline and tab
print("Hello\nWorld")  
# Output:
# Hello
# World

print("Name\tAge")  
print("Priya\t22")
# Output:
# Name    Age
# Priya   22




## 6. **Formatting**

```python
name = "Priya"
age = 22

print(f"My name is {name}, I am {age}")   # f-string
print("My name is {}, I am {}".format(name, age))  # format()
```


# 🔹 **1. Using `format()`**

```python
# Basic placeholders
print("My name is {} and I am {} years old".format("Priya", 22))

# Index based
print("{0} scored {1} marks".format("Priya", 95.5))

# Named placeholders
print("Name: {n}, Age: {a}".format(n="Priya", a=22))

# Formatting numbers
print("Pi value is {:.2f}".format(3.14159))
```

# 🔹 **2. Using f-Strings**

```python
name = "Priya"
age = 22
marks = 95.5

# Simple insertion
print(f"My name is {name}, I am {age} years old")

# With expressions
print(f"Next year I will be {age+1}")

# Number formatting
pi = 3.14159
print(f"Value of pi: {pi:.3f}")   # 3 decimal places


✨ Quick recap:

* `format()` → `"{}".format(value)`
* `f-string` → `f"{value}"` (most used today)
* `map()` → apply a function to each element

\

