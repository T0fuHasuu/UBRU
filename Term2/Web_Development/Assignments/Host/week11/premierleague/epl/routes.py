from epl import app, db
from flask import render_template, request, redirect, url_for
from epl.models import Club, Player

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/clubs', methods=['GET', 'POST'])
def clubs():
    # Retrieve all clubs from the database
    teams = db.session.scalars(db.select(Club)).all()

    # Check if the form was submitted
    if request.method == 'POST':
        # Get the search term entered by the user
        club_name = request.form['club_name']
        
        # Query the database for clubs that match the search term (using LIKE)
        club_list = db.session.scalars(db.select(Club).where(Club.name.like(f'%{club_name}%'))).all()

        # Pass the search term and filtered results to the template
        return render_template('clubs/index.html', title='Clubs Page', teams=club_list, search_term=club_name)

    # If no search is performed, return the full list of teams
    return render_template('clubs/index.html', title='Clubs Page', teams=teams, search_term='')


@app.route('/clubs/update/<int:id>', methods=['GET', 'POST'])
def update_club(id):
    team = db.session.get(Club, id)
    if request.method == 'POST':
        # Get the new club name from the form
        name = request.form['name']
        
        # Update the club name in the database
        team.name = name
        db.session.commit()
        
        # Redirect to the clubs page after updating
        return redirect(url_for('clubs'))

    # If GET request, display the club name in the form for editing
    return render_template('clubs/update_club.html', title='Update Club Page', team=team)

@app.route('/clubs/delete/<int:id>')
def delete_club(id):
    club = db.session.get(Club, id)
    if club:
        db.session.delete(club)
        db.session.commit()
    return redirect(url_for('clubs'))

@app.route('/clubs/new', methods=['GET', 'POST'])
def new_club():
    if request.method == 'POST':
        name = request.form['name']
        new_club = Club(name=name)
        db.session.add(new_club)
        db.session.commit()
        return redirect(url_for('clubs'))
    
    return render_template('clubs/new_club.html', title='Add New Club')

@app.route('/players', methods=['GET', 'POST'])
def players():
    players = db.session.scalars(db.select(Player)).all()  # Get all players

    if request.method == 'POST':  # Check if form is submitted
        player_name = request.form['player_name']
        footballers = db.session.scalars(db.select(Player).where(Player.name.like(f'%{player_name}%'))).all()
        return render_template('players/index.html', title='Players Page', footballers=footballers, search_term=player_name)

    return render_template('players/index.html', title='Players Page', footballers=players, search_term='')


@app.route('/players/new', methods=['GET', 'POST'])
def new_player():
    clubs = db.session.scalars(db.select(Club)).all()
    if not clubs:
        return redirect(url_for('new_club')) 

    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        club_id = request.form['club']
        nationality = request.form['nationality']
        img_url = request.form['img_url']

        new_player = Player(name=name, position=position, club_id=club_id, nationality=nationality, img_url=img_url)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('players'))

    return render_template('players/new_player.html', title='Add New Player Page', teams=clubs)

@app.route('/players/details/<int:id>')
def player_detail(id):
    player = db.session.get(Player, id)
    if player:
        return render_template('players/player_detail.html', title='More Detail', footballer=player)
    return redirect(url_for('players'))  
