import feedparser
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

RSS_FEED_URL = "https://feeds.feedburner.com/ndtvnews-latest"

def fetch_news():
    news_feed = feedparser.parse(RSS_FEED_URL)
    news_items = []
    for entry in news_feed.entries[:5]:  
        news_items.append(f"{entry.title}\n{entry.link}")
    return "\n\n".join(news_items)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Type anything to get the latest news from NDTV.')

def send_news(update: Update, context: CallbackContext) -> None:
    news = fetch_news()
    update.message.reply_text(news)

def main() -> None:
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, send_news))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
