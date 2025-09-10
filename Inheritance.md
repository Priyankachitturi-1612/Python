
In **Python inheritance**, the `super()` keyword is used to **call methods/constructors of the parent class** inside a child class.


## 1. **Using `super()` to Call Parent Constructor**

```python
class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor called")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # Calls Parent __init__
        self.age = age
        print("Child constructor called")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

obj = Child("Priya", 22)
obj.display()
```

**Output:**

```
Parent constructor called
Child constructor called
Name: Priya, Age: 22
```

---

## 2. **Using `super()` to Call Parent Method**

```python
class Parent:
    def show(self):
        print("This is Parent method")

class Child(Parent):
    def show(self):
        super().show()   # Calls Parent method
        print("This is Child method")

obj = Child()
obj.show()
```

**Output:**

```
This is Parent method
This is Child method
```


## 3. **In Multilevel Inheritance**

```python
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greet(self):
        super().greet()
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

obj = Child()
obj.greet()
```

**Output:**

```
Hello from Grandparent
Hello from Parent
Hello from Child
```

