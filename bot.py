import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

logging.basicConfig(level=logging.INFO)

async def auto_caption_engine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post if update.channel_post else update.message
    if not msg or not (msg.video or msg.document):
        return

    await asyncio.sleep(5)
    original = msg.caption if msg.caption else ""
    
    if "@MovieAddaHubOfficial02" not in original:
        new_caption = f"{original}{CUSTOM_CAPTION}"
        try:
            # এটি চ্যানেলে ১০০% কাজ করবে
            await context.bot.edit_message_caption(
                chat_id=msg.chat_id,
                message_id=msg.message_id,
                caption=new_caption
            )
        except Exception:
            # গ্রুপে এডিট না হলে এটি ফাইলের নিচেই ক্যাপশনসহ রিপ্লাই দিবে
            if not update.channel_post:
                await msg.reply_text(new_caption)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, auto_caption_engine))
    app.run_polling(drop_pending_updates=True)









