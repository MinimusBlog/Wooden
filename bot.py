import telebot
from telebot import types

bot = telebot.TeleBot('6756052562:AAG7R51KH84u_ao4lGSLLuFXDUMHWbmb64Y')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('Помощь'), types.KeyboardButton('Статус заказа'))
    markup.row(types.KeyboardButton('Связаться с оператором'), types.KeyboardButton('Перейти на сайт'))
    file = open('./ava.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')

@bot.message_handler(func=lambda message: message.text == 'Связаться с оператором')
def contact_operator(message):
    bot.send_message(message.chat.id, 'Оператор свяжется с вами в ближайшее время.')

@bot.message_handler(func=lambda message: message.text == 'Перейти на сайт')
def contact_operator(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='http://www.google.com'))
    file = open('./ava.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup, caption='Переход на сайт Wooden!')
    #bot.send_message(message.chat.id, 'Переход на сайт Wooden!', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '''Добро пожаловать в службу технической поддержки!

Мы здесь, чтобы помочь вам решить любые технические проблемы или вопросы, с которыми вы столкнулись. Вот некоторые полезные команды, которые вы можете использовать:

/help - отображает это сообщение с информацией о доступных командах.
/site - отображает наш сайт с товарами.''')

bot.polling(none_stop=True)