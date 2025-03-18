### **Pokemon Cheatsheet**

---

### **1. Basic Understanding**
- **Flask**: A lightweight web framework for Python.
- **SQLAlchemy**: ORM (Object-Relational Mapping) for database interactions.
- **Flask-Login**: Manages user authentication and sessions.
- **Bcrypt**: Used for password hashing.
- **Flask-Migrate**: Handles database migrations.

---

### **2. Key Files**

#### **`server.py`**
- Runs the Flask app.
```python
from pokedex import app

if __name__ == '__main__':
    app.run(debug=True)
```

#### **`__init__.py`**
- Initializes the Flask app, database, and extensions.
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemondb.sqlite'
app.secret_key = b'huhjuytdf678ijo;k8uy'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from pokedex import models, routes
```

---

### **3. Models (`models.py`)**

#### **User Model**
- Represents a user in the database.
```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(25), nullable=True)
    lastname = db.Column(db.String(25), nullable=True)
    avatar = db.Column(db.String(25), nullable=False, default='avatar.png')
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    types = db.relationship('PokemonType', back_populates='user')
    pokemons = db.relationship('Pokemon', back_populates='user')
```

#### **Pokemon Model**
- Represents a Pokémon in the database.
```python
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    height = db.Column(db.String(25), nullable=False)
    weight = db.Column(db.String(25), nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    user = db.relationship('User', back_populates='pokemons')
    types = db.relationship('PokemonType', secondary='pokedex', back_populates='pokemons')
```

#### **PokemonType Model**
- Represents a Pokémon type.
```python
class PokemonType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='types')
    pokemons = db.relationship('Pokemon', secondary='pokedex', back_populates='types')
```

#### **Association Table**
- Links Pokémon and their types.
```python
pokedex = db.Table('pokedex',
    db.Column('type_id', db.Integer, db.ForeignKey('pokemon_type.id'), primary_key=True),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
)
```

---

### **4. Routes (`routes.py`)**

#### **Home Route**
- Displays a paginated list of Pokémon.
```python
@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    pokemons = Pokemon.query.paginate(page=page, per_page=4)
    return render_template('index.html', pokemons=pokemons)
```

#### **Register Route**
- Handles user registration.
```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'warning')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, email=email, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Account created!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')
```

#### **Login Route**
- Handles user login.
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check username and password.', 'danger')
    return render_template('login.html')
```

#### **Logout Route**
- Handles user logout.
```python
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
```

---

### **5. Templates**

#### **Base Template (`layout.html`)**
- Defines the base structure for all pages.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Pokemon - {% block title %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    {% include 'navbar.html' %}
    {% block content %}{% endblock %}
</body>
</html>
```

#### **Navbar (`navbar.html`)**
- Navigation bar with links to different pages.
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-success">
    <a class="navbar-brand" href="{{ url_for('home') }}">PokemonGo</a>
    <div class="collapse navbar-collapse">
        <ul class="navbar-nav">
            <li class="nav-item"><a class="nav-link" href="{{ url_for('home') }}">Home</a></li>
            {% if current_user.is_authenticated %}
            <li class="nav-item"><a class="nav-link" href="{{ url_for('pokemon_types') }}">Types</a></li>
            <li class="nav-item"><a class="nav-link" href="{{ url_for('pokedex') }}">Pokemon</a></li>
            {% endif %}
        </ul>
    </div>
</nav>
```

#### **Index Page (`index.html`)**
- Displays a list of Pokémon.
```html
{% extends 'layout.html' %}
{% block content %}
    <div class="container">
        <h1>Pokemon List</h1>
        <div class="row">
            {% for pokemon in pokemons.items %}
            <div class="col-md-3">
                <div class="card">
                    <img src="{{ pokemon.img_url }}" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">{{ pokemon.name }}</h5>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
{% endblock %}
```

---

### **6. Key Points for Exam**
- **Basic Understanding**:
  - Flask setup, database configuration, and user authentication.
  - Relationship between models (User, Pokemon, PokemonType).
- **Code Construction**:
  - Be able to write routes for CRUD operations.
  - Understand how to use templates and pass data to them.
  - Know how to handle user authentication and authorization.
