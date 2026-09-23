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

##  1. Even or Odd Checker

```python
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))  # Even
print(check_even_odd(7))   # Odd
```


##  2. Factorial (using function)

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 120
```


## 3. Sum of Numbers (using \*args → arbitrary arguments)

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # 15
```



##  4. Greeting with Default Argument

```python
def greet(name="User"):
    return f"Hello {name}!"

print(greet())         # Hello User!
print(greet("Priya"))  # Hello Priya!
```



##  5. Student Info (using \*\*kwargs → keyword arguments)

```python
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Priya", age=21, course="Python")
```

 Output:

```
name: Priya
age: 21
course: Python
```


##  6. Power Function with Multiple Parameters

```python
def power(base, exponent):
    return base ** exponent

print(power(2, 3))  # 8
print(power(5, 2))  # 25
```


##  7. Max of Three Numbers

```python
def maximum(a, b, c):
    return max(a, b, c)

print(maximum(10, 20, 15))  # 20
```


#  **1. Lambda Functions (Anonymous Functions)**

 A **lambda function** is a small, unnamed (anonymous) function defined with the keyword `lambda`.

* It can take any number of arguments.
* But can only contain **a single expression**.
* Commonly used for short, simple tasks.

###  Syntax:

```python
lambda arguments: expression
```

###  Example 1: Square of a number

```python
square = lambda x: x * x
print(square(5))   # 25
```

###  Example 2: Add two numbers

```python
add = lambda a, b: a + b
print(add(10, 20))  # 30
```
**Checking even or odd**
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(7))  # Odd

Yes. Since you're learning **functions**, lambda functions are a good next topic.

# Python Lambda Functions

A **lambda function** is a small anonymous function written in a single line.

### Normal function

```python
def square(n):
    return n * n

print(square(5))
```

### Lambda function

```python
square = lambda n: n * n

print(square(5))
```

**Output:**

```text
25
```

### Syntax

```python
lambda arguments: expression
```

For example:

```python
lambda a, b: a + b
```

## 1. Square of a Number

**Question:** Write a lambda function to find the square of a number.

```python
square = lambda n: n * n

n = int(input())

print(square(n))
```

**Input:**

```text
8
```

**Output:**

```text
64
```

---

## 2. Cube of a Number

**Question:** Write a lambda function to find the cube of a number.

```python
cube = lambda n: n ** 3

n = int(input())

print(cube(n))
```

**Input:**

```text
4
```

**Output:**

```text
64
```

---

## 3. Even or Odd

**Question:** Write a lambda function to determine whether a number is even or odd.

```python
check = lambda n: "Even" if n % 2 == 0 else "Odd"

n = int(input())

print(check(n))
```

**Input:**

```text
17
```

**Output:**

```text
Odd
```

---

## 4. Largest of Two Numbers

**Question:** Write a lambda function to find the largest of two numbers.

```python
largest = lambda a, b: a if a > b else b

a = int(input())
b = int(input())

print(largest(a, b))
```

**Input:**

```text
45
72
```

**Output:**

```text
72
```

---

## 5. Largest of Three Numbers

**Question:** Write a lambda function to find the largest of three numbers.

```python
largest = lambda a, b, c: max(a, b, c)

a = int(input())
b = int(input())
c = int(input())

print(largest(a, b, c))
```

**Input:**

```text
45
72
61
```

**Output:**

```text
72
```

---

## 6. Check Positive, Negative or Zero

```python
check = lambda n: "Positive" if n > 0 else "Negative" if n < 0 else "Zero"

n = int(input())

print(check(n))
```

**Input:**

```text
-25
```

**Output:**

```text
Negative
```

---

## 7. Find Last Digit

**Question:** Write a lambda function to extract the last digit of a number.

```python
last_digit = lambda n: n % 10

n = int(input())

print(last_digit(n))
```

**Input:**

```text
58329
```

**Output:**

```text
9
```

---

## 8. Check Divisibility

**Question:** Write a lambda function to check whether a number is divisible by both 3 and 5.

```python
check = lambda n: "Divisible" if n % 3 == 0 and n % 5 == 0 else "Not Divisible"

n = int(input())

print(check(n))
```

**Input:**

```text
45
```

**Output:**

```text
Divisible
```

---

# Lambda + `map()`

Lambda functions become especially useful with functions such as `map()`.

## 9. Square Every Number

```python
numbers = list(map(int, input().split()))

result = list(map(lambda n: n * n, numbers))

print(result)
```

**Input:**

```text
2 4 6 8 10
```

**Output:**

```text
[4, 16, 36, 64, 100]
```

---

## 10. Cube Every Number

```python
numbers = list(map(int, input().split()))

result = list(map(lambda n: n ** 3, numbers))

print(result)
```

**Input:**

```text
1 2 3 4
```

**Output:**

```text
[1, 8, 27, 64]
```

---

# Lambda + `filter()`

## 11. Extract Even Numbers

```python
numbers = list(map(int, input().split()))

result = list(filter(lambda n: n % 2 == 0, numbers))

print(result)
```

**Input:**

```text
11 24 35 42 57 60
```

**Output:**

```text
[24, 42, 60]
```

---

## 12. Extract Numbers Greater Than 50

```python
numbers = list(map(int, input().split()))

result = list(filter(lambda n: n > 50, numbers))

print(result)
```

**Input:**

```text
25 67 42 89 51 30
```

**Output:**

```text
[67, 89, 51]
```

---

## 13. Extract Numbers Divisible by 3 and 5

```python
numbers = list(map(int, input().split()))

result = list(filter(lambda n: n % 3 == 0 and n % 5 == 0, numbers))

print(result)
```

**Input:**

```text
15 20 30 42 45 50 60
```

**Output:**

```text
[15, 30, 45, 60]
```

---

# More Difficult Lambda Problems

## 14. Find the Maximum Using Lambda

**Question:** Use `reduce()` and a lambda function to find the largest number.

```python
from functools import reduce

numbers = list(map(int, input().split()))

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print(maximum)
```

**Input:**

```text
25 78 42 91 36 64
```

**Output:**

```text
91
```

---

## 15. Product of All Numbers Using Lambda

```python
from functools import reduce

numbers = list(map(int, input().split()))

product = reduce(lambda a, b: a * b, numbers)

print(product)
```

**Input:**

```text
2 3 4 5
```

**Output:**

```text
120
```

---

### A good learning order for your students

Teach lambda in this order:

```text
Normal function
      ↓
Lambda syntax
      ↓
Lambda with one argument
      ↓
Lambda with multiple arguments
      ↓
Conditional expression with lambda
      ↓
map() + lambda
      ↓
filter() + lambda
      ↓
reduce() + lambda
```

The **most important three combinations** to teach are:

```python
map(lambda x: ...)
filter(lambda x: ...)
reduce(lambda x, y: ...)
```



## 1. Check Prime Number

**Question:** Write a function to check whether a given number is prime.

```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input())

if is_prime(n):
    print("Prime")
else:
    print("Not Prime")
```

**Input:**

```text
29
```

**Output:**

```text
Prime
```

---

## 2. Prime Numbers in a Range

**Question:** Write a function to print all prime numbers between two given numbers.

```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


start = int(input())
end = int(input())

for n in range(start, end + 1):
    if is_prime(n):
        print(n, end=" ")
```

**Input:**

```text
10
30
```

**Output:**

```text
11 13 17 19 23 29
```

---

## 3. Armstrong Number

**Question:** Write a function to check whether a number is an Armstrong number.

```python
def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


n = int(input())

if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
```

**Input:**

```text
153
```

**Output:**

```text
Armstrong Number
```

---

## 4. Armstrong Numbers in a Range

**Question:** Write a function to print all Armstrong numbers between two given numbers.

```python
def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


start = int(input())
end = int(input())

for n in range(start, end + 1):
    if is_armstrong(n):
        print(n, end=" ")
```

**Input:**

```text
100
500
```

**Output:**

```text
153 370 371 407
```

---

## 5. Strong Number

**Question:** Write a function to check whether a number is a Strong number.

```python
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


def is_strong(n):
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == n


n = int(input())

if is_strong(n):
    print("Strong Number")
else:
    print("Not Strong Number")
```

**Input:**

```text
145
```

**Output:**

```text
Strong Number
```

---

## 6. Reverse a Number

**Question:** Write a function to reverse a number without converting it into a string.

```python
def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return reverse


n = int(input())

print(reverse_number(n))
```

**Input:**

```text
58321
```

**Output:**

```text
12385
```

---

## 7. Palindrome Number

**Question:** Write a function to check whether a number is a palindrome.

```python
def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return reverse


def is_palindrome(n):
    return n == reverse_number(n)


n = int(input())

if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
```

**Input:**

```text
1221
```

**Output:**

```text
Palindrome
```

---

## 8. GCD of Two Numbers

**Question:** Write a function to find the GCD of two numbers.

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


a = int(input())
b = int(input())

print("GCD =", gcd(a, b))
```

**Input:**

```text
36
48
```

**Output:**

```text
GCD = 12
```

---

## 9. LCM Using GCD

**Question:** Write a function to find the LCM of two numbers using a separate GCD function.

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


a = int(input())
b = int(input())

print("LCM =", lcm(a, b))
```

**Input:**

```text
12
18
```

**Output:**

```text
LCM = 36
```

---

## 10. Count Even, Odd and Zero Digits

**Question:** Write a function to count the number of even, odd, and zero digits in a number.

```python
def count_digits(n):
    even = 0
    odd = 0
    zero = 0

    while n > 0:
        digit = n % 10

        if digit == 0:
            zero += 1
        elif digit % 2 == 0:
            even += 1
        else:
            odd += 1

        n //= 10

    return even, odd, zero


n = int(input())

even, odd, zero = count_digits(n)

print("Even =", even)
print("Odd =", odd)
print("Zero =", zero)
```

**Input:**

```text
20578340
```

**Output:**

```text
Even = 4
Odd = 3
Zero = 1
```

---

# 11. Decimal to Binary

**Question:** Write a function to convert a decimal number into binary without using `bin()`.

```python
def decimal_to_binary(n):
    binary = ""

    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return binary


n = int(input())

print(decimal_to_binary(n))
```

**Input:**

```text
25
```

**Output:**

```text
11001
```

---

# 12. Binary to Decimal

**Question:** Write a function to convert a binary number into decimal.

```python
def binary_to_decimal(binary):
    decimal = 0
    power = 0

    while binary > 0:
        digit = binary % 10
        decimal += digit * (2 ** power)
        power += 1
        binary //= 10

    return decimal


binary = int(input())

print(binary_to_decimal(binary))
```

**Input:**

```text
11001
```

**Output:**

```text
25
```

---

# 13. Fibonacci Series

**Question:** Write a function to print the first `n` Fibonacci numbers.

```python
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input())

fibonacci(n)
```

**Input:**

```text
10
```

**Output:**

```text
0 1 1 2 3 5 8 13 21 34
```

---

# 14. Recursive Factorial

**Question:** Write a recursive function to find the factorial of a number.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


n = int(input())

print(factorial(n))
```

**Input:**

```text
6
```

**Output:**

```text
720
```

---

# 15. Recursive Sum of Digits

**Question:** Write a recursive function to find the sum of all digits of a number.

```python
def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)


n = int(input())

print(digit_sum(n))
```

**Input:**

```text
98765
```

**Output:**

```text
35
```

---

# 16. Recursive String Reverse

**Question:** Write a recursive function to reverse a string.

```python
def reverse_string(s):
    if len(s) == 0:
        return ""

    return reverse_string(s[1:]) + s[0]


s = input()

print(reverse_string(s))
```

**Input:**

```text
PYTHON
```

**Output:**

```text
NOHTYP
```

---

# 17. Recursive Power

**Question:** Write a recursive function to calculate `x` raised to the power `n`.

```python
def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n - 1)


x = int(input())
n = int(input())

print(power(x, n))
```

**Input:**

```text
3
5
```

**Output:**

```text
243
```

---

# 18. Perfect Number

**Question:** Write a function to check whether a number is a Perfect number.

```python
def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


n = int(input())

if is_perfect(n):
    print("Perfect Number")
else:
    print("Not Perfect Number")
```

**Input:**

```text
28
```

**Output:**

```text
Perfect Number
```

---

# 19. Automorphic Number

**Question:** A number is Automorphic if its square ends with the number itself. Write a function to check it.

```python
def is_automorphic(n):
    square = n * n
    digits = len(str(n))

    return square % (10 ** digits) == n


n = int(input())

if is_automorphic(n):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")
```

**Input:**

```text
25
```

**Output:**

```text
Automorphic Number
```

Because:

```text
25 × 25 = 625
```

and `625` ends with `25`.

---

# 20. Harshad Number

**Question:** A number is a Harshad number if it is divisible by the sum of its digits.

```python
def digit_sum(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def is_harshad(n):
    total = digit_sum(n)

    return n % total == 0


n = int(input())

if is_harshad(n):
    print("Harshad Number")
else:
    print("Not Harshad Number")
```

**Input:**

```text
18
```

**Output:**

```text
Harshad Number
```

---

# 21. Happy Number

**Question:** Write a function to check whether a number is a Happy number.

```python
def sum_square_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10

    return total


def is_happy(n):
    while n != 1 and n != 4:
        n = sum_square_digits(n)

    return n == 1


n = int(input())

if is_happy(n):
    print("Happy Number")
else:
    print("Not Happy Number")
```

**Input:**

```text
19
```

**Output:**

```text
Happy Number
```

---

# 22. Digital Root

**Question:** Write a function to repeatedly add the digits of a number until a single digit remains.

```python
def digit_sum(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def digital_root(n):
    while n >= 10:
        n = digit_sum(n)

    return n


n = int(input())

print(digital_root(n))
```

**Input:**

```text
9875
```

**Output:**

```text
2
```

Explanation:

```text
9 + 8 + 7 + 5 = 29
2 + 9 = 11
1 + 1 = 2
```

---

# 23. Sum of Factorials of Digits

**Question:** Write a function to find the sum of the factorials of all digits of a number.

```python
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


def factorial_digit_sum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += factorial(digit)
        n //= 10

    return total


n = int(input())

print(factorial_digit_sum(n))
```

**Input:**

```text
145
```

**Output:**

```text
145
```

Because:

```text
1! + 4! + 5!
= 1 + 24 + 120
= 145
```

---

# 24. Largest and Smallest Digit

**Question:** Write a function to find the largest and smallest digit in a number.

```python
def largest_smallest(n):
    largest = 0
    smallest = 9

    while n > 0:
        digit = n % 10

        if digit > largest:
            largest = digit

        if digit < smallest:
            smallest = digit

        n //= 10

    return largest, smallest


n = int(input())

largest, smallest = largest_smallest(n)

print("Largest digit =", largest)
print("Smallest digit =", smallest)
```

**Input:**

```text
583214
```

**Output:**

```text
Largest digit = 8
Smallest digit = 1
```

---

# 25. Frequency of Each Digit

**Question:** Write a function to count how many times each digit occurs in a number.

```python
def digit_frequency(n):
    frequency = [0] * 10

    while n > 0:
        digit = n % 10
        frequency[digit] += 1
        n //= 10

    return frequency


n = int(input())

frequency = digit_frequency(n)

for digit in range(10):
    if frequency[digit] > 0:
        print(digit, "->", frequency[digit])
```

**Input:**

```text
1223334555
```

**Output:**

```text
1 -> 1
2 -> 2
3 -> 3
4 -> 1
5 -> 3
```

> Note: This uses a small list internally as a frequency counter. If you want **strictly no lists at all**, this question can be replaced with a nested-loop digit-frequency version.

---

# 26. `*args` – Largest Number

**Question:** Write a function using `*args` to find the largest number among any number of arguments.

```python
def largest(*args):
    maximum = args[0]

    for num in args:
        if num > maximum:
            maximum = num

    return maximum


print(largest(12, 45, 7, 89, 34, 56))
```

**Output:**

```text
89
```

---

# 27. `*args` – Sum and Average

**Question:** Write a function using `*args` to calculate the sum and average of any number of numbers.

```python
def calculate(*numbers):
    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    return total, average


total, average = calculate(10, 20, 30, 40, 50)

print("Sum =", total)
print("Average =", average)
```

**Output:**

```text
Sum = 150
Average = 30.0
```

---

# 28. `**kwargs` – Student Marks

**Question:** Write a function using `**kwargs` to calculate the total marks of different subjects.

```python
def total_marks(**marks):
    total = 0

    for subject, mark in marks.items():
        total += mark

    return total


total = total_marks(
    Python=85,
    Java=90,
    SQL=78,
    Angular=88
)

print("Total Marks =", total)
```

**Output:**

```text
Total Marks = 341
```

---

# 29. Student Result Using Multiple Functions

**Question:** Write a program using separate functions to calculate total marks, percentage, and grade.

```python
def total_marks(m1, m2, m3, m4, m5):
    return m1 + m2 + m3 + m4 + m5


def percentage(total):
    return total / 5


def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"


m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())

total = total_marks(m1, m2, m3, m4, m5)
percent = percentage(total)
result = grade(percent)

print("Total =", total)
print("Percentage =", percent)
print("Grade =", result)
```

**Input:**

```text
85
92
78
88
95
```

**Output:**

```text
Total = 438
Percentage = 87.6
Grade = B
```
`



# 🔹 **2. Recursive Functions**

 A **recursive function** is a function that calls **itself** until a base condition is met.

* Must have a **base case** (to stop recursion).
* Useful for problems that can be broken down into smaller sub-problems.


###  Example 1: Factorial

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


