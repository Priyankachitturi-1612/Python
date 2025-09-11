


## 📌 1. What is File Handling in Python?

**File Handling** is the process of working with files using Python code.
It allows you to:

* **Create** a file (if it doesn’t exist)
* **Read** data from a file
* **Write** data into a file
* **Append** (add more data without deleting old content)
* **Close** files properly to save resources

📖 **In short:**
File handling helps you store data **permanently** (not just in memory) so you can use it later, even after the program ends.

---

## 📌 2. Why Do We Need File Handling?

Imagine a program where you take user input, process it, and then **lose everything** when you close the program.
That’s where **files** are useful — you can save the data permanently.

✅ **Real-life examples:**

* Saving user information in a registration system.
* Writing logs (errors, events) to a file.
* Storing results of a program (like exam results).
* Reading configuration files for applications.
* Copying images, PDFs, or any binary files.


## 📌 3. Steps in File Handling (Concept Flow)

1️⃣ **Open** the file
2️⃣ **Perform operation** (read, write, append, etc.)
3️⃣ **Close** the file (or let Python close it automatically using `with`)

Think of it like:
📂 *"Open the file box → work with papers inside → close the file box properly"*

---

## 📌 4. File Modes

| Mode | Meaning | Use                                            |
| ---- | ------- | ---------------------------------------------- |
| `r`  | Read    | Opens file for reading (must exist)            |
| `w`  | Write   | Creates a new file or overwrites existing file |
| `a`  | Append  | Adds new data at the end of file               |
| `x`  | Create  | Creates file, gives error if it already exists |
| `b`  | Binary  | Opens file in binary mode (images, videos)     |
| `t`  | Text    | Opens file in text mode (default)              |

You can **combine modes**, e.g.:

* `"rb"` = Read binary
* `"wt"` = Write text (default)

---

## 📌 5. Basic Operations (with Explanation)

### ✅ 5.1 Opening and Reading a File


with open("myfile.txt", "r") as f:
    data = f.read()      # Reads entire file
    print(data)


**Explanation:**

* `open("myfile.txt", "r")` → open file in **read mode**
* `f.read()` → read all contents as a string
* `with` → ensures file is closed automatically



### ✅ 5.2 Writing (Creating or Overwriting)

with open("myfile.txt", "w") as f:
    f.write("Hello Priya!\n")
    f.write("This is file handling in Python.\n")


**Explanation:**

* `"w"` → write mode (creates new file or overwrites old one)
* `f.write()` → writes string to file


### ✅ 5.3 Appending Data

with open("myfile.txt", "a") as f:
    f.write("This line is appended at the end.\n")


**Explanation:**
No content is deleted — new data is **added** at the end.



### ✅ 5.4 Reading Line by Line

with open("myfile.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())


**Explanation:**
Best way for large files — reads one line at a time.



### ✅ 5.5 Working with Binary Files


with open("image.jpg", "rb") as src, open("copy.jpg", "wb") as dst:
    dst.write(src.read())


**Explanation:**
Copies an image from one file to another (works for any binary file).


## 📌 6. File Pointer Operations (Advanced)

* **`tell()`** → shows current cursor position in file
* **`seek(position)`** → move cursor to specific position

Example:

with open("myfile.txt", "r") as f:
    print("Position:", f.tell())   # 0 (start)
    f.read(5)
    print("Position after reading 5 chars:", f.tell())
    f.seek(0)                      # Move back to start
    print("After seek(0):", f.read())


## 📌 7. Error Handling in File Handling

Sometimes, files may not exist — handle safely:

try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the name!")


## 📌 8. Best Practice – Use `with`

Using `with open(...)` is recommended because:

* You **don’t have to manually close** the file
* It prevents data loss if an error occurs



## 1️⃣ Example with `readline()`

# myfile.txt content:
# Hello
# How are you?
# Bye

with open("myfile.txt", "r") as f:
    print("Position:", f.tell())  # 0 (start)

    line1 = f.readline()          # Reads first line only
    print("Line 1:", line1.strip())
    print("Position after readline:", f.tell())

    line2 = f.readline()          # Reads next line
    print("Line 2:", line2.strip())
    print("Position after second readline:", f.tell())
```

✅ **What you will see**

* It will print first line (`Hello`), show pointer moved.
* Then print second line (`How are you?`), pointer moves again.
* Each `readline()` reads one line at a time.

---

## 2️⃣ Example with `readlines()`

```
with open("myfile.txt", "r") as f:
    print("Position:", f.tell())  # 0 (start)

    lines = f.readlines()         # Reads ALL lines as a list
    print("All lines as list:", lines)
    print("Position after readlines:", f.tell())  # End of file

    f.seek(0)                     # Move pointer back to start
    print("After seek(0):", f.readlines())  # Read all again
```

✅ **What you will see**

* `lines` will look like `['Hello\n', 'How are you?\n', 'Bye']`
* `tell()` after `readlines()` will show end-of-file position.
* After `seek(0)` you can read them again.

---

## 3️⃣ Example with `writelines()`

```
lines_to_write = ["First line\n", "Second line\n", "Third line\n"]

with open("output.txt", "w") as f:
    f.writelines(lines_to_write)
    print("Data written using writelines()!")

# Now verify by reading the file again
with open("output.txt", "r") as f:
    print("Content of output.txt after writing:")
    print(f.read())




* A new file `output.txt` will be created (or old one replaced).
* It will have:


First line
Second line
Third line


## 🔑 Key Learning (Same as `tell`/`seek` Example)

* **`readline()`** → reads **one line** at a time, pointer moves forward.
* **`readlines()`** → reads **all lines** into a list, pointer goes to end.
* **`writelines()`** → writes a list of strings to a file (no `\n` added automatically).

---

Would you like me to combine **all three** (`readline`, `readlines`, `writelines`) into a **single program** so you can run once and see everything step by step?

## 📝 Summary (In Simple Words)

* **File Handling = Open → Do Something → Close**
* Modes: `r` (read), `w` (write), `a` (append), `x` (create), `b` (binary)
* Always use `with open()` for safety
* Methods:

  * `read()`, `readline()`, `readlines()`
  * `write()`, `writelines()`
  * `seek()`, `tell()`




## 🧠 What is Exception Handling?

* **Exception** = an error that occurs during program execution (e.g., dividing by zero, opening a missing file, wrong input type).
* If you **don’t handle** exceptions, your program will crash.
* **Exception handling** lets you **catch errors** and take safe action (like showing a message instead of crashing).

---

## 🏗️ Syntax of Exception Handling

```python
try:
    # Code that might raise an error
except SomeError:
    # What to do if that error happens
```

| Block     | Purpose                            |
| --------- | ---------------------------------- |
| `try`     | Code that might throw an exception |
| `except`  | Code to handle the error           |
| `else`    | Runs only if no exception occurred |
| `finally` | Always runs (cleanup code)         |
| `raise`   | Manually raise an exception        |


## 🔑 Example 1: Basic Exception Handling

```
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter only numbers!")
```

✅ This prevents the program from crashing if user enters invalid input or `y = 0`.

---

## 🔑 Example 2: Using `else` and `finally`

```
try:
    f = open("myfile.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File contents:", content)
finally:
    print("Execution completed.")
```

* **`else`** → runs only if no exception occurs
* **`finally`** → runs no matter what (good for cleanup like closing files or database connections)

---

## 🔑 Example 3: Catching Any Error

```python
try:
    num = int("abc")
except Exception as e:
    print("Some error occurred:", e)
```

Here, `e` will contain the actual error message (`invalid literal for int()`).

---

## 🔑 Example 4: Custom Exceptions (Advanced)

You can even **raise your own exceptions**:

```
age = -5
try:
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Your age is", age)
except ValueError as e:
    print("Error:", e)
```
Perfect, Priya! ✅
Let’s create **one complete program** that uses **all five keywords** (`try`, `except`, `else`, `finally`, `raise`) together so you can clearly see how they work in a single flow.

---

## 📝 Full Example: Age Validation Program

```python
try:
    age = int(input("Enter your age: "))  # 🔹 Code that might throw ValueError

    if age < 0:
        raise ValueError("Age cannot be negative!")  # 🔹 Manually raise exception

except ValueError as e:
    print("❌ Exception caught:", e)  # 🔹 Handle error

else:
    print("✅ No exception occurred.")
    print("Your age is:", age)       # 🔹 Runs only if no error

finally:
    print("🔄 Program execution finished (finally block)")  # 🔹 Always runs
```

---

### 🔎 Explanation:

| Keyword       | What Happened Here                                                 |
| ------------- | ------------------------------------------------------------------ |
| **`try`**     | Contains risky code: input + conversion to `int`                   |
| **`raise`**   | If age is negative, manually triggers a `ValueError`               |
| **`except`**  | Catches both input errors (`ValueError`) and raised error          |
| **`else`**    | Runs only if no exception occurred (displays age)                  |
| **`finally`** | Always runs (cleanup message, like closing files or DB connection) |

---

### 🧪 Example Run 1: Valid Input

**Input:**

```
Enter your age: 25
```

**Output:**

```
✅ No exception occurred.
Your age is: 25
🔄 Program execution finished (finally block)
```

---

### 🧪 Example Run 2: Negative Age

**Input:**

```
Enter your age: -5
```

**Output:**

```
❌ Exception caught: Age cannot be negative!
🔄 Program execution finished (finally block)
```

---

### 🧪 Example Run 3: Invalid Input

**Input:**

```
Enter your age: hello
```

**Output:**

```
❌ Exception caught: invalid literal for int() with base 10: 'hello'
🔄 Program execution finished (finally block)
```

---

✅ **This one program covers all five keywords in action.**
You can run it in VS Code and test with different inputs (`25`, `-10`, `abc`) to see all cases.



