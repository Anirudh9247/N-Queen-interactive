# ♛ N-Queen Problem Visualizer

An interactive web-based visualizer for solving and displaying solutions to the **N-Queen Problem** using Python and Flask.

This project allows users to enter a value of **N** and visually see how queens are placed on a chessboard such that no two queens attack each other.

---

## 📌 About the N-Queen Problem

The N-Queen problem is a classic backtracking problem where the goal is to:

- Place **N queens** on an **N × N chessboard**
- Ensure that no two queens attack each other:
  - Not in the same row
  - Not in the same column
  - Not on the same diagonal

---

## 🚀 Features

- ✅ Input any value of N
- ♟️ Visual chessboard representation
- 👑 Queen placement visualization
- ⚡ Fast backtracking-based solution
- 🎨 Clean and simple UI
- 🌐 Web-based interface using Flask

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```text
N-QUEEN/
│
├── app.py              # Flask application
├── solver.py           # N-Queen solving logic
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/N-QUEEN.git
cd N-QUEEN
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

Open your browser and go to:

```text
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

- Uses the **Backtracking Algorithm**
- Recursively places queens column by column
- Checks for:
  - Row safety
  - Upper diagonal safety
  - Lower diagonal safety
- Displays the solution on a visual chessboard

---

## 📦 Implementation Details

A closer look at the code and assets that power the visualizer:

### 🧩 `solver.py`

Contains the core algorithm. Key components:

- `is_safe(board, row, col, n)` – verifies that a queen can be placed at the given coordinates.
- `solve_n_queens(n)` – initializes the board and starts recursive backtracking.
- `backtrack(board, col, n)` – attempts to place queens in each column, undoing moves when a conflict arises.

This module returns a single solution as a list of row positions or `None` if no solution exists.

### 🚀 `app.py`

The Flask app that handles HTTP requests:

- `@app.route('/', methods=['GET', 'POST'])` – renders the input form and, upon submission, calls the solver.
- Parses the integer `N` from the form and invokes `solver.solve_n_queens(n)`.
- Passes the resulting board configuration to `result.html` for rendering.

The server runs on port 5000 by default and reloads automatically in debug mode.

### 🖼️ Templates

`templates/index.html` – contains the form where users enter the board size.
`templates/result.html` – uses a loop to render an `N × N` table, placing a queen icon (`♛`) in the appropriate cells.

### 🎨 Static Assets

`static/style.css` – styles the chessboard, buttons, and layout.
`static/script.js` – optionally handles client-side enhancements such as validating the input value.

These files work together to provide a responsive, interactive interface for exploring N‑Queen solutions.

---

## 📸 Example Output

For N = 4:

```text
. Q . .
. . . Q
Q . . .
. . Q .
```

---

## 🔮 Future Improvements

- Animate queen placement step-by-step
- Display all possible solutions
- Show total solution count
- Improve UI styling
- Add time complexity display

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.
