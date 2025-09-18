## 📌 1. What is a Stack?

A **stack** is a **linear data structure** that follows the rule:

**LIFO → Last In, First Out**

Think of a **stack of plates** in a cafeteria:

* You put a new plate on top (**push**)
* You take the top plate first (**pop**)


### 🔑 Key Operations of Stack:

1. **Push** → Add an element to the top of the stack
2. **Pop** → Remove (and return) the top element from the stack
3. **Peek / Top** → See the top element without removing it
4. **isEmpty** → Check if stack is empty
5. **Size** → Get number of elements in the stack


## 📌 2. Why Do We Use a Stack? (Applications)

Stacks are super useful in many real-world and computer problems:

* **Undo/Redo functionality** (text editors, Photoshop)
* **Backtracking** (mazes, puzzles, DFS)
* **Expression evaluation** (`(a+b)*c`, postfix/prefix conversion)
* **Function call stack** (when you call a function in Python, it gets pushed on call stack, when function ends, it pops)
* **Browser history** (back/forward buttons)


## 📌 3. How Can We Implement a Stack?

In Python, we can implement a stack in **three ways**:

---

### ✅ Option 1: Using Python List (Simple & Built-in)

```
class Stack:
    def __init__(self):
        self.stack = []  # use list internally

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element:", s.peek())  # 30
print("Popped:", s.pop())       # removes 30
print("Popped:", s.pop())       # removes 20
print("Is empty?", s.is_empty()) # False
print("Popped:", s.pop())       # removes 10
print("Is empty?", s.is_empty()) # True
```

---

### ✅ Option 2: Using `collections.deque` (Better Performance)

```
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"
```

---

### ✅ Option 3: Using Linked List (Custom Implementation)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "Stack is empty"
        removed = self.top.data
        self.top = self.top.next
        return removed

    def peek(self):
        return self.top.data if self.top else "Stack is empty"

    def is_empty(self):
        return self.top is None
```

---

## 📌 4. Quick Visualization

If we `push(10), push(20), push(30)`, stack looks like:

```
Top → [30]
       [20]
       [10]
```

If we `pop()`, we remove `30` (last inserted).


✅ **Summary:**

* Stack = LIFO data structure
* Operations: Push, Pop, Peek, isEmpty, Size
* Uses: Undo, recursion, parsing, backtracking
* Implementation: List, deque, or Linked List

##  **Stack**

```
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class
class Stack:
    def __init__(self):
        self.top = None  # pointer to top node

    # PUSH operation
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {value} onto stack.")

    # POP operation
    def pop(self):
        if self.is_empty():
            print("Stack is empty, nothing to pop.")
            return None
        removed = self.top.data
        self.top = self.top.next  # move top to next node
        print(f"Popped {removed} from stack.")
        return removed

    # PEEK operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty, nothing on top.")
            return None
        print(f"Top element is: {self.top.data}")
        return self.top.data

    # CHECK IF EMPTY
    def is_empty(self):
        return self.top is None

    # SIZE (calculate count dynamically)
    def size(self):
        count = 0
        curr = self.top
        while curr:
            count += 1
            curr = curr.next
        print(f"Stack size: {count}")
        return count

    # DISPLAY
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack (top to bottom): ", end="")
        curr = self.top
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


# -------------------------------
# Directly using stack operations
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

s.peek()
s.size()

s.pop()
s.display()
s.size()

s.pop()
s.pop()
s.pop()  # extra pop to check empty condition
s.size()
```

