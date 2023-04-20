# coding=utf-8
from .variables import bot, telebot

print("Импорт функций.")


# ФУНКЦИЯ ЛОГИРОВАНИЯ СООБЩЕНИЙ
def logMessage(message):
    if message.from_user.is_bot:
        print(f"Бот: {message.text}     ({message.chat.username})")
        if message.reply_markup:
            for button in message.reply_markup.keyboard:
                print(f"|{button[0].text}|")
    else:
        print(f"\n@{message.from_user.username}: {message.text}")
        # print(f"https://t.me/{message.from_user.username}: {message.text}") # для вывода ссылки на пользователя


def sendMenu(chatId, text, massButtons):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in massButtons:
        keyboard.row(*item)
    logMessage(bot.send_message(chatId, text, reply_markup=keyboard))


def sendInlineMenu(chatId, text, massButtons):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for button in massButtons:
        keyboard.add(telebot.types.InlineKeyboardButton(button["text"], callback_data=button["data"]))
    logMessage(bot.send_message(chatId, text, reply_markup=keyboard))
