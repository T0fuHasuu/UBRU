from todo import db, login_manager
from sqlalchemy import Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from flask_login import UserMixin
from datetime import date

@login_manager.user_loader
def load_user(user_id):
  return db.session.get(User, int(user_id))

class User(db.Model, UserMixin):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  username: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
  email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  password: Mapped[str] = mapped_column(String(100), nullable=False)
  fullname: Mapped[str] = mapped_column(String(50), nullable=True)
  avatar: Mapped[str] = mapped_column(String(50), default='default.png')

  todos: Mapped[List['Todo']] = relationship(back_populates='user')
  def __repr__(self):
    return f'<User: {self.username}>'
  
class Todo(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  created_at: Mapped[date] = mapped_column(Date, default=date.today())
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey(User.id))

  user: Mapped[User] = relationship(back_populates='todos')
  tasks: Mapped[List['Task']] = relationship(back_populates='todo')

  def __repr__(self):
    return f'<Todo: {self.created_at}>'
  
class Task(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  task: Mapped[str] = mapped_column(String(100), nullable=False)
  completed: Mapped[bool] = mapped_column(Boolean, default=False)
  todo_id: Mapped[int] = mapped_column(Integer, ForeignKey(Todo.id))

  todo: Mapped[Todo] = relationship(back_populates='tasks')
  
  def __repr__(self):
    return f'<Task: {self.task}>'