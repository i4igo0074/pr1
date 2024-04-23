# import os
# import dotenv
# import telebot
# import datetime
# from telebot import types
# import csv

# dotenv.load_dotenv()

# token = os.getenv("token")
# admin_id = os.getenv("admin_id")

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=["start"])

# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Sheet", request_location=True)
#     markup.add(btn1)
#     bot.send_message(message.chat.id, "Have u sheeted?", reply_markup=markup)

# def save_location(message):
#     try:
#         with open("location.csv", "a", newline="") as file:
#             date = datetime.datetime.now()
#             writer = csv.writer(file)
#             writer.writerow([
#                 message.chat.id,
#                 message.from_user.first_name,
#                 message.from_user.last_name,
#                 message.from_user.username,
#                 message.location.latitude,
#                 message.location.longitude,
#                 date,
#             ])
#             return True
#     except:
#         return False


# @bot.message_handler(content_types=["location"])
# def location(message):
#     if not save_location(message):
#         bot.send_message(message.chat.id, "Smthng wrong")
#         return
#     bot.send_message(message.chat.id, "Cool!")

# if __name__ == "__main__":
#     print("Bot started")
#     bot.polling(none_stop=True)