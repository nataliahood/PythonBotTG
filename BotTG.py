import random
import telebot
from telebot import types
import os
import schedule
from threading import Thread
from time import sleep

folder_dir = 'pic'

file = open('support.txt', 'r', encoding='utf-8')
support = file.read().split('\n')
file.close()

file = open('stic.txt', 'r', encoding='utf-8')
stic = file.read().split('\n')
file.close()

bot = telebot.TeleBot('5593550302:AAEq5dkID1q0l_LnlnSY3YLQhxY162uVI1k')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Приуныл😔')
    item2 = types.KeyboardButton('Совсем приуныл😞')
    item3 = types.KeyboardButton('Кто тебя создал?')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Как себя чувствуешь?💜', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_handle_text(message):

    if message.text.strip() == 'Приуныл😔' or message.text.strip() == 'Нужно больше поддержки!':
        answer = random.choice(support)
        images = os.path.join(folder_dir, random.choice(os.listdir(folder_dir)))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Нужно больше поддержки!')
        item2 = types.KeyboardButton('Спасибо, мне уже лучше👍🏽')
        item3 = types.KeyboardButton('Совсем приуныл😞')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, answer, reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open(images, 'rb'))
    elif message.text.strip() == 'Совсем приуныл😞':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Спасибо, мне уже лучше👍🏽')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Я буду присылать тебе слова поддержки каждый вечер! До тех пор, пока тебе не станет легче😌', reply_markup=markup)
        user_id = message.from_user.id
        def function_to_run():
            bot.send_message(user_id, random.choice(support))
        schedule.every().minutes.do(function_to_run)
    elif message.text.strip() == 'Спасибо, мне уже лучше👍🏽':
        stickers = str(random.choice(stic))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Приуныл😔')
        item2 = types.KeyboardButton('Совсем приуныл😞')
        item3 = types.KeyboardButton('Кто тебя создал?')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Очень рад за тебя! Так держать😁👍🏽', reply_markup=markup)
        bot.send_sticker(message.chat.id, stickers)
        schedule.clear()
    elif message.text.strip() == 'Кто тебя создал?':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Сайт-визитка', url='https://nataliahood.github.io/')
        markup.add(button1)
        bot.send_message(message.chat.id, 'Тебе правда интересно?☺ Переходи по ссылке!'.format(message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Ой... кажется, я еще не умею читать сообщения с клавиатуры😥 Если хочешь написать мне, жми по кнопкам ниже😊')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEMszhitv7mZurHw02jOtUsHXmO9O84-QACDxUAAlAAATlItNCNfsmsILopBA')


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


Thread(target=schedule_checker).start()


bot.polling(none_stop=True, interval=0)