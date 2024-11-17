import telebot
import random
from config_bot import TOKEN_bot
from bot_logic import gen_pass
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(TOKEN_bot)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! Команды: /start /hello /gen_pass /bye /random_number")
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
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
def echo_all(message):
   bot.reply_to(message, message.text)
    
bot.polling()
