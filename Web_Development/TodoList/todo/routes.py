from flask import render_template, request, redirect, url_for
from todo import db, app, bcrypt
from todo.forms import RegisterForm, LoginForm, TaskForm, UpdateAccountForm
from todo.models import User, Task, Todo
from flask_login import login_user, logout_user, current_user, login_required
import os, secrets
from datetime import date
from PIL import Image

@app.route('/')
def home():
  return render_template('index.html', title='Todo Home Page')

@app.route('/user/register', methods=['GET', 'POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    username = form.username.data
    email = form.email.data
    password = form.password.data
    hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, email=email, password=hash_password)

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login'))
  
  return render_template('user/register.html', title='Register Page', form=form)

@app.route('/user/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    remember = form.remember.data

    user = db.session.scalar(db.select(User).where(User.username==username))

    if user and bcrypt.check_password_hash(user.password, password):
      login_user(user=user, remember=remember)
      return redirect(url_for('home'))
  return render_template('user/login.html', title='Login Page', form=form)

@app.route('/user/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))

def save_avatar(form_avatar):
  random_hex = secrets.token_hex(8)
  _, ext = os.path.splitext(form_avatar.filename)
  avatar_fn = random_hex + ext

  avatar_path = os.path.join(app.root_path, 'static/img', avatar_fn)

  img_size = (256, 256)
  img = Image.open(form_avatar)
  img.thumbnail(img_size)
  img.save(avatar_path)

  return avatar_fn

@app.route('/user/account', methods=['GET', 'POST'])
@login_required
def account():
  form = UpdateAccountForm()
  if request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
    form.fullname.data = current_user.fullname
  elif form.validate_on_submit():
    if form.avatar.data:
      avatar = save_avatar(form.avatar.data)
      current_user.avatar = avatar
    current_user.fullname = form.fullname.data
    db.session.commit()
    return redirect(url_for('account'))
  avatar_pic = current_user.avatar
  return render_template('user/account.html', title='Account Info Page', form=form, avatar_pic=avatar_pic)

@app.route('/todo/todo_today', methods=['GET', 'POST'])
@login_required
def todo_today():
  form = TaskForm()
  todo = db.session.scalar(db.select(Todo).where(Todo.created_at==date.today(), Todo.user==current_user))
  if todo:
    tasks = db.session.scalars(db.select(Task).where(Task.todo==todo)).all()
    if form.validate_on_submit():
      task = form.task.data
      tk = Task(task=task, todo=todo)
      db.session.add(tk)
      db.session.commit()
      return redirect(url_for('todo_today'))
  else:
    tasks = None
  
  return render_template('todo/todos.html', title='Todo Today Page', form=form, todo=todo, tasks=tasks)

@app.route('/todo/new_todo', methods=['GET', 'POST'])
@login_required
def new_todo():
  todo = Todo(user=current_user)
  db.session.add(todo)
  db.session.commit()

  return redirect(url_for('todo_today'))

@app.route('/todo/<int:id>/task_completed')
@login_required
def task_completed(id):
  task = db.session.get(Task, id)
  task.completed = True
  db.session.commit()

  return redirect(url_for('todo_today'))

@app.route('/todo/all_todos')
@login_required
def all_todos():
  tasks = db.session.scalars(db.select(Task).where(Task.todo_id==Todo.id, Todo.user==current_user).order_by(Todo.created_at.desc())).all()
  return render_template('todo/all_todos.html', title='Show All Todos', tasks=tasks)

@app.route('/todo/completed_todos')
@login_required
def completed_todos():
  tasks = db.session.scalars(db.select(Task).where(Task.todo_id==Todo.id, Todo.user==current_user, Task.completed==True).order_by(Todo.created_at.desc())).all()
  return render_template('todo/all_todos.html',
                         title='Show Completed Tasks',
                         tasks=tasks)

@app.route('/todo/uncompleted_todos')
@login_required
def uncompleted_todos():
  tasks = db.session.scalars(db.select(Task).where(Task.todo_id==Todo.id, Todo.user==current_user, Task.completed==False).order_by(Todo.created_at.desc())).all()
  return render_template('todo/all_todos.html',
                         title='Show Uncompleted Tasks',
                         tasks=tasks)