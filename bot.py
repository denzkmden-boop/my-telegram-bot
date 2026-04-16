from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("бот жив 😎")

app = Application.builder().token("YOUR_TOKEN").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()