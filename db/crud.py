from core import db
from models import Habit, User


def create_habit(user_id: int, name: str) -> Habit:
    habit = Habit()
    habit.name = name
    habit.owner_id = user_id
    db.session.add(habit)
    db.session.commit()
    db.session.refresh(habit)
    return habit


def get_user_by_telegram_id(telegram_id: int) -> User | None:
    return User.query.filter_by(telegram_id=telegram_id).first()