from pokedex import app, db, bcrypt
from flask import render_template, request, url_for, redirect, flash
from pokedex.models import User, Pokemon, PokemonType
from flask_login import login_user, logout_user, current_user

@app.route('/')
def home():
  return render_template('index.html', 
                         title='Home Page',
                         pokemons=[])

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    user = db.session.scalar(db.select(User).where(User.username==username))

    if user:
      flash('Username is already exists!', 'warning')
    else:
      user = db.session.scalar(db.select(User).where(User.email==email))
      if user:
        flash('Email is already exists!', 'warning')
      else:
        if password != confirm_password:
          flash('Password Not Match', 'warning')
        else:
          user = User(username=username,
                      email=email,
                      password=bcrypt.generate_password_hash(password))
          db.session.add(user)
          db.session.commit()

          return redirect(url_for('login'))

  return render_template('user/register.html',
                         title='Register Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form['password']

    user = db.session.scalar(db.select(User).where(User.username==username))
    if user:
      if bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('home'))
      
      else:
        flash('Password is invalid!', 'warning')
    else:
      flash('Username is not exists!', 'warning')

  return render_template('user/login.html',
                         title='Login Page')

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
  if request.method == 'POST':
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    current_user.firstname = firstname
    current_user.lastname = lastname

    db.session.commit()
    flash('Update profile successful.', 'success')
    return redirect(url_for('profile'))
  
  return render_template('user/profile.html',
                         title='Profile Page')

@app.route('/pokemon/type')
def pokemon_types():
  types = db.session.scalars(db.select(PokemonType)).all()
  return render_template('type/index.html',
                         title='Pokemon Type Page',
                         types=types)

@app.route('/pokemon/type/new', methods=['GET', 'POST'])
def new_type():
  if request.method == 'POST':
    name = request.form.get('name')
    type = db.session.scalar(db.select(PokemonType).where(PokemonType.name == name))
    if type:
      flash('Pokemon Type already exists!', 'warning')
    else:
      # type = PokemonType(name=name, user=current_user)
      type = PokemonType(name=name, user_id=current_user.id)
      db.session.add(type)
      db.session.commit()
      flash('Add New Pokemon Type Successful.', 'success')
      return redirect(url_for('pokemon_types'))
  
  return render_template('type/new_type.html',
                         title='New Pokemon Type Page')

@app.route('/pokemon/type/<int:id>/update', methods=['GET', 'POST'])
def update_type(id):
  type = db.session.get(PokemonType, id)
  if request.method == 'POST':
    name = request.form.get('name')
    pokemon_type = db.session.scalar(db.select(PokemonType).where(PokemonType.name == name))
    if pokemon_type:
      flash('Pokemon Type already exists!', 'warning')
    else:
      # type = PokemonType(name=name, user=current_user)
      type.name = name
      type.user = current_user
      # type.user_id = current_user.id
      db.session.commit()
      flash('Update Pokemon Type Successful.', 'success')
      return redirect(url_for('pokemon_types'))
  
  return render_template('type/update_type.html',
                         title='Update Pokemon Type Page',
                         type=type)