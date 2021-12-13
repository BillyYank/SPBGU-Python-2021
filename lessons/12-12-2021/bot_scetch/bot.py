import telebot
import os

bot = telebot.TeleBot("5060188187:AAFfhE0HkPPnAE8ObK07oIQmDITv8DJhJ5I")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['/notify'])
def make_notification(message):
	os.system("python3 make_call.py 'Buy milk' at 2021-12-14 12:00:00")
	bot.reply_to(message, "Success")


@bot.message_handler(func=lambda message: True)
def hi_reply(message):
	bot.reply_to(message, "42")


bot.infinity_polling()


# ssh root@45.147.179.106 3cIG8A*j