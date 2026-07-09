from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Вставь сюда токен, который дал @BotFather
TOKEN = "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Камила лошара")


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
