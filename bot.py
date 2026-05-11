from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = 8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38

async def caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        await update.message.reply_text("Photo received!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.PHOTO, caption))

print("Bot running...")
app.run_polling()
