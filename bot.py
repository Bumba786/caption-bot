import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# আপনার টোকেন এবং ক্যাপশন সেটিংস
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
# {file_name} দিলে ফাইলের আসল নাম আসবে, তার নিচে আপনার লিঙ্ক
CUSTOM_CAPTION = "**{file_name}**\n\n🎬 Join: @MovieAddaHubOfficial02\n📢 Backup: @movieaddahub_02"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট বা গ্রুপের মেসেজ ফিল্টার করা
    msg = update.channel_post if update.channel_post else update.message
    if not msg:
        return

    # চেক করা হচ্ছে এটি ভিডিও না কি কোনো ডকুমেন্ট (ফাইল)
    media = msg.video or msg.document
    if media:
        # ৮ সেকেন্ড অপেক্ষা (সার্ভার প্রসেসিং টাইমের জন্য)
        await asyncio.sleep(8)
        
        # ফাইলের নাম সংগ্রহ করা (যদি থাকে)
        file_name = getattr(media, 'file_name', "Movie File")
        if not file_name:
            file_name = "Movie File"
            
        # নতুন ক্যাপশন তৈরি করা
        new_text = CUSTOM_CAPTION.format(file_name=file_name)
        
        # যদি আপনার লিঙ্ক অলরেডি না থাকে তবেই এডিট করবে
        current_caption = msg.caption if msg.caption else ""
        if "@MovieAddaHubOfficial02" not in current_caption:
            try:
                await context.bot.edit_message_caption(
                    chat_id=msg.chat_id,
                    message_id=msg.message_id,
                    caption=new_text,
                    parse_mode='Markdown'
                )
                print(f"Success: Updated {file_name}")
            except Exception as e:
                # গ্রুপে অন্যের মেসেজ এডিট করা না গেলে এটি রিপ্লাই হিসেবে দিবে
                if not update.channel_post:
                    await msg.reply_text(new_text, parse_mode='Markdown')
                logging.error(f"Error: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # সব মিডিয়া মেসেজ হ্যান্ডেল করার জন্য
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_caption))
    
    print("🚀 Bot is starting on Railway...")
    application.run_polling(drop_pending_updates=True)












