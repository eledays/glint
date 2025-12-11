from core import bot, app, db

from db.crud import create_habit, get_user_by_telegram_id
from models import User

import handlers.command_handlers

import threading


if __name__ == "__main__":
    threading.Thread(target=bot.infinity_polling).start()
    threading.Thread(target=app.run).start()
