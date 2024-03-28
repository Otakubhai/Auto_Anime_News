import logging

logging.basicConfig(
    filename="anime_news_bot.log",  # Log file name
    level=logging.INFO,  # Minimum logging level (can be DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(name)
