from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey, Table, Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from eralchemy2 import render_er


db = SQLAlchemy()

#Favoritos
class Favorite(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)

#Usuario
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name:  Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

# #Relaciones
    favorites: Mapped[list["Favorite"]] = relationship(back_populates= 'user')

#Personajes
class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(120), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(120), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=False)
    height: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites: Mapped[list["Favorite"]] = relationship(back_populates= 'people')

#Planetas
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    diameter: Mapped[str] = mapped_column(String(120), nullable=False)
    gravity: Mapped[str] = mapped_column(String(120), nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites: Mapped[list["Favorite"]] = relationship(back_populates= 'planet')

#Vehiculos
class Vehicle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(String(120), nullable=False)
    vehicle_class: Mapped[str] = mapped_column(String(120), nullable=False)
    length: Mapped[str] = mapped_column(String(120), nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites: Mapped[list["Favorite"]] = relationship(back_populates= 'vehicle')
