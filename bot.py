import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# আপনার তথ্য
TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
# {caption} মানে হলো ভিডিওর আসল লেখা, তার নিচে আপনার লিঙ্ক যোগ হবে
CUSTOM_CAPTION = "{caption}\n\n🎬 Join: @MovieAddaHubOfficial02\n📢 Backup: @movieaddahub_02"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def auto_caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল বা গ্রুপ থেকে মেসেজ ধরা
    msg = update.channel_post if update.channel_post else update.message
    
    if not msg:
        return

    # শুধু ভিডিও, ডকুমেন্ট বা অডিও হলে কাজ করবে
    if msg.video or msg.document or msg.audio:
        # ৫-১০ সেকেন্ড অপেক্ষা যাতে টেলিগ্রাম সার্ভারে ফাইলটি সেটল হয়
        await asyncio.sleep(7)
        
        original_caption = msg.caption if msg.caption else ""
        
        # চেক করা হচ্ছে আপনার লিঙ্ক অলরেডি আছে কি না
        if "@MovieAddaHubOfficial02" not in original_caption:
            # নতুন ক্যাপশন তৈরি
            formatted_caption = CUSTOM_CAPTION.format(caption=original_caption)
            
            try:
                # এডিট করার মূল কমান্ড
                await context.bot.edit_message_caption(
                    chat_id=msg.chat_id,
                    message_id=msg.message_id,
                    caption=formatted_caption,
                    parse_mode='Markdown' # লেখাগুলো সুন্দর দেখাবে
                )
                logging.info(f"Successfully updated caption in {msg.chat_id}")
            except Exception as e:
                logging.error(f"Error while editing: {e}")
                # গ্রুপে যদি এডিট না করা যায়, তবে সে নিচে আলাদা রিপ্লাই দিবে
                if not update.channel_post:
                    await msg.reply_text(formatted_caption)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # সব মিডিয়া ফাইল হ্যান্ডেল করবে
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, auto_caption))
    
    print("🚀 Auto Caption Bot is Running...")
    application.run_polling(drop_pending_updates=True)










