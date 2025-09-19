
## 🟢 **Introduction to Queue**

A **Queue** is a **linear data structure** that follows the **FIFO (First In, First Out)** rule.
That means the **first element inserted** will be the **first one removed** — just like a line of people waiting at a counter.

---

### 📌 **Real-Life Example**

Imagine a **ticket counter**:

* The person who comes **first** gets the ticket **first**.
* The person who comes **last** will have to wait until their turn comes.

This is exactly how a queue works in DSA.

---

## 🔑 **Key Terms: Front & Rear**

In a queue, there are two important pointers:

| Term      | Meaning                                                                 | Analogy              |
| --------- | ----------------------------------------------------------------------- | -------------------- |
| **Front** | The position from where elements are **removed** (Dequeue happens here) | First person in line |
| **Rear**  | The position where elements are **added** (Enqueue happens here)        | Last person in line  |

---

### 📊 **Visual Representation**

Let's say we enqueue 10, 20, 30 into the queue:

```
Front → [10] [20] [30] ← Rear
```

* **Front = first element (10)** → will be removed first when we do Dequeue.
* **Rear = last element (30)** → new elements will be added after this.

---

### 🔧 **Queue Operations**

| Operation        | Description                                        | Example                                               |
| ---------------- | -------------------------------------------------- | ----------------------------------------------------- |
| **Enqueue**      | Insert element at **rear**                         | Add `40`: Queue becomes `10 20 30 40`                 |
| **Dequeue**      | Remove element from **front**                      | Remove first element (`10`): Queue becomes `20 30 40` |
| **Peek / Front** | View the first element without removing it         | Gives `20`                                            |
| **isEmpty**      | Check if queue is empty                            | True / False                                          |
| **isFull**       | Check if queue is full (only for fixed-size queue) | True / False                                          |

---

### 🧠 **Why Front & Rear Are Needed**

* `front` ensures we always remove the **oldest inserted element**.
* `rear` ensures we always add at the **end of the queue**.
* Together, they maintain the **FIFO order**.

---

### 🖥 **Quick Example (Conceptual)**

Initial Queue: (empty)

```
Front = -1, Rear = -1
```

1️⃣ Enqueue 10 →

```
Front = 0, Rear = 0 → [10]
```

2️⃣ Enqueue 20 →

```
Front = 0, Rear = 1 → [10 20]
```

3️⃣ Dequeue → removes 10 →

```
Front = 1, Rear = 1 → [20]
```

Now front moves forward, pointing to next element.

---

### ✅ Key Takeaways

* **Front** → points to where next element will be removed.
* **Rear** → points to where next element will be added.
* Queue always follows **FIFO** (First In, First Out).
* Used in **OS (scheduling), networking (requests), BFS in graphs**, etc.



## 🟢 **Queue **

A **Queue** is a **linear data structure** that follows **FIFO** (First In First Out) principle.
This means the **first element inserted is the first one removed** – just like a line of people waiting.

---

### 🔑 **Main Queue Operations**

| Operation        | Meaning                                         | Example                                      |
| ---------------- | ----------------------------------------------- | -------------------------------------------- |
| **Enqueue**      | Insert element at the **rear** (end)            | `10 → 20 → 30` (new element goes at the end) |
| **Dequeue**      | Remove element from the **front**               | Removes `10`, queue becomes `20 → 30`        |
| **Front / Peek** | Get element at the **front** (without removing) | Gives `20`                                   |
| **isEmpty**      | Check if queue is empty                         | `True` / `False`                             |
| **Size**         | Number of elements                              |                                              |

---

### 🔧 **Queue Implementation Approaches in DSA**

We can implement a queue using:

* **Array** (Fixed size – easy but may waste memory after many dequeues)
* **Linked List** (Dynamic size – no memory wastage)

---

## 🖥 **Queue Implementation using Array **

```
class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity  # fixed size array
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    # Enqueue -> add element to rear
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    # Dequeue -> remove element from front
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    # Get front element
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        count = 0
        print("Queue elements:", end=" ")
        while count < self.size:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.capacity
            count += 1
        print()
        

# Example usage
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Dequeued:", q.dequeue())
q.display()

print("Front element:", q.peek())
```

---

### 📊 **Example Output**

```
Queue elements: 10 20 30
Dequeued: 10
Queue elements: 20 30
Front element: 20
```

---

## 🔑 **Key Points**

✅ **FIFO Principle** → First element added is first removed
✅ **Array-based queue** uses `front` & `rear` pointers
✅ If we use `% capacity` we make it a **Circular Queue** (no wasted space)
✅ Time complexity for Enqueue / Dequeue → **O(1)**

