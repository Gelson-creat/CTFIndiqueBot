import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Dicionário para armazenar indicações temporariamente (substituir por banco de dados depois)
indicacoes = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    indicacoes.setdefault(user_id, [])  # Garante que o usuário está na base de dados
    bot.reply_to(message, "Olá! Bem-vindo ao *CTFIndiqueBot*.\n\n"
                          "✅ Use /indicar para gerar seu link de indicação.\n"
                          "📊 Acompanhe suas indicações com /minhas_indicacoes.", parse_mode="MarkdownV2")

@bot.message_handler(commands=['indicar'])
def indicar(message):
    user_id = message.from_user.id
    link = f"https://t.me/CTFIndiqueBot?start={user_id}"
    bot.reply_to(message, f"📢 *Seu link de indicação:* {link}\n"
                          "Compartilhe com seus amigos!", parse_mode="MarkdownV2")

@bot.message_handler(commands=['minhas_indicacoes'])
def minhas_indicacoes(message):
    user_id = message.from_user.id
    qtd = len(indicacoes.get(user_id, []))
    bot.reply_to(message, f"👥 Você já indicou {qtd} pessoas.", parse_mode="MarkdownV2")

@bot.message_handler(commands=['regras'])
def regras(message):
    bot.reply_to(message, "📌 *Regras do Programa de Indicação:*\n"
                          "1. Convide amigos com seu link.\n"
                          "2. Você recebe CTFs pelas indicações válidas.\n"
                          "3. Indicações falsas podem levar ao banimento.", parse_mode="MarkdownV2")

@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    bot.reply_to(message, "ℹ️ *Como usar o bot:*\n"
                          "👉 /start - Começar\n"
                          "👉 /indicar - Gerar link de indicação\n"
                          "👉 /minhas_indicacoes - Ver indicações\n"
                          "👉 /regras - Saber as regras\n"
                          "👉 /ajuda - Mais informações", parse_mode="MarkdownV2")

bot.polling()
