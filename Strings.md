Nice question Priya 🌸! Strings are one of the most important topics in Python. Let’s go step by step.

---

# 🔹 **String Operations in Python**

A **string** is a sequence of characters inside quotes.
Example:

```python
s = "Hello World"
```

Python provides many operations we can perform on strings:

---

## 1. **Concatenation (Joining Strings)**

```python
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)   # Output: Hello World
```

---

## 2. **Repetition**

```python
s = "Hi "
print(s * 3)   # Output: Hi Hi Hi 
```

---

## 3. **Indexing**

(Access characters using position → starts from 0)

```python
s = "Python"
print(s[0])   # P
print(s[3])   # h
print(s[-1])  # n (last character)
```

---

## 4. **Slicing**

(Get part of a string)

```python
s = "Programming"
print(s[0:6])   # Progra
print(s[3:])    # gramming
print(s[:5])    # Progr
print(s[::2])   # Pormig (step by 2)
```

---

## 5. **Membership Operators**

```python
s = "Hello World"
print("Hello" in s)     # True
print("Python" not in s) # True
```

---

## 6. **String Methods (Built-in Functions)**

👉 Some useful ones:

```python
s = "  python programming  "

print(s.upper())       # PYTHON PROGRAMMING
print(s.lower())       # python programming
print(s.strip())       # removes spaces → "python programming"
print(s.replace("python", "java"))  # java programming
print(s.split())       # ['python', 'programming']
print("-".join(["a","b","c"])) # a-b-c
```

---

## 7. **Finding and Counting**

```python
s = "banana"
print(s.find("na"))    # 2 (first index of 'na')
print(s.count("na"))   # 2 (occurrences)
```

---

## 8. **Formatting**

```python
name = "Priya"
age = 21
print("Hello {}, you are {} years old".format(name, age))
print(f"Hello {name}, you are {age} years old")  # f-string
```

---

✅ Strings in Python are **immutable** (cannot be changed once created).
If you "modify" a string, Python actually creates a **new string** in memory.
