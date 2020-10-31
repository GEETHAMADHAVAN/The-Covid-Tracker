from telegram.ext import Updater
updater = Updater(token='1462186534:AAG1b2FeG14TXy1NtG2a03a4LRy26cmQS8o', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from covid_india import states
ma=states.getdata('Maharashtra')
ka=states.getdata('Karnataka')
ap=states.getdata('Andhra Pradesh')
up=states.getdata('Uttar Pradesh')
wb=states.getdata('West Bengal')
ke=states.getdata('Kerala')
gu=states.getdata('Gujarat')
tn=states.getdata('Tamil Nadu')
asa=states.getdata('Assam')
bi=states.getdata('Bihar')
ch=states.getdata('Chhattisgarh')
go=states.getdata('Goa')
uk=states.getdata('Uttarakhand')
ra=states.getdata('Rajasthan')
pu=states.getdata('Punjab')
od=states.getdata('Odisha')
mp=states.getdata('Madhya Pradesh')
de=states.getdata('New Delhi')
tot=states.getdata('Total')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Maharashtra : {ma}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Karnataka : {ka}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Andra Pradesh : {ap}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Uttar Pradesh : {up}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"West Bengal : {wb}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Kerala : {ke}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Gujarat : {gu}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tamil Nadu : {tn}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Assam : {asa}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bihar : {bi}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Chhattisgarh : {ch}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Goa : {go}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Uttarakhand : {uk}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Rajasthan : {ra}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Punjab : {pu}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Odisha : {od}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Madhya Pradesh : {mp}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"New Delhi : {de}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Cases Overview : {tot}")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)
