import sys
import telebot
import os

bot = telebot.TeleBot('777849028:AAFKdy8OJcLn37H7A8bJVsSCTSB-5S37zf4')
admin_id = 197216910
print(bot.send_message(admin_id, 2))
print(os.environ['ERROR_MSG'])



if __name__ == '__main__':
    bot.skip_pending = True
    bot.delete_webhook()
    bot.polling(none_stop=True)
