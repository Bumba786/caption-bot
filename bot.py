import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# আপনার টোকেন
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"

# লগ সেটআপ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# আপনার ক্যাপশন
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট বা গ্রুপ/প্রাইভেট মেসেজ চেক করা
    message = update.channel_post if update.channel_post else update.message
    
    if not message:
        return

    # যদি ভিডিও বা ডকুমেন্ট হয়
    if message.video or message.document:
        original_caption = message.caption if message.caption else ""
        
        # যদি আপনার লিঙ্ক অলরেডি না থাকে তবেই কাজ করবে
        if "@MovieAddaHubOfficial02" not in original_caption:
            new_caption = f"{original_caption}{CUSTOM_CAPTION}"
            
            # চ্যানেলের ক্ষেত্রে এডিট করবে
            if update.channel_post:
                try:
                    await message.edit_caption(caption=new_caption)
                except Exception as e:
                    logging.error(f"Error in Channel: {e}")
            
            # পার্সোনাল মেসেজ বা গ্রুপের ক্ষেত্রে রিপ্লাই দেবে
            else:
                try:
                    await message.reply_text(text=new_caption, reply_to_message_id=message.message_id)
                except Exception as e:
                    logging.error(f"Error in Chat: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_media))
    print("Bot is running...")
    application.run_polling()

