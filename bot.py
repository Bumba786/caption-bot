import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# কনফিগারেশন
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"

# MarkdownV2 ফরম্যাটে বোল্ড করার জন্য কাস্টম টেক্সট
CUSTOM_CAPTION = "\n\n🎬 *Join: @MovieAddaHubOfficial02*\n📢 *Backup: @movieaddahub\\_02*"

logging.basicConfig(level=logging.INFO)

async def auto_caption_fix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট ধরবে
    msg = update.channel_post
    if not msg or not (msg.video or msg.document):
        return

    # ⚡ সময় কমিয়ে ২ সেকেন্ড করা হলো (সুপার-ফাস্ট এডিট)
    await asyncio.sleep(2)

    original = msg.caption if msg.caption else ""
    
    # আপনার লিঙ্ক না থাকলে এডিট করবে
    if "@MovieAddaHubOfficial02" not in original:
        new_text = f"{original}{CUSTOM_CAPTION}"
        
        try:
            # MarkdownV2 ফরম্যাটে দ্রুত এডিট সম্পন্ন হবে
            await context.bot.edit_message_caption(
                chat_id=msg.chat_id,
                message_id=msg.message_id,
                caption=new_text,
                parse_mode="MarkdownV2"
            )
            print("⚡ দ্রুত এডিট ও বোল্ড সফল হয়েছে!")
        except Exception as e:
            logging.error(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    # শুধুমাত্র চ্যানেলের জন্য ফিল্টার
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, auto_caption_fix))
    
    print("বট স্পিড মোডে চলছে...")
    app.run_polling(drop_pending_updates=True)
















