from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    # Functionality for home page
    return "Welcome to the Home Page. Go to /calculator for operations."

@app.route('/fullname/<name>')
def about(name):
    # Functionality for displaying a name
    return f"Hello, {escape(name)}"

@app.route('/calculator')
def calculator():
    # Functionality for calculator menu
    return "Choose a Calculator Operation: Addition, Subtraction, Multiplication, Division, Power, Modulo"

@app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a, b):
    # Functionality for addition
    return f"{a} + {b} = {a + b}"

@app.route('/calculator/subtraction/<int:a>/<int:b>')
def subtraction(a, b):
    # Functionality for subtraction
    return f"{a} - {b} = {a - b}"

@app.route('/calculator/multiply/<int:a>/<int:b>')
def multiply(a, b):
    # Functionality for multiplication
    return f"{a} x {b} = {a * b}"

@app.route('/calculator/divide/<int:a>/<int:b>')
def divide(a, b):
    # Functionality for division
    if b == 0:
        return "Division by zero is not allowed."
    return f"{a} / {b} = {a / b}"

@app.route('/calculator/power/<int:a>/<int:b>')
def power(a, b):
    # Functionality for power
    return f"{a}^({b}) = {a ** b}"

@app.route('/calculator/modulo/<int:a>/<int:b>')
def modulo(a, b):
    # Functionality for modulo
    return f"{a} % {b} = {a % b}"

if __name__ == '__main__':
    app.run(debug=True)