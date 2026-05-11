import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

logging.basicConfig(level=logging.INFO)

async def auto_edit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট বা গ্রুপের মেসেজ ধরবে
    msg = update.channel_post if update.channel_post else update.message
    if not msg or not (msg.video or msg.document):
        return

    # ১০ সেকেন্ড অপেক্ষা যাতে টেলিগ্রাম সার্ভারে ফাইলটি এডিট করার জন্য তৈরি হয়
    await asyncio.sleep(10)

    original = msg.caption if msg.caption else ""
    
    if "@MovieAddaHubOfficial02" not in original:
        new_text = f"{original}{CUSTOM_CAPTION}"
        try:
            # এটিই মূল কমান্ড যা ক্যাপশন বদলে দিবে
            await context.bot.edit_message_caption(
                chat_id=msg.chat_id,
                message_id=msg.message_id,
                caption=new_text
            )
            print("Successfully Edited!")
        except Exception as e:
            # যদি এডিট করতে না পারে, তবেই শুধু সে রিপ্লাই দিবে (বিকল্প হিসেবে)
            logging.error(f"Edit failed: {e}")
            if not update.channel_post:
                await msg.reply_text(new_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    # filters.ALL ব্যবহার করা হয়েছে যাতে সব মিডিয়া পায়
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, auto_edit))
    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)







