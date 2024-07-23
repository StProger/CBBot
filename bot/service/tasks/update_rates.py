from bot.service.cb_client import cb_client

from bot.service.redis_serv.api import update_rates


async def update_rates_():

    rates = await cb_client.get_rates()
    print(rates)

    parsed_rates = await cb_client.parse_rates(rates)
    print(parsed_rates)

    await update_rates(parsed_rates)
