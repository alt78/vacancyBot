import telebot
import parse
token='899091252:AAFaYn270FWkionhic3fbeYS_Wod3EeZWxY'
bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Показать список вакансий')

urlList=parse.get_url_list()
vacancyList=parse.get_vacany(urlList)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Поехали', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'показать список вакансий':
        for vacancy in vacancyList:
            bot.send_message(message.chat.id, '<strong>Вакансия:</strong>', parse_mode='html')
            bot.send_message(message.chat.id, vacancy['tittle'])
            bot.send_message(message.chat.id, vacancy['href'])
    else:
        bot.send_message(message.chat.id, 'Не понимаю тебя')
bot.polling()
