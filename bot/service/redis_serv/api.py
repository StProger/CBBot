from bot.service.redis_serv.base import redis_pool


async def update_rates(rates):

    for rate in rates:

        data = {
            "value": rate["value"],
            "name": rate["name"]
        }
        await redis_pool.hmset(f"cb_{rates['id']}", data)
