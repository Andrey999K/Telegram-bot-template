from utils.variables import bot
from utils.functions import *


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call)
    if call.data == 'button1':
        bot.answer_callback_query(callback_query_id=call.id, text='Вы выбрали кнопку 1')
    elif call.data == 'button2':
        bot.answer_callback_query(callback_query_id=call.id, text='Вы выбрали кнопку 2')
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)