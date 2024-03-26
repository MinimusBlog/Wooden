import telebot
from telebot import types

bot_token = '6756052562:AAG7R51KH84u_ao4lGSLLuFXDUMHWbmb64Y'
operators = {'123456789': 'Operator 1', '987654321': 'Operator 2'}  # Словарь ID операторов и их имен

bot = telebot.TeleBot(bot_token)
user_requests = {}  # Словарь для хранения запросов на связь с оператором

orders = {
    '100667': 'Заказ оформлен',
    '125668': 'Заказ доставлен',
    '130668': 'Заказ в пути'
}

def is_operator(user_id):
    return user_id in operators

def send_to_user(user_id, text):
    bot.send_message(user_id, text)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('Помощь'), types.KeyboardButton('Статус заказа'))
    markup.row(types.KeyboardButton('Связаться с оператором'), types.KeyboardButton('Перейти на сайт'))
    file = open('./ava.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Связаться с оператором')
def contact_operator(message):
    user_requests[message.chat.id] = message.from_user.id  # Сохраняем запрос на связь с оператором
    bot.send_message(message.chat.id, 'Оператор свяжется с вами в ближайшее время.')

@bot.message_handler(commands=['connect_operator'])
def connect_operator(message):
    bot.send_message(message.chat.id, 'Введите свой ID:')
    bot.register_next_step_handler(message, process_operator_id)

def process_operator_id(message):
    operator_id = message.text.strip()
    if operator_id in operators:
        bot.send_message(message.chat.id, 'Теперь вы оператор!')
        operators[operator_id] = message.from_user.username  # Добавляем оператора в список
        for chat_id, user_id in user_requests.items():
            send_to_user(operator_id, f'Пользователь {user_id} хотел уточнить что-то.')
    else:
        bot.send_message(message.chat.id, 'Введенный ID оператора не найден.')

def process_operator_id(message):
    operator_id = message.text.strip()
    if operator_id in operators:
        for chat_id, user_id in user_requests.items():
            send_to_user(operator_id, f'Пользователь {user_id} хотел уточнить что-то.')
    else:
        bot.send_message(message.chat.id, 'Введенный ID оператора не найден.')

@bot.message_handler(func=lambda message: message.text == 'Перейти на сайт')
def contact_operator(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='http://www.google.com'))
    file = open('./ava.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup, caption='Переход на сайт Wooden!')

@bot.message_handler(func=lambda message: message.text == 'Статус заказа')
def check_order_status(message):
    bot.send_message(message.chat.id, 'Введите номер заказа:')
    bot.register_next_step_handler(message, process_order_status)

def process_order_status(message):
    order_number = message.text
    if order_number in orders:
        bot.send_message(message.chat.id, f'Статус заказа {order_number}: {orders[order_number]}')
    else:
        bot.send_message(message.chat.id, 'Заказ с таким номером не найден.')

@bot.message_handler(func=lambda message: message.text == 'Помощь')
def help_message(message):
    instructions = """
    Привет! Это инструкции по использованию бота:

    1. Связаться с оператором: Нажмите кнопку "Связаться с оператором", чтобы запросить помощь оператора.
    2. Перейти на сайт: Нажмите кнопку "Перейти на сайт", чтобы перейти на сайт Wooden.
    3. Статус заказа: Нажмите кнопку "Статус заказа", чтобы проверить статус вашего заказа.
    """
    bot.send_message(message.chat.id, instructions)

bot.polling(none_stop=True)