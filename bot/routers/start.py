from aiogram import Router, F, types
from aiogram.filters.command import CommandStart


router = Router()


available_commands = """Доступные команды:

/exchange, например /exchange <code>USD RUB 10</code> отобразит стоимость 10 долларов в рублях.

/rates - актуальные курсы валют"""


@router.message(CommandStart())
async def start_handler(message: types.Message):

    await message.answer(
        text=available_commands
    )
