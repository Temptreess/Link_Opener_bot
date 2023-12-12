# Link_Opener_bot
# This is a python script who allows you to open link in telegram bot!
# Этот скрипт позволяет открыть ссылку через телеграм бота!
# ENG
# Instructions
Firstly, you'll need Python version 3.11 or higher (tested on 3.11.5) and the pytelegrambotapi library version 4.14.0.

You can download Python from: https://www.python.org/downloads/
Install pytelegrambotapi (4.14.0) by executing the command: `pip install pytelegrambotapi` or `pip install -r requirements.txt` (the second option is preferable as other 
libraries might be added during the project's development).
    
Next, you'll need to create two bots in Telegram. To do this, message @BotFather and use the command /newbot, following the instructions to create the two bots.
    
To find the chat_id, use the @getmyid_bot. Send the command /start and copy the received chat_id.
    
Now, you need to store this data in variables:
    
TOKEN1: This token will be used to send information about the bot's status, its startup, addition to auto-start, etc. (insert the first bot token here).
TOKEN: This token will be used to receive commands for specific actions, for instance, opening a particular link (insert the second bot token here).
chat_id1: Here, insert the chat_id obtained from @getmyid_bot (insert id here).
    
After this, you'll need to compile the file. You can use tools like auto-py-to-exe or pyinstaller.
    
# Disclaimer:
# This text is provided for informational purposes only. The use of the provided instructions and tools is at your own risk. I am not liable for any issues that may arise     
# from the use of the provided information or tools.

# RU
# Иструкция:
Прежде всего, для работы необходим Python версии 3.11 или выше (проверено на 3.11.5) и библиотека pytelegrambotapi версии 4.14.0.
    
Python можно загрузить с сайта: https://www.python.org/downloads/
Установить pytelegrambotapi (4.14.0) можно выполнив команду: `pip install pytelegrambotapi` или `pip install -r requirements.txt` (второй вариант предпочтительнее, так как      в процессе разработки проекта могут быть добавлены и другие библиотеки).
    
Затем необходимо зайти в Telegram и создать двух ботов. Это можно сделать, написав боту @BotFather и выполнить команду /newbot, следуя инструкциям, чтобы создать два бота.
    
Чтобы узнать chat_id, необходимо воспользоваться ботом @getmyid_bot, выполнить команду /start и скопировать полученный chat_id.
    
Теперь все эти данные нужно записать в переменные:
    
TOKEN1: Этот токен будет использоваться для отправки информации о статусе бота, его запуске, добавлении в автозагрузку и т.д. (вставить первый токен бота сюда);
TOKEN: Этот токен будет использоваться для получения команд о необходимых действиях, например, открытии определенной ссылки (вставить второй токен бота сюда);
chat_id1: Сюда нужно вставить chat_id, который мы получили от бота @getmyid_bot (вставить id сюда).
 
После этого необходимо скомпилировать файл. Для этого можно использовать инструменты типа auto-py-to-exe или pyinstaller.
    
# Отказ от ответственности:
# Этот текст предоставлен исключительно в ознакомительных целях. Использование указанных инструкций и инструментов происходит на ваш собственный риск. Я не несу       
# ответственности за возможные проблемы, возникшие в результате использования предоставленной информации или инструментов.
