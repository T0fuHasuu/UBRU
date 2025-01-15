from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html>
            <head>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                        background-color: pink;
                    }
                    h1 {
                        font-size: 50px;
                        text-align: center;
                    }
                    a {
                        font-size: 100px;
                        text-align: center;
                        display: block;
                        margin: 10px;
                        text-decoration: none;
                        color: #007BFF;
                    }
                    a:hover {
                        color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <h1><a href="/calculator">Calculator</a></h1><br>
            </body>
        </html>
    """

@app.route('/fullname/<name>')
def about(name):
    return f"""
        <html>
            <head>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                    }}
                    h1 {{
                        font-size: 50px;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>Hello, {escape(name)}</h1>
            </body>
        </html>
    """

@app.route('/calculator')
def calculator():
    return """
        <html>
            <head>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                        background-color: red;
                    }
                    h1 {
                        font-size: 50px;
                        text-align: center;
                    }
                    a {
                        font-size: 25px;
                        text-align: center;
                        display: block;
                        margin: 10px;
                        text-decoration: none;
                        color: #007BFF;
                    }
                    a:hover {
                        color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <h1>Choose a Calculator Operation</h1>
                <a href="/calculator/addition/50/2">Addition/</a>
                <a href="/calculator/subtraction/50/2">Subtraction/</a>
                <a href="/calculator/multiply/50/2">Multiplication/</a>
                <a href="/calculator/divide/50/2">Division/</a>
                <a href="/calculator/power/50/2">Power/</a>
                <a href="/calculator/modulo/50/2">Modulo/</a>
            </body>
        </html>
    """

@app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a,b):
    return f"""
        <html>
            <head>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                    }}
                    h1 {{
                        font-size: 50px;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>{a} + {b} = {a+b}</h1>
            </body>
        </html>
    """

@app.route('/calculator/subtraction/<int:a>/<int:b>')
def subtraction(a,b):
    return f"""
        <html>
            <head>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                    }}
                    h1 {{
                        font-size: 50px;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>{a} - {b} = {a-b}</h1>
            </body>
        </html>
    """

@app.route('/calculator/multiply/<int:a>/<int:b>')
def multiply(a,b):
    return f"""
        <html>
            <head>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                    }}
                    h1 {{
                        font-size: 50px;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>{a} x {b} = {a*b}</h1>
            </body>
        </html>
    """

@app.route('/calculator/divide/<int:a>/<int:b>')
def divide(a,b):
    return f"""
        <html>
            <head>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                    }}
                    h1 {{
                        font-size: 50px;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>{a} / {b} = {int(a/b)}</h1>
            </body>
        </html>
    """

@app.route('/calculator/power/<int:a>/<int:b>')
def power(a, b):
    return f"""
        <html>
            <head>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                    }}
                    h1 {{
                        font-size: 50px;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>{a}<sup>{b}</sup> = {a ** b}</h1>
            </body>
        </html>
    """

@app.route('/calculator/modulo/<int:a>/<int:b>')
def modulo(a, b):
    return f"""
        <html>
            <head>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                    }}
                    h1 {{
                        font-size: 50px;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>{a} % {b} = {a % b}</h1>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
