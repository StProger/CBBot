import sys
import os

from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from aiogram import Dispatcher, Bot

from bot.service.tasks.update_rates import update_rates_
from bot.settings import settings # , BOT_SCHEDULER
from bot.routers import register_all_routers
from bot import logging

import asyncio


async def main():

    storage = RedisStorage.from_url(settings.fsm_redis_url)

    dp = Dispatcher(storage=storage)

    bot = Bot(settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML", link_preview_is_disabled=True))

    register_all_routers(dp)


    await logging.setup()
    await update_rates_()

    # BOT_SCHEDULER.start()

    try:

        await dp.start_polling(bot)

    except KeyboardInterrupt:
        sys.exit(1)
    finally:
        await bot.session.close()


if __name__ == '__main__':

    asyncio.run(main())
    # asyncio.get_event_loop().create_task(main())

