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
bot = telebot.TeleBot('6387895070:AAHjLpYxgGdfPRFgsNNyh0HOIvhDD496Sks')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://ramza.netlify.com/')

@bot.message_handler(commands=['start', 'main', 'hello', 'salom'])
def main(message):
    bot.send_message(message.chat.id, f'Assalomu alaykum, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Qanday masalada yordam kerak')

# @bot.message_handler(commands=['code'])
# def main(message):
#     bot.send_message(message.chat.id, message)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'salom':
        bot.send_message(message.chat.id,f'Assalomu alaykum, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    # elif message.text.lower() == 'start':


bot.polling(none_stop=True)
