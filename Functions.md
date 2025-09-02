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


# 🔹 **1. Lambda Functions (Anonymous Functions)**

👉 A **lambda function** is a small, unnamed (anonymous) function defined with the keyword `lambda`.

* It can take any number of arguments.
* But can only contain **a single expression**.
* Commonly used for short, simple tasks.

### ✅ Syntax:

```python
lambda arguments: expression
```

### ✅ Example 1: Square of a number

```python
square = lambda x: x * x
print(square(5))   # 25
```

### ✅ Example 2: Add two numbers

```python
add = lambda a, b: a + b
print(add(10, 20))  # 30
```


 **Use Case:** Quick functions where you don’t want to define a full `def` function.


# 🔹 **2. Recursive Functions**

👉 A **recursive function** is a function that calls **itself** until a base condition is met.

* Must have a **base case** (to stop recursion).
* Useful for problems that can be broken down into smaller sub-problems.


### ✅ Example 1: Factorial

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))   # 120
```

###  Fibonacci Series

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))   # 8  (0,1,1,2,3,5,8)
```



##  Reverse a Number (Recursion)

```python
def reverse_number(n, rev=0):
    # Base case: when n becomes 0, return the reversed number
    if n == 0:
        return rev
    
    # Extract last digit and build reverse
    last_digit = n % 10
    rev = rev * 10 + last_digit
    
    return reverse_number(n // 10, rev)

# Example
num = 1234
print("Reverse of", num, "is:", reverse_number(num))  # 4321
```

---

##  Count Digits of a Number (Recursion)

```python
def count_digits(n):
    # Base case: if n becomes 0, no more digits left
    if n == 0:
        return 0
    
    # Count 1 digit + recursive call on remaining number
    return 1 + count_digits(n // 10)

# Example
num = 98765
print("Number of digits:", count_digits(num))  # 5
```


📌 Difference:

* **Lambda** → For *short, inline, one-expression* functions.
* **Recursive** → For *repeated self-calling problems with base case*.

