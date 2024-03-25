import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6756052562:AAG7R51KH84u_ao4lGSLLuFXDUMHWbmb64Y')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open("http://www.google.com")

@bot.message_handler(content_types=['photo', 'document'])
def  get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add()
    markup.add(types.InlineKeyboardButton('Главное меню', callback_data='menu'))
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url= "http://www.google.com"))
    bot.reply_to(message, 'Отправлено оператору!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'menu':
        bot.menu_message(callback.message.chat.id, callback.message.message_id)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url= "http://www.google.com"))
    file = open('./ava.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Веб-сайт открыт')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '''Добро пожаловать в службу технической поддержки!

Мы здесь, чтобы помочь вам решить любые технические проблемы или вопросы, с которыми вы столкнулись. Вот некоторые полезные команды, которые вы можете использовать:

/help - отображает это сообщение с информацией о доступных командах.
/site - отображает наш сайт с товарами.''')

@bot.message_handler()
def info(message):
    if  message.text.lower() == "привет":
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == '/start':
         bot.send_message(message.chat.id, '''Добро пожаловать в службу технической поддержки!

Мы здесь, чтобы помочь вам решить любые технические проблемы или вопросы, с которыми вы столкнулись. Вот некоторые полезные команды, которые вы можете использовать:

/help - отображает это сообщение с информацией о доступных командах.''')



bot.polling(none_stop=True)