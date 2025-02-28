"""import telebot

# Встав токен, який надіслав BotFather
bot = telebot.TeleBot('7611417175:AAF9IDQ-5vJ_SxARcJ7Reofhm5ulN9GcxBY')
# Команда /start: відправляє привітання, коли користувач пише /start
@bot.message_handler(commands=['start'])
def send_welcome (message):
    bot.reply_to(message, "Привіт! Я твій новий бот")
# Команда /help: відправляє повідомлення з підказками
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to (message, "Я можу допомогти тобі з основними командами: /start, /help")
# Запуск бота
bot.polling()"""



"""import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN= "7611417175:AAF9IDQ-5vJ_SxARcJ7Reofhm5ulN9GcxBY"
bot=telebot.TeleBot (TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome (message):
# Створення клавіатури
    keyboard = ReplyKeyboardMarkup (resize_keyboard=True)
    button1 = KeyboardButton("Привіт")
    button2 = KeyboardButton("Почати")
    keyboard.add(button1, button2)

# Надсилання повідомлення з кнопками
    bot.send_message(message.chat.id, "Привіт! Обери опцію:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Привіт":
        bot.send_message(message.chat.id, "Привіт! Як у тебе справи?")
    elif message.text == "Почати":
        keyboard = InlineKeyboardMarkup ()
        button1 = InlineKeyboardButton("Сайт програмування", url="https://codehs.com/")
        button2 = InlineKeyboardButton("Сайт школи ", url="https://justschool.me/uk")
        keyboard.add(button1, button2)
        bot.send_message(message.chat.id, "Обери дію:", reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, "Я не знаю такої команди, натисни на кнопку")
# команда help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з основними командами: /start, /help")
@bot.message_handler(commands=["tell jake"])
def tell_jake(message):
    bot.reply_to(message, "Тут має бути жарт")
@bot.message_handler(commands=["info"])
def tell_jake(message):
    bot.reply_to(message, "Я бот")
@bot.message_handler(commands=["random"])
def random_message(message):
    a = random.randint(1,10)
    bot.reply_to(message, f"Random number {a}")
bot.polling()"""






"""import telebot
import schedule
import time

# Токен бота
TOKEN = "7611417175:AAF9IDQ-5vJ_SxARcJ7Reofhm5ulN9GcxBY"
bot = telebot.TeleBot(TOKEN)

# ID користувача
CHAT_ID = 6166128745  # Введи ID чату, його можна знайти за допомогою @userinfobot

# Налаштування розкладу
def send_reminder():
    bot.send_message(CHAT_ID, "⏰ Час зробити важливу справу!")

# Заплановані нагадування
schedule.every().day.at("09:00").do(send_reminder)  # Надсилає нагадування о 09:00
schedule.every().day.at("18:00").do(send_reminder)  # Надсилає нагадування о 18:00
schedule.every(0.10).seconds.do(send_reminder)  # Надсилає нагадування кожні 2 секунди

# Основний цикл
while True:
    try:
        schedule.run_pending()  # Виконуємо заплановані завдання
        time.sleep(1)  # Робимо паузу, щоб зменшити навантаження
    except Exception as e:
        print(f"Помилка: {e}")
        time.sleep(5)  # У разі помилки робимо паузу"""

"""#1
text = "Hello, world!"
print(text)
text= text.split(",")
print(text)

students = "Андрій, Олена, Микола, Світлана, Юлія, Дмитро"
students_list = students.split(",")
print(students_list)
com1 = students_list[0:3]
com2 = students_list[3:6]
print(com1)
#2
dates = "25.12.2021, 01.01.2020, 5.15.2023"
dates_list = dates.split(", ")
print(dates_list)
years = []
for date in dates_list:
    year = date[-4:]
    years.append(years)

print(years)"""


"""#3
url = "https://example.com/?page=5&sort=asc&filter=new"
query = url.split("?") [1]
params = query.split("&")
print(params)
for param in params:
    key, value = param.split("-")
    print(key,"-", value)"""


"""import telebot

TOKEN = '7611417175:AAF9IDQ-5vJ_SxARcJ7Reofhm5ulN9GcxBY'
CHAT_ID = 6166128745

bot = telebot.TeleBot(TOKEN)

def convert_unit(value, from_units, to_units):
    conversions = {
        "чашки": {"мілілітри": 240},
        "столові ложки": {"мілілітри": 15},
        "чайні ложки": {"мілілітри": 5},
    }
    if from_units in conversions and to_units in conversions[from_units]:
        return value * conversions[from_units][to_units]
    else:
        return None

@bot.message_handler(commands=["start"])
def send_hello(message):
    bot.send_message(message.chat.id, "Привіт! Я допоможу тобі конвертувати задану кількість чашок, ложок, склянкок. Напиши в такому форматі: 5 чашки в мілілітри.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    try:
        parts = text.split(" в ")
        value_and_from_unit = parts[0].split()
        to_unit = parts[1]
        value = float(value_and_from_unit[0])
        from_unit = value_and_from_unit[1]
        result = convert_unit(value, from_unit, to_unit)
        if result is not None:
            bot.send_message(message.chat.id, f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            bot.send_message(message.chat.id, "Спробуйте ще раз")
    except Exception as e:
        bot.send_message(message.chat.id, f"Все погано, у тебе помилка в коді: {str(e)}")

bot.polling()"""


"""import telebot
import random

TOKEN = "7611417175:AAF9IDQ-5vJ_SxARcJ7Reofhm5ulN9GcxBY"
bot = telebot.TeleBot(TOKEN)

UPLOAD_FOLDER =r"C:\memes/"
memes = [1.jpg, 2.jpg, 3.jpg, 4.jpg]

@bot.message_handler(content_types=['photo'])
def receive_meme(message):
    file_info = bot.get_file(message.photo[-1], file_id)
    downloaded_file = bot.download_file(file_info file_path)
    file_name = str(len(memes) + 1) + ".jpg"
    with open(UPLOAD_FOLDER + file_name, 'wb' ) as new_file:
        new_file.write(downloaded_file)
    memes.append(file_name)
    bot.reply_to(message, "Мем збережено")

@bot.message_handler(commands=['meme'])
def send_random_meme(message):
    if memes:
        meme = random.choice(memes)
        with open(UPLOAD_FOLDER + meme, 'rb') as photo:

            bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "Мемів поки немає")

bot.polling()"""


import telebot
import random

TOKEN = "7611417175:AAF9IDQ-5vJ_SxARcJ7Reofhm5ulN9GcxBY"
bot = telebot.TeleBot(TOKEN)

UPLOAD_FOLDER = r"c:\memes/"  # Заміна зворотного слешу на прямий для кроссплатформенності
memes = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]  # Імена файлів мають бути рядками

@bot.message_handler(content_types=['photo'])
def receive_meme(message):
    # Виправлення отримання файлу
    file_info = bot.get_file(message.photo[-1].file_id) # Додано .file_id для доступу до ID файлу
    downloaded_file = bot.download_file(file_info.file_path) # Виправлення синтаксису file_info.file_path
    file_name = str(len(memes) + 1) + ".jpg"
with open(UPLOAD_FOLDER + file_name, 'wb') as new_file:
    new_file.write(downloaded_file)
    memes.append(file_name)  # Додавання імені файлу до списку
    bot.reply_to(message, "Мем збережено")

@bot.message_handler(commands=['meme'])
def send_random_meme(message):
    if memes:
        meme = random.choice(memes)
        with open(UPLOAD_FOLDER + meme, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "Мемів поки немає")

bot.polling()



