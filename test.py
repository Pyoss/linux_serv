import os
import sys
import subprocess
import time
import telebot

bot = bot_watcher.bot
admins_id = 197216910
bot.send_message(admin_id, 'Инициация бота...')

#subprocess.call(['./monitor.sh']) # Thanks @Jim Dennis for suggesting the []
#

@bot.message_handler(commands=['restart'])
def start(message):
  os.execl(sys.executable, 'python',  __file__, *sys.argv[1:])

@bot.message_handler(commands=['error'])
def start(message):
    print(message.for_error)


@bot.message_handler(commands=['update'])
def start(message):
    main.send_error(repr(message))
    try:
        payload = message.successful_payment.invoice_payload
        total_amount = message.successful_payment.total_amount
        message_id = message.message_id
        menu_messages.payment_handle(message.chat.id, payload, total_amount, message_id)
    except Exception as e:
        main.send_error(repr(e))


@bot.message_handler(commands=['echo'])
def start(message):
   bot.send_message(admin_id, message.text)




if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True)
