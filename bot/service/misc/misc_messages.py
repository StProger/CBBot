from mailbox import Message

from aiogram import types

from bot.service.redis_serv.api import get_rate_by_char_code, get_rates


async def exchange_message(message: types.Message,
                           amount_rate: float,
                           char_code_first: str | None = None,
                           char_code_second: str = "RUB"
                           ):

    if char_code_second == "RUB":
        rate = await get_rate_by_char_code(char_code=char_code_first)

        if rate is None:

            await message.answer(f"Нет такой валюты в базе: <code>{char_code_first}</code>")
        else:

            rate_to_rub = float(rate["value"]) * amount_rate

            await message.answer(
                f"Стоимость {amount_rate} {char_code_first} в рублях: {rate_to_rub:.2f}"
            )

    else:

        rate_first = await get_rate_by_char_code(char_code=char_code_first)

        if rate_first is None:

            await message.answer(f"Нет такой валюты в базе: <code>{char_code_first}</code>")

        rate_second = await get_rate_by_char_code(char_code=char_code_second)

        if rate_second is None:
            await message.answer(f"Нет такой валюты в базе: <code>{char_code_second}</code>")

        price_rate_first = float(rate_first["value"])
        price_rate_second = float(rate_second["value"])

        one_rate_amount = price_rate_first / price_rate_second

        exchange_value = amount_rate * one_rate_amount

        await message.answer(
            f"Стоимость {amount_rate} {char_code_first} в {char_code_second}: {exchange_value:.2f}"
        )


async def rates_message(message: types.Message):

    rates = await get_rates()

    text = "Курс валют:\n\n"

    for rate in rates:

        text += f"1 {rate['char_code']} ({rate['name']}) - {rate['value']} RUB\n"


    await message.answer(text)
