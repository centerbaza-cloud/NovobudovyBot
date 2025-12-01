import telebot
from config import TOKEN, ADMIN_ID
import keyboards as kb

bot = telebot.TeleBot(TOKEN)

selected_jk = {}
selected_rooms = {}
selected_budget = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Вітаю 👋\n"
        "Я – бот Наталії Рахматової, ріелтора з підбору квартир у Житомирі.\n\n"
        "Оберіть дію у меню 👇",
        reply_markup=kb.main_menu()
    )


# --- ЖК ---
@bot.message_handler(func=lambda m: m.text == "🏢 Підібрати по ЖК")
def select_jk(message):
    bot.send_message(message.chat.id, "Оберіть житловий комплекс:", reply_markup=kb.jk_menu())


@bot.message_handler(func=lambda m: m.text in ["Абрикос","Панорама","Домбровський","Мрія","Статус","Домашній"])
def choose_rooms(message):
    chat_id = message.chat.id
    selected_jk[chat_id] = message.text

    bot.send_message(chat_id, "Скільки кімнат вас цікавить?", reply_markup=kb.rooms_menu())


@bot.message_handler(func=lambda m: m.text in ["1 кімната","2 кімнати","3+ кімнати"])
def choose_budget(message):
    chat_id = message.chat.id
    selected_rooms[chat_id] = message.text

    bot.send_message(chat_id, "Який бюджет ви розглядаєте?", reply_markup=kb.budget_menu())


@bot.message_handler(func=lambda m: m.text in ["до 40 000$","до 60 000$","до 80 000$","Інший бюджет"])
def ask_name(message):
    chat_id = message.chat.id
    selected_budget[chat_id] = message.text

    bot.send_message(chat_id, "Як вас звати?")
    bot.register_next_step_handler(message, send_request)


def send_request(message):
    chat_id = message.chat.id
    name = message.text

    jk = selected_jk.get(chat_id, "не вказано")
    rooms = selected_rooms.get(chat_id, "не вказано")
    budget = selected_budget.get(chat_id, "не вказано")

    # відправка заявки тобі
    bot.send_message(
        ADMIN_ID,
        f"🔥 Нова заявка!\n"
        f"ЖК: {jk}\n"
        f"Кімнат: {rooms}\n"
        f"Бюджет: {budget}\n"
        f"Ім’я: {name}\n"
        f"Telegram: @{message.from_user.username}"
    )

    # відповідь клієнту
    bot.send_message(
        chat_id,
        "Дякую! Я передала вашу заявку 💛\n"
        "Наталія зв’яжеться з вами найближчим часом.",
        reply_markup=kb.main_menu()
    )


# --- Контакти ---
@bot.message_handler(func=lambda m: m.text == "📞 Зв’язатися з ріелтором")
def contacts(message):
    bot.send_message(
        message.chat.id,
        "📞 Контакти:\n"
        "Viber: https://viber.me/0933597656\n"
        "Telegram: @Rakhmatova_Natalia\n"
        "WhatsApp: https://wa.me/380933597656\n"
        "Телефон: 093 359 76 56"
    )


bot.polling(none_stop=True)
