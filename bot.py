import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# আপনার কনফিগারেশন
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
# {file_name} দিলে ফাইলের আসল নাম আসবে, তারপর আপনার লিঙ্ক
CUSTOM_CAPTION = "**{file_name}**\n\n🎬 Join: @MovieAddaHubOfficial02\n📢 Backup: @movieaddahub_02"

logging.basicConfig(level=logging.INFO)

async def start_pro_caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল এবং গ্রুপ উভয় পোস্ট রিড করবে
    msg = update.channel_post if update.channel_post else update.message
    if not msg: return

    # মিডিয়া ফাইল (ভিডিও/ডকুমেন্ট) চেক
    media = msg.video or msg.document or msg.audio
    if media:
        # একটু সময় দেওয়া যাতে ফাইলটি সার্ভারে ঠিকমতো প্রসেস হয়
        await asyncio.sleep(5)
        
        # ফাইলের আসল নাম বের করা
        file_name = media.file_name if hasattr(media, 'file_name') and media.file_name else "Movie File"
        
        # নতুন ক্যাপশন ফরম্যাট করা
        new_caption = CUSTOM_CAPTION.format(file_name=file_name)

        # যদি অলরেডি ক্যাপশন এডিট করা না থাকে
        if "@MovieAddaHubOfficial02" not in (msg.caption or ""):
            try:
                await context.bot.edit_message_caption(
                    chat_id=msg.chat_id,
                    message_id=msg.message_id,
                    caption=new_caption,
                    parse_mode='Markdown'
                )
                print(f"Success: Caption updated for {file_name}")
            except Exception as e:
                # গ্রুপে এডিট না করা গেলে সে নিচে রিপ্লাই দিবে
                if not update.channel_post:
                    await msg.reply_text(new_caption, parse_mode='Markdown')
                logging.error(f"Error: {e}")

if __name__ == '__main__':
    # বটের অ্যাপ্লিকেশন তৈরি
    app = ApplicationBuilder().token(TOKEN).build()
    
    # সব ধরণের মিডিয়া মেসেজ ধরার জন্য হ্যান্ডলার
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, start_pro_caption))
    
    print("🚀 Pro Caption Bot is Running on Railway...")
    app.run_polling(drop_pending_updates=True)











