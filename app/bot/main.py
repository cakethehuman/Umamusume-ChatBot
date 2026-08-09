from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler

from app.core.config import settings

async def hello(update: Update, content: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello this bot was made by cake")
    
def main() -> None:
    application = Application.builder().token(settings.BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("Hello", hello))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    
if __name__ == "__main__":
    main()
    