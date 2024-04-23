# import os
# import dotenv
# import telebot
# import datetime
# from telebot import types

# dotenv.load_dotenv()

# token = os.getenv("token")
# admin_id = os.getenv("admin_id")

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=["start"])
# def start(message):
#     date = datetime.datetime.now()
#     user_info = f"Info about user: \n\n"\
#                 f"Id of chat: {message.chat.id}\n"\
#                 f"Id of user: {message.from_user.id}\n"\
#                 f"Name: {message.from_user.first_name}\n"\
#                 f"Surname: {message.from_user.last_name}\n"\
#                 f"Nickname: {message.from_user.username}\n"\
#                 f"Text of message: {date}\n"
    
#     bot.send_message(message.chat.id, user_info)

# @bot.message_handler(commands=["help"])

# def help(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Connect operator", request_contact=True)
#     btn2 = types.KeyboardButton("FAQ")
#     markup.add(btn1,btn2)
#     bot.send_message(message.chat.id, "Choose option!", reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def text(message):
#     if message.text == "Связаться с Оператором":
#         bot.send_message(message.chat.id, "Оператор свяжется с Вами в ближайшее время!")
#     elif message.text == "FAQ":
#         bot.send_message(message.chat.id, "Оператор свяжется с Вами в ближайшее время!")

# @bot.message_handler(content_types=['contact'])
# def contact(message):
#     bot.send_message(admin_id, f"Новая заявка:\n\n"
#                                 f"ID чата: {message.chat.id}\n"
#                                 f"ID пользователя: {message.from_user.id}\n"
#                                 f"Имя: {message.from_user.first_name}\n"
#                                 f"Фамилия: {message.from_user.last_name}\n"
#                                 f"Псевдоним: {message.from_user.username}\n"
#                                 f"Телефон: {message.contact.phone_number}\n")
#     bot.send_message(message.chat.id, "Оператор свяжется с Вами в ближайшее время!")



# if __name__ == "__main__":
#     print("Bot started")
#     bot.polling(none_stop=True)


# 1. Приветствие и ответ на команду /start: Напишите бота, который будет отвечать на команду /start приветственным сообщением.

# import os
# import dotenv
# import telebot
# import datetime
# from telebot import types
# dotenv.load_dotenv()

# token = os.getenv("token")
# admin_id = os.getenv("admin_id")

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=["start"])
# def start(message):
#     date = datetime.datetime.now()
#     welcome = "U r welcome"
    
#     bot.send_message(message.chat.id, welcome)

# if __name__ == "__main__":
#     print("Bot started")
#     bot.polling(none_stop=True)

# 2. Эхо-бот: Создайте бота, который будет повторять все текстовые сообщения, полученные от пользователя.


# import os
# import dotenv
# import telebot

# dotenv.load_dotenv()

# token = os.getenv("token")

# bot = telebot.TeleBot(token)

# @bot.message_handler(func=lambda message: True)
# def echo(message):
#     bot.send_message(message.chat.id, message.text)

# if __name__ == "__main__":
#     print("Bot started")
#     bot.polling(none_stop=True)




# 3. Отправка изображений: Реализуйте функцию, которая позволит боту отправлять изображения в ответ на определенные команды или сообщения.

# import telebot
# import requests
# import os
# import dotenv

# dotenv.load_dotenv()

# token = os.getenv("token")
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=["cat"])
# def send_cat(message):
#     # URL изображения с котом
#     cat_image_url = "https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg"
    
#     # Загружаем изображение по URL
#     response = requests.get(cat_image_url)
    
#     # Проверяем успешность запроса
#     if response.status_code == 200:
#         # Отправляем изображение
#         bot.send_photo(message.chat.id, response.content)
#     else:
#         bot.send_message(message.chat.id, "Не удалось загрузить изображение кота")

# @bot.message_handler(commands=["dog"])
# def send_dog(message):
#     # URL изображения с собакой
#     dog_image_url = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQgByBT5IiAT_a2x9pUVb4VMoOrlzHH7Jrzj-HB5jzHlR4lNLMS"
    
#     # Загружаем изображение по URL
#     response = requests.get(dog_image_url)
    
#     # Проверяем успешность запроса
#     if response.status_code == 200:
#         # Отправляем изображение
#         bot.send_photo(message.chat.id, response.content)
#     else:
#         bot.send_message(message.chat.id, "Не удалось загрузить изображение собаки")

# if __name__ == "__main__":
#     print("Bot started")
#     bot.polling(none_stop=True)



# 4. Калькулятор: Создайте бота, который будет принимать математические выражения от пользователя (например, "2 + 2") и отправлять результат вычислений.

# import os
# import dotenv
# import telebot
# import re

# dotenv.load_dotenv()

# token = os.getenv("token")

# bot = telebot.TeleBot(token)

# @bot.message_handler(func=lambda message: True)
# def calculate(message):
#     try:
#         expression = message.text
#         result = eval(expression)
#         bot.send_message(message.chat.id, f"Результат: {result}")
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# if __name__ == "__main__":
#     print("Bot started")
#     bot.polling(none_stop=True)



# 5. Счетчик сообщений: Напишите бота, который будет подсчитывать количество сообщений, отправленных пользователем, и выводить это количество при запросе.
# import os
# import dotenv
# import telebot

# dotenv.load_dotenv()

# token = os.getenv("token")

# bot = telebot.TeleBot(token)

# user_message_count = {}

# @bot.message_handler(commands=["count"])
# def show_message_count(message):
#     user_id = message.from_user.id
#     count = user_message_count.get(user_id, 0)
#     bot.send_message(message.chat.id, f"Вы отправили {count} сообщений.")

# @bot.message_handler(func=lambda message: True)
# def count_messages(message):
#     user_id = message.from_user.id
#     if user_id not in user_message_count:
#         user_message_count[user_id] = 1
#     else:
#         user_message_count[user_id] += 1

# if __name__ == "__main__":
#     print("Bot started")
#     bot.polling(none_stop=True)


# 6. Уведомления: Реализуйте функцию, позволяющую боту отправлять уведомления пользователю в определенное время.
# import os
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# import asyncio
# from datetime import datetime

# bot = Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
# async def command_start(message : types.Message):
# 	while True:
# 		await asyncio.sleep(1)
# 		now = datetime.now()
# 		current_time = now.strftime("%H:%M:%S")
# 		if current_time == '23:44:01': 
# 			await bot.send_message(message.chat.id, f'"Это сообщение отправлено в {current_time}"')

# @dp.message_handler(commands=['mess'])
# async def command(message : types.Message):
# 	await bot.send_message(message.chat.id, 'Для полной картины, асинхронность работает')

# executor.start_polling(dp, skip_updates=True)







# import asyncio
# from datetime import datetime

# async def send_notification(bot, message):
#     time = datetime.now()
#     if time.hour == 8 and time.minute == 52:
#         await bot.send_message(message.from_user.id, f'Время: {time.hour}:{time.minute}')
#     else:
#         await bot.send_message(message.from_user.id, time)

# # Предполагается, что экземпляр `bot` и `message` определены где-то в другом месте вашего кода


# # Запустите асинхронную функцию
# asyncio.run(send_notification(bot, message))



# 7. Случайные шутки: Создайте бота, который будет отправлять случайные шутки или анекдоты при запросе пользователя.


# import requests
# import telebot
# import os
# import dotenv

# dotenv.load_dotenv()

# token = os.getenv("token")
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=["joke"])
# def send_joke(message):
#     # Отправляем запрос к API для получения случайной шутки
#     response = requests.get("https://api.chucknorris.io/jokes/random")
    
#     # Проверяем успешность запроса
#     if response.status_code == 200:
#         # Извлекаем текст шутки из ответа
#         joke_text = response.json()["value"]
#         # Отправляем шутку пользователю
#         bot.reply_to(message, joke_text)
#     else:
#         # В случае ошибки отправляем сообщение о проблеме
#         bot.reply_to(message, "Произошла ошибка при получении шутки. Попробуйте позже.")

# if __name__ == "__main__":
#     print("Bot started")
#     bot.polling(none_stop=True)
