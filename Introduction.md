# Python
## 🔹 1. History of Python  

- Created by **Guido van Rossum** in the **late 1980s** at **CWI (Netherlands)**.  
- Name comes from **“Monty Python’s Flying Circus”** (a British comedy show).  

📌 Timeline:  
- **1991** → Python 0.9.0 released (functions, exceptions, modules).  
- **2000** → Python 2.0 released (list comprehensions, garbage collection).  
- **2008** → Python 3.0 released (not backward compatible).  
- **Now** → Latest versions are in the Python 3.x series.  

---
# 🔤 ASCII vs Unicode

---

## ✅ ASCII (American Standard Code for Information Interchange)

- Developed in the **1960s**.  
- Represents characters using **7 bits** → Maximum **128 characters**.  
- Mainly supports **English letters, digits, and symbols**.  

**Examples (ASCII values):**  
- `A` → 65  
- `B` → 66  
- `a` → 97  
- `0` → 48  

⚠️ **Limitation:** Only supports basic English characters → cannot represent Telugu, Hindi, Chinese, Arabic, Emojis, etc.  

| Dec   | Char    | Description         | Dec | Char | Description   |
| ----- | ------- | ------------------- | --- | ---- | ------------- |
| 0     | NUL     | Null character      | 64  | @    | At symbol     |
| 1     | SOH     | Start of Heading    | 65  | A    | Capital A     |
| 2     | STX     | Start of Text       | 66  | B    | Capital B     |
| 3     | ETX     | End of Text         | 67  | C    | Capital C     |
| 4     | EOT     | End of Transmission | 68  | D    | Capital D     |
| 5     | ENQ     | Enquiry             | 69  | E    | Capital E     |
| 6     | ACK     | Acknowledge         | 70  | F    | Capital F     |
| 7     | BEL     | Bell (Beep)         | 71  | G    | Capital G     |
| 8     | BS      | Backspace           | 72  | H    | Capital H     |
| 9     | TAB     | Horizontal Tab      | 73  | I    | Capital I     |
| 10    | LF      | Line Feed (Newline) | 74  | J    | Capital J     |
| 11    | VT      | Vertical Tab        | 75  | K    | Capital K     |
| 12    | FF      | Form Feed           | 76  | L    | Capital L     |
| 13    | CR      | Carriage Return     | 77  | M    | Capital M     |
| 14    | SO      | Shift Out           | 78  | N    | Capital N     |
| 15    | SI      | Shift In            | 79  | O    | Capital O     |
| 16–31 | –       | Control Characters  | 80  | P    | Capital P     |
| 32    | (space) | Space               | 81  | Q    | Capital Q     |
| 33    | !       | Exclamation         | 82  | R    | Capital R     |
| 34    | "       | Double Quote        | 83  | S    | Capital S     |
| 35    | #       | Hash                | 84  | T    | Capital T     |
| 36    | \$      | Dollar              | 85  | U    | Capital U     |
| 37    | %       | Percent             | 86  | V    | Capital V     |
| 38    | &       | Ampersand           | 87  | W    | Capital W     |
| 39    | '       | Single Quote        | 88  | X    | Capital X     |
| 40    | (       | Left Parenthesis    | 89  | Y    | Capital Y     |
| 41    | )       | Right Parenthesis   | 90  | Z    | Capital Z     |
| 42    | \*      | Asterisk            | 91  | \[   | Left Bracket  |
| 43    | +       | Plus                | 92  | \\   | Backslash     |
| 44    | ,       | Comma               | 93  | ]    | Right Bracket |
| 45    | -       | Hyphen              | 94  | ^    | Caret         |
| 46    | .       | Dot (Period)        | 95  | \_   | Underscore    |
| 47    | /       | Slash               | 96  | \`   | Backtick      |
| 48    | 0       | Digit 0             | 97  | a    | Small a       |
| 49    | 1       | Digit 1             | 98  | b    | Small b       |
| 50    | 2       | Digit 2             | 99  | c    | Small c       |
| 51    | 3       | Digit 3             | 100 | d    | Small d       |
| 52    | 4       | Digit 4             | 101 | e    | Small e       |
| 53    | 5       | Digit 5             | 102 | f    | Small f       |
| 54    | 6       | Digit 6             | 103 | g    | Small g       |
| 55    | 7       | Digit 7             | 104 | h    | Small h       |
| 56    | 8       | Digit 8             | 105 | i    | Small i       |
| 57    | 9       | Digit 9             | 106 | j    | Small j       |
| 58    | :       | Colon               | 107 | k    | Small k       |
| 59    | ;       | Semicolon           | 108 | l    | Small l       |
| 60    | <       | Less Than           | 109 | m    | Small m       |
| 61    | =       | Equal               | 110 | n    | Small n       |
| 62    | >       | Greater Than        | 111 | o    | Small o       |
| 63    | ?       | Question Mark       | 112 | p    | Small p       |
|       |         |                     | 113 | q    | Small q       |
|       |         |                     | 114 | r    | Small r       |
|       |         |                     | 115 | s    | Small s       |
|       |         |                     | 116 | t    | Small t       |
|       |         |                     | 117 | u    | Small u       |
|       |         |                     | 118 | v    | Small v       |
|       |         |                     | 119 | w    | Small w       |
|       |         |                     | 120 | x    | Small x       |
|       |         |                     | 121 | y    | Small y       |
|       |         |                     | 122 | z    | Small z       |
|       |         |                     | 123 | {    | Left Brace    |
|       |         |                     | 124 | \|   | Vertical Bar  |
|       |         |                     | 125 | }    | Right Brace   |
|       |         |                     | 126 | \~   | Tilde         |
|       |         |                     | 127 | DEL  | Delete        |


---

## ✅ Unicode

- Developed to represent **all characters in all languages**.  
- Uses encodings like **UTF-8, UTF-16, UTF-32**.  
- Supports **1 million+ characters**.  

**Examples (Unicode code points):**  
- `A` → U+0041  
- `😊` → U+1F60A  
- `అ` (Telugu A) → U+0C05  
- `क` (Hindi Ka) → U+0915  
- `中` (Chinese Zhong) → U+4E2D  

✅ Unicode supports English, Telugu, Hindi, Chinese, Arabic, Emojis, and more.  

---

## ✅ ASCII vs Unicode in Python

- **Python 2:** Strings were **ASCII by default** → only safe for English.  
- **Python 3:** Strings are **Unicode by default** → supports all languages and emojis.  

**Example in Python 3:**
```python
print("Hello")        # English
print("నమస్తే")       # Telugu
print("こんにちは")    # Japanese
print("😊")            # Emoji
````

---

## 📊 Comparison Table

| Feature   | ASCII             | Unicode                        |
| --------- | ----------------- | ------------------------------ |
| Size      | 7-bit (128 chars) | 8/16/32-bit (1M+ chars)        |
| Languages | English only      | All languages (multi-lingual)  |
| Example   | `A = 65`          | `A = U+0041`, `😊 = U+1F60A`   |
| Python 2  | Default = ASCII   | Unicode needs `u"text"`        |
| Python 3  | Default = Unicode | Handles all languages + emojis |

---

* **ASCII** = Old, simple, English only.
* **Unicode** = Modern, universal, supports all languages and emojis.
* **Python 3 uses Unicode by default** → global language support.


---



## 🔹 2. Roots of Python  

Python was influenced by:  
- **ABC Language** → Simplicity.  
- **C** → Performance and system access.  
- **Modula-3** → Exception handling and modularity.  
- **Unix Shell & Perl** → Scripting style.  

Philosophy:  
- **Simple is better than complex.**  
- **Readability counts.**  
- **Practicality beats purity.**  
 
## 🔹 3. What is Python?  

Python is a **high-level, interpreted, general-purpose programming language** that emphasizes **code readability** and **developer productivity**.  

- **High-level** → You don’t need to manage memory manually.  
- **Interpreted** → Runs line by line using the Python interpreter.  
- **General-purpose** → Used in many domains:  
  - Web development  
  - Data Science & Machine Learning  
  - Artificial Intelligence  
  - Automation & Scripting  
  - Game Development  
  - Desktop & Mobile Apps  
  - Networking, IoT, Cybersecurity  

It supports **Object-Oriented, Functional, and Procedural Programming**.  

---


## 🔹 4. Why Python is Popular Today?

* Beginner-friendly.
* Huge demand in **AI, ML, Data Science**.
* Active community and open-source support.
* Used by **Google, Netflix, NASA, YouTube, Instagram**.

---
## 🔹 5. Advantages of Python  

✅ **Easy to Learn & Read** (syntax close to English).  
✅ **Cross-platform** (Windows, Linux, macOS).  
✅ **Large Libraries & Frameworks** (NumPy, Pandas, Django, TensorFlow, etc.).  
✅ **Versatile** – used in almost all domains.  
✅ **Open-source & Strong Community** support.  
✅ **Integration Support** with C, C++, Java, .NET.  
✅ **Rapid Development** – fast prototyping.  

Example:  
```python
for i in range(5):
    print("Hello")
````

---

## 🔹 6. Disadvantages of Python

⚠️ **Slower Execution** (interpreted, not compiled).
⚠️ **High Memory Usage** (not good for embedded systems).
⚠️ **Weak Mobile Development Support** (not widely used for Android/iOS).
⚠️ **Global Interpreter Lock (GIL)** limits multi-threading.
⚠️ **Not Low-Level** (unsuitable for OS kernels, device drivers).

---

