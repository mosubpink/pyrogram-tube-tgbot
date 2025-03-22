import logging

from environs import env
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

env.read_env()
api_id  = env('id')
api_hash = env('hash')
token = env('token')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def yt_download(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    pass

bot = ApplicationBuilder().token(token).build()

bot.add_handler(CommandHandler("start", hello))


bot.run_polling()

