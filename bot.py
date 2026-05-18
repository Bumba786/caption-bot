import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# কনফিগারেশন
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"

# 💎 আপনার দেওয়া কাস্টমাইজড স্টাইলিশ ফন্ট লেআউট
CUSTOM_CAPTION = (
    "\n\n"
    "𝕵𝖔𝖎𝖓 :- @MovieAddaHubOfficial02\n"
    "           ☟ 𝕽𝖊𝖖𝖚𝖊𝖘𝖙 𝕲𝖗𝖔𝖚𝖕 ☟\n"
    "📢 @movieaddahub_02"
)

logging.basicConfig(level=logging.INFO)

async def auto_caption_fix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট ধরবে
    msg = update.channel_post
    if not msg or not (msg.video or msg.document):
        return

    # ⚡ ২ সেকেন্ডের সুপার-ফাস্ট বাফার সময়
    await asyncio.sleep(2)

    original = msg.caption if msg.caption else ""
    
    # আপনার লিঙ্ক অলরেডি পোস্টে না থাকলে এডিট করবে (ডুপ্লিকেট প্রটেকশন)
    if "@MovieAddaHubOfficial02" not in original:
        new_text = f"{original}{CUSTOM_CAPTION}"
        
        try:
            # কোনো পার্স মোড ছাড়া ডিরেক্ট এডিট (যা ১০০% সেফ এবং ফাস্ট)
            await context.bot.edit_message_caption(
                chat_id=msg.chat_id,
                message_id=msg.message_id,
                caption=new_text
            )
            print("⚡ স্টাইলিশ ক্যাপশন এডিট সফল হয়েছে!")
        except Exception as e:
            logging.error(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    # শুধুমাত্র চ্যানেলের ভিডিও এবং ফাইলের ফিল্টার
    channel_filter = filters.ChatType.CHANNEL & (filters.VIDEO | filters.Document.ALL)
    app.add_handler(MessageHandler(channel_filter, auto_caption_fix))
    
    print("🚀 বট এখন আপনার দেওয়া নিউ স্টাইলে রকেটের গতিতে চলছে...")
    app.run_polling(drop_pending_updates=True)

















