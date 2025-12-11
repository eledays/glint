from core import bot, app
import threading


# Telegram Bot Code

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, World :)")


if __name__ == "__main__":
    threading.Thread(target=bot.infinity_polling).start()
    threading.Thread(target=app.run).start()
    