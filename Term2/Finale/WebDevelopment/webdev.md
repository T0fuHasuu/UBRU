## **📢 Exam Announcement 📢**  
### **Final Exam Outline - Semester 2/67**  

📝 **Exam Structure**  
- **Part 1:** Subjective Questions (60 points, divided by 2)  
- **Total Score:** 30 points  

✅ **Topics Covered:**  
- Setting up the development environment for **Flask framework** 🔥  
- Creating **packages** 🔥  
- Designing **models (classes)** 🔥🔥  
- Using **Flask shell** to manage database tables 🔥🔥🔥  
- Understanding **routes** 🔥  
- Working with **views (templates)** 🔥  

🗓 **Exam Date & Time:**  
📅 **Tuesday, March 18, 2025**  
⏰ **13:00 - 15:00**  
🏫 **Exam Room: 30-402**  

### **Notes:**  
✅ **Students are allowed to bring documents into the exam room.**  

---

### **How to Prepare & Key Focus Areas**  

#### **1️⃣ Setting Up Flask Environment**  
- Install Flask and dependencies  
- Virtual environments (`venv`)  
- Running a basic Flask app  

**Example:**  
```bash
pip install flask
```
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

#### **2️⃣ Creating Packages in Flask**  
- Organizing Flask projects  
- Using `__init__.py` for modular applications  

**Example Directory Structure:**  
```
/my_flask_app
    /app
        __init__.py
        routes.py
        models.py
    run.py
```

#### **3️⃣ Designing Models (Classes)**  
- Using SQLAlchemy  
- Creating database models  

**Example Model:**  
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

#### **4️⃣ Flask Shell & Database Management**  
- Initializing database  
- Adding and querying records  

**Example:**  
```bash
flask shell
```
```python
from app import db
from app.models import User

new_user = User(username="john_doe", email="john@example.com")
db.session.add(new_user)
db.session.commit()
```

#### **5️⃣ Routes in Flask**  
- Handling different URL paths  
- Using dynamic routing  

**Example:**  
```python
@app.route('/user/<username>')
def profile(username):
    return f"User: {username}"
```

#### **6️⃣ Views & Templates**  
- Using Jinja2 templates  
- Passing data to HTML  

**Example (`index.html`)**  
```html
<h1>Welcome, {{ username }}!</h1>
```
**Example Flask Code:**  
```python
@app.route('/dashboard')
def dashboard():
    return render_template("index.html", username="John")
```

---

### **Final Tips:**  
✅ Practice coding with Flask  
✅ Understand how to interact with the database using Flask Shell  
✅ Review the Flask directory structure and `__init__.py`  
✅ Work with routes and templates  
✅ Bring notes or documents as reference  

Would you like any additional practice questions? 😊