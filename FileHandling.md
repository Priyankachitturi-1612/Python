


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

