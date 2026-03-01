from flask import Flask, render_template, request
from solver import solve_n_queens

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    solutions = []
    n = None

    if request.method == "POST":
        n = int(request.form["size"])
        solutions = solve_n_queens(n)

    return render_template("index.html", solutions=solutions, n=n)

@app.route('/solve', methods=['POST'])
def solve():
    n = int(request.form['n'])
    solution = solve_n_queens(n)
    return render_template('result.html', solution=solution, n=n) 
   
if __name__ == "__main__":
    app.run(debug=True)