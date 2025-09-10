
## 🟢 What is Operator Overloading?

Normally, operators like `+`, `-`, `*`, `/` work for **built-in types**:

```python
print(10 + 20)      # 30
print("Priya" + " Kumari")  # Priya Kumari
```

Here:

* `+` **adds numbers** if operands are numbers.
* `+` **joins strings** if operands are strings.


* `+` → `__add__()`
* `-` → `__sub__()`
* `*` → `__mul__()`
* `/` → `__truediv__()`



## 🟢 Example Without Overloading

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)   # ❌ Error: unsupported operand type(s)
```

We get an **error** because Python doesn’t know **how to add two Book objects**.

---

## 🟢 Example With Operator Overloading

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):   # Overload +
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print("Total pages:", b1 + b2)   # Works now
```

**Output:**

```
Total pages: 300
```

Here:

* When we write `b1 + b2`, Python internally calls → `b1.__add__(b2)`
* Our `__add__` method tells Python **how to add two Book objects**.



✅ **Summary:**

* **Operator overloading = customizing how operators work for user-defined classes.**
* Built-in types already use it (numbers, strings, lists).
* We define it using **magic methods** (`__add__`, `__sub__`, etc.).

Great one Priya 👍
**Method overriding** happens when a **child class defines a method with the same name as its parent class**.
When you call that method using the child object → the **child’s method runs**, not the parent’s.

Here are some clear examples 👇

---

## 1. **Simple Method Overriding**

```python
class Parent:
    def display(self):
        print("This is Parent class method")

class Child(Parent):
    def display(self):
        print("This is Child class method (Overridden)")

obj = Child()
obj.display()   # Child method will run
```

**Output:**

```
This is Child class method (Overridden)
```

---

## 2. **Method Overriding with `super()`**

```python
class Parent:
    def show(self):
        print("Hello from Parent")

class Child(Parent):
    def show(self):
        super().show()   # Call Parent method also
        print("Hello from Child (Overridden)")

obj = Child()
obj.show()
```

**Output:**

```
Hello from Parent
Hello from Child (Overridden)
```

---

## 3. **Real Example – Animal Sounds**

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()
```

**Output:**

```
Dog barks
Cat meows
```

---

👉 Overriding helps in **polymorphism**: the same method name works differently based on the object type.

