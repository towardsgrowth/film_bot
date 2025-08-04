from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("Adventure")
    btn2 = KeyboardButton("Triller")
    btn3 = KeyboardButton("Romantik")
    btn4 = KeyboardButton("Detektiv")
    btn5 = KeyboardButton("Horror")
    btn6 = KeyboardButton("Dramma")
    markup.add(btn1, btn2, btn3, btn4,btn5,btn6)
    back = KeyboardButton("Back")
    markup.add(back)

    