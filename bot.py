import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# আপনার বর্তমান টোকেন
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"

# আপনার নতুন ক্যাপশন
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল বা গ্রুপের মেসেজ চেক
    message = update.channel_post if update.channel_post else update.message
    if not message:
        return

    # ভিডিও বা ফাইল হলে ৫ সেকেন্ড অপেক্ষা করবে (যাতে টেলিগ্রামের সাথে কনফ্লিক্ট না হয়)
    if message.video or message.document:
        await asyncio.sleep(5)
        
        original_caption = message.caption if message.caption else ""
        
        # যদি আপনার নাম অলরেডি না থাকে তবেই এডিট করবে
        if "@MovieAddaHubOfficial02" not in original_caption:
            new_caption = f"{original_caption}{CUSTOM_CAPTION}"
            try:
                # সরাসরি এডিট করার কমান্ড
                await context.bot.edit_message_caption(
                    chat_id=message.chat_id,
                    message_id=message.message_id,
                    caption=new_caption
                )
                logging.info("Caption successfully updated!")
            except Exception as e:
                logging.error(f"Error while editing: {e}")

if __name__ == '__main__':
    # অ্যাপ্লিকেশন তৈরি
    application = ApplicationBuilder().token(TOKEN).build()
    
    # সব মিডিয়া মেসেজ হ্যান্ডেল করার জন্য
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_media))
    
    print("Bot is starting...")
    # drop_pending_updates=True দিলে পুরনো সব জ্যাম বা এরর মেসেজ ক্লিয়ার হয়ে যাবে
    application.run_polling(drop_pending_updates=True)





