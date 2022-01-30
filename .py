import speech_recognition as sr
import requests
import logging
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

r = sr.Recognizer()
updater = Updater("BOTAPI", # enter there your BOT API
                  use_context=True)
dispatcher: Dispatcher = updater.dispatcher

def telegram_bot_sendtext(bot_message):
    bot_token = 'BOTAPI' # BOT API
    bot_chatID = 'CHATID' # CHATID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def record(source, sg):
    while True:
        try:
            text = r.recognize_google(r.record(source, duration=sg), language="es-ES")
            if "name" in text.lower() or "surname" in text.lower() or "surname2" in text.lower(): # introduce the words you need to recognize
                telegram_bot_sendtext("\U0001F916 Your NAME has been DETECTED: in '{}'".format(text.lower()))
            else:
                return text
        except:
            pass

def listen(update: Update, context: CallbackContext): 
    try:
        bot: Bot = context.bot
        sg = int(context.args[0])
        with sr.Microphone() as source:
            text = r.recognize_google(r.record(source, duration=sg), language="es-ES")
            bot.send_message(chat_id=update.effective_chat.id,
                                text="\U0001F916 '{}'".format(text))
    except:
        bot.send_message(chat_id=update.effective_chat.id,
                            text="\U0001F916 FAIL!")

def main():
    if __name__ == '__main__':
        telegram_bot_sendtext("\U0001F916 BOT RUNNING")
        updater.dispatcher.add_handler(CommandHandler("listen", listen))
        updater.start_polling()
        while True:
            with sr.Microphone() as source:
                record(source, 5)

telegram_bot_sendtext("\U0001F916 BOT ARMED")

