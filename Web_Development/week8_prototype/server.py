from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

teams = [
    {'id' : 1 , 'league' : 'Arsnal'},
    {'id' : 2 , 'league' : 'Liverpool'},
    {'id' : 3 , 'league' : 'Chelsea'},
    {'id' : 4 , 'league' : 'Bacelona'},
    {'id' : 5 , 'league' : 'Real Madrid'},
    {'id' : 6 , 'league' : 'Paris'},
    {'id' : 7 , 'league' : 'Cambodia'},
    {'id' : 8 , 'league' : 'Manchester'},
    {'id' : 9 , 'league' : 'Brentford'},
]

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

@app.route('/clubs')
def clubs():
    return render_template('clubs/index.html', title = "Clubs", teams = teams)

@app.route('/clubs/update/<int:id>', methods =['GET', 'POST'])
def update(id):
    for t in teams:
        if t['id'] == id:
            team = t
            break
    if request.method == 'POST':
        league = request.form['name']    
        id = request.form['id']    
        for i in range(len(teams)):
            if teams[i]['id'] == int(id):
                teams[i]['league'] = league
                break
        return redirect(url_for('clubs'))
    return render_template('clubs/update.html', title='Update', team=team)

@app.route('/clubs/delete/<int:id>')
def delete():
    return render_template('clubs/delete.html', title='Delete')

if __name__ == '__main__':
    app.run(debug=True)