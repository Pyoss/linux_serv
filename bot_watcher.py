import sys
import telebot

bot = telebot.TeleBot('777849028:AAFKdy8OJcLn37H7A8bJVsSCTSB-5S37zf4')
admin_id = 197216910
print(sys.argv[1])

bot.send_message(admin_id, sys.argv[1])
