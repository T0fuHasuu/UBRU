from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from typing import List
from epl import db

class Club(db.Model):
  __tablename__ = 'club'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

  players: Mapped[List['Player']] = relationship(back_populates='club', cascade='all, delete')
  def __repr__(self):
    return f'<Club: {self.name}>'
  

class Player(db.Model):
  __tablename__ = 'player'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  position: Mapped[str] = mapped_column(String(50), nullable=False)
  nationality: Mapped[str] = mapped_column(String(50), nullable=False)
  img_url: Mapped[str] = mapped_column(Text, nullable=False)
  club_id: Mapped[int] = mapped_column(Integer, ForeignKey(Club.id, ondelete='CASCADE'))

  club: Mapped[Club] = relationship(back_populates='players')
  def __repr__(self):
    return f'<Player: {self.name}>'