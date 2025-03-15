## **1️⃣ Flask SQLAlchemy (ORM)**  

### **Basic Concepts**  

1. **What is SQLAlchemy in Flask?**  
   → **SQLAlchemy is an Object Relational Mapper (ORM) that allows Flask applications to interact with databases using Python objects instead of raw SQL queries.**  

2. **How do you initialize SQLAlchemy in Flask?**  
   ```python
   from flask_sqlalchemy import SQLAlchemy
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
   db = SQLAlchemy(app)
   ```

3. **How do you define a model in Flask SQLAlchemy?**  
   ```python
   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), unique=True, nullable=False)
   ```

4. **How do you create a new table using SQLAlchemy?**  
   ```python
   db.create_all()
   ```

5. **How do you insert a new record into a database using SQLAlchemy?**  
   ```python
   user = User(username="JohnDoe")
   db.session.add(user)
   db.session.commit()
   ```

6. **How do you retrieve all records from a table?**  
   ```python
   users = User.query.all()
   ```

7. **How do you delete a record in SQLAlchemy?**  
   ```python
   user = User.query.get(1)
   db.session.delete(user)
   db.session.commit()
   ```

8. **How do you filter data in SQLAlchemy?**  
   ```python
   user = User.query.filter_by(username="JohnDoe").first()
   ```

9. **What is the difference between `first()` and `all()` in queries?**  
   → **`first()` returns only the first matching record, while `all()` returns a list of all matching records.**

10. **How do you define relationships between tables in SQLAlchemy?**  
    ```python
    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        user = db.relationship('User', backref='posts')
    ```

---

## **2️⃣ Flask Blueprint**  

11. **What is a Blueprint in Flask?**  
    → **A Blueprint is a way to organize Flask applications into smaller, modular components.**

12. **How do you create a Blueprint?**  
    ```python
    from flask import Blueprint
    auth = Blueprint('auth', __name__)
    ```

13. **How do you register a Blueprint in the main Flask app?**  
    ```python
    app.register_blueprint(auth, url_prefix='/auth')
    ```

14. **How do you define routes inside a Blueprint?**  
    ```python
    @auth.route('/login')
    def login():
        return "Login Page"
    ```

---

## **3️⃣ CSS Framework (Bootstrap)**  

15. **How do you integrate Bootstrap in Flask?**  
    → **Include the Bootstrap CDN in the HTML file.**  
    ```html
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    ```

16. **What are some commonly used Bootstrap classes?**  
    → `container`, `row`, `col`, `btn btn-primary`, `form-control`

---

## **4️⃣ Static Files in Flask**  

17. **Where should static files be stored in a Flask project?**  
    → **Inside the `static/` folder.**

18. **How do you reference a static file in an HTML template?**  
    ```html
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    ```

---

## **5️⃣ Flask Migrations**  

19. **What is Flask-Migrate?**  
    → **It manages database migrations using Alembic.**

20. **How do you initialize Flask-Migrate?**  
    ```python
    from flask_migrate import Migrate
    migrate = Migrate(app, db)
    ```

21. **How do you create a new migration?**  
    ```bash
    flask db migrate -m "Initial migration"
    ```

22. **How do you apply migrations?**  
    ```bash
    flask db upgrade
    ```

---

## **6️⃣ Flask-Login (Authentication System)**  

23. **What is Flask-Login used for?**  
    → **User authentication and session management.**

24. **How do you initialize Flask-Login?**  
    ```python
    from flask_login import LoginManager
    login_manager = LoginManager(app)
    ```

25. **How do you load a user in Flask-Login?**  
    ```python
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    ```

---

## **7️⃣ Flask Pagination**  

26. **How do you paginate query results?**  
    ```python
    users = User.query.paginate(page=1, per_page=10)
    ```

---

## **8️⃣ Flask Web Forms (WTForms)**  

27. **How do you define a Flask form using WTForms?**  
    ```python
    class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        submit = SubmitField('Login')
    ```

28. **How do you handle form validation?**  
    ```python
    if form.validate_on_submit():
        # Process form data
    ```

---

## **9️⃣ Flash Messages**  

29. **What is the purpose of Flash Messages in Flask?**  
    → **To display temporary success/error messages.**

30. **How do you flash a message in Flask?**  
    ```python
    flash("Login successful!", "success")
    ```

---

## **More Questions on Flask Concepts**  

### **31-40: Flask Request & Response Handling**  
31. How do you get query parameters in Flask?  
    ```python
    request.args.get('param')
    ```
32. How do you handle form submissions in Flask?  
    ```python
    request.form['fieldname']
    ```
33. What HTTP methods does Flask support?  
    → **GET, POST, PUT, DELETE, PATCH**

---

### **41-50: Flask Error Handling**  
41. How do you define a custom error page in Flask?  
    ```python
    @app.errorhandler(404)
    def not_found(error):
        return "Page not found", 404
    ```

---

### **51-60: Flask Security & Sessions**  
51. How do you set a session variable in Flask?  
    ```python
    session['username'] = 'John'
    ```
52. How do you protect routes in Flask?  
    ```python
    @login_required
    ```

