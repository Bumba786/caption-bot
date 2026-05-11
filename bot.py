import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

logging.basicConfig(level=logging.INFO)

async def start_process(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # গ্রুপের মেসেজ বা চ্যানেলের পোস্ট—উভয়ই ধরবে
    msg = update.message if update.message else update.channel_post
    if not msg: return

    # যদি ভিডিও বা কোনো ফাইল (Document) হয়
    if msg.video or msg.document:
        # ৫ সেকেন্ড অপেক্ষা করবে যাতে ফাইলটি টেলিগ্রাম সার্ভারে পুরোপুরি আসে
        await asyncio.sleep(5)
        
        original_text = msg.caption if msg.caption else ""
        
        # যদি আপনার ইউজারনেম অলরেডি না থাকে তবেই এডিট করবে
        if "@MovieAddaHubOfficial02" not in original_text:
            try:
                await context.bot.edit_message_caption(
                    chat_id=msg.chat_id,
                    message_id=msg.message_id,
                    caption=f"{original_text}{CUSTOM_CAPTION}"
                )
                print("সফলভাবে এডিট হয়েছে!")
            except Exception as e:
                # যদি গ্রুপে এডিট করার অনুমতি না থাকে, তবে সে নিচে একটি রিপ্লাই দিবে
                if not update.channel_post:
                    await msg.reply_text(f"{original_text}{CUSTOM_CAPTION}")
                logging.error(f"Error: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    # filters.ALL ব্যবহার করেছি যাতে গ্রুপ এবং চ্যানেলের সব ফাইল বটটি পায়
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, start_process))
    
    print("বট সচল হচ্ছে...")
    application.run_polling(drop_pending_updates=True)






