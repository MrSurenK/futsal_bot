import logging
import os
from dotenv import load_dotenv, dotenv_values

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

session_info = {
    "date": " ",
    "time": " ",
    "location": " ",
    "players": {},
    "paid": []
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'll help you organise your futsal session!")

# aysnc def organise(update: Update, context: ContextTypes.DEFAULT_TYPE):


if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("API_KEY")).build()

    # Must be last handler to handle wrong commands
    unknown_handler = MessageHandler(filters.COMMAND, unknown)


    # Must be last handler in application instance
    application.add_handler(unknown_handler)

    application.run_polling()

