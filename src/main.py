import telebot

from src.config import settings


bot = telebot.TeleBot(settings.TOKEN_BOT)

@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'У тебя очень красивый голос!')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Приветствую, тебя, {message.chat.username}!")

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Классная картинка!')

bot.polling(non_stop=True)

