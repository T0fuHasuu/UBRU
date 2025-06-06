from epl import app, db
from flask import render_template, request, redirect, url_for
from epl.models import Club, Player

@app.route('/')
def index():
  return render_template('index.html', title='Home Page')

@app.route('/clubs', methods=['GET', 'POST'])
def clubs():
  teams = db.session.scalars(db.select(Club)).all()
  if request.method == 'POST':
    club_name = request.form['club_name']
    teams = db.session.scalars(db.select(Club)
                    .where(Club.name
                    .like(f'%{club_name}%'))).all()
    
  return render_template('clubs/index.html', title='Clubs Page', teams=teams)

@app.route('/clubs/update/<int:id>', methods=['GET', 'POST'])
def update_club(id):
  pass
  # for t in teams:
  #   if t['id'] == id:
  #     team = t
  #     break
  
  # if request.method == 'POST':
  #   id = request.form['id']
  #   name = request.form['name']
  #   # print(f'{name}, {id}')
  #   for i in range(len(teams)):
  #     # print(f'{teams[i]["name"]}, {teams[i]["id"]}')
  #     if teams[i]['id'] == int(id):
  #       # print(f'{i}')
  #       teams[i]['name'] = name
  #       break
    
  #   return redirect(url_for('clubs'))

  # return render_template('clubs/update_club.html', 
  #                        title='Update Club', 
  #                        team=team)

@app.route('/clubs/delete/<int:id>')
def delete_club(id):
  pass
  # for i in range(len(teams)): 
  #   if teams[i]['id'] == id:
  #     del teams[i]
  #     break

  # return redirect(url_for('clubs'))

@app.route('/clubs/new', methods=['GET', 'POST'])
def new_club():
  pass
  # if request.method == 'POST':
  #   name = request.form['name']
  #   size = len(teams)
  #   if size>0:
  #     id = teams[size-1]['id'] + 1
  #   else:
  #     id = 1
  #   team = {'id':id, 'name':name}
  #   teams.append(team)

  #   return redirect(url_for('clubs'))
  
  # return render_template('clubs/new_club.html',
  #                         title='Add New Club')

@app.route('/players')
def players():
  pass
  # return render_template('players/index.html', 
  #                        title='Players Page',
  #                        footballers=footballers)

@app.route('/players/new', methods=['GET', 'POST'])
def new_player():
  pass
  # if request.method == 'POST':
  #   name = request.form['name']
  #   position = request.form['position']
  #   club = request.form['club']
  #   nationality = request.form['nationality']
  #   img_url = request.form['img_url']

  #   size = len(footballers)
  #   if size>0:
  #     id = footballers[size-1]['id'] + 1
  #   else:
  #     id = 1

  #   footballer = {'id':id, 'name': name, 'position':position, 'club':club, 'nationality': nationality, 'img_url': img_url}
  #   footballers.append(footballer)
    
  #   return redirect(url_for('players'))

  # return render_template('players/new_player.html',
  #                         title='Add New Player Page',
  #                         teams=teams)

@app.route('/players/details/<int:id>')
def player_detail(id):
  pass
  # footballer = None
  # for f in footballers:
  #   if f['id'] == id:
  #     footballer = f
  #     break
  # return render_template('players/player_detail.html',
  #                        title='More Detail',
  #                        footballer=footballer)