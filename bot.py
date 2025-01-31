import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("ERRO: A variável TELEGRAM_BOT_TOKEN não foi encontrada no ambiente!")
    exit(1)
else:
    print(f"TOKEN carregado: {TOKEN[:5]}********")  # Mostra só o início do token para verificar

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá! Bem-vindo ao *CTFIndiqueBot*.\n"
                          "Use /indicar para gerar seu link de indicação.\n"
                          "Acompanhe suas indicações com /minhas_indicacoes.", parse_mode="MarkdownV2")

bot.polling()
