
### 1. Solid Square

```python
n = 4

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

**Output:**

```text
* * * *
* * * *
* * * *
* * * *
```

### 2. Right Triangle

```python
n = 4

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
```

**Output:**

```text
*
* *
* * *
* * * *
```

### 3. Inverted Right Triangle

```python
n = 4

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

**Output:**

```text
* * * *
* * *
* *
*
```

### 4. Hollow Square

```python
n = 4

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

**Output:**

```text
* * * *
*     *
*     *
* * * *
```

### 5. Full Pyramid

```python
n = 4

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
```

**Output:**

```text
      *
    * * *
  * * * * *
* * * * * * *
```

### 6. Inverted Full Pyramid

```python
n = 4

for i in range(n, 0, -1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
```

**Output:**

```text
* * * * * * *
  * * * * *
    * * *
      *
```

### 7. Diamond Pattern

```python
n = 4

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()

for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
```

**Output:**

```text
      *
    * * *
  * * * * *
* * * * * * *
  * * * * *
    * * *
      *
```

### 8. Number Triangle

```python
n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**Output:**

```text
1
1 2
1 2 3
1 2 3 4
```

### 9. Floyd's Triangle

```python
n = 4
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

**Output:**

```text
1
2 3
4 5 6
7 8 9 10
```

### 10. Alphabet Triangle

```python
n = 4

for i in range(1, n + 1):
    ch = 'A'

    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)

    print()
```

**Output:**

```text
A
A B
A B C
A B C D
```

### 11. Number Square

```python
n = 4

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
```

**Output:**

```text
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
```

### 12. Same Number Triangle

```python
n = 4

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
```

**Output:**

```text
1
2 2
3 3 3
4 4 4 4
```

### 13. Alphabet Square

```python
n = 4

for i in range(n):
    ch = 'A'

    for j in range(n):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)

    print()
```

**Output:**

```text
A B C D
A B C D
A B C D
A B C D
```

### 14. Right-Aligned Triangle

```python
n = 4

for i in range(1, n + 1):

    for j in range(n - i):
        print("  ", end="")

    for j in range(i):
        print("* ", end="")

    print()
```

**Output:**

```text
      *
    * *
  * * *
* * * *
```

### 15. Inverted Right-Aligned Triangle

```python
n = 4

for i in range(n, 0, -1):

    for j in range(n - i):
        print("  ", end="")

    for j in range(i):
        print("* ", end="")

    print()
```

**Output:**

```text
* * * *
  * * *
    * *
      *
```

### 16. Reverse Number Pattern

```python
n = 4

for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()
```

**Output:**

```text
4 3 2 1
4 3 2
4 3
4
```

### 17. Checkerboard Pattern

```python
n = 4

for i in range(n):
    for j in range(n):

        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")

    print()
```

**Output:**

```text
* # * #
# * # *
* # * #
# * # *
```

### 18. Half Diamond

```python
n = 3

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

**Output:**

```text
*
* *
* * *
* *
*
```

### 19. Row Number Pattern

```python
n = 4

for i in range(1, n + 1):
    for j in range(n):
        print(i, end=" ")
    print()
```

**Output:**

```text
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

### 20. Column Number Pattern

```python
n = 4

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
```

**Output:**

```text
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
```


### 21. Multiplication Tables

```python
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
```

**Output:**

```text
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
```

---



### 22. Hollow Diamond Pattern

```python
n = 4

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**Output:**

```text
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```

The main pattern rule is:

```python
for i in range(...):       # rows
    for j in range(...):   # columns
        print(...)
    print()                # next row
```


