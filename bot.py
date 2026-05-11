import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# আপনার টোকেন
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"

# লগ সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# আপনার ক্যাপশন
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

# /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("বট সক্রিয় আছে! মুভি ফাইল বা ভিডিও পাঠান, আমি ক্যাপশন যোগ করে দেব।")

# মুভি বা ফাইল হ্যান্ডেল করার ফাংশন
async def handle_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চেক করা হচ্ছে এটি ভিডিও, ডকুমেন্ট নাকি এনিমেশন
    message = update.message
    file_id = None
    original_caption = message.caption if message.caption else ""
    
    # নতুন ক্যাপশন তৈরি
    new_caption = f"{original_caption}{CUSTOM_CAPTION}"

    if message.video:
        await message.reply_video(video=message.video.file_id, caption=new_caption)
    elif message.document:
        await message.reply_document(document=message.document.file_id, caption=new_caption)
    elif message.audio:
        await message.reply_audio(audio=message.audio.file_id, caption=new_caption)
    elif message.photo:
        await message.reply_photo(photo=message.photo[-1].file_id, caption=new_caption)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # হ্যান্ডেলার সেটআপ
    application.add_handler(CommandHandler('start', start))
    # সব ধরনের মিডিয়া ফাইল (ভিডিও, ডকুমেন্ট, অডিও, ফটো) এর জন্য
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_files))
    
    print("বটটি সক্রিয় হচ্ছে...")
    application.run_polling()
