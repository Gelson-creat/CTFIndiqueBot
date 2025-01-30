import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("ERRO: A variável de ambiente 'TELEGRAM_BOT_TOKEN' não foi encontrada!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá! Bem-vindo ao CTFIndiqueBot. Use /indicar para gerar seu link de indicação.")

@bot.message_handler(commands=['indicar'])
def indicar(message):
    user_id = message.from_user.id
    link = f"https://t.me/CTFIndiqueBot?start={user_id}"
    bot.reply_to(message, f"Seu link de indicação: {link}\nCompartilhe com seus amigos!")

bot.polling()
