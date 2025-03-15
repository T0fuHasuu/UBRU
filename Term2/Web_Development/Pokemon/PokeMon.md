# Pokemon Cheatsheet

### server.py
```py
from pokedex import app

if __name__ == '__main__':
    app.run(debug=True)
```
1. Import the apph in the init of pokemon package
2. run the file if the name is __main__

---
## pokedex 
![catEngineer](https://media1.tenor.com/m/6PUE1PAsXQUAAAAd/scaler-create-impact.gif)

### __init__.py
```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemondb.sqlite'
app.secret_key = b'huhjuytdf678ijo;k8uy'
# app.config['SECRET_KEY'] = b'huhjuytdf678ijo;k8uy'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from pokedex import models, routes
```
**1. FlASK SETUP**
```py
from flask import Flask
app = Flask(__name__)
```
**2. Database Setup**
```py
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemondb.sqlite'
db = SQLAlchemy(app)
```
**3. Login Manager**
```py
from flask_login import LoginManager
app.secret_key = b'huhjuytdf678ijo;k8uy'
app.config['SECRET_KEY'] = b'huhjuytdf678ijo;k8uy'
login_manager = LoginManager(app)
```
**4. PassCode Bycrypt**
```py
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
```
**5. SQL Migration**
```py
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
```
**6. Import models and routes in init**
```py
from pokedex import models, routes
```

### models (File : [models.py]())
**1. Importation**
```py
from pokedex import db, login_manager
from sqlalchemy import Integer, String, DateTime, func, Table, Column, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from flask_login import UserMixin
from typing import List
```
- **`pokedex` modules** – Handles database (`db`) and user login (`login_manager`).  
- **`SQLAlchemy`** – Manages database models, columns, relationships, and data types.  
- **`datetime`** – Provides timestamp functionality.  
- **`Flask-Login`** – Enables user authentication with `UserMixin`.  
- **`typing`** – Supports type hinting with `List`.  

**2. User Loader Function**  
```py
@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))
```
- **`@login_manager.user_loader`** – A decorator that registers the function as the user loader for Flask-Login.  
- **`load_user(id)`** – Fetches a user from the database using their `id`.  
- **`db.session.get(User, int(id))`** – Queries the `User` table for the given `id`, converting it to an integer for safety.  
- **Purpose** – Ensures Flask-Login can retrieve user details for authentication sessions.

**3. `User` Class (Database Model)**  
Defines the structure of the `user` table in the database.  
```py
class User(db.Model, UserMixin):
  __tablename__ = 'user'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  password: Mapped[str] = mapped_column(String(100), nullable=False)
  firstname: Mapped[str] = mapped_column(String(25), nullable=True)
  lastname: Mapped[str] = mapped_column(String(25), nullable=True)
  avatar: Mapped[str] = mapped_column(String(25), nullable=False, default='avatar.png')
  created_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now(), onupdate=func.now())

  types: Mapped[List['PokemonType']] = relationship(back_populates='user')
  pokemons: Mapped[List['Pokemon']] = relationship(back_populates='user')

  def __repr__(self):
    return f'<User: {self.username}>'
```

- **`User(db.Model, UserMixin)`** – Inherits from SQLAlchemy's `Model` and Flask-Login's `UserMixin`.  
- **Columns:**  
  - `id` – Primary key (unique user ID).  
  - `username`, `email` – Unique, required fields.  
  - `password` – Stores hashed passwords.  
  - `firstname`, `lastname` – Optional user details.  
  - `avatar` – Defaults to `'avatar.png'`.  
  - `created_at`, `updated_at` – Timestamp fields (auto-filled).  
- **Relationships:**  
  - `types` – Links user to `PokemonType`.  
  - `pokemons` – Links user to `Pokemon`.  
- **`__repr__` method** – Returns a string representation (`<User: username>`).  

---

**4. `pokedex` Table (Association Table)**  
A many-to-many relationship table linking `type` and `pokemon`.  
```py
pokedex = Table(
  'pokedex',
  db.metadata,
  Column('type_id', Integer, ForeignKey('type.id'), primary_key=True),
  Column('pokemon_id', Integer, ForeignKey('pokemon.id'), primary_key=True)
)
```
- **`pokedex = Table(...)`** – Defines an intermediary table.  
- **Columns:**  
  - `type_id` – Foreign key linking to `type.id`.  
  - `pokemon_id` – Foreign key linking to `pokemon.id`.  
- **Purpose:**  
  - Enables multiple Pokémon to have multiple types.

**4. `Pokemon` Model**  
Defines the structure of the `pokemon` table in the database.  
```py
class Pokemon(db.Model):
  __tablename__ = 'pokemon'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  height: Mapped[str] = mapped_column(String(25), nullable=False)
  weight: Mapped[str] = mapped_column(String(25), nullable=False)
  description: Mapped[str] = mapped_column(Text, nullable=False)
  img_url: Mapped[str] = mapped_column(Text, nullable=False)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
  created_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now(), onupdate=func.now())

  user: Mapped[User] = relationship(back_populates='pokemons')
  types: Mapped[List[PokemonType]] = relationship(back_populates='pokemons',
                                                  secondary=pokedex)
```
- **`Pokemon(db.Model)`** – SQLAlchemy model for Pokémon data.  
- **Columns:**  
  - `id` – Primary key (unique Pokémon ID).  
  - `name` – Unique name of the Pokémon.  
  - `height`, `weight` – Stores physical attributes.  
  - `description` – Text field for Pokémon details.  
  - `img_url` – Stores image URL.  
  - `user_id` – Foreign key linking to the `user` table.  
  - `created_at`, `updated_at` – Timestamp fields (auto-filled).  
- **Relationships:**  
  - `user` – Links Pokémon to its owner (`User`).  
  - `types` – Many-to-many relation with `PokemonType` via `pokedex`. 

**5. `add_all_types` Function**  
```py
def add_all_types(user: User):
```
- Takes a `User` object as an argument.  

```py
fairy = PokemonType(name='Fairy', user=user)
```
- Creates a `PokemonType` instance with the name `'Fairy'`, linked to the given `user`.  

```py
db.session.add_all([fairy])
```
- Adds the `fairy` type to the database session (can be expanded for more types).  

```py
db.session.commit()
```
- Saves changes to the database.  

### routes (**File :** [routes.py]())
**1. Importation**
```py
from pokedex import app, db, bcrypt
from flask import render_template, request, url_for, redirect, flash
from pokedex.models import User, Pokemon, PokemonType
from flask_login import login_user, logout_user, current_user, login_required
```
- Import things which neccessary for the function to be work

**2. Home Route**
```py
@app.route('/')
def home():
  page = request.args.get('page', type=int)
  pokemons = db.paginate(db.select(Pokemon), per_page=4, page=page)
  return render_template('index.html', 
                         title='Home Page',
                         pokemons=pokemons)
```
**Breakdown**
---
```py
page = request.args.get('page', type=int)
```
- Retrieves the `page` number from the URL query parameters (defaults to `None`).  

```py
pokemons = db.paginate(db.select(Pokemon), per_page=4, page=page)
```
- Uses SQLAlchemy’s `paginate()` to fetch Pokémon data:  
  - **`db.select(Pokemon)`** – Selects all Pokémon.  
  - **`per_page=4`** – Displays 4 Pokémon per page.  
  - **`page=page`** – Retrieves the requested page.  

```py
return render_template('index.html', 
                       title='Home Page',
                       pokemons=pokemons)
```
- Renders `index.html`, passing:  
  - **`title`** – Sets the page title.  
  - **`pokemons`** – Sends paginated Pokémon data to the template.  

**Code the rest**
```py
@app.route('/detail/<int:id>/')
def detail(id):
  pokemon = db.session.get(Pokemon, id)
  return render_template('detail_pokemon.html',
                         title='Pokemon\'s Detail Page',
                         pokemon=pokemon)


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
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
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
@login_required
def pokemon_types():
  types = db.session.scalars(db.select(PokemonType)).all()
  return render_template('type/index.html',
                         title='Pokemon Type Page',
                         types=types)

@app.route('/pokemon/type/new', methods=['GET', 'POST'])
@login_required
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
@login_required
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

@app.route('/pokemon/pokedex')
@login_required
def pokedex():
  pokemons = db.session.scalars(db.select(Pokemon)).all()
  return render_template('pokemon/index.html',
                         title='Pokedex Page',
                         pokemons=pokemons)

@app.route('/pokemon/pokedex/new_pokemon', methods=['GET', 'POST'])
@login_required
def new_pokemon():
  types = db.session.scalars(db.select(PokemonType)).all()
  if request.method == 'POST':
    name = request.form.get('name')
    weight = request.form.get('weight')
    height = request.form.get('height')
    description = request.form.get('description')
    img_url = request.form.get('img_url')
    pokemon_types = request.form.getlist('pokemon_types')

    pokemon = db.session.scalar(db.select(Pokemon).where(
      Pokemon.name == name))
    if pokemon:
      flash('Pokemon is already exists!', 'warning')
    else:

      p_types = []
      for id in pokemon_types:
        p_types.append(db.session.get(PokemonType, id))
      
      pokemon = Pokemon(name=name, 
                        weight=weight,
                        height=height,
                        description=description,
                        img_url=img_url,
                        user=current_user,
                        types=p_types)
      db.session.add(pokemon)
      db.session.commit()
      flash('Add new pokemon successful!', 'success')
      return redirect(url_for('pokedex'))
  
  return render_template('pokemon/new_pokemon.html',
                         title='New Pokemon Page',
                         types=types)

@app.route('/pokemon/pokedex/<int:id>/detail')
@login_required
def detail_pokemon(id):
  pokemon = db.session.get(Pokemon, id)
  return render_template('pokemon/detail_pokemon.html',
                         title='Pokemon\'s Detail Page',
                         pokemon=pokemon)
```

### template

#### layout (File : [layout.html]())
**Based Structure**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pokemon - {% block title %}{% endblock %}
  </title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link href="https://fonts.googleapis.com/css2?family=Mitr:wght@200;300;400;500;600;700&family=Nunito:ital,wght@0,200..1000;1,200..1000&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <style>
    * {
      font-family: "Nunito", "Mitr", serif;
    }
  </style>
</head>
<body>
  {% include "navbar.html" %}
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
      
      {% for category, message in messages %}
      <div class="alert alert-{{category}} alert-dismissible fade show" role="alert">
        <strong>{{message}}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      {% endfor %}
      
    {% endif %}
  {% endwith %}
  {% block content %}{% endblock %}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
```

#### Navbar (File : [navbar.html]())
**Code**
```html
<nav class="navbar navbar-expand-lg bg-success" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="{{url_for('home')}}">PokemonGo</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="{{url_for('home')}}">Home</a>
        </li>
        {% if current_user.is_authenticated %}
        <li class="nav-item">
          <a class="nav-link" href="{{url_for('pokemon_types')}}">Type</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{{url_for('pokedex')}}">Pokemon</a>
        </li>
        {% endif %}
      </ul>
      <ul class="navbar-nav">
        {% if current_user.is_authenticated %}
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="{{url_for('static', filename='img/' + current_user.avatar)}}" width="25" height="25">
            Welcome, {{current_user.username}}
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="{{url_for('profile')}}">Profile</a></li>
            <li><a class="dropdown-item" href="#">Change Password</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="{{url_for('logout')}}">Logout</a></li>
          </ul>
        </li>
        {% else %}
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{{url_for('register')}}">Register</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{{url_for('login')}}">Login</a>
        </li>
        {% endif %}
      </ul>
    </div>
  </div>
</nav>
```

#### index (File : [index.html]())
**Code**
```html
{% extends 'layout.html' %}

{% block title %}
  {{title}}
{% endblock %}

{% block content %}
  <div class="container">
    <h1 class="mt-3">{{title}}</h1>
    <hr>
    <div class="row">
      {% for pokemon in pokemons %}
        <div class="col-lg-3">
          <div class="card mt-4 card-pokemon">
            <a href="{{url_for('detail', id=pokemon.id)}}">
              <img src="{{pokemon.img_url}}" alt="{{pokemon.name}}" class="card-img-top bg-secondary">
            </a>
            <div class="card-body">
              <h2 class="text-success">{{pokemon.name}}</h2>
              {% for type in pokemon.types %}
                <a class="btn btn-outline-secondary btn-sm">{{type.name}}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
    {% include "pagination.html" %}
  </div>
{% endblock %}
```

#### pagination (File : [pagination.html]())
**Code**
```html
<nav aria-label="Page navigation example" class="mb-3">
  <ul class="pagination">
    {% if pokemons.has_prev %}
    <li class="page-item"><a class="page-link" href="{{url_for('home', page=pokemons.prev_num)}}">Previous</a></li>
    {% endif %}
    
    {% for number in pokemons.iter_pages() %}
        {% if number %}
          {% if pokemons.page != number %}
          <li class="page-item"><a class="page-link" href="{{url_for('home', page=number)}}">{{number}}</a></li>
          {% else %}
          <li class="page-item"><p class="page-link" href="#">{{number}}</p></li>
          {% endif %}
        {% else %}
          <li class="page-item"><p class="page-link" href="#">...</p></li>
        {% endif %}
        
    {% endfor %}

    {% if pokemons.has_next %}
    <li class="page-item"><a class="page-link" href="{{url_for('home', page=pokemons.next_num)}}">Next</a></li>
    {% endif %}
    
    
  </ul>
</nav>
```

#### Login (File : [login.html]())
**Code**
```html 
{% extends 'layout.html' %}

{% block title %}
  {{title}}
{% endblock %}


{% block content %}
  <div class="container mt-3">
    <h1>{{title}}</h1>
    <hr>
    <div class="card">
      <div class="card-header text-bg-success">
        <h3>Login Form</h3>
      </div>
      <div class="card-body">
        <form method="post">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input name="username" type="text" class="form-control" id="username">
          </div>
          
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input name="password" type="password" class="form-control" id="password">
          </div>
          
          <button type="submit" class="btn btn-outline-success">
            <i class="bi bi-box-arrow-in-right"></i>
            Login
          </button>
        </form>
      </div>
    </div>
  </div>
{% endblock %}
```

#### Register (File : [register.html]())
**Code**
```html
{% extends 'layout.html' %}

{% block title %}
  {{title}}
{% endblock %}


{% block content %}
  <div class="container mt-3">
    <h1>{{title}}</h1>
    <hr>
    <div class="card">
      <div class="card-header text-bg-success">
        <h3>Registration Form</h3>
      </div>
      <div class="card-body">
        <form method="post" >
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input name="username" type="text" class="form-control" id="username">
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email Address</label>
            <input name="email" type="email" class="form-control" id="email">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input name="password" type="password" class="form-control" id="password">
          </div>
          <div class="mb-3">
            <label for="confirm_password" class="form-label">Confirm Password</label>
            <input name="confirm_password" type="password" class="form-control" id="confirm_password">
          </div>
          <button type="submit" class="btn btn-outline-success">
            <i class="bi bi-check-square"></i>
            Submit
          </button>
        </form>
      </div>
    </div>
  </div>
{% endblock %}
```
