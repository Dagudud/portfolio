import telebot
import datetime
import time

TOKEN = os.environ.get('BOT_TOKEN', '')
bot = telebot.TeleBot(TOKEN)

keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Привет', 'Пока')
keybord1.row('Дата', 'Время', 'День недели')
reply_markup = keybord1

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я бот который может показывать дату и время.\n'
                     'Используй кнопки ниже или напиши:\n'
                     '- Привет/Пока\n'
                     '- Дата\n'
                     '- Время\n',
                    reply_markup = keybord1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    text_lower = message.text.lower()

    if text_lower == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет!', reply_markup=keybord1)
    elif text_lower == 'пока':
        bot.send_message(message.chat.id, 'И тебе пока!', reply_markup=keybord1)
    elif text_lower == 'дата':
        date = datetime.datetime.now()
        formatted_date = date.strftime('%d.%m.%Y')
        bot.send_message(message.chat.id, f'Сегодня: {formatted_date}', reply_markup=keybord1)
    elif text_lower == 'время':
        time = datetime.datetime.now()
        formatted_time = time.strftime('%H:%M:%S')
        bot.send_message(message.chat.id, f'Сейчас: {formatted_time}', reply_markup=keybord1)
    elif text_lower == 'день недели':
        date = datetime.datetime.now()
        days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
        day_of_week = days[date.weekday()]
        formatted_date = date.strftime('%d.%m.%Y')
        bot.send_message(message.chat.id,
                         f'Сегодня {day_of_week.capitalize()}\n'
                         f'Дата: {formatted_date}',
                         reply_markup=keybord1)

bot.polling()