from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    game = [
            {
                "Game": "Elden RinG",
                "favnum": 1
            },
            {
                "Game": "Valorant",
                "favnum": 2
            },
            {
                "Game": "CS:GO",
                "favnum": 3
            },
            {
                "Game": "DARK SOUL",
                "favnum": 1
            }
            ]
    return render_template('about.html', title="About", game=game)

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

if __name__ == '__main__':
    app.run(debug=True)