import telebot
from configSheets import updateCellSheet
token = "5793842632:AAEfmB24aPWvVT78AAI2jmC8PbQgMp1kKpQ"
bot = telebot.TeleBot(token)

order_dict = {}
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):
    global order_dict
    order_name = message.chat.id
    order_dict[order_name] = message.text
    bot.send_message(message.from_user.id, 'Какой у тебя заказ?')
    bot.register_next_step_handler(message, get_order)


def get_order(message):
    global order_dict
    order_name = message.chat.id
    data = order_dict.get(order_name)
    order_dict[order_name] =str(data) + ";" + message.text
    updateCellSheet(order_dict[order_name],int((len(order_dict))))
    order_dict[int(len(order_dict))] = order_dict.pop(order_name)
    bot.send_message(message.from_user.id, "Ваш заказ принят")





if __name__ == '__main__':
     bot.infinity_polling()






