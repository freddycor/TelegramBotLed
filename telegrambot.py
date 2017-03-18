#coder :- Salman Faris

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def Accendi(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def Spegni(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'Accendi':
       bot.sendMessage(chat_id, on(11))
    elif command =='Spegni':
       bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('Bot Token')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
