from telebot import TeleBot
from telebot.types import Message
from buttons import main_buttons

TOKEN = "7670840809:AAGZz7wsWgXH05ZDoBn2ilycTWIsy49Aj5U"
bot = TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def reaction_to_start(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, reply_markup=main_buttons())

@bot.message_handler(func=lambda message: message.text == "Adventure")
def handle_adventure(message: Message):
    bot.send_message(message.chat.id, "Bu sarguzasht haqida kino!")

@bot.message_handler(func=lambda message: message.text == "Triller")
def handle_thriller(message: Message):
    bot.send_message(message.chat.id, "Bu triller janridagi kino!")

@bot.message_handler(func=lambda message: message.text == "Romantik")
def handle_romantic(message: Message):
    bot.send_message(message.chat.id, "Bu romantik janridagi kino!")

@bot.message_handler(func=lambda message: message.text == "Detektiv")
def handle_detective(message: Message):
    bot.send_message(message.chat.id, "Bu detektiv kino!")

@bot.message_handler(func=lambda message: message.text == "Horror")
def handle_horror(message: Message):
    bot.send_message(message.chat.id, "Bu qo'rqinchli kino!")

@bot.message_handler(func=lambda message: message.text == "Dramma")
def handle_dramma(message: Message):
    bot.send_message(message.chat.id, "Bu dramaviy kino!")

@bot.message_handler(func=lambda message: message.text == "Back")
def handle_back(message: Message):
    bot.send_message(message.chat.id, "Bosh menyuga qaytdingiz.", reply_markup=main_buttons())




if __name__ == '__main__':
    bot.infinity_polling()
