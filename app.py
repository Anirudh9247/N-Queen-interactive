from flask import Flask, render_template, request

from solver import solve_n_queens



app = Flask(__name__)



@app.route("/", methods=["GET"])

def home():

    # Cleaned up unnecessary POST logic since the form submits to /solve

    return render_template("index.html")



@app.route('/solve', methods=['POST'])

def solve():

    try:

        n = int(request.form.get('n', 0))

    except ValueError:

        return "Invalid input for N. Must be an integer.", 400



    # Add bounds checking to prevent server crashes on extreme inputs

    if n < 1 or n > 12:

        return "N must be between 1 and 12 for performance reasons.", 400



    all_solutions = solve_n_queens(n)

    

    # Extract the first solution and format it as a 2D integer array (1s and 0s)

    # This is required because result.html expects cell values to be 1 for a queen

    formatted_solution = None

    if all_solutions:

        formatted_solution = [

            [1 if cell == 'Q' else 0 for cell in row]

            for row in all_solutions[0]

        ]



    return render_template('result.html', solution=formatted_solution, n=n) 

   

if __name__ == "__main__":

    app.run(debug=True)