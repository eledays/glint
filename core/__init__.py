import os
import telebot
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


app = Flask(__name__)

# Configs
token = os.getenv('BOT_TOKEN', '')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join('..') + '/instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bot = telebot.TeleBot(token, parse_mode='HTML')

