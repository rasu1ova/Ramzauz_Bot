# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('6387895070:AAHjLpYxgGdfPRFgsNNyh0HOIvhDD496Sks')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://ramza.netlify.com/')




@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Qanday masalada yordam kerak')

@bot.message_handler(commands=['code'])
def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'salom':
        bot.send_message(message.chat.id,f'Assalomu alaykum, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    # elif message.text.lower() == 'start':

@bot.message_handler(commands=['start' ])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Web sahifaga o`tish')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Platforma')
    btn3 = types.KeyboardButton('Kurslar')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Assalomu alaykum, {message.from_user.first_name}', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Web sahifaga o`tish', url='https://ramza.netlify.com/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Platforma', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Kurslar', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'qanday rasm bu?', reply_markup=markup)


bot.polling(none_stop=True)
