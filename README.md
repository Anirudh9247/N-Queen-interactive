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

```
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

```
git clone https://github.com/your-username/N-QUEEN.git
cd N-QUEEN
```

### 2️⃣ Create a virtual environment (recommended)

```
python -m venv venv
```

Activate it:

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the application

```
python app.py
```

Open your browser and go to:

```
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

## 📸 Example Output

For N = 4:

```
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