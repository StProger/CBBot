from bot.service.redis_serv.base import redis_pool


async def update_rates(rates):

    for rate in rates:

        data = {
            "value": rate["value"].replace(",", "."),
            "name": rate["name"]
        }
        await redis_pool.hmset(f"cb_{rate['char_code']}", data)


async def get_rates():
    """ Возвращает все валюты """

    rates_list = []

    for key in (await redis_pool.keys(pattern="cb_*")):

        info_rate = await redis_pool.hgetall(key)
        info_rate["char_code"] = key.split("_")[-1]
        rates_list.append(info_rate)

    return rates_list


async def get_rate_by_char_code(char_code):
    """ Возвращает валюту """

    return await redis_pool.hgetall(f"cb_{char_code}")
