from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from datetime import date
from sqlalchemy.ext.declarative import declarative_base
# from project.infrastructure.postgres.database import Base
Base = declarative_base()

class Cooking(Base):
    __tablename__ = "cooking"

    id_sposob: Mapped[str] = mapped_column(primary_key=True)
    per_kkal: Mapped[int] = mapped_column(nullable=False)
    # extend_existing = True

class Kbzu(Base):
    __tablename__ = "kbzu"

    id_kbzu: Mapped[int] = mapped_column(primary_key=True)
    id_ingredient: Mapped[str] = mapped_column(ForeignKey('ingredients.id_ingredient', ondelete='CASCADE'))
    belki: Mapped[float] = mapped_column(nullable=False)
    zhiri: Mapped[float] = mapped_column(nullable=False)
    uglevodi: Mapped[float] = mapped_column(nullable=False)
    kkal: Mapped[float] = mapped_column(nullable=False)
    # extend_existing=True
class Ingredients(Base):
    __tablename__ = "ingredients"

    id_ingredient: Mapped[str] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(nullable=False)
    ed_izm: Mapped[str] = mapped_column(nullable=False)

class Sostav(Base):
    __tablename__ = "sostav"

    id_sostav: Mapped[int] = mapped_column(primary_key=True)
    id_meal: Mapped[str] = mapped_column(ForeignKey('meals.id_meal', ondelete='CASCADE'))
    id_ingredient: Mapped[str] = mapped_column(ForeignKey('ingredients.id_ingredient', ondelete='CASCADE'))
    cnt: Mapped[int] = mapped_column(nullable=False)
    ed_izm: Mapped[str] = mapped_column(nullable=False)
    id_sposob: Mapped[int] = mapped_column(ForeignKey('cooking.id_sposob', ondelete='CASCADE'),nullable=False)

class Country(Base):
    __tablename__ = "country"

    id:Mapped[int]=mapped_column(primary_key=True)
    id_country: Mapped[str] = mapped_column(nullable=False)
    id_meal: Mapped[str] = mapped_column(ForeignKey('meals.id_meal', ondelete='CASCADE'))

class Users(Base):
    __tablename__ = "users"

    surname: Mapped[str] = mapped_column(nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    fathername: Mapped[str] = mapped_column(nullable=True)
    id_username: Mapped[str] = mapped_column(primary_key=True)
    age: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)

class Feedback(Base):
    __tablename__ = "feedback"

    id_coment: Mapped[int] = mapped_column(primary_key=True)
    id_meal: Mapped[str] = mapped_column(ForeignKey('meals.id_meal', ondelete='CASCADE'),nullable=False)
    id_username: Mapped[str] = mapped_column(ForeignKey('users.id_username', ondelete='CASCADE'),nullable=False)
    mark: Mapped[int] = mapped_column(nullable=False)
    coment: Mapped[str] = mapped_column(nullable=False)
    dat: Mapped[date] = mapped_column(nullable=False)

class Vostreb(Base):
    __tablename__ = "vostreb"

    id:Mapped[int]=mapped_column(primary_key=True)
    id_username: Mapped[str] = mapped_column(ForeignKey('users.id_username', ondelete='CASCADE'))
    id_meal: Mapped[str] = mapped_column(ForeignKey('meals.id_meal', ondelete='CASCADE'))
    count_obr: Mapped[int] = mapped_column(nullable=False)

