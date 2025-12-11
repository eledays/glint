from core import db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, BigInteger



class User(DeclarativeBase):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

    # Relationships
    habits: Mapped[list['Habit']] = mapped_column(back_populates='owner')


class Habit(DeclarativeBase):
    __tablename__ = 'habits'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer, nullable=False)

    # Relationships
    owner: Mapped['User'] = mapped_column(back_populates='habits')

