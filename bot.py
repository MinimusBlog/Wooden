from flask import Flask, request, render_template
import telebot
from telebot import types

# Токен бота
bot_token = '6756052562:AAG7R51KH84u_ao4lGSLLuFXDUMHWbmb64Y'

# Инициализация Flask приложения
app = Flask(__name__)

# Инициализация бота
bot = telebot.TeleBot(bot_token)

# Словарь ID операторов и их имен
operators = {'123456789': 'Operator 1', '987654321': 'Operator 2'}

# Словарь для хранения запросов на связь с оператором
user_requests = {}

# Словарь для хранения сообщений пользователей
user_messages = {}

# Словарь статусов заказов
orders = {
    '100667': 'Заказ оформлен',
    '125668': 'Заказ доставлен',
    '130668': 'Заказ в пути'
}

# Функция для отправки сообщения пользователю
def send_to_user(user_id, text):
    bot.send_message(user_id, text)

# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('Помощь'), types.KeyboardButton('Статус заказа'))
    markup.row(types.KeyboardButton('Связаться с оператором'), types.KeyboardButton('Перейти на сайт'))
    file = open('./ava.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!', reply_markup=markup)

# Обработчик для кнопки "Связаться с оператором"
@bot.message_handler(func=lambda message: message.text == 'Связаться с оператором')
def contact_operator(message):
    user_requests[message.chat.id] = message.from_user.id  # Сохраняем запрос на связь с оператором
    bot.send_message(message.chat.id, 'Оператор свяжется с вами в ближайшее время.')

# Обработчик для кнопки "Перейти на сайт"
@bot.message_handler(func=lambda message: message.text == 'Перейти на сайт')
def go_to_site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='http://www.google.com'))
    file = open('./ava.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup, caption='Переход на сайт Wooden!')

# Обработчик для кнопки "Статус заказа"
@bot.message_handler(func=lambda message: message.text == 'Статус заказа')
def check_order_status(message):
    bot.send_message(message.chat.id, 'Введите номер заказа:')
    bot.register_next_step_handler(message, process_order_status)

# Обработчик для получения статуса заказа
def process_order_status(message):
    order_number = message.text
    if order_number in orders:
        bot.send_message(message.chat.id, f'Статус заказа {order_number}: {orders[order_number]}')
    else:
        bot.send_message(message.chat.id, 'Заказ с таким номером не найден.')

# Обработчик для кнопки "Помощь"
@bot.message_handler(func=lambda message: message.text == 'Помощь')
def help_message(message):
    instructions = """
    Привет! Это инструкции по использованию бота:

    1. Связаться с оператором: Нажмите кнопку "Связаться с оператором", чтобы запросить помощь оператора.
    2. Перейти на сайт: Нажмите кнопку "Перейти на сайт", чтобы перейти на сайт Wooden.
    3. Статус заказа: Нажмите кнопку "Статус заказа", чтобы проверить статус вашего заказа.
    """
    bot.send_message(message.chat.id, instructions)

# Обработчик для команды /connect_operator 
@bot.message_handler(commands=['connect_operator']) 
def connect_operator(message): 
    bot.send_message(message.chat.id, 'Введите свой ID:') 
    bot.register_next_step_handler(message, process_operator_id) 
 
# Обработчик для обработки введенного ID оператора 
def process_operator_id(message): 
    operator_id = message.text.strip() 
    if operator_id in operators: 
        bot.send_message(message.chat.id, 'Теперь вы оператор!') 
        operators[operator_id] = message.from_user.username  # Добавляем оператора в список 
        for chat_id, user_id in user_requests.items(): 
            send_to_user(user_id, f'Пользователь {chat_id} хотел уточнить что-то.') 
    else: 
        bot.send_message(message.chat.id, 'Введенный ID оператора не найден.') 

# Обработчик для получения сообщений от пользователей и сохранения их
@bot.message_handler(func=lambda message: message.chat.id not in operators and message.chat.id in user_requests)
def save_user_message(message):
    user_id = message.chat.id
    user_messages.setdefault(user_id, []).append(message.text)
    bot.send_message(message.chat.id, 'Ваше сообщение принято.')

@app.route("/operator-interface", methods=["GET", "POST"])
def operator_interface_page():
    if request.method == "POST":
        reply = request.form.get("reply")
        user_id = request.form.get("user_id")
        
        # Проверяем, существует ли ключ user_id в словаре user_messages
        if user_id not in user_messages:
            user_messages[user_id] = []  # Создаем новую запись, если ключ отсутствует
        
        # Добавляем новое сообщение оператора
        user_messages[user_id].append(f"Operator: {reply}")
        
        # Отправляем ответ пользователю
        send_to_user(user_id, f"Operator: {reply}")
        
    return render_template("operator.html", user_messages=user_messages)

# Установка вебхука
@app.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

# Установка вебхука при первом запуске
@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://821e-188-92-182-195.ngrok-free.app/" + bot_token)
    return "!", 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000)