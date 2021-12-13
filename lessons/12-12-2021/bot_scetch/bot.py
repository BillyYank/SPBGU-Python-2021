import telebot

bot = telebot.TeleBot("5060188187:AAFfhE0HkPPnAE8ObK07oIQmDITv8DJhJ5I")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: message.text.startswith('Привет'))
def hi_reply(message):
	bot.reply_to(message, "И тебе привет!")


@bot.message_handler(func=lambda message: True)
def hi_reply(message):
	bot.reply_to(message, "42")


bot.infinity_polling()


# 3cIG8A*j