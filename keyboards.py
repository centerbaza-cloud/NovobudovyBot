from telebot import types

def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("🏢 Підібрати по ЖК", "📍 Пошук за районом")
    menu.add("💰 Пошук за бюджетом", "📞 Зв’язатися з ріелтором")
    return menu

def jk_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("Абрикос", "Панорама")
    menu.add("Домбровський", "Мрія")
    menu.add("Статус", "Домашній")
    menu.add("⬅️ Назад")
    return menu

def rooms_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("1 кімната", "2 кімнати", "3+ кімнати")
    return menu

def budget_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("до 40 000$", "до 60 000$", "до 80 000$", "Інший бюджет")
    return menu
