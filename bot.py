import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

logging.basicConfig(level=logging.INFO)

async def handle_posts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট ধরবে (চ্যানেলে এটি ১০০% এডিট হবে)
    msg = update.channel_post if update.channel_post else update.message
    if not msg: return

    # শুধু ভিডিও বা ফাইল হলে কাজ করবে
    if msg.video or msg.document:
        await asyncio.sleep(5)
        
        original = msg.caption if msg.caption else ""
        if "@MovieAddaHubOfficial02" not in original:
            try:
                # এডিট করার চেষ্টা
                await context.bot.edit_message_caption(
                    chat_id=msg.chat_id,
                    message_id=msg.message_id,
                    caption=f"{original}{CUSTOM_CAPTION}"
                )
            except Exception as e:
                # গ্রুপে এডিট না করা গেলে সে আপনার ফাইলের ঠিক নিচেই একটি রিপ্লাই দিবে
                if not update.channel_post:
                    await msg.reply_text(f"{original}{CUSTOM_CAPTION}")
                logging.error(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_posts))
    # drop_pending_updates=True দিলে সব জ্যাম ক্লিয়ার হবে
    app.run_polling(drop_pending_updates=True)








