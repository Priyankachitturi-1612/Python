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
Got it Priya 👍 you want **practice codes like FizzBuzz but using the *functions concept*** (with parameters, default args, \*args, \*\*kwargs etc.).
I’ll give you a set of small problems with **code examples** just like FizzBuzz.


## 🔹 1. Even or Odd Checker

```python
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))  # Even
print(check_even_odd(7))   # Odd
```


## 🔹 2. Factorial (using function)

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 120
```


## 🔹 3. Sum of Numbers (using \*args → arbitrary arguments)

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # 15
```



## 🔹 4. Greeting with Default Argument

```python
def greet(name="User"):
    return f"Hello {name}!"

print(greet())         # Hello User!
print(greet("Priya"))  # Hello Priya!
```



## 🔹 5. Student Info (using \*\*kwargs → keyword arguments)

```python
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Priya", age=21, course="Python")
```

✅ Output:

```
name: Priya
age: 21
course: Python
```


## 🔹 6. Power Function with Multiple Parameters

```python
def power(base, exponent):
    return base ** exponent

print(power(2, 3))  # 8
print(power(5, 2))  # 25
```


## 🔹 7. Max of Three Numbers

```python
def maximum(a, b, c):
    return max(a, b, c)

print(maximum(10, 20, 15))  # 20
```

