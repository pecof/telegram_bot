import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if msg['text'] == '/flag':
        bot.sendMessage(chat_id, '你想要flag吗？')
    else :
        bot.sendMessage(chat_id, "I don't understand your mean")

TOKEN = '1342730108:AAFPzPKiVm-0k0JTII3WtqczzDZqiBafbxc'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(100000000)
