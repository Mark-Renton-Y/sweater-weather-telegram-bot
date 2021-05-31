import requests

from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging

OWM_API_KEY = '9b1099459b708345b4ed125e2b5eb05e'

def getWeather(city):
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={OWM_API_KEY}')

    result = result.json()

    if(result.get('message')):
        return result['message']

    return f"{result['main']['temp']}°C, {result['weather'][0]['main']}"


updater = Updater(token='1566611420:AAGXpOeQ2MqNjPZ4d9pszwRC3_zCcQGqf2I', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hazar barev, expair, gri kaxaky anune anglerenov, axpers")

def sendWeather(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=getWeather(update.message.text.split()[-1]))

def forecast(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="this feature is not ready yet")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

forecast_handler = CommandHandler('forecast', forecast)
dispatcher.add_handler(forecast_handler)

sendWeather_handler = MessageHandler(Filters.text & (~Filters.command), sendWeather)
dispatcher.add_handler(sendWeather_handler)

updater.start_polling()