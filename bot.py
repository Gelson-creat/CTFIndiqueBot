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
    bot.reply_to(message, "Olá! Bem-vindo ao *CTFIndiqueBot*.\n"
                          "Use /indicar para gerar seu link de indicação.\n"
                          "Acompanhe suas indicações com /minhas_indicacoes.", parse_mode="Markdown")

@bot.message_handler(commands=['indicar'])
def indicar(message):
    user_id = message.from_user.id
    link = f"https://t.me/CTFIndiqueBot?start={user_id}"
    bot.reply_to(message, f"📢 *Seu link de indicação:* {link}\n"
                          "Compartilhe com seus amigos!", parse_mode="Markdown")

@bot.message_handler(commands=['minhas_indicacoes'])
def minhas_indicacoes(message):
    user_id = message.from_user.id
    qtd = len(indicacoes.get(user_id, []))
    bot.reply_to(message, f"👥 Você já indicou {qtd} pessoas.")

@bot.message_handler(commands=['indicacoes'])
def ver_indicacoes(message):
    if message.chat.type == "private" and message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        qtd = len(indicacoes.get(user_id, []))
        bot.reply_to(message, f"O usuário indicou {qtd} pessoas.")
    else:
        bot.reply_to(message, "Responda a uma mensagem para ver as indicações desse usuário.")

@bot.message_handler(commands=['top_indicadores'])
def top_indicadores(message):
    ranking = sorted(indicacoes.items(), key=lambda x: len(x[1]), reverse=True)[:5]
    texto = "🏆 *Top Indicadores:*\n"
    for i, (user, indicados) in enumerate(ranking, 1):
        texto += f"{i}. Usuário {user} - {len(indicados)} indicações\n"
    bot.reply_to(message, texto, parse_mode="Markdown")

@bot.message_handler(commands=['recompensar'])
def recompensar(message):
    if message.chat.type == "private":
        bot.reply_to(message, "Este comando só pode ser usado no grupo oficial.")
        return
    try:
        _, user, qtd = message.text.split()
        user_id = int(user.replace("@", ""))
        qtd = int(qtd)
        bot.send_message(user_id, f"🎉 Você recebeu {qtd} CTFs por suas indicações! Parabéns!")
    except:
        bot.reply_to(message, "Formato inválido! Use: /recompensar @usuario quantidade")

@bot.message_handler(commands=['regras'])
def regras(message):
    bot.reply_to(message, "📌 *Regras do Programa de Indicação:*\n"
                          "1. Convide amigos com seu link.\n"
                          "2. Você recebe CTFs pelas indicações válidas.\n"
                          "3. Indicações falsas podem levar ao banimento.", parse_mode="Markdown")

@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    bot.reply_to(message, "ℹ️ *Como usar o bot:*\n"
                          "👉 /start - Começar\n"
                          "👉 /indicar - Gerar link de indicação\n"
                          "👉 /minhas_indicacoes - Ver indicações\n"
                          "👉 /regras - Saber as regras\n"
                          "👉 /ajuda - Mais informações", parse_mode="Markdown")

bot.polling()
