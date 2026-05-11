import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
# আপনার কাঙ্ক্ষিত ক্যাপশন
CUSTOM_CAPTION = "\n\n🎬 Join: @MovieAddaHubOfficial02\n📢 Backup: @movieaddahub_02"

logging.basicConfig(level=logging.INFO)

async def auto_caption_pro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট ধরবে
    msg = update.channel_post
    if not msg or not (msg.video or msg.document):
        return

    # একটু সময় দিন ফাইলটি প্রসেস হতে
    await asyncio.sleep(5)
    
    original = msg.caption if msg.caption else ""
    if "@MovieAddaHubOfficial02" not in original:
        new_caption = f"{original}{CUSTOM_CAPTION}"
        
        try:
            # ১. সরাসরি এডিট করার চেষ্টা (প্রথম অপশন)
            await context.bot.edit_message_caption(
                chat_id=msg.chat_id,
                message_id=msg.message_id,
                caption=new_caption,
                parse_mode='Markdown'
            )
        except Exception:
            # ২. যদি এডিট না হয়, তবে পুরানোটি ডিলিট করে নতুন করে পাঠাবে (ব্যাকআপ অপশন)
            try:
                # ভিডিও বা ডকুমেন্ট ফাইল আইডি নিয়ে আবার পাঠানো
                file_id = msg.video.file_id if msg.video else msg.document.file_id
                await context.bot.send_video(
                    chat_id=msg.chat_id,
                    video=file_id,
                    caption=new_caption,
                    parse_mode='Markdown'
                )
                # পুরানো ভুল ক্যাপশনের ভিডিওটি ডিলিট করে দিবে
                await context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id)
            except Exception as e:
                logging.error(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, auto_caption_pro))
    print("Bot is working now...")
    app.run_polling(drop_pending_updates=True)













