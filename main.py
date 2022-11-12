import telebot
from telebot import types
from analisys import get_sentiment

bot = telebot.TeleBot('5743469016:AAGhYAyPhtXHr9dTA7qezzildjyl4UIL0nI')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я анализирую твои сообщения и выделяю эмоциональный контекст! Перешли мне "
                          "сообщение, чтобы узнать функционал бота! \n Напиши /help, чтобы узнать, как пользоваться "
                          "ботом")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Разработчик: @sw-ruhub Ruslan Martynov\nХотел создать анализатор сообщений. А вдруг "
                          "поможет кому-то.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, get_sentiment([message.text]))


bot.infinity_polling()
