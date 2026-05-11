import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def handle_posts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট ধরবে
    message = update.channel_post if update.channel_post else update.message
    if not message: return

    # শুধু ভিডিও এবং ডকুমেন্ট এডিট করবে
    if message.video or message.document:
        original = message.caption if message.caption else ""
        
        if "@MovieAddaHubOfficial02" not in original:
            new_text = f"{original}{CUSTOM_CAPTION}"
            try:
                # চ্যানেলে সরাসরি এডিট করার কমান্ড
                await context.bot.edit_message_caption(
                    chat_id=message.chat_id,
                    message_id=message.message_id,
                    caption=new_text
                )
                logging.info("Caption updated successfully!")
            except Exception as e:
                logging.error(f"Failed to edit: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_posts))
    application.run_polling(drop_pending_updates=True) # পুরনো মেসেজ ইগনোর করবে



