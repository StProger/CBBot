from aiogram import types, F, Router
from aiogram.filters.command import Command

from bot.service.misc.misc_messages import rates_message

router = Router()


@router.message(Command("rates"))
async def rates_handler(message: types.Message):

    await rates_message(message)
