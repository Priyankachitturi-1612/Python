# 🔹  Basic Function

```python
def greet():
    print("Hello World")

greet()   # Calling function
```

## 🔹 Positional Arguments

Arguments are passed in the **same order** as defined.

```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling with positional arguments
greet("Priya", 22)
```

Output:

```
Hello Priya, you are 22 years old.
```

---

## 🔹  Keyword Arguments

We explicitly specify which parameter we are passing.

```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling with keyword arguments
greet(age=22, name="Priya")
```

Output:

```
Hello Priya, you are 22 years old.
```

---

## 🔹 Default Arguments

If no value is passed, the default is used.

```python
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

# Case 1: With both arguments
greet("Priya", 22)

# Case 2: Without age (default will be used)
greet("Ravi")
```

Output:

```
Hello Priya, you are 22 years old.
Hello Ravi, you are 18 years old.
```

# 🔹 Function with Multiple Parameters 

```python
def add(a, b, c):
    print(a + b + c)

add(2, 3, 4)   # 9
```

---

# 🔹  Arbitrary Arguments (`*args`)

```python
def show_numbers(*nums):
    print(nums)   # Stored as tuple

show_numbers(1, 2, 3, 4, 5)
```

Output:

```
(1, 2, 3, 4, 5)
```

---

# 🔹 Keyword Arguments

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=21, name="Priya")
```

---

# 🔹 Arbitrary Keyword Arguments (`**kwargs`)

```python
def details(**info):
    print(info)   # Stored as dictionary

details(name="Priya", age=21, city="Vellore")
```

Output:

```
{'name': 'Priya', 'age': 21, 'city': 'Vellore'}
```
