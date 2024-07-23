from aiogram import Router, types, F
from aiogram.filters.command import Command, CommandObject

from bot.service.misc.misc_messages import exchange_message

router = Router()


@router.message(Command("exchange"))
async def exchange_handler(message: types.Message, command: CommandObject):

    print(command.args)
    args = command.args.split()
    if args is None:

        await message.answer("Не переданы аргументы")

    elif len(args) < 3 or len(args) > 3:

        await message.answer("Напишите только 3 аргумента.")

    else:

        if not args[-1].replace(".", "").isdigit():
            await message.answer("Количество валюты должно содержать только цифры.")
        if args[0].upper() == args[1].upper():
            await message.answer("Нельзя вводить одинаковую валюту.")
        else:
            char_code_first = args[0].upper()
            char_code_second = args[1].upper()
            amount_rate = float(args[-1])
            await exchange_message(
                message=message,
                char_code_first=char_code_first,
                char_code_second=char_code_second,
                amount_rate=amount_rate
            )