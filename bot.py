
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# আপনার টোকেন
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"

# লগ সেটআপ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# আপনার নতুন ক্যাপশন
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

async def edit_caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট বা গ্রুপ মেসেজ চেক করা
    message = update.channel_post if update.channel_post else update.message
    
    if not message:
        return

    # ভিডিও বা ডকুমেন্ট এডিট করা
    if message.video or message.document:
        original_caption = message.caption if message.caption else ""
        
        # ডুপ্লিকেট ক্যাপশন রোধ করতে চেক
        if "@MovieAddaHubOfficial02" not in original_caption:
            new_caption = f"{original_caption}{CUSTOM_CAPTION}"
            try:
                await message.edit_caption(caption=new_caption)
            except Exception as e:
                logging.error(f"Error: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, edit_caption))
    application.run_polling()
