import telebot
from config import keys, token
from extensions import APIException, CryptoConverter
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help','start'])
def help(message):
    help_text = "Чтобы начать работу введите команду боту в формате:\n<имя валюты>  <в какую валюту перевести>   <количество>\n/values - Увидеть список всех валют"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    values_text = "Доступные валюты:"
    for key in keys.keys():
        values_text = '\n'.join((values_text,key,))
    bot.reply_to(message, values_text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise APIException('Количество параметров не соответствует трём')
        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать вашу команду\n{e}')
    else:
        text = f' цена {amount} {quote} - {total_base} {base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)