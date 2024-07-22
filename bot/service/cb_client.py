import aiohttp

from bot.settings import settings


class HttpClient:

    def __init__(self):

        self._session = aiohttp.ClientSession()


class CentralBankClient(HttpClient):

    async def get_rates(self):

        async with self._session.get(url=settings.CB_URL) as response:

            if response.status == 200:

                cb_rates = await response.content
                print(cb_rates)
                return cb_rates
            else:

                return None
