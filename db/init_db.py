from core import app, db


def init_db():
    """
    Инициализация базы данных: создание всех таблиц
    """
    with app.app_context():
        db.create_all()