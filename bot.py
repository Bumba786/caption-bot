import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def handle_posts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট বা গ্রুপ মেসেজ চেক
    message = update.channel_post if update.channel_post else update.message
    if not message: return

    # ভিডিও বা ফাইল হলে কাজ শুরু করবে
    if message.video or message.document:
        # ৫ সেকেন্ড অপেক্ষা করবে যাতে ফাইলটি ঠিকমতো আপলোড হতে পারে
        await asyncio.sleep(5)
        
        original = message.caption if message.caption else ""
        
        if "@MovieAddaHubOfficial02" not in original:
            new_text = f"{original}{CUSTOM_CAPTION}"
            try:
                await context.bot.edit_message_caption(
                    chat_id=message.chat_id,
                    message_id=message.message_id,
                    caption=new_text
                )
                logging.info("ক্যাপশন সফলভাবে এডিট হয়েছে!")
            except Exception as e:
                logging.error(f"এডিট করা যায়নি: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    # drop_pending_updates=True দিলে পুরনো এররগুলো আটকে যাবে না
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_posts))
    
    print("বট চালু হচ্ছে...")
    application.run_polling(drop_pending_updates=True)




