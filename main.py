from core import bot, app
import threading


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, это glint — простой трекер привычек\n"
                     "Давай создадим первую привычку — /create\n\n"
                     "Помощь по управлению — /help")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "В разработке")


if __name__ == "__main__":
    threading.Thread(target=bot.infinity_polling).start()
    threading.Thread(target=app.run).start()
