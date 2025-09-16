A **linked list** in Python is a **linear data structure** where each element (called a **node**) contains:

1. The **data** (value),
2. A **reference (or link)** to the next node in the sequence.

Unlike arrays or lists in Python, **linked lists don't store elements in contiguous memory locations**, which allows for efficient insertions and deletions.


### ✅ Components of a Linked List:

#### 1. **Node**

Each node stores:

* `data`: the value of the node
* `next`: a pointer/reference to the next node

#### 2. **LinkedList**

This class manages the linked list and contains:

* `head`: a reference to the first node in the list

---

### 📌  Singly Linked List

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # Traverse to the end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()
```

**Output:**

```
10 -> 20 -> 30 -> None
```


* ✅ Insert at the beginning
* ✅ Insert at the end
* ✅ Delete a node by value


## ✅ Simple Singly Linked List (Only Basic Operations)

```
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # If head node holds the key
        if current and current.data == key:
            self.head = current.next
            return

        # Search for the node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Value {key} not found.")
            return

        prev.next = current.next

    # Print the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```

---

## ✅ Example Usage:

```python
ll = LinkedList()

ll.insert_at_beginning(30)
ll.insert_at_end(40)
ll.insert_at_beginning(20)
ll.insert_at_end(50)

ll.traverse()  # Output: 20 -> 30 -> 40 -> 50 -> None

ll.delete(30)
ll.traverse()  # Output: 20 -> 40 -> 50 -> None

ll.delete(100)  # Output: Value 100 not found.
```

---

## ✅ Summary of What You Get:

| Operation           | Method Name             | Time Complexity |
| ------------------- | ----------------------- | --------------- |
| Insert at beginning | `insert_at_beginning()` | O(1)            |
| Insert at end       | `insert_at_end()`       | O(n)            |
| Delete by value     | `delete()`              | O(n)            |
| Display list        | `traverse()`            | O(n)            |


## ✅ Singly Linked List with Operations

```
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 3. Insert after a node (by value)
    def insert_after(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # 4. Delete a node by value
    def delete_node(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Node with value {key} not found.")
            return

        prev.next = current.next

    # 5. Delete at a specific position (0-based index)
    def delete_at_position(self, pos):
        if pos < 0:
            print("Position must be >= 0.")
            return

        current = self.head

        if pos == 0 and current:
            self.head = current.next
            return

        prev = None
        count = 0
        while current and count != pos:
            prev = current
            current = current.next
            count += 1

        if not current:
            print(f"No node at position {pos}")
            return

        prev.next = current.next

    # 6. Search for a value
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # 7. Update a node's value
    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next
        print(f"Value {old_value} not found.")

    # 8. Traverse and print
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 9. Length of the list
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 10. Reverse the list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 11. Check if list is empty
    def is_empty(self):
        return self.head is None
```

---

## ✅ Example Usage:

```python
# Create linked list
ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(5)
ll.insert_after(20, 25)

ll.traverse()  # Output: 5 -> 10 -> 20 -> 25 -> 30 -> None

ll.delete_node(10)
ll.traverse()  # Output: 5 -> 20 -> 25 -> 30 -> None

ll.update(25, 26)
ll.traverse()  # Output: 5 -> 20 -> 26 -> 30 -> None

print("Found 20?", ll.search(20))   # True
print("Length:", ll.length())       # 4

ll.reverse()
ll.traverse()  # Output: 30 -> 26 -> 20 -> 5 -> None
```



## ✅ Problem 1: Insert Elements & Display the List

### 🧾 Problem:

Take `n` numbers as input from the user, insert each at the **end** of a singly linked list, and print the final list.

---

### ✅ Code:

```python
# Node and LinkedList setup
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ---------- MAIN ----------
ll = LinkedList()

n = int(input("How many elements? "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    ll.insert_at_end(val)

print("Linked List:")
ll.traverse()
```

---

### 🧠 Example:

**Input:**

```
How many elements? 4
Enter element 1: 10
Enter element 2: 20
Enter element 3: 30
Enter element 4: 40
```

**Output:**

```
Linked List:
10 -> 20 -> 30 -> 40 -> None
```

---

## ✅ Problem 2: Delete a Node by Value

### 🧾 Problem:

* Create a linked list.
* Let the user delete a node by entering a value.
* Display the updated list.

---

### ✅ Code:

```
# Reuse Node and LinkedList setup

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Value {key} not found.")
            return

        prev.next = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ---------- MAIN ----------
ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

print("Original List:")
ll.traverse()

to_delete = int(input("Enter value to delete: "))
ll.delete(to_delete)

print("Updated List:")
ll.traverse()
```

---

### 🧠 Example:

**Input:**

```
Enter value to delete: 30
```

**Output:**

```
Original List:
10 -> 20 -> 30 -> 40 -> 50 -> None
Updated List:
10 -> 20 -> 40 -> 50 -> None
```

