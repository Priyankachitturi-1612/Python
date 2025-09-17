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



## 4️⃣ Find the Length of the Linked List

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to count nodes
def length(head):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    return count

# Example Usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Length of Linked List:", length(head))
```

---

## 5️⃣ Search for a Value in the Linked List

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search(head, key):
    temp = head
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False

# Example Usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

key = int(input("Enter value to search: "))
print("Found!" if search(head, key) else "Not Found!")
```

---

## 6️⃣ Find Maximum and Minimum Values in the List

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_max_min(head):
    if not head:
        return None, None
    max_val = min_val = head.data
    temp = head.next
    while temp:
        if temp.data > max_val:
            max_val = temp.data
        if temp.data < min_val:
            min_val = temp.data
        temp = temp.next
    return max_val, min_val

# Example Usage
head = Node(10)
head.next = Node(50)
head.next.next = Node(5)
head.next.next.next = Node(40)

max_val, min_val = find_max_min(head)
print("Max:", max_val, " Min:", min_val)
```

---

## 7️⃣ Reverse a Linked List (In-Place)

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # new head

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Example Usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original List:")
display(head)

head = reverse(head)
print("Reversed List:")
display(head)
```

---

## 8️⃣ Find the Middle Element of the List

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None

# Example Usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Middle Element:", find_middle(head))
```

---

## 9️⃣ Detect a Cycle in the Linked List (Floyd’s Algorithm)

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example Usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Creating a cycle for testing (uncomment to check)
# head.next.next.next = head.next

print("Cycle Detected!" if has_cycle(head) else "No Cycle Found!")
```

---

## 🔟 Remove Duplicates from a Sorted Linked List

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates_sorted(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Example Usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)

print("Original List:")
display(head)

head = remove_duplicates_sorted(head)
print("After Removing Duplicates:")
display(head)
```

Let’s break this down step by step — this is an important topic in Data Structures.

---

##  **Doubly Linked List (DLL)**

A **Doubly Linked List** is a type of linked list where each node contains:

1. **Data** (the actual value stored)
2. **Pointer to the next node** (`next`)
3. **Pointer to the previous node** (`prev`)

This means you can **traverse the list in both directions** (forward and backward), unlike a singly linked list which only moves forward.
---

##  **How to Create a Doubly Linked List**

Each node is an object with three parts.
In Python, a basic implementation looks like this:


```python
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
✅ Creates a **Doubly Linked List**
✅ Inserts some elements
✅ Traverses **forward** (head → tail)
✅ Traverses **backward** (tail → head)

---

##  **Code – DLL with Forward & Backward Traversal**

```
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return
        curr = self.head
        print("Forward Traversal: ", end="")
        while curr:
            print(curr.data, end=" <-> ")
            last = curr  # keep track of last node
            curr = curr.next
        print("None")
        return last  # return last node for backward traversal

    def display_backward(self):
        if self.head is None:
            print("List is empty.")
            return
        # go to last node first
        curr = self.head
        while curr.next:
            curr = curr.next
        print("Backward Traversal: ", end="")
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.prev
        print("None")


# ---------- DEMO ----------
dll = DoublyLinkedList()

# Insert some elements
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

dll.display_forward()   # Head → Tail
dll.display_backward()  # Tail → Head
```

---

## ✅ **Sample Output**

```
Forward Traversal: 10 <-> 20 <-> 30 <-> 40 <-> None
Backward Traversal: 40 <-> 30 <-> 20 <-> 10 <-> None
```

---

## 🔑 Key Points

* **Forward traversal:** Uses `next` pointers → natural order.
* **Backward traversal:** First moves to last node, then uses `prev` pointers → reverse order.
* This demonstrates the **biggest advantage** of a doubly linked list — **bidirectional traversal**.


# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # empty list
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Display forward
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
```


##  **Operations on Doubly Linked List**

Here are the main operations you can perform:

1. **Traversal**

   * Forward traversal (head → tail)
   * Backward traversal (tail → head)

2. **Insertion**

   * At the beginning
   * At the end
   * After a given node
   * Before a given node

3. **Deletion**

   * From the beginning
   * From the end
   * A specific node by value or position

4. **Searching**

   * Find if a value exists in the list

5. **Reversing**

   * Reverse the entire list by swapping `next` and `prev` pointers

6. **Length**

   * Count the number of nodes in the list


**No — insert at beginning and insert at end are *not* the same.**
They are similar in that both create a new node and adjust pointers, but **where you link the node changes completely.**



## 🟢 **Insert at Beginning**

You add the node **before the current head** and make it the new head.

### Steps:

1. Create a new node.
2. Set `new_node.next = self.head`.
3. If list is not empty, set `self.head.prev = new_node`.
4. Move `self.head = new_node`.

### Code:

```
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head  # link new node to old head
    if self.head is not None:  # update old head's prev pointer
        self.head.prev = new_node
    self.head = new_node  # make new node the head
```


## 🔵 **Insert at End**

You add the node **after the current last node (tail)**.

### Steps:

1. Create a new node.
2. If list is empty, make it head.
3. Otherwise, traverse to last node.
4. Set `last.next = new_node` and `new_node.prev = last`.

### Code:

```
def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:  # empty list
        self.head = new_node
        return
    curr = self.head
    while curr.next:  # go to last node
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
```



## 🧠 **Key Difference**

| Operation               | Pointer Adjustments                  | Traversal Needed?       | Time Complexity                             |
| ----------------------- | ------------------------------------ | ----------------------- | ------------------------------------------- |
| **Insert at Beginning** | Change only `head` & `new_node.next` | ❌ No                    | **O(1)**                                    |
| **Insert at End**       | Change `last.next`, `new_node.prev`  | ✅ Yes (go to last node) | **O(n)** (unless you keep a `tail` pointer) |



## 📌 Example (Both in Action)

```
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")


dll = DoublyLinkedList()
dll.insert_at_beginning(20)
dll.insert_at_beginning(10)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("List after inserting at beginning and end:")
dll.display()
```

### Output:

```
List after inserting at beginning and end:
10 <-> 20 <-> 30 <-> 40 <-> None
```


✅ **Summary:**

* **Insert at beginning** → directly attach before head → **O(1)**
* **Insert at end** → must traverse to last node → **O(n)** (unless tail pointer is used)


## 🔧 **Doubly Linked List – Deletion & Utility Operations**

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ------------ INSERTS (for testing) ------------
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # ------------ DELETE OPERATIONS ------------
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        removed = self.head.data
        self.head = self.head.next
        if self.head:  # update prev of new head
            self.head.prev = None
        print(f"Deleted {removed} from beginning.")

    def delete_at_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next is None:  # only one node
            removed = self.head.data
            self.head = None
            print(f"Deleted {removed}, list is now empty.")
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        removed = curr.data
        curr.prev.next = None
        print(f"Deleted {removed} from end.")

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return
        curr = self.head
        while curr and curr.data != value:
            curr = curr.next
        if curr is None:
            print(f"Value {value} not found.")
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next  # if node is head
        if curr.next:
            curr.next.prev = curr.prev
        print(f"Deleted value {value}.")

    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty.")
            return
        if position <= 0:
            print("Invalid position!")
            return
        curr = self.head
        count = 1
        while curr and count < position:
            curr = curr.next
            count += 1
        if curr is None:
            print(f"Position {position} is out of range.")
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        print(f"Deleted node at position {position} (value {curr.data}).")

    # ------------ SEARCH, LENGTH, REVERSE ------------
    def search(self, value):
        curr = self.head
        pos = 1
        while curr:
            if curr.data == value:
                print(f"Value {value} found at position {pos}.")
                return pos
            curr = curr.next
            pos += 1
        print(f"Value {value} not found.")
        return -1

    def length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        print(f"Length of list = {count}")
        return count

    def reverse(self):
        curr = self.head
        prev_node = None
        while curr:
            # swap next and prev
            curr.prev, curr.next = curr.next, curr.prev
            prev_node = curr
            curr = curr.prev  # move "backwards" since swapped
        self.head = prev_node
        print("List reversed.")

    # ------------ DISPLAY ------------
    def display(self):
        curr = self.head
        if curr is None:
            print("List is empty.")
            return
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
print("Initial list:")
dll.display()

dll.delete_at_beginning()
dll.display()

dll.delete_at_end()
dll.display()

dll.delete_by_value(30)
dll.display()

dll.delete_by_position(2)  # deletes node at 2nd position (remaining list)
dll.display()

dll.search(50)  # not found
dll.search(10)  # found

dll.length()

dll.reverse()
dll.display()

---

## ✅ **Sample Output (When You Run the File)**

```
Initial list:
10 <-> 20 <-> 30 <-> 40 <-> 50 <-> None
Deleted 10 from beginning.
20 <-> 30 <-> 40 <-> 50 <-> None
Deleted 50 from end.
20 <-> 30 <-> 40 <-> None
Deleted value 30.
20 <-> 40 <-> None
Deleted node at position 2 (value 40).
20 <-> None
Value 50 not found.
Value 10 found at position 1.
Length of list = 1
List reversed.
20 <-> None
```

---

## 🔑 Key Takeaways

* **Delete at beginning** → just update `head` to `head.next`
* **Delete at end** → traverse to last node, unlink it
* **Delete by value** → search for node, then unlink
* **Delete by position** → traverse until position, unlink node
* **Search** → traverse until match is found
* **Length** → simple counter while traversing
* **Reverse** → swap `next` and `prev` of each node, then update head
 
