from telegram.ext import Updater
updater = Updater(token='1462186534:AAG1b2FeG14TXy1NtG2a03a4LRy26cmQS8o', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from covid import Covid
covid = Covid()
india=covid.get_status_by_country_name("India")
usa=covid.get_status_by_country_name('US')
france=covid.get_status_by_country_name('France')
germany=covid.get_status_by_country_name('Germany')
spain=covid.get_status_by_country_name('Spain')
china=covid.get_status_by_country_name('China')
italy=covid.get_status_by_country_name('Italy')
aus=covid.get_status_by_country_name('Australia')
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"India's stats : {india}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"America's stats : {usa}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"France's stats : {france}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Germany's stats : {germany}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Spain stats : {spain}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"China's stats : {china}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Italy's stats : {italy}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Australia's stats : {aus}")


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