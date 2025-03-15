from pokedex import db, login_manager
from sqlalchemy import Integer, String, DateTime, func, Table, Column, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from flask_login import UserMixin
from typing import List

@login_manager.user_loader
def load_user(id):
  return db.session.get(User, int(id))

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
  
pokedex = Table(
  'pokedex',
  db.metadata,
  Column('type_id', Integer, ForeignKey('type.id'), primary_key=True),
  Column('pokemon_id', Integer, ForeignKey('pokemon.id'), primary_key=True)
)

class PokemonType(db.Model):
  __tablename__ = 'type'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
  created_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now(), onupdate=func.now())

  user: Mapped[User] = relationship(back_populates='types')
  pokemons: Mapped[List['Pokemon']] = relationship(back_populates='types', 
                                                   secondary=pokedex)
  
  def __repr__(self):
    return f'<PokemonType: {self.name}>'

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
  
  def __repr__(self):
    return f'<Pokemon: {self.name}>'
  

def add_all_types(user: User):
  water = PokemonType(name='Water', user=user)
  fire = PokemonType(name='Fire', user=user)
  rock = PokemonType(name='Rock', user=user)
  ground = PokemonType(name='Ground', user=user)
  flying = PokemonType(name='Flying', user=user)  
  dragon = PokemonType(name='Dragon', user=user)
  bug = PokemonType(name='Bug', user=user)
  psychic = PokemonType(name='Psychic', user=user)
  poison = PokemonType(name='Poison', user=user)
  fighting = PokemonType(name='Fighting', user=user)
  ice = PokemonType(name='Ice', user=user)
  normal = PokemonType(name='Normal', user=user)
  steel = PokemonType(name='Steel', user=user)
  electric = PokemonType(name='Electric', user=user)
  grass = PokemonType(name='Grass', user=user)
  ghost = PokemonType(name='Ghost', user=user)
  dark = PokemonType(name='Dark', user=user)
  fairy = PokemonType(name='Fairy', user=user)

  db.session.add_all([
    water, fire, rock, ground, flying, dragon,
    bug, psychic, poison, fighting, ice, normal,
    steel, electric, grass, ghost, dark, fairy
  ])

  db.session.commit()