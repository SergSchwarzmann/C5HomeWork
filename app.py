import telebot
from config import keys, TOKEN
from extensions import CurrecyConverter, APIExeptions

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'For start enter: from currency, to currency, quantity separated by "space"\nExample: dollar euro 100 \n\
To see currencies enter: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Current currencies:'
    for i in keys:
        text = '\n'.join((text, i, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIExeptions('Check parameters!')

        base, quote, amount = values
        total, rate = CurrecyConverter.get_price(base, quote, amount)
    except APIExeptions as e:
        bot.reply_to(message, f'User error: \n {e}')
    except Exception as e:
        bot.reply_to(message, f'Cannot fulfill request: \n {e}')
    else:
        text = f'Value of {amount} {base} in {quote} is {total} with rate {rate} {quote} for 1 {base}'
        bot.send_message(message.chat.id, text)


bot.polling()
