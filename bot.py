import telebot
import random
from config_bot import TOKEN_bot
from bot_logic import gen_pass
from telebot import types

name = "Not information"

bot = telebot.TeleBot(TOKEN_bot)

qizz = {
    "bot_on_python":
        "Основной класс, который представляет ссобой бота?"


}

text_info = {
    "info":
        "Привет! Это информация о боте Bot_T\n"
        "Команды бота: /start /hello /bye /gen_pass /random_number /quiz_telebot\n"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! Узнать о боте /info")


@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, text_info["info"])


@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=["quiz_telebot"])
def qizz_b(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("telebot", callback_data="quizzT_1")
    button2 = types.InlineKeyboardButton("TeleBot", callback_data="quizzT_2")
    button3 = types.InlineKeyboardButton("@bot", callback_data="quizzT_3")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, qizz["bot_on_python"], reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "quizzT_1":
            bot.send_message(call.message.chat.id, "Нет, неверно(")
        elif call.data == "quizzT_3":
            bot.send_message(call.message.chat.id, "Нет, неправильно(")
        elif call.data == "quizzT_2":
            bot.send_message(call.message.chat.id, "Да! Это правильный ответ")

@bot.message_handler(commands=['random_number'])
def send_random(message):
    number = random.randrange(1, 10) 
    bot.reply_to(message, number)


@bot.message_handler(commands=['bye'])
def send_bye(message):
   bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['gen_pass'])
def gen_pass_tg(message):
   pasword = gen_pass(10)   
   bot.reply_to(message, f"Твой пароль: {pasword}")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Что?")


bot.polling()
