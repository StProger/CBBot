from aiogram import Dispatcher

from bot.routers import start
from bot.routers import exchange
from bot.routers import rates


def register_all_routers(dp: Dispatcher):

    dp.include_router(start.router)
    dp.include_router(exchange.router)
    dp.include_router(rates.router)