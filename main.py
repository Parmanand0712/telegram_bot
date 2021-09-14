import os
import telebot

token = os.getenv('API_KEY')
bot = telebot.TeleBot('token', parse_mode=None)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey, how's it going?")

# @bot.message_handler(commands=['Hello'])
# def hello(message):
#     bot.reply_to(message, "Hello!")


@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id, "Welcome to Polkadot India Official")
# To keep checking for the messages
bot.polling()