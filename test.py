import os
import sys
import subprocess
import time
import telebot
import bot_watcher

bot = bot_watcher.bot
admin_id = 197216910
bot.send_message(admin_id, 'Инициация бота...')

#) # Thanks @Jim Dennis for suggesting the []
#

@bot.message_handler(commands=['restart'])
def start(message):
  os.execl(sys.executable, 'python',  __file__, *sys.argv[1:])
  
@bot.message_handler(commands=['update'])
def start(message):
  subprocess.call(['./update.sh'])

@bot.message_handler(commands=['error'])
def start(message):
    print(message.for_error)

@bot.message_handler(commands=['stop'])
def start(message):
    bot.stop_polling()


@bot.message_handler(commands=['echo'])
def start(message):
   bot.send_message(admin_id, message.text)




if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True)
