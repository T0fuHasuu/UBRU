from epl import app
from flask import render_template, request, redirect, url_for
from epl.models import teams, footballers



@app.route('/')
def index():
  return render_template('index.html',
                         title='Home Page')

@app.route('/clubs', methods=['GET', 'POST'])
def clubs():
  if request.method == 'POST':
    club_name = request.form['club_name']
    club_list = []
    for team in teams:
      if club_name in team['name']:
        club_list.append(team)
    
    return render_template('clubs/index.html',
                         title='Clubs Page',
                         teams=club_list) 

  return render_template('clubs/index.html',
                         title='Clubs Page',
                         teams=teams)

@app.route('/clubs/<int:id>/update', methods=['GET', 'POST'])
def update_club(id):
  team = None
  for t in teams:
    if t['id']==id:
      team = t
      break

  if request.method == 'POST':
    name = request.form['name']
    for i in range(len(teams)):
      if teams[i]['id'] == id:
        teams[i]['name'] = name
        break
    return redirect(url_for('clubs'))

  return render_template('clubs/update_club.html',
                         title='Update Club Page',
                         team=team)

@app.route('/clubs/<int:id>/delete')
def delete_club(id):
  for i in range(len(teams)):
    if teams[i]['id'] == id:
      del teams[i]
      break
  return redirect(url_for('clubs'))

@app.route('/clubs/new', methods=['GET', 'POST'])
def new_club():
  if request.method == 'POST':
    name = request.form['name']

    size = len(teams)
    if size>0:
      id = teams[size-1]['id'] + 1
    else:
      id = 1

    team = {'id': id, 'name': name}
    teams.append(team)

    return redirect(url_for('clubs'))


  return render_template('clubs/new_club.html',
                         title='Add New Club')

@app.route('/players')
def players():
  return render_template('players/index.html',
                         title='Players Page',
                         footballers=footballers)

@app.route('/players/new', methods=['GET', 'POST'])
def new_player():
  if request.method == 'POST':
    name = request.form['name']
    position = request.form['position']
    club = request.form['club']
    nationality = request.form['nationality']
    img_url = request.form['img_url']

    size = len(footballers)
    if size>0:
      id = footballers[size-1]['id'] + 1
    else:
      id = 1

    footballer = {
      'id': id, 
      'name': name,
      'position': position,
      'club': club,
      'nationality': nationality,
      'img_url': img_url
    }

    footballers.append(footballer)

    return redirect(url_for('players'))


  return render_template('players/new_player.html',
                         title='Add New Player',
                         teams=teams)

@app.route('/players/<int:id>/info')
def info_player(id):
  footballer = None
  for f in footballers:
    if f['id'] == id:
      footballer = f
      break
  return render_template('players/info_player.html',
                         title="Player's Information",
                         footballer=footballer)