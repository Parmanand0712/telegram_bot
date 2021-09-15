import os
import telebot
from telebot import types,util

token = os.getenv('API_KEY')
bot = telebot.TeleBot('1987145389:AAFxTTk_ikmI4JMo0FOdG7PrITjTLuUiUh8', parse_mode=None)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.send_message(message, "Hey, how's it going?")

@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id, "Welcome to Polkadot India Official")

@bot.chat_member_handler()
def chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id,"Hello {name}! Welcome to Polkadot India. Checked pinned messages for more information".format(name=new.user.first_name)) # Welcome message
# To keep checking for the messages
#bot.polling()
bot.polling(allowed_updates=util.update_types)