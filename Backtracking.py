
##  **Backtracking**

```
def find_paths(path, r, c):
    # Check for out of bounds OR blocked cell
    if r < 0 or c < 0 or r >= n or c >= m or maze[r][c] == 0:
        return

    # Add current cell to path
    path.append(maze[r][c])

    # If destination is reached, print path
    if r == n - 1 and c == m - 1:
        print(path)
    else:
        # Move Right
        find_paths(path, r, c + 1)
        # Move Down
        find_paths(path, r + 1, c)

    # Backtrack - remove last step
    path.pop()


# Main Program

  n, m = map(int, input("Enter n m: ").split())

  print("Enter maze matrix (0=blocked, 1=open):")
  maze = []
  for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

  print("\nAll Possible Paths:")
  find_paths([], 0, 0)
```


## 🟢 **Example Maze**

```
1 0 0
1 1 0
0 1 1
```

* `1` → open cell
* `0` → blocked cell

Start at **top-left (0,0)**, end at **bottom-right (2,2)**.

---

### Step 1️⃣ **Start at (0,0)**

* Path = `[1]` (add maze\[0]\[0] = 1)
* Can move **Right** → (0,1) → blocked (`0`) ❌
* Can move **Down** → (1,0) → open ✅

---

### Step 2️⃣ **Move Down to (1,0)**

* Path = `[1, 1]` (add maze\[1]\[0] = 1)
* Move **Right** → (1,1) → open ✅
* Move **Down** → (2,0) → blocked ❌

---

### Step 3️⃣ **Move Right to (1,1)**

* Path = `[1, 1, 1]` (add maze\[1]\[1] = 1)
* Move **Right** → (1,2) → blocked ❌
* Move **Down** → (2,1) → open ✅

---

### Step 4️⃣ **Move Down to (2,1)**

* Path = `[1, 1, 1, 1]` (add maze\[2]\[1] = 1)
* Move **Right** → (2,2) → destination ✅
* Move **Down** → (3,1) → out of bounds ❌

**Destination reached → print path**

```
[1, 1, 1, 1]
```

---

### Step 5️⃣ **Backtracking**

* After printing, remove last step → Path = `[1,1,1]`
* Check other directions (Right/Down) from (2,1) → none valid → return
* Backtrack to (1,1) → Path = `[1,1]`
* Check other directions from (1,1) → none valid → return
* Backtrack to (1,0) → Path = `[1]`
* Check other directions → none valid → return
* Backtrack to (0,0) → Path = `[]`

---

### ✅ **Key Concept of Backtracking**

1. Add current cell to path
2. Explore all valid moves (Right, Down) recursively
3. If destination reached → print path
4. **Remove last step (backtrack)** to explore other paths

---

### 📌 **Visual Summary**

```
Start (0,0) → Down → (1,0) → Right → (1,1) → Down → (2,1) → Right → Destination (2,2)
Path = [1, 1, 1, 1]
```

**Backtracking ensures:**

* We explore **all possible paths**
* The `path` list always represents the **current path from start to current cell**

