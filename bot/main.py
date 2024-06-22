import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv, find_dotenv

from handlers.user_commands import handlers_router
from handlers.admin_commands import admin_router

from callback_main.callback_factory.main_callback import main_callback_router
from callback_main.callback_factory.event_callback import event_cb_router
from callback_main.callback_factory.test_callback import test_cb_router
from callback_main.callback_factory.game_callback import game_cb_router
from callback_main.callback_factory.admin_callback import admin_cb_router

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

ALLOWED_UPDATES = ["message", "callback_query"]


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_routers(
        handlers_router,
        event_cb_router,
        test_cb_router,
        game_cb_router,
        main_callback_router,
        admin_router,
        admin_cb_router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
