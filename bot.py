import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")  # Define o parse_mode globalmente

# Dicionário para armazenar indicações temporárias
indicacoes = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    indicacoes.setdefault(user_id, [])  # Garante que o usuário está na base de dados
    bot.reply_to(message, "Olá! Bem-vindo ao *CTFIndiqueBot*.\n\n"
                          "Use */indicar* para gerar seu link de indicação.\n"
                          "Acompanhe suas indicações com */minhas_indicacoes*.")

@bot.message_handler(commands=['indicar'])
def indicar(message):
    user_id = message.from_user.id
    link = f"https://t.me/CTFIndiqueBot?start={user_id}"
    bot.reply_to(message, f"📢 *Seu link de indicação:* [{link}]({link})\n\n"
                          "Compartilhe com seus amigos!")

@bot.message_handler(commands=['minhas_indicacoes'])
def minhas_indicacoes(message):
    user_id = message.from_user.id
    qtd = len(indicacoes.get(user_id, []))
    bot.reply_to(message, f"👥 Você já indicou *{qtd}* pessoas.")

@bot.message_handler(commands=['top_indicadores'])
def top_indicadores(message):
    ranking = sorted(indicacoes.items(), key=lambda x: len(x[1]), reverse=True)[:5]
    texto = "🏆 *Top Indicadores:*\n"
    for i, (user, indicados) in enumerate(ranking, 1):
        texto += f"{i}. Usuário `{user}` - *{len(indicados)}* indicações\n"
    bot.reply_to(message, texto)

@bot.message_handler(commands=['regras'])
def regras(message):
    bot.reply_to(message, "📌 *Regras do Programa de Indicação:*\n"
                          "1️⃣ Convide amigos com seu link.\n"
                          "2️⃣ Você recebe CTFs pelas indicações válidas.\n"
                          "3️⃣ Indicações falsas podem levar ao banimento.")

@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    bot.reply_to(message, "ℹ️ *Comandos do bot:*\n"
                          "👉 */start* - Começar\n"
                          "👉 */indicar* - Gerar link de indicação\n"
                          "👉 */minhas_indicacoes* - Ver indicações\n"
                          "👉 */regras* - Saber as regras\n"
                          "👉 */ajuda* - Mais informações")

bot.polling()
