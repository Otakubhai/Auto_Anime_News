import asyncio
import logging

from pymongo import MongoClient
from pyrogram import Client
from pyrogram.types import InputMediaPhoto

from config import config  # Import configuration from separate file
from utils import check_for_new_items, send_news


async def main():
    logger = logging.getLogger(name)  # Get logger from separate file

    while True:
        latest_entry = check_for_new_items()
        if latest_entry:
            try:
                await send_news(latest_entry)
                logger.info(f"Sent news update: {latest_entry.title}")
            except Exception as e:
                logger.error(f"Error sending news update: {e}")
        await asyncio.sleep(config.CHECK_INTERVAL)  # Use check interval from config

with Client("my_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN) as app:
    logging.info('Bot has been restarted')
    app.loop.run_until_complete(main())
