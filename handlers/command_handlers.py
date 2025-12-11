from core import bot, app, db
from db.crud import create_habit, get_user_by_telegram_id
from db.models import User

@bot.message_handler(commands=['start'])
def start_message(message):
    with app.app_context():
        user: User | None = get_user_by_telegram_id(message.from_user.id)

        if user is None:
            user = User()
            user.telegram_id = message.from_user.id
            db.session.add(user)
            db.session.commit()
    
    bot.send_message(message.chat.id, "Привет, это glint — простой трекер привычек\n"
                     "Давай создадим первую привычку — /create\n\n"
                     "Помощь по управлению — /help")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "В разработке")


@bot.message_handler(commands=['create'])
def create_message(message, step=0):
    if step == 0:
        bot.send_message(message.chat.id, "Как назовём привычку?")
        bot.register_next_step_handler(message, create_message, step=1)
    elif step == 1:
        with app.app_context():
            user: User | None = get_user_by_telegram_id(message.from_user.id)

            if user is None:
                bot.send_message(message.chat.id, "Пользователь не найден")
                return 

            habit = create_habit(user.id, message.text)