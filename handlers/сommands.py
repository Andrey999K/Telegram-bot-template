from utils.variables import bot
from utils.functions import *
from utils.decorators import *

print("Импорт команд.")


# Handle '/start'
@bot.message_handler(commands=['start'])
@loggingMessage
def send_welcome(message):
    # пример отправки клавиатуры
    sendMenu(message.chat.id, 'Держи меню😉', [
        ['Кнопка1', 'Кнопка2'],
        ['Кнопка3', 'Кнопка4', 'Кнопка5'],
    ])

    # пример отправки inline-клавиатуры
    # sendInlineMenu(message.chat.id, 'Выберите кнопку👇',
    #                [
    #                    {"text": "Кнопка1", "data": "button1"},
    #                    {"text": "Кнопка2", "data": "button2"}
    #                ]
    #                )


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
