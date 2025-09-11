## 🔹 What is Abstraction?

**Abstraction** means **hiding the implementation details** and **showing only the essential features** to the user.
In Python, we achieve abstraction mainly using **abstract classes** and **abstract methods**.


## 🔹 Key Points:

✅ Abstract Class → A class that **cannot be instantiated** (you cannot create an object of it).
✅ Abstract Method → A method that is **declared but not implemented** (must be implemented by child classes).
✅ To create abstract classes, we use `ABC` (Abstract Base Class) from the `abc` module.


## 🔹 Syntax of Abstraction

from abc import ABC, abstractmethod

class ClassName(ABC):   # Inherit from ABC
    @abstractmethod
    def method_name(self):
        pass   # only declaration, no implementation

class ChildClass(ClassName):
    def method_name(self):
        # must implement this method
        print("Implementation of abstract method")

obj = ChildClass()  # We can only create object of child class
obj.method_name()

## 🔹 Example 1: Simple Abstraction

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):          # Abstract Class
    @abstractmethod
    def start(self):         # Abstract Method
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

# v = Vehicle()  # ❌ Error: Can't create object of abstract class
c = Car()
b = Bike()

c.start()  # Output: Car engine started
b.start()  # Output: Bike engine started
```

---

## 🔹 Example 2: Abstract Class with Concrete Method

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def info(self):   # normal (concrete) method
        print("All animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]
for a in animals:
    a.info()   # concrete method from parent
    a.sound()  # child implementation
```

---

### ✅ Key Benefits of Abstraction:

* Hides unnecessary implementation details.
* Provides a **blueprint** for child classes.
* Improves **code security** and **readability**.
* Makes code easier to maintain.




## 🔑 What is Encapsulation?

**Encapsulation = Binding (wrapping) data and methods together in a single unit (class) + controlling access to that data.**

In Python, we use **access modifiers** to achieve encapsulation:

* **Public** → Can be accessed anywhere.
* **Protected (`_variable`)** → Can be accessed in the class and subclasses (but still not strictly private).
* **Private (`__variable`)** → Cannot be accessed directly outside the class.



## ✅ Example 1: Simple Encapsulation (Public)

```python
class Student:
    def __init__(self, name, marks):
        self.name = name      # public variable
        self.marks = marks

    def display(self):        # method to show data
        print(f"Name: {self.name}, Marks: {self.marks}")

s = Student("Priya", 90)
s.display()
print(s.name)  # ✅ Can access directly (public)


Here, data and methods are inside one class → this is **basic encapsulation**.


## ✅ Example 2: Encapsulation with Private Variables

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance  # controlled access

# Create object
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.get_balance())  # ✅ Access via method

# print(acc.__balance)  # ❌ Error: can't access private variable directly


### 🔎 What Happened Here:

* `__balance` is **private** → cannot be accessed directly outside.
* We provide methods (`deposit`, `withdraw`, `get_balance`) to control how it is modified → **this is true encapsulation**.



## ✅ Example 3: Protected Members

```python
class Employee:
    def __init__(self, name, salary):
        self._salary = salary   # protected variable
        self.name = name

class Manager(Employee):
    def show(self):
        print(f"Manager: {self.name}, Salary: {self._salary}")  # can access

m = Manager("Priya", 50000)
m.show()
print(m._salary)  # ⚠️ Can access but should be avoided (not strictly private)


## 🧠 Why Use Encapsulation?

* **Security** → hide sensitive data (like balance, password).
* **Control** → give controlled way to access/modify data (through methods).
* **Flexibility** → you can change internal logic later without breaking outside code.



## 1️⃣ **Iterator (Python)**

An **iterator** lets you access elements **one by one**.

# Simple iterator example
nums = [1, 2, 3]

it = iter(nums)  # create iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# ❌ next(it) now will give StopIteration error


### ✅ Using `while` loop

nums = [1, 2, 3]
it = iter(nums)  # create iterator

while True:
    try:
        val = next(it)  # get next element
        print(val)
    except StopIteration:  # stop when iterator ends
        break
```

**Output:**

```
1
2
3
```


💡 **Tip:**

* `for` loop is easier because Python internally calls `iter()` and `next()`.
* Use `while + try-except` only if you want to **control iteration manually**.



✅ **Key idea:** `iter()` + `next()` lets you go through elements **manually**.


### Easy Custom Iterator Example

class Counter:
    def __init__(self, limit):
        self.num = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

for n in Counter(5):
    print(n)
```

Output:

```
1
2
3
4
5


## 2️⃣ **Generator (Python)**

A **generator** is a simpler way to create an iterator using `yield`.

# Simple generator example
def numbers(n):
    for i in range(1, n+1):
        yield i

for val in numbers(5):
    print(val)

Output:

```
1
2
3
4
5
```

✅ **Key idea:** `yield` produces one value at a time, **saves memory**.


### Generator Example: Squares

def squares(n):
    for i in range(n):
        yield i * i

for s in squares(5):
    print(s)

Output:

```
0
1
4
9
16
```

---

## 3️⃣ **Decorator (Python)**

A **decorator** adds extra behavior to a function **without changing the function code**.


# Simple decorator example
def greet_decorator(func):
    def wrapper():
        print("Hello! Welcome!")  # extra behavior
        func()
        print("Thanks!")           # extra behavior
    return wrapper

@greet_decorator
def say_hello():
    print("This is the main function.")

say_hello()


Output:

```
Hello! Welcome!
This is the main function.
Thanks!
```

✅ **Key idea:** Use `@decorator` above a function to **wrap it**.

---

### Quick Summary

| Concept   | Usage in 1 line                                     |
| --------- | --------------------------------------------------- |
| Iterator  | Access elements one by one (`iter()` + `next()`)    |
| Generator | Create lazy sequences using `yield`                 |
| Decorator | Modify/enhance function behavior using `@decorator` |



