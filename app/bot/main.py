from telegram import Update
from telegram.ext import ContextTypes

from ..core.config import settings

async def hello(update: Update, content: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello this bot was made by cake")
    
# def main() -> None:
#     application =APp
    