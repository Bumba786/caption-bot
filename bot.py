import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8496302598:AAFMBxGqRGG7mZeINTPWLfCGl06u9SLWN38"

# আপনার চ্যানেলের লিঙ্ক/ক্যাপশন
CUSTOM_CAPTION = "\n\n[@MovieAddaHubOfficial02]\n[@movieaddahub_02]"

async def handle_posts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চ্যানেল পোস্ট ধরবে
    post = update.channel_post if update.channel_post else update.message
    if not post: return

    # শুধু ভিডিও বা ফাইল এডিট করবে
    if post.video or post.document:
        original = post.caption if post.caption else ""
        
        # আপনার নাম অলরেডি থাকলে আর এডিট করবে না
        if "@MovieAddaHubOfficial02" not in original:
            new_text = f"{original}{CUSTOM_CAPTION}"
            try:
                # চ্যানেলে হলে এডিট করার চেষ্টা করবে
                await post.edit_caption(caption=new_text)
            except Exception as e:
                logging.error(f"Error: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    # সব ধরনের মিডিয়া ফাইল চেক করবে
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_posts))
    application.run_polling()


