import telebot
from telebot import types
from datetime import datetime
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📅 Сколько дней до ЕГЭ", "📚 Шпаргалки", "🧘 Антистресс")
    return markup

def subject_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🏛 История", "⚖️ Обществознание", "↩️ Назад")
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я помогу тебе подготовиться к ЕГЭ 👇", reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if "дней до егэ" in text:
        exam_date = datetime(2025, 6, 13)
        today = datetime.now()
        days_left = (exam_date - today).days
        bot.send_message(message.chat.id, f"До ЕГЭ по истории осталось {days_left} дней! 📅")

    elif "антистресс" in text:
        bot.send_message(message.chat.id, "🧘‍♂️ Сделай глубокий вдох на 4 счёта, задержи дыхание, медленно выдохни. Повтори 3 раза 💆")

    elif "шпаргалк" in text:
        bot.send_message(message.chat.id, "Выбери предмет 👇", reply_markup=subject_menu())

    elif "назад" in text:
        bot.send_message(message.chat.id, "Возвращаемся в главное меню 👇", reply_markup=main_menu())

    elif "история" in text:
        bot.send_message(message.chat.id, "📚 История: https://yadi.sk/d/your_history_link")

    elif "обществознание" in text:
        bot.send_message(message.chat.id, "📚 Обществознание: https://yadi.sk/d/your_obsch_link")

    else:
        bot.send_message(message.chat.id, "Не совсем понял 🤔 Попробуй выбрать команду из меню ниже.")

bot.polling()